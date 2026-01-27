import os
import re
import traceback

from PySide6.QtCore import Signal
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QInputDialog, QHeaderView
from app.models.ini_settings import ins_game_setting
from app.ui_utils.base_page.base_page import BasePage
from src.ui.main_page.ui_main_page import Ui_MainPage


class MainPage_WorldConfigSet(BasePage, Ui_MainPage):

    update_world_config_signal = Signal()  # 新增信号
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_config = "default"  # 当前选中的配置文件(不带.ini)

    def ins_init(self):
        self.__setup_ui()
        self.__bind_events()
        self.__load_config_list()
        self.__load_config_data()

    def __setup_ui(self):
        """初始化UI设置(Initialize UI settings)"""
        # 设置表格属性(Set table properties)
        self.wc_show_world_setting.setColumnCount(4)
        self.wc_show_world_setting.setHorizontalHeaderLabels(["归属项(Section)", "配置项(Key)", "说明(Description)", "值(Value)"])
        self.wc_show_world_setting.horizontalHeader().setStretchLastSection(True)

        # 设置所有列内容靠左对齐(Set all columns left-aligned)
        for col in range(self.wc_show_world_setting.columnCount()):
            self.wc_show_world_setting.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
            self.wc_show_world_setting.horizontalHeaderItem(col).setTextAlignment(Qt.AlignLeft)

    def __bind_events(self):
        """绑定所有UI控件的事件(Bind all UI control events)"""

        # 禁止下拉框的滚轮事件
        self.wc_choose_config.setFocusPolicy(Qt.StrongFocus)  # 确保只有获得焦点时才能键盘操作
        self.wc_choose_config.wheelEvent = lambda event: None  # 禁用滚轮事件

        self.wc_choose_config.currentTextChanged.connect(self.__on_config_changed)
        self.wc_add_new_file.clicked.connect(self.__on_add_new_file)
        self.wc_save_change.clicked.connect(self.__on_save_changes)
        self.wc_add_row.clicked.connect(self.__on_add_row)
        self.wc_delete_row.clicked.connect(self.__on_delete_row)
        self.wc_copy_config.clicked.connect(self.__on_copy_config)

    def __update_to_other_tab(self):
        self.update_world_config_signal.emit()

    def __on_copy_config(self):
        """复制当前配置(Copy current config)"""
        # 1. 获取当前配置文件名
        current_config = self.current_config
        if not current_config:
            self.message_box(
                "没有选中任何配置!\n(No config selected!)"
            )
            return

        # 2. 弹出输入对话框获取新配置名
        new_name, ok = self.input_dialog(
            "复制配置(Copy Config)",
            "请输入新配置名称(不需要.ini后缀):\n(Enter new config name without .ini suffix):",
            f"{current_config}_copy"
        )

        if not ok or not new_name:
            return

        # 3. 验证文件名合法性
        if not re.match(r'^[a-zA-Z0-9_\-]+$', new_name):
            self.message_box(
                "配置名称只能包含字母、数字、下划线和连字符\n(Config name can only contain letters, numbers, underscores and hyphens)"
            )
            return

        # 4. 检查是否已存在
        new_file_path = f"config/game_settings/{new_name}.ini"
        if os.path.exists(new_file_path):
            self.message_box(
                f"配置 {new_name} 已存在!\n(Config {new_name} already exists!)"
            )
            return

        # 5. 复制文件
        try:
            current_file_path = f"config/game_settings/{current_config}.ini"

            # 读取当前文件内容
            with open(current_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # 6. 更新下拉框并选中新文件
            self.__load_config_list()
            index = self.wc_choose_config.findText(new_name)
            if index >= 0:
                self.wc_choose_config.setCurrentIndex(index)

            self.message_box(
                f"已从 {current_config} 创建新配置: {new_name}\n(Created new config {new_name} from {current_config})",
                "成功(Success)"
            )

            # 更新到其他页面
            self.__update_to_other_tab()

        except Exception as e:
            self.message_box(
                f"复制配置失败: {str(e)}\n(Failed to copy config: {str(e)})"
            )

    def __load_config_list(self):
        """加载所有配置文件列表到下拉框(Load all config files to dropdown)"""
        self.wc_choose_config.clear()
        config_dir = "config/game_settings"

        if os.path.exists(config_dir):
            for file in os.listdir(config_dir):
                if file.endswith(".ini"):
                    config_name = file[:-4]  # 去掉.ini后缀(remove .ini suffix)
                    self.wc_choose_config.addItem(config_name)

        # 设置当前选中项(Set current selection)
        index = self.wc_choose_config.findText(self.current_config)
        if index >= 0:
            self.wc_choose_config.setCurrentIndex(index)

    def __load_config_data(self):
        """加载当前选中的配置文件数据到表格(Load selected config data to table)"""
        # 先清空表格
        self.wc_show_world_setting.setRowCount(0)
        # 获取全部section
        all_section = ins_game_setting.get_all_section()
        for section_name in all_section:
            if "_ARKToolTip" in section_name:
                continue
            # 获取ServerSettings和Tip数据(Get ServerSettings and Tip data)
            server_settings = ins_game_setting.get_section(section_name)
            tips = ins_game_setting.get_section(f"{section_name}_ARKToolTip")

            # 如果ServerSettings为空，则不显示任何内容
            if not server_settings:
                continue

            # 确保Tip部分存在且与ServerSettings键一致
            if not tips:
                tips = {key: f"请添加{key}的说明(Please add description for {key})"
                        for key in server_settings.keys()}

            # 填充表格(Populate table)
            for key, value in server_settings.items():
                row_position = self.wc_show_world_setting.rowCount()
                self.wc_show_world_setting.insertRow(row_position)

                # 归属项(Section)
                section_item = QTableWidgetItem(section_name)
                section_item.setTextAlignment(Qt.AlignLeft)
                self.wc_show_world_setting.setItem(row_position, 0, section_item)

                # 配置项(Key)
                key_item = QTableWidgetItem(key)
                key_item.setTextAlignment(Qt.AlignLeft)
                self.wc_show_world_setting.setItem(row_position, 1, key_item)

                # 说明(Description)
                tip_item = QTableWidgetItem(tips.get(key, ""))
                tip_item.setTextAlignment(Qt.AlignLeft)
                self.wc_show_world_setting.setItem(row_position, 2, tip_item)

                # 值(Value)
                value_item = QTableWidgetItem(value)
                value_item.setTextAlignment(Qt.AlignLeft)
                self.wc_show_world_setting.setItem(row_position, 3, value_item)

    def __on_config_changed(self, config_name):
        """当下拉框选择改变时(When dropdown selection changes)"""
        if config_name:
            self.current_config = config_name
            # 切换配置文件路径
            ins_game_setting.change_config_path(config_name)
            # 重置表格
            self.wc_show_world_setting.setRowCount(0)
            # 重新加载数据
            self.__load_config_data()

    def __on_add_new_file(self):
        """添加新配置文件(Add new config file)"""
        new_name, ok = self.input_dialog(
            "新建配置(Create New Config)",
            "请输入配置名称(不需要.ini后缀):\n(Enter config name without .ini suffix):",
            "new_config"
        )

        if ok and new_name:
            # 验证文件名合法性(Validate filename)
            if not re.match(r'^[a-zA-Z0-9_\-]+$', new_name):
                self.message_box(
                    "配置名称只能包含字母、数字、下划线和连字符\n(Config name can only contain letters, numbers, underscores and hyphens)"
                )
                return

            # 检查是否已存在(Check if already exists)
            file_path = f"config/game_settings/{new_name}.ini"
            if os.path.exists(file_path):
                self.message_box(
                    f"配置 {new_name} 已存在!\n(Config {new_name} already exists!)"
                )
                return

            # 创建空文件(Create empty file)
            try:
                os.makedirs("config/game_settings", exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write("[ServerSettings]\n[Tip]\n")

                # 更新下拉框并选中新文件(Update dropdown and select new file)
                self.__load_config_list()
                index = self.wc_choose_config.findText(new_name)
                if index >= 0:
                    self.wc_choose_config.setCurrentIndex(index)

                self.message_box(
                    f"已创建新配置: {new_name}\n(New config created: {new_name})"
                )

                # 更新到其他页面
                self.__update_to_other_tab()

            except Exception as e:
                self.message_box(
                    f"创建配置失败: {str(e)}\n(Failed to create config: {str(e)})"
                )

    def __on_save_changes(self):
        """保存表格中的修改到当前配置文件(Save table changes to current config)"""
        try:
            server_settings = {}
            tips = {}

            # 收集表格中的数据(Collect data from table)
            for row in range(self.wc_show_world_setting.rowCount()):
                section = self.wc_show_world_setting.item(row, 0).text()
                key = self.wc_show_world_setting.item(row, 1).text()
                tip = self.wc_show_world_setting.item(row, 2).text()
                value = self.wc_show_world_setting.item(row, 3).text()

                server_settings.setdefault(section, {})
                tips.setdefault(f"{section}_ARKToolTip", {})

                server_settings[section][key] = value
                tips[f"{section}_ARKToolTip"][key] = tip

            for section in server_settings.keys():
                # 更新到配置(Update to config)
                ins_game_setting.update_section(section, server_settings[section])
                ins_game_setting.update_section(f"{section}_ARKToolTip", tips[f"{section}_ARKToolTip"])

            self.message_box(
                "配置已保存!\n(Config saved successfully!)"
            )
        except Exception as e:
            self.message_box(
                f"保存失败: {str(e)}\n(Save failed: {str(e)})"
            )
            print(traceback.format_exc())

    def __on_add_row(self):
        """添加新行(Add new row)"""
        row_position = self.wc_show_world_setting.rowCount()
        self.wc_show_world_setting.insertRow(row_position)

        # 归属项(Section)
        section_item = QTableWidgetItem("")
        section_item.setTextAlignment(Qt.AlignLeft)
        self.wc_show_world_setting.setItem(row_position, 0, section_item)

        # 配置项(Key)
        key_item = QTableWidgetItem("")
        key_item.setTextAlignment(Qt.AlignLeft)
        self.wc_show_world_setting.setItem(row_position, 1, key_item)

        # 说明(Description)
        tip_item = QTableWidgetItem("")
        tip_item.setTextAlignment(Qt.AlignLeft)
        self.wc_show_world_setting.setItem(row_position, 2, tip_item)

        # 值(Value)
        value_item = QTableWidgetItem("")
        value_item.setTextAlignment(Qt.AlignLeft)
        self.wc_show_world_setting.setItem(row_position, 3, value_item)

        # 滚动到最后一行(Scroll to bottom)
        self.wc_show_world_setting.scrollToBottom()

    def __on_delete_row(self):
        """删除选中行(Delete selected row)"""
        selected_rows = self.wc_show_world_setting.selectionModel().selectedRows()

        if not selected_rows:
            self.message_box(
                "请先选择要删除的行!\n(Please select a row to delete first!)"
            )
            return

        if len(selected_rows) > 1:
            self.message_box(
                "每次只能删除一行!\n(Can only delete one row at a time!)"
            )
            return
        row = selected_rows[0].row()
        # 获取section和key
        section = self.wc_show_world_setting.item(row, 0).text()
        key = self.wc_show_world_setting.item(row, 1).text()
        # tip
        tip_section = f"{section}_ARKToolTip"
        # 删除
        ins_game_setting.delete(section, key)
        ins_game_setting.delete(tip_section, key)

        self.wc_show_world_setting.removeRow(row)