import configparser
import os
import time

from app.models.ini_settings import ins_server_setting, ins_game_setting
from app.models.json_setting import ins_mods_setting, ins_world_info
from app.models.log_data import ins_tool_logger

class OpenServer:

    @staticmethod
    def start():
        # 获取服务器启动文件
        server_root = ins_server_setting.root_path
        server_exe = os.path.join(server_root, "ShooterGame", "Binaries", "Win64", "ArkAscendedServer.exe")
        # if not os.path.exists(server_exe):
        #     ins_tool_logger.add_log(f"********{server_exe}启动文件不存在!终止执行！(Error: {server_exe} startup file does not exist! Execution terminated!)")
        #     return
        # 获取拼接命令
        all_world = ins_world_info.get_all()
        ind = 0
        for this_world_id in all_world:
            if not all_world[this_world_id]["open"]:
                continue
            if ind != 0:
                ins_tool_logger.add_log(f"防止配置覆盖，等待60s后继续开启下一个世界！(To prevent configuration overwriting, waiting 60s before opening next world!)")
                time.sleep(60)

            ins_tool_logger.add_log(f'''准备开启服务器(Open Server)
            {this_world_id}-{all_world[this_world_id]['name']}
            Port:{all_world[this_world_id]['port']}
            RCONPort:{all_world[this_world_id]['rcon_port']}
            WorldConfig:{all_world[this_world_id]['world_set']}
            ''')

            # 获取其他参数
            run_command = OpenServer.get_command(this_world_id, all_world[this_world_id])
            # 拼接
            result_command = f'"{server_exe}" {run_command}'
            # 输出
            ins_tool_logger.add_log(f"(Executing startup command)执行启动命令:{result_command}")
            #
            ind += 1

        ins_tool_logger.add_log(f"服务器启动完成！等待全部弹出的黑色窗口左下角变成绿色标记并且提示Server Ready即可！(Server startup completed! Wait until all black windows show green indicator and 'Server Ready' message!)")

    @staticmethod
    def get_command(world_id, world_data):
        # 读取世界的数据
        port = world_data["port"]
        rcon_port = world_data["rcon_port"]
        world_set = world_data["world_set"]
        # 获取世界配置参数
        param_world_config = OpenServer.get_world_config(world_set)
        # 获取服务器配置，密码、等需要拼接的参数
        param_server_config = OpenServer.get_server_config_pj(port, rcon_port)
        # 获取额外参数
        param_server_config_ex = OpenServer.get_server_config_ex()
        # 获取模组配置
        param_mods = ""
        if ins_server_setting.mods_open:
            param_mods = OpenServer.get_mods_open()
        # 拼接
        result = f"{world_id}?listen?{param_world_config}?{param_server_config} {param_server_config_ex} {param_mods}"
        return result

    @staticmethod
    def get_mods_open():
        param_str = ""
        all_mods = ins_mods_setting.get_all()
        for mods_id in all_mods:
            if not all_mods[mods_id]["open"]:
                continue
            param_str += mods_id + ","
        if param_str:
            param_str = "-mods=" + param_str[:-1]
        return param_str

    @staticmethod
    def get_server_config_ex():
        cluster_id = ins_server_setting.cluster_id
        cluster_path = ins_server_setting.cluster_path
        be_open = ins_server_setting.be_open
        more_worlds_open = ins_server_setting.more_worlds_open
        #
        battleye_param = ""
        if not be_open:
            battleye_param = "-NoBattlEye"
        # 拼接
        if more_worlds_open:
            if battleye_param:
                param_str = f'-ClusterID={cluster_id} {battleye_param} -ClusterDirOverride="{cluster_path}"'
            else:
                param_str = f'-ClusterID={cluster_id} -ClusterDirOverride="{cluster_path}"'
        else:
            param_str = f"{battleye_param}"
        return param_str

    @staticmethod
    def get_server_config_pj(port, rcon_port):
        server_session_name = ins_server_setting.server_session_name
        server_pwd = ins_server_setting.server_pwd
        admin_pwd = ins_server_setting.admin_pwd
        max_player = ins_server_setting.max_player
        # # bAllowCrossARKTravel=True?bAllowCrossARKDataTransfers=True?bAllowCrossARKTribeData=True
        param_str = f"Port={port}?RCONPort={rcon_port}?MaxPlayers={max_player}?SessionName={server_session_name}?ServerPassword={server_pwd}?ServerAdminPassword={admin_pwd}"
        return param_str

    @staticmethod
    def get_world_config(world_set):
        '''
        获取服务器配置信息
        Get server configuration information
        :return:
        '''
        # 提取配置文件
        file_path = f"config/game_settings/{world_set}.ini"
        if not os.path.exists(file_path):
            ins_tool_logger.add_log(f"**************配置文件未找到！{world_set}.ini(Configuration file not found!)")
            raise Exception("error")
        # 读取config
        config = configparser.ConfigParser()
        with open(file_path, 'r', encoding='utf-8') as f:
            config.read_file(f)
        # 检查ServerSettings段是否存在
        if 'ServerSettings' not in config:
            ins_tool_logger.add_log(f"{world_set}.ini是空的，不修改任何服务器参数！({world_set}.ini is empty, no server parameters modified!)")
            return ""
        # 提取 看是否有值
        server_settings = config['ServerSettings']
        if not server_settings:
            ins_tool_logger.add_log(f"{world_set}.ini的ServerSettings是空的，不修改任何服务器参数！(ServerSettings in {world_set}.ini is empty, no server parameters modified!)")
            return ""
        # 参数串
        param_str = ""
        # 遍历所有值
        for key, value in server_settings.items():
            param_str += f"{key}={value}?"
        # 去掉最后一个问号
        param_str = param_str[:-1]
        return param_str