import configparser
import os
import time
import subprocess
import psutil
from typing import Dict, Any, Optional, Tuple
from pathlib import Path

from app.models.ini_settings import ins_server_setting, ins_game_setting, ins_game_ini_setting
from app.models.json_setting import ins_mods_setting, ins_world_info
from app.models.log_data import ins_tool_logger


class OpenServer:
    _processes = {}  # 保存所有服务器进程
    _max_retry_attempts = 10  # 最大重试次数
    _temp_process = None  # 保存临时服务器进程
    _server_ready_timeout = 600  # 服务器就绪超时时间(秒)

    @classmethod
    def start(cls):
        """启动所有配置开启的世界服务器（带自动配置和模组检查）"""
        server_exe = cls._get_server_executable()
        if not os.path.exists(server_exe):
            cls._log(f"{server_exe} 不存在(does not exist)", error=True)
            return

        try:
            # 第一步：检查并生成GameUserSettings.ini文件
            if not cls._ensure_game_user_settings():
                return

            # 第二步：检查所有模组是否已下载
            if not cls._ensure_all_mods_downloaded():
                return

            # 第三步：正常启动所有世界
            cls._start_all_worlds()
        finally:
            # 确保临时服务器被关闭
            cls._cleanup_temp_server()

    @classmethod
    def _cleanup_temp_server(cls):
        """终极版强制终止临时服务器进程"""
        if cls._temp_process is None:
            return

        pid = cls._temp_process.pid
        cls._log(
            f"开始强制终止临时服务器进程 (PID: {pid}) (Starting force termination of temporary server process (PID: {pid}))")

        # # 方法1: 标准终止流程
        # try:
        #     cls._temp_process.terminate()
        #     cls._temp_process.wait(timeout=5)
        #     cls._log(f"标准终止成功 (PID: {pid}) (Standard termination succeeded (PID: {pid}))")
        #     cls._temp_process = None
        #     return
        # except:
        #     pass

        # 方法2: 使用psutil彻底终止进程树
        try:
            parent = psutil.Process(pid)
            for child in parent.children(recursive=True):  # 终止所有子进程
                try:
                    child.terminate()
                except:
                    try:
                        child.kill()
                    except:
                        pass
            parent.terminate()
            parent.wait(timeout=5)
            cls._log(f"终止进程树成功 (PID: {pid}) (Terminated process tree (PID: {pid}))")
            cls._temp_process = None
            return
        except psutil.NoSuchProcess:
            cls._log(f"进程已不存在 (PID: {pid}) (Process no longer exists (PID: {pid}))")
            cls._temp_process = None
            return
        except Exception as e:
            cls._log(f"psutil终止失败: {str(e)} (PID: {pid}) (psutil termination failed: {str(e)} (PID: {pid}))",
                     error=True)

        # 方法3: 使用Windows系统命令强制终止
        try:
            subprocess.run(f"taskkill /F /T /PID {pid}", shell=True, check=True)
            cls._log(f"使用taskkill强制终止成功 (PID: {pid}) (Force killed with taskkill (PID: {pid}))")
            cls._temp_process = None
            return
        except subprocess.CalledProcessError as e:
            cls._log(f"taskkill终止失败: {str(e)} (PID: {pid}) (taskkill failed: {str(e)} (PID: {pid}))", error=True)
        except Exception as e:
            cls._log(f"终止进程时发生意外错误: {str(e)} (PID: {pid}) (Unexpected error: {str(e)} (PID: {pid}))",
                     error=True)

        # 最终确认
        try:
            if cls._temp_process.poll() is None:  # 进程仍在运行
                cls._log(
                    f"警告: 可能未能完全终止进程 (PID: {pid}) (Warning: Process may still be running (PID: {pid}))",
                    warning=True)
            else:
                cls._log(f"进程已终止 (PID: {pid}) (Process terminated (PID: {pid}))")
        except:
            cls._log(f"无法确认进程状态 (PID: {pid}) (Unable to verify process status (PID: {pid}))", error=True)

        cls._temp_process = None

    @classmethod
    def _ensure_game_user_settings(cls) -> bool:
        """确保GameUserSettings.ini文件存在"""
        settings_file = cls._get_server_settings_file()
        if os.path.exists(settings_file):
            return True

        cls._log(
            "GameUserSettings.ini不存在，将启动临时服务器生成该文件... (GameUserSettings.ini not found, starting temporary server to generate it...)")

        all_worlds = ins_world_info.get_all()
        if not all_worlds:
            cls._log("没有可用的世界配置 (No world configurations available)", error=True)
            return False

        # 获取第一个开启的世界
        first_world_id, first_world_data = next(((k, v) for k, v in all_worlds.items() if v["open"]), (None, None))
        if not first_world_id:
            cls._log("没有开启的世界 (No enabled worlds)", error=True)
            return False

        # 启动临时服务器
        server_exe = cls._get_server_executable()
        command = cls._build_server_command(first_world_id, first_world_data, server_exe)
        cls._temp_process = cls._launch_temp_server(first_world_id, command)

        # 等待文件生成
        max_wait_time = 300  # 5分钟超时
        start_time = time.time()
        result = False

        try:
            while not os.path.exists(settings_file):
                if time.time() - start_time > max_wait_time:
                    cls._log(
                        "等待GameUserSettings.ini生成超时 (Timeout waiting for GameUserSettings.ini to be generated)",
                        error=True)
                    return False

                # 检查进程是否仍在运行
                if cls._temp_process.poll() is not None:
                    cls._log("临时服务器意外退出，正在重新启动... (Temporary server crashed, restarting...)",
                             warning=True)
                    cls._temp_process = cls._launch_temp_server(first_world_id, command)
                    start_time = time.time()  # 重置超时计时器

                time.sleep(5)

            cls._log("GameUserSettings.ini已成功生成 (GameUserSettings.ini has been successfully generated)")
            result = True
        finally:
            # 无论成功与否都关闭临时服务器
            cls._cleanup_temp_server()

        return result

    @classmethod
    def _launch_temp_server(cls, world_id: str, command: str) -> subprocess.Popen:
        """启动临时服务器用于生成配置文件"""
        cls._log(f"启动临时服务器 {world_id} (Starting temporary server {world_id})")
        try:
            proc = subprocess.Popen(
                command,
                shell=True,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
                close_fds=True
            )
            cls._processes[world_id] = proc
            return proc
        except Exception as e:
            cls._log(f"启动临时服务器失败: {str(e)} (Failed to start temporary server: {str(e)})", error=True)
            raise

    @classmethod
    def _ensure_all_mods_downloaded(cls) -> bool:
        """确保所有启用的模组已下载"""
        if not ins_server_setting.mods_open:
            return True

        enabled_mods = {mod_id for mod_id, mod_data in ins_mods_setting.get_all().items() if mod_data["open"]}
        if not enabled_mods:
            return True

        cls._log(f"需要检查的模组: {enabled_mods} (Mods to check: {enabled_mods})")

        # 检查是否所有模组都已下载
        mods_path = cls._get_mods_directory()
        if mods_path and cls._check_all_mods_downloaded(mods_path, enabled_mods):
            return True

        cls._log(
            "模组目录不存在或模组未下载，将启动临时服务器下载模组... (Mods directory not found or mods not downloaded, starting temporary server to download mods...)")

        all_worlds = ins_world_info.get_all()
        if not all_worlds:
            cls._log("没有可用的世界配置 (No world configurations available)", error=True)
            return False

        # 获取第一个开启的世界
        first_world_id, first_world_data = next(((k, v) for k, v in all_worlds.items() if v["open"]), (None, None))
        if not first_world_id:
            cls._log("没有开启的世界 (No enabled worlds)", error=True)
            return False

        # 启动临时服务器下载模组
        server_exe = cls._get_server_executable()
        command = cls._build_server_command(first_world_id, first_world_data, server_exe)

        attempt = 0
        result = False

        try:
            while attempt < cls._max_retry_attempts:
                attempt += 1
                cls._log(f"尝试下载模组 (第 {attempt} 次) (Attempting to download mods (attempt {attempt}))")

                cls._temp_process = cls._launch_temp_server(first_world_id, command)
                start_time = time.time()
                max_wait_time = 600  # 10分钟超时

                while time.time() - start_time < max_wait_time:
                    # 检查模组目录是否存在
                    mods_path = cls._get_mods_directory()
                    if mods_path and cls._check_all_mods_downloaded(mods_path, enabled_mods):
                        cls._log("所有模组已成功下载 (All mods have been successfully downloaded)")
                        result = True
                        break

                    # 检查进程是否仍在运行
                    if cls._temp_process.poll() is not None:
                        cls._log("服务器意外退出，正在重新启动... (Server crashed, restarting...)", warning=True)
                        cls._temp_process = cls._launch_temp_server(first_world_id, command)
                        start_time = time.time()  # 重置超时计时器

                    time.sleep(10)

                if result:
                    break

                cls._cleanup_temp_server()

            if not result:
                cls._log(
                    f"下载模组失败，已达到最大重试次数 {cls._max_retry_attempts} (Failed to download mods, reached max retry attempts {cls._max_retry_attempts})",
                    error=True)
        finally:
            # 无论成功与否都关闭临时服务器
            cls._cleanup_temp_server()

        return result

    @classmethod
    def _get_mods_directory(cls) -> Path:
        """获取模组目录路径，如果不存在则返回None"""
        mods_root = Path(ins_server_setting.root_path) / "ShooterGame" / "Binaries" / "Win64" / "ShooterGame" / "Mods"
        if not mods_root.exists():
            return None

        # 查找第一个子目录（通常是Steam Workshop ID）
        workshop_dirs = list(mods_root.iterdir())
        if not workshop_dirs:
            return None

        return workshop_dirs[0]

    @classmethod
    def _check_all_mods_downloaded(cls, mods_path: Path, required_mods: set) -> bool:
        """检查所有需要的模组是否已下载"""
        if not mods_path or not mods_path.exists():
            return False

        downloaded_mods = set()
        for mod_dir in mods_path.iterdir():
            if mod_dir.is_dir() and "_" in mod_dir.name:
                mod_id = mod_dir.name.split("_")[0]
                downloaded_mods.add(mod_id)

        return required_mods.issubset(downloaded_mods)

    @classmethod
    def _start_all_worlds(cls):
        """启动所有配置开启的世界服务器"""
        server_exe = cls._get_server_executable()
        all_worlds = ins_world_info.get_all()

        for world_id, world_data in all_worlds.items():
            if not world_data["open"]:
                continue

            cls._log_server_startup(world_id, world_data)
            command = cls._build_server_command(world_id, world_data, server_exe)
            cls._write_game_user_settings()

            # 启动并监控服务器
            success = cls._launch_and_monitor_server(world_id, command)
            if not success:
                cls._log(
                    f"服务器 {world_id} 启动失败，跳过后续世界 (Server {world_id} failed to start, skipping subsequent worlds)",
                    error=True)
                break

        cls._log_startup_completion()

    @classmethod
    def _launch_and_monitor_server(cls, world_id: str, command: str) -> bool:
        """启动服务器并监控日志文件判断是否启动成功（完全独立进程）"""
        max_retries = 3  # 最大重试次数
        retry_count = 0
        server_ready = False
        ready_patterns = [
            "Server has completed startup and is now advertising for join",
            "Server has completed",
            "Server is ready",
            "is now advertising for join"
        ]
        error_patterns = [
            "Error querying server mods: ApiError: Failed (serverUnreachable)",
            "Error querying server mods",
            "Failed (serverUnreachable)",
            # 可以添加其他需要监控的错误模式
        ]
        log_file = Path(ins_server_setting.root_path) / "ShooterGame" / "Saved" / "Logs" / f"{world_id}_server_tool.log"

        # 如果存在，则删除
        if log_file.exists():
            log_file.unlink(missing_ok=True)

        while retry_count < max_retries and not server_ready:
            retry_count += 1
            if retry_count > 1:
                cls._log(
                    f"尝试重启服务器 {world_id} (第 {retry_count} 次) (Attempting to restart server {world_id} (attempt {retry_count}))",
                    warning=True)
                time.sleep(5)  # 重启前短暂等待

            try:
                log_file.unlink(missing_ok=True)
                # 配置启动信息使进程完全独立
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE

                # 启动完全独立的服务器进程
                proc = subprocess.Popen(
                    command,
                    shell=True,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    close_fds=True,
                    creationflags=(
                            subprocess.CREATE_NEW_PROCESS_GROUP |
                            subprocess.DETACHED_PROCESS |
                            subprocess.CREATE_NO_WINDOW
                    ),
                    startupinfo=startupinfo
                )

                # 只记录PID，不保持进程引用
                cls._processes[world_id] = {"pid": proc.pid}
                cls._log(f"服务器 {world_id} 已启动 (PID: {proc.pid}) (Server {world_id} started with PID: {proc.pid})")
                # 立即释放进程引用，使子进程完全独立
                proc = None

                # 监控日志文件判断启动状态
                start_time = time.time()
                last_log_size = 0
                max_wait_time = cls._server_ready_timeout
                check_interval = 5  # 检查间隔(秒)
                cls._log("正在等待服务器就绪(Waiting for server ready)...")

                while time.time() - start_time < max_wait_time:
                    # 检查进程是否仍然存活
                    if world_id not in cls._processes or not cls._is_process_alive(cls._processes[world_id]["pid"]):
                        cls._log(f"服务器进程已意外终止 (Server process terminated unexpectedly)", warning=True)
                        break

                    # 检查日志文件
                    if log_file.exists():
                        try:
                            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                                # 只读取新增的日志内容
                                f.seek(last_log_size)
                                new_content = f.read()
                                last_log_size = f.tell()
                        except Exception as e:
                            cls._log(f"读取日志文件失败, 等待日志...(Failed to read log file, wait for log)")
                            time.sleep(check_interval)
                            continue

                        # 检查服务器就绪标志
                        if any(pattern in new_content for pattern in ready_patterns):
                            server_ready = True
                            cls._log(f"服务器 {world_id} 已就绪 (Server {world_id} is ready)")
                            break

                        # 检查错误日志
                        if any(error_pattern in new_content for error_pattern in error_patterns):
                            cls._log(
                                "获取模组服务失败，尝试重启服务器，如果频繁出现此问题，请前往本工具的模组配置页面一键安装证书...\n"
                                "Failed to query mod service, attempting to restart server. If this occurs frequently, "
                                "please go to the mod configuration page of this tool to install the certificate with one click...",
                                error=True
                            )
                            # 强制终止当前进程并重启
                            pid = cls._processes[world_id]["pid"]
                            subprocess.run(f"taskkill /F /T /PID {pid}", shell=True, check=True)
                            del cls._processes[world_id]
                            raise RuntimeError("Mod service error detected, restarting server")


                    time.sleep(check_interval)

                if server_ready:
                    return True

                # 如果超时或进程已终止，尝试终止进程
                try:
                    if world_id in cls._processes:
                        pid = cls._processes[world_id]["pid"]
                        subprocess.run(f"taskkill /F /T /PID {pid}", shell=True, check=True)
                        cls._log(
                            f"强制终止超时服务器进程 (PID: {pid}) (Force killed timeout server process (PID: {pid}))")
                except:
                    pass

            except RuntimeError as e:
                if "Mod service error" in str(e):
                    # 如果是模组服务错误导致的异常，减少重试计数以便立即重试
                    retry_count -= 1
                continue
            except Exception as e:
                cls._log(f"启动服务器 {world_id} 失败: {str(e)} (Failed to start server {world_id}: {str(e)})",
                         error=True)
                if world_id in cls._processes:
                    del cls._processes[world_id]

        # 达到最大重试次数仍未成功
        if not server_ready:
            cls._log(
                f"服务器 {world_id} 启动失败，已达到最大重试次数 {max_retries} (Server {world_id} failed to start after {max_retries} retries)",
                error=True)
        return server_ready

    @classmethod
    def _is_process_alive(cls, pid: int) -> bool:
        """检查指定PID的进程是否仍在运行"""
        try:
            # Windows系统使用tasklist命令检查
            result = subprocess.run(f'tasklist /FI "PID eq {pid}"',
                                    shell=True,
                                    capture_output=True,
                                    text=True)
            return str(pid) in result.stdout
        except Exception:
            return False

    @classmethod
    def stop(cls, world_id: str = None):
        """停止服务器进程"""
        if world_id:
            if world_id in cls._processes:
                cls._terminate_process(cls._processes[world_id])
                del cls._processes[world_id]
        else:
            for proc in cls._processes.values():
                cls._terminate_process(proc)
            cls._processes.clear()

    @classmethod
    def _get_server_executable(cls) -> str:
        """获取服务器可执行文件路径"""
        return os.path.join(
            ins_server_setting.root_path,
            "ShooterGame", "Binaries", "Win64", "ArkAscendedServer.exe"
        )

    @classmethod
    def _get_server_settings_file(cls) -> str:
        """获取服务器配置文件路径"""
        return os.path.join(
            ins_server_setting.root_path,
            "ShooterGame", "Saved", "Config", "WindowsServer", "GameUserSettings.ini"
        )

    @classmethod
    def _get_server_game_settings_file(cls) -> str:
        """获取服务器配置文件路径"""
        return os.path.join(
            ins_server_setting.root_path,
            "ShooterGame", "Saved", "Config", "WindowsServer", "Game.ini"
        )

    @classmethod
    def _write_game_user_settings(cls) -> bool:
        '''将非serversettings的模组内容写入Config
        Write non-serversettings mod content to Config'''
        # 处理GameUserSettings.ini
        settings_file = cls._get_server_settings_file()
        game_file = cls._get_server_game_settings_file()

        success = False

        # 写入GameUserSettings.ini
        cls._log("正在写入GameUserSettings.ini部分配置(Writing configuration for GameUserSettings.ini section...)...")
        if os.path.exists(settings_file):
            try:
                config = configparser.ConfigParser(strict=False)
                config.optionxform = str
                with open(settings_file, 'r', encoding='utf-8') as f:
                    config.read_file(f)

                all_section = ins_game_setting.get_all_section()
                for section_name in all_section:
                    if "_ARKToolTip" in section_name:
                        continue
                    if section_name == "ServerSettings":
                        continue

                    section_data = ins_game_setting.get_section(section_name)
                    if not section_data:
                        continue

                    if not config.has_section(section_name):
                        config.add_section(section_name)

                    for key, value in section_data.items():
                        config[section_name][key] = value

                with open(settings_file, 'w', encoding="utf-8") as f:
                    config.write(f)
                success = True
            except Exception as e:
                cls._log(f"写入GameUserSettings.ini失败(Failed to write GameUserSettings.ini): {str(e)}")

        # 处理Game.ini
        cls._log("正在写入Game.ini部分配置(Writing configuration for Game.ini section...)...")
        try:
            config = configparser.ConfigParser(strict=False)
            config.optionxform = str

            # 如果文件存在则读取现有内容
            if os.path.exists(game_file):
                with open(game_file, 'r', encoding='utf-8') as f:
                    config.read_file(f)

            # 写入Game.ini配置
            all_section = ins_game_ini_setting.get_all_section()
            has_changes = False

            for section_name in all_section:
                if "_ARKToolTip" in section_name:
                    continue

                section_data = ins_game_ini_setting.get_section(section_name)
                if not section_data:
                    continue

                if not config.has_section(section_name):
                    config.add_section(section_name)
                    has_changes = True

                for key, value in section_data.items():
                    if config.get(section_name, key, fallback=None) != value:
                        config[section_name][key] = value
                        has_changes = True

            # 只有有变更或文件不存在时才写入
            if has_changes or not os.path.exists(game_file):
                # 确保目录存在
                os.makedirs(os.path.dirname(game_file), exist_ok=True)

                with open(game_file, 'w', encoding="utf-8") as f:
                    config.write(f)
                success = True

        except Exception as e:
            cls._log(f"写入Game.ini失败(Failed to write Game.ini): {str(e)}")

        return success

    @classmethod
    def _build_server_command(cls, world_id: str, world_data: Dict[str, Any], server_exe: str) -> str:
        """构建完整的服务器启动命令"""
        world_params = cls._get_world_config(world_data["world_set"])
        server_params = cls._get_server_params(
            world_data["port"],
            world_data["rcon_port"],
            world_data["session_name"]
        )
        extra_params = cls._get_extra_params()
        mods_params = cls._get_mods_params()

        return (
            f'"{server_exe}" '
            f'{world_id}?listen?{world_params}?{server_params} '
            f'{extra_params} {mods_params} '
            f"-log={world_id}_server_tool.log"
        )

    @classmethod
    def _terminate_process(cls, process):
        """终止服务器进程"""
        try:
            process.terminate()
            process.wait(timeout=10)
            cls._log(f"已成功终止进程 (PID: {process.pid}) (Successfully terminated process (PID: {process.pid}))")
        except:
            try:
                process.kill()
                cls._log(f"已强制终止进程 (PID: {process.pid}) (Force killed process (PID: {process.pid}))")
            except:
                cls._log(f"终止进程失败 (PID: {process.pid}) (Failed to terminate process (PID: {process.pid}))",
                         error=True)

    @classmethod
    def _get_world_config(cls, world_set: str) -> str:
        """获取世界配置参数"""
        file_path = f"config/game_settings/{world_set}.ini"
        if not os.path.exists(file_path):
            cls._log(f"配置文件未找到！{world_set}.ini (Configuration file not found: {world_set}.ini)", error=True)
            raise FileNotFoundError(f"Config file not found: {world_set}.ini")

        config = configparser.ConfigParser()
        with open(file_path, 'r', encoding='utf-8') as f:
            config.read_file(f)

        if 'ServerSettings' not in config:
            cls._log(f"{world_set}.ini 没有 ServerSettings 段 ({world_set}.ini has no ServerSettings section)",
                     warning=True)
            return ""

        server_settings = config['ServerSettings']
        return "?".join(f"{k}={v}" for k, v in server_settings.items())

    @classmethod
    def _get_server_params(cls, port: int, rcon_port: int, session_name: str) -> str:
        """获取服务器基本参数"""
        return (
            f"Port={port}?"
            f"RCONPort={rcon_port}?"
            f"MaxPlayers={ins_server_setting.max_player}?"
            f"SessionName={session_name}?"
            f"ServerPassword={ins_server_setting.server_pwd}?"
            f"ServerAdminPassword={ins_server_setting.admin_pwd}"
        )

    @classmethod
    def _get_extra_params(cls) -> str:
        """获取额外参数"""
        params = []
        if not ins_server_setting.be_open:
            params.append("-NoBattlEye")
        if ins_server_setting.more_worlds_open:
            params.append(f"-ClusterID={ins_server_setting.cluster_id}")
            params.append(f'-ClusterDirOverride="{ins_server_setting.cluster_path}"')
        return " ".join(params)

    @classmethod
    def _get_mods_params(cls) -> str:
        """获取Mod参数"""
        if not ins_server_setting.mods_open:
            return ""

        mod_ids = [
            mod_id for mod_id, mod_data in ins_mods_setting.get_all().items()
            if mod_data["open"]
        ]
        return f"-mods={','.join(mod_ids)}" if mod_ids else ""

    @classmethod
    def _log_server_startup(cls, world_id: str, world_data: Dict[str, Any]):
        """记录服务器启动日志"""
        cls._log(
            f"准备开启服务器: \n" +
            cls.boxed_text(
                f"\n该世界服务器名称(SessionName): {world_data['session_name']}\n"
                f"世界信息(World Info): {world_id}-{world_data['name']}\n"
                f"端口(Port): {world_data['port']}\n"
                f"RCON端口(RCONPort): {world_data['rcon_port']}\n"
                f"世界配置文件(WorldConfig): {world_data['world_set']}\n"
                , border_char='║')
        )

    @classmethod
    def _log_startup_completion(cls):
        """记录启动完成日志"""
        cls._log(
            "服务器启动完成！等待全部弹出的黑色窗口左下角变成绿色标记并且提示Server Ready即可！(Server startup completed! Wait for all console windows to show green 'Server Ready' indicator!)")

    @classmethod
    def _log(cls, message: str, warning: bool = False, error: bool = False):
        """统一的日志记录方法"""
        log_type = "WARNING" if warning else ("ERROR" if error else "INFO")
        ins_tool_logger.add_log(f"{message}", log_type)

    @classmethod
    def boxed_text(cls, text, padding=1, border_char='#'):
        lines = text.split('\n')
        max_length = max(len(line) for line in lines)

        # 上边框（左边框 + 水平线，右边不闭合）
        top_border = border_char + (border_char * (max_length + 2 * padding))

        # 下边框（左边框 + 水平线，右边不闭合）
        bottom_border = border_char + (border_char * (max_length + 2 * padding))

        # 构建文本框
        box = []
        box.append(top_border)
        for line in lines:
            box.append(f"{border_char}{' ' * padding}{line.ljust(max_length)}{' ' * padding}")
        box.append(bottom_border)

        return '\n'.join(box)