import configparser
import os
import time
import subprocess
import psutil
from typing import Dict, Any

from app.models.ini_settings import ins_server_setting, ins_game_setting
from app.models.json_setting import ins_mods_setting, ins_world_info
from app.models.log_data import ins_tool_logger


class OpenServer:
    _processes = {}  # 保存所有服务器进程

    @classmethod
    def start(cls):
        """启动所有配置开启的世界服务器（非阻塞方式）"""
        server_exe = cls._get_server_executable()
        if not os.path.exists(server_exe):
            cls._log(f"{server_exe} 不存在(does not exist)", error=True)
            return
        all_worlds = ins_world_info.get_all()

        for idx, (world_id, world_data) in enumerate(all_worlds.items()):
            if not world_data["open"]:
                continue

            if idx > 0:
                cls._log_wait_between_servers()
                time.sleep(60)

            cls._log_server_startup(world_id, world_data)
            command = cls._build_server_command(world_id, world_data, server_exe)
            cls._write_game_user_settings()
            cls._launch_server(world_id, command)

        cls._log_startup_completion()

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
    def _write_game_user_settings(cls):
        '''将非serversettings的模组内容写入Config'''
        settings_file = cls._get_server_settings_file()
        if not os.path.exists(settings_file):
            cls._log('''
            *****************************
            注意，无法找到GameUserSettings.ini, 可能这是你首次启动游戏，无法正常运行游戏，请关闭所有服务器并重新启动
            GameUserSettings.ini将会在首次启动服务器exe程序后进行创建，若您是首次启动，重启即可。
            
            Warning: Could not locate GameUserSettings.ini. This may be your first time launching the game. The game cannot run properly under these conditions. Please shut down all servers and restart.
            GameUserSettings.ini will be automatically created during the first launch of the server executable. If this is your first launch, simply restart the application.
            *****************************''')
            return
        # 找到了文件，读取文件
        config = configparser.ConfigParser()
        config.optionxform = str
        if os.path.exists(settings_file):
            with open(settings_file, 'r', encoding='utf-8') as f:
                config.read_file(f)
        # 获取服务器配置中的全部内容
        all_section = ins_game_setting.get_all_section()
        for section_name in all_section:
            if "_ARKToolTip" in section_name:
                continue
            # ServerSettings走参数
            if section_name == "ServerSettings":
                continue
            # 获取ServerSettings数据
            section_data = ins_game_setting.get_section(section_name)
            # 空section跳过
            if not section_data:
                continue
            # 如果section不存在则创建
            if not config.has_section(section_name):
                config.add_section(section_name)
            # 合并键值对
            for key, value in section_data.items():
                config[section_name][key] = value
        # 写入文件
        with open(settings_file, 'w', encoding="utf-8") as f:
            config.write(f)

        return True

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
            f'{extra_params} {mods_params}'
        )

    @classmethod
    def _launch_server(cls, world_id: str, command: str):
        """启动服务器进程（非阻塞）"""
        try:
            # 创建独立的进程组，确保进程独立运行
            creationflags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS

            # 启动进程
            proc = subprocess.Popen(
                command,
                shell=True,
                creationflags=creationflags,
                close_fds=True
            )

            # 设置进程优先级为高
            try:
                p = psutil.Process(proc.pid)
                p.nice(psutil.HIGH_PRIORITY_CLASS)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

            cls._processes[world_id] = proc
            cls._log(" ".join(command))
            cls._log(f"服务器 {world_id} 已启动 (PID: {proc.pid}) (Server {world_id} started with PID: {proc.pid})")

        except Exception as e:
            cls._log(f"启动服务器 {world_id} 失败: {str(e)} (Failed to start server {world_id}: {str(e)})", error=True)
            raise

    @classmethod
    def _terminate_process(cls, process):
        """终止服务器进程"""
        try:
            process.terminate()
            process.wait(timeout=10)
        except:
            try:
                process.kill()
            except:
                pass

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
    def _log_wait_between_servers(cls):
        """记录等待日志"""
        cls._log(
            "防止配置覆盖，等待60s后继续开启下一个世界！(To prevent configuration conflicts, waiting 60s before starting next world!)")

    @classmethod
    def _log_server_startup(cls, world_id: str, world_data: Dict[str, Any]):
        """记录服务器启动日志"""
        cls._log(
            f"准备开启服务器: {world_id}-{world_data['name']}\n"
            f"Port: {world_data['port']}\n"
            f"RCONPort: {world_data['rcon_port']}\n"
            f"WorldConfig: {world_data['world_set']}\n"
            f"(Preparing to start server: {world_id}-{world_data['name']}\n"
            f"Port: {world_data['port']}\n"
            f"RCONPort: {world_data['rcon_port']}\n"
            f"WorldConfig: {world_data['world_set']})"
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