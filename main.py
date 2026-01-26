import sys
from PySide6.QtWidgets import QApplication

from app.ui_utils.main_page.main_page import MainPage

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建并显示主窗口
    window = MainPage()
    window.show()

    sys.exit(app.exec())

# 测试提交
