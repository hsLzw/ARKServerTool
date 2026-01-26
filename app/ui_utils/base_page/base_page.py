from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QMessageBox


class BasePage(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

    def _bind_events(self):
        """绑定所有UI控件的事件"""
        # 按钮点击事件
        pass
