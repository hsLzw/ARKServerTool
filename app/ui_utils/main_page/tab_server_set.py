from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QMessageBox

from app.ui_utils.base_page.base_page import BasePage
from src.ui.main_page.ui_main_page import Ui_MainPage


class MainPage_ServerSet(BasePage, Ui_MainPage):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._bind_events()

    def _bind_events(self):
        """绑定所有UI控件的事件"""
        # 按钮点击事件
        pass
