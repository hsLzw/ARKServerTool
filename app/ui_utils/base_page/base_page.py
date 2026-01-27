from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog
from PySide6.QtCore import Qt


class BasePage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def message_box(self,
                    content="",
                    title="提示",
                    button_yes_text="是",
                    button_no_text="",
                    message_type=QMessageBox.Information,
                    default_button=QMessageBox.Yes):
        """
        通用消息框方法

        参数:
            content (str): 消息内容
            title (str): 标题
            button_yes_text (str): 确认按钮文本
            button_no_text (str): 取消按钮文本（为空则只显示确认按钮）
            message_type (QMessageBox.Icon): 消息类型
                - QMessageBox.Information
                - QMessageBox.Warning
                - QMessageBox.Critical
                - QMessageBox.Question
            default_button (QMessageBox.StandardButton): 默认选中按钮

        返回:
            bool:
                - True: 用户点击了确认按钮 (Yes/OK)
                - False: 用户点击了取消按钮 (No/Cancel)
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(content)
        msg_box.setIcon(message_type)

        # 根据是否有取消按钮决定按钮组合
        if button_no_text:
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setButtonText(QMessageBox.No, button_no_text)
        else:
            msg_box.setStandardButtons(QMessageBox.Ok)
            button_yes_text = "确定"  # 单按钮时默认使用"确定"

        # 设置确认按钮文本
        msg_box.setButtonText(QMessageBox.Yes if button_no_text else QMessageBox.Ok, button_yes_text)
        msg_box.setDefaultButton(default_button)

        # 设置窗口模态
        msg_box.setWindowModality(Qt.ApplicationModal)

        # 执行消息框并返回布尔结果
        result = msg_box.exec()
        return result == QMessageBox.Yes or result == QMessageBox.Ok


    def input_dialog(self, title, label, default_text=""):

        new_name, ok = QInputDialog.getText(
            self,
            "复制配置(Copy Config)",
            "请输入新配置名称(不需要.ini后缀):\n(Enter new config name without .ini suffix):",
            text=default_text
        )
        return new_name, ok

