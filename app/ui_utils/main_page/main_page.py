from app.ui_utils.main_page.tab_mods_set import MainPage_ModsSet
from app.ui_utils.main_page.tab_server_open import MainPage_ServerOpen
from app.ui_utils.main_page.tab_tool_log import MainPage_ToolLog
from app.ui_utils.main_page.tab_world_config_set import MainPage_WorldConfigSet


class MainPage(MainPage_ServerOpen, MainPage_WorldConfigSet, MainPage_ModsSet, MainPage_ToolLog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 初始化各页面
        MainPage_ServerOpen.ins_init(self)
        MainPage_WorldConfigSet.ins_init(self)
        MainPage_ModsSet.ins_init(self)
        # 连接信号
        self.update_world_config_signal.connect(self.cross_update_show_world_config)
        MainPage_ToolLog.ins_init(self)
        self.main_tabWidget.setCurrentIndex(0)

    def cross_update_show_world_config(self):
        '''跨tab界面的子类调用的，更新配置文件'''
        MainPage_ServerOpen.refresh_world_config_options(self)



