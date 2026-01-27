import hashlib
import os
import re
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QInputDialog, QHeaderView
from app.models.ini_settings import ins_game_setting
from app.models.log_data import ins_tool_logger
from app.ui_utils.base_page.base_page import BasePage
from src.ui.main_page.ui_main_page import Ui_MainPage
from PySide6.QtCore import QObject, Signal, QThread, QTimer
from PySide6.QtGui import Qt, QTextCursor


class LogWorker(QObject):
    """日志工作线程（带MD5去重）"""
    log_updated = Signal(str)  # 日志更新信号

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_logs)
        self.timer.start(1000)  # 1秒触发一次
        self.last_md5 = None  # 保存上一次日志的MD5值

    def fetch_logs(self):
        """获取日志并检查变化"""
        all_logs = ins_tool_logger.get_all_logs()
        log_text = "\n".join(
            f"[{log['timestamp']}] {log['type'].upper()}: {log['content']}"
            for log in all_logs
        )

        # 计算当前日志的MD5
        current_md5 = hashlib.md5(log_text.encode('utf-8')).hexdigest()

        # 仅当MD5变化时发送信号
        if current_md5 != self.last_md5:
            self.log_updated.emit(log_text)
            self.last_md5 = current_md5  # 更新MD5记录


class MainPage_ToolLog(BasePage, Ui_MainPage):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.log_worker = None

    def ins_init(self):
        self.log_thread = QThread()
        self.log_worker = LogWorker()

        self.log_worker.moveToThread(self.log_thread)
        self.log_worker.log_updated.connect(self.update_log_display)
        self.log_thread.start()


    def update_log_display(self, log_text):
        """更新日志显示（主线程执行）"""
        # 保存当前滚动条位置
        scrollbar = self.mp_show_logs.verticalScrollBar()
        at_bottom = scrollbar.value() == scrollbar.maximum()

        # 更新文本
        self.mp_show_logs.setPlainText(log_text)

        # 如果之前已经在底部，则保持滚动到底部
        if at_bottom:
            cursor = self.mp_show_logs.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.mp_show_logs.setTextCursor(cursor)
            self.mp_show_logs.ensureCursorVisible()

    def closeEvent(self, event):
        """清理资源"""
        self.log_thread.quit()
        self.log_thread.wait()
        super().closeEvent(event)



















