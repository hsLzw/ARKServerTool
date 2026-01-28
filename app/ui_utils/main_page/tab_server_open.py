import os
import re
import traceback
from typing import Tuple, Optional, Dict
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtWidgets import QMessageBox

from app.models.ini_settings import ins_server_setting
from app.models.json_setting import ins_world_info
from app.models.log_data import ins_tool_logger
from app.ui_utils.main_page.server_open_page.tab_server_open_widget import ServerOpen_Widget
from app.utils.start_game import OpenServer
from PySide6.QtCore import QThread, Signal, QObject

class ServerWorker(QObject):
    """
    服务器工作线程
    """

    reset_button = Signal(bool)
    self_finished = Signal()

    def run(self):
        ins_tool_logger.add_log("Start...")
        try:
            OpenServer.start()  # 执行耗时操作
        except Exception as e:
            ins_tool_logger.add_log(traceback.format_exc())
        finally:
            self.reset_button.emit(True)
        # 提示界面可以在此点击开始了
        self.self_finished.emit()
        ins_tool_logger.add_log("End...")
        # 退出
        self.thread().quit()

class MainPage_ServerOpen(ServerOpen_Widget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.choose_root = ""
        self.choose_cluster_path = ""
        self.worker_thread = None
        self.worker = None
        self.worker_finished = True

    def ins_init(self):
        MainPage_ServerOpen.widget_init(self)
        self.__init_data()
        self.__bind_events()



    def __bind_events(self):
        """绑定所有UI控件的事件"""
        # 获取服务器路径
        self.choose_server_root.clicked.connect(self.__on_choose_server_root)
        # 获取cluster路径
        self.choose_cluster_path_btn.clicked.connect(self.__on_choose_cluster_path)
        # 保存输入
        self.save_set_input.clicked.connect(self.__save_set_input_data)
        # 提示
        self.cluster_id_ask.clicked.connect(self.__ask_info_cluster_id)
        self.cluster_path_ask.clicked.connect(self.__ask_info_cluster_path)
        # 开始游戏
        self.run_button.clicked.connect(self.__run_server)

    def __init_data(self):
        self.__init_param_info()

    def __init_param_info(self):
        # 服务器路径
        self.server_root.setText(ins_server_setting.root_path)
        self.choose_root = ins_server_setting.root_path
        # 设置be选择
        self.open_param_be.setChecked(ins_server_setting.be_open)
        # 设置mods选择
        self.open_param_mods.setChecked(ins_server_setting.mods_open)
        # 设置多世界选择
        self.open_param_mworlds.setChecked(ins_server_setting.more_worlds_open)
        # 设置账号密码等数据
        self.server_pwd.setText(ins_server_setting.server_pwd)
        self.admin_pwd.setText(ins_server_setting.admin_pwd)
        self.max_player.setValue(ins_server_setting.max_player)
        self.server_session_name.setText(ins_server_setting.server_session_name)
        self.cluster_id.setText(ins_server_setting.cluster_id)
        # cluster路径
        self.cluster_path.setText(ins_server_setting.cluster_path)
        self.choose_cluster_path = ins_server_setting.cluster_path

    def __ask_info_cluster_id(self):
        self.message_box(
            "多通存档ID是用于多通世界的，他们共同指向一个ClusterID才可以。(ClusterID is used in the multi-world system. They must all point to the same ClusterID in order to be valid.)")

    def __ask_info_cluster_path(self):
        self.message_box(
            "多通数据路径是用于多通世界的，跨世界存档转移时，数据会存到这里！。(ClusterPath is used for multi-world scenarios. During cross-world save file transfer, the data will be stored here!)")

    def __on_choose_server_root(self):
        """处理选择服务器根目录按钮点击事件"""
        # 弹出文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "选择服务器根目录(Choose server root path)",
            ins_server_setting.root_path,  # 起始目录为空表示默认
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        # 只有当选择了有效路径时才更新显示
        if folder_path:
            self.server_root.setText(folder_path)
            self.choose_root = folder_path

    def __on_choose_cluster_path(self):
        """处理选择服务器根目录按钮点击事件"""
        # 弹出文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "选择cluster路径(Choose cluster path)",
            ins_server_setting.root_path,  # 起始目录为空表示默认
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        # 只有当选择了有效路径时才更新显示
        if folder_path:
            self.cluster_path.setText(folder_path)
            self.choose_cluster_path = folder_path

    def __save_set_input_data(self, ignore_success_tip=False):
        # 判断路径
        if not self.choose_root:
            self.message_box("请选择服务器路径！(Choose Server Root Pls!)", button_yes_text="OK")
            return False
        # 提取输入文字
        server_pwd = self.server_pwd.text()
        admin_pwd = self.admin_pwd.text()
        max_player = self.max_player.value()
        cluster_id = self.cluster_id.text()
        cluster_path = self.cluster_path.text()
        server_session_name = self.server_session_name.text()
        # 验证所有字段
        is_valid, errors = self.__validate_all_fields(
            server_pwd=server_pwd,
            admin_pwd=admin_pwd,
            max_player=max_player,
            cluster_id=cluster_id,
            cluster_path=cluster_path,
            server_session_name=server_session_name
        )
        if not is_valid:
            self.message_box(errors, button_yes_text="OK")
            return False
        # 如果没有Cluter_id
        if not cluster_id:
            cluster_id = "Cluster_01"
            self.cluster_id.setText(cluster_id)
        # 如果没有路径
        if not self.choose_cluster_path:
            self.choose_cluster_path = os.path.join(self.choose_root, cluster_id)
            if not os.path.exists(self.choose_cluster_path):
                os.mkdir(self.choose_cluster_path)
            self.cluster_path.setText(self.choose_cluster_path)
        # 开始写入
        ins_server_setting.set_server_pwd(server_pwd)
        ins_server_setting.set_admin_pwd(admin_pwd)
        ins_server_setting.set_max_player(int(max_player))
        ins_server_setting.set_cluster_id(cluster_id)
        ins_server_setting.set_cluster_path(self.choose_cluster_path)
        ins_server_setting.set_server_session_name(server_session_name)
        # 服务器路径
        ins_server_setting.set_root_path(self.choose_root)
        # 三个多选框
        ins_server_setting.set_be_open(self.open_param_be.isChecked())
        ins_server_setting.set_mods_open(self.open_param_mods.isChecked())
        ins_server_setting.set_more_worlds_open(self.open_param_mworlds.isChecked())
        # 保存
        ins_server_setting.save()
        if not ignore_success_tip:
            self.message_box("配置保存成功！(Save Success!)", button_yes_text="OK")
        return True

    def __validate_pwd(self, pwd: str, field_name: str) -> Tuple[bool, Optional[str]]:
        """验证密码格式（仅英文+数字）

        参数:
            pwd: 待验证的密码字符串
            field_name: 字段名称（用于错误提示）

        返回:
            Tuple[是否有效, 错误信息]
        """
        if not re.match(r'^[a-zA-Z0-9]+$', pwd):
            return False, f"密码只能包含字母和数字(password only number or letters)"
        return True, ""

    def __validate_max_player(self, max_player: str) -> Tuple[bool, Optional[str]]:
        """验证最大玩家数

        参数:
            max_player: 待验证的字符串

        返回:
            Tuple[是否有效, 错误信息]
        """
        try:
            num = int(max_player)
            if num <= 0:
                return False, "最大玩家数必须大于0(Max player must be greater than 0)"
            return True, ""
        except ValueError:
            return False, "请输入有效的数字(Max player must be integer)"

    def __validate_cluster_id(self, cluster_id: str) -> Tuple[bool, Optional[str]]:
        """验证并处理集群数据

        参数:
            cluster_id: 待验证的字符串

        返回:
            Tuple[处理后的值, 错误信息]
        """
        if not re.match(r'^[a-zA-Z0-9_]+$', cluster_id):
            return False, "集群ID只能包含字母、数字和下划线(Cluster ID only number or letters or _)"
        return True, ""

    def __validate_cluster_path(self, cluster_path: str) -> Tuple[bool, Optional[str]]:
        """验证并处理集群路径

        参数:
            cluster_path: 待验证的字符串
            default_root: 默认根路径

        返回:
            Tuple[处理后的值, 错误信息]
        """
        if not os.path.exists(cluster_path):
            return False, "多通数据路径不存在！(Cluster Path does not exist)"
        return True, ""

    def __validate_all_fields(
            self,
            server_pwd: str,
            admin_pwd: str,
            max_player: str,
            cluster_id: str,
            cluster_path: str,
            server_session_name: str
    ) -> Tuple[bool, str]:
        """验证所有字段

        参数:
            server_pwd: 服务器密码
            admin_pwd: 管理员密码
            max_player: 最大玩家数
            cluster_id: 集群ID
            cluster_path: 集群路径
            default_root: 默认根路径

        返回:
            Tuple[是否全部有效, 处理后的字段值, 错误信息]
        """
        errors = {}
        validated = {}

        # 验证密码
        valid, err = self.__validate_pwd(server_pwd, "服务器密码(server_pwd)")
        if not valid:
            return False, err

        valid, err = self.__validate_pwd(admin_pwd, "管理员密码")
        if not valid:
            return False, err

        # 验证最大玩家数
        valid, err = self.__validate_max_player(max_player)
        if not valid:
            return False, err

        # 验证集群ID
        if cluster_id:
            valid, err = self.__validate_cluster_id(cluster_id)
            if not valid:
                return False, err

        if cluster_id and not cluster_path:
            return False, "填写存档ID则必须填写存档路径,两个都不填写则自动设置默认路径！(To fill in the Cluter ID, you must provide the Cluster path. If neither is filled in, the default path will be automatically set!)"

        # 验证集群路径
        if cluster_path:
            valid, err = self.__validate_cluster_path(cluster_path)
            if not valid:
                return False, err

        return True, ""

    def __run_server(self):
        self.__set_run_button(False)
        # if not self.message_box(
        #     "启动游戏将会保存所有配置，是否继续？(Starting the game will save all settings. Do you want to continue?)",
        #         button_yes_text="是(Continue)",
        #         button_no_text="否(Cancel)"):
        #     return
        # 保存输入配置
        input_flag = self.__save_set_input_data(True)
        if not input_flag:
            self.message_box("配置存在问题，游戏启动失败！(There is a problem with the configuration, and the game failed to launch!)")
            self.__set_run_button(True)
            return
        # 保存地图配置
        map_flag = self.public_server_map_save()
        if not map_flag:
            self.message_box("配置存在问题，游戏启动失败！(There is a problem with the configuration, and the game failed to launch!)")
            self.__set_run_button(True)
            return

        # 提取开启地图数量
        world_data = ins_world_info.get_all()
        # 遍历
        open_counts = 0
        for map_id in world_data:
            if world_data[map_id]["open"]:
                open_counts += 1
        # 如果还是0
        if open_counts <= 0:
            self.message_box("你必须先选则至少一个地图才能开启服务器！(You must select at least one map before you can start the server!)")
            self.__set_run_button(True)
            return
        # 判断地图选择
        if open_counts > 1 and not self.open_param_mworlds.isChecked():
            self.message_box("开启多个地图必须开启[多通世界]选项！或者只开启一个地图！(To open multiple maps, you must enable the [More World Open] option! Or you can just open one map!)")
            self.__set_run_button(True)
            return
        # 大于1个世界给出提示
        if open_counts > 1:
            message_tip = f"你开启了{open_counts}个世界，每个世界大概会占用10G内存，点击确认继续启动服务器！(You have opened {open_counts} worlds. Each world will approximately occupy 10G of memory. Click 'Confirm' to continue and start the server!)"
            if not self.message_box(message_tip, button_yes_text="确认(Confirm)", button_no_text="取消(Cancel)"):
                self.__set_run_button(True)
                return

        if not self.worker_finished:
            self.message_box("服务器正在启动中，请稍候(Server is opening, please wait...)")
            return
        # 服务器开启
        self.worker_thread = QThread()
        self.worker_thread.finished.connect(lambda: self.worker_thread.deleteLater())
        self.worker = ServerWorker()
        self.worker_thread.started.connect(self.worker.run)
        self.worker.reset_button.connect(self.__set_run_button)
        self.worker.self_finished.connect(self.__set_finished_status)

        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.worker_finished = False
        self.main_tabWidget.setCurrentIndex(3)

    def __set_run_button(self, is_ok):
        if is_ok:
            self.run_button.setEnabled(True)
            self.run_button.setText("启动(RUN)")
        else:
            self.run_button.setEnabled(False)
            self.run_button.setText("启动中(Running)")

    def __set_finished_status(self):
        self.worker_finished = True


