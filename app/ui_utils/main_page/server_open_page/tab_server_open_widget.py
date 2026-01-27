import os
import re
from typing import Tuple, Optional, Dict
from PySide6.QtWidgets import (QDialog, QFileDialog, QTableWidgetItem,
                               QHeaderView, QMessageBox, QTableWidget, QComboBox)
from PySide6.QtCore import Qt
from app.models.json_setting import ins_world_info
from app.ui_utils.base_page.base_page import BasePage
from src.ui.main_page.ui_main_page import Ui_MainPage


class ServerOpen_Widget(BasePage, Ui_MainPage):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._world_config_options = []  # 存储世界配置选项

    def widget_init(self):
        self.__setup_ui()
        self.__connect_signals()
        self.__load_world_data()
        self.refresh_world_config_options()  # 初始化时加载一次配置


    def refresh_world_config_options(self):
        """刷新世界配置选项并更新UI"""
        config_dir = "config/game_settings"
        old_options = self._world_config_options.copy()
        self._world_config_options = ["default"]  # 默认包含default

        try:
            if os.path.exists(config_dir):
                for file in os.listdir(config_dir):
                    if file.endswith(".ini"):
                        config_name = file[:-4]  # 去掉.ini后缀
                        if config_name != "default":  # 避免重复添加default
                            self._world_config_options.append(config_name)

            # 检查default.ini是否存在
            if not os.path.exists(os.path.join(config_dir, "default.ini")):
                self.message_box("default.ini配置丢失", "错误(Error)", message_type=QMessageBox.Critical)

            # 如果选项有变化，则更新UI
            if old_options != self._world_config_options:
                self.__update_world_config_comboboxes()

        except Exception as e:
            self.message_box(f"加载配置失败: {str(e)}", "错误(Error)", message_type=QMessageBox.Critical)

    def __update_world_config_comboboxes(self):
        """更新所有行的世界配置下拉框，并保留原来的选择"""
        for row in range(self.choose_world_show.rowCount()):
            combo = self.choose_world_show.cellWidget(row, 5)
            if combo:
                # 获取当前选择的值
                current_value = combo.currentText()

                # 保存当前下拉框的信号连接
                # 我们需要先断开信号，否则clear()会触发信号
                combo.blockSignals(True)

                # 更新下拉框选项
                combo.clear()
                combo.addItems(self._world_config_options)

                # 尝试恢复原来的选择
                new_index = combo.findText(current_value)
                if new_index >= 0:
                    combo.setCurrentIndex(new_index)
                else:
                    # 如果原来的选项不存在，尝试从数据源获取
                    world_id = self.choose_world_show.item(row, 0).text()
                    if world_id:
                        world_data = ins_world_info.get(world_id, {})
                        saved_config = world_data.get('world_set', 'default')
                        saved_index = combo.findText(saved_config)
                        combo.setCurrentIndex(saved_index if saved_index >= 0 else 0)
                    else:
                        combo.setCurrentIndex(0)
                # 恢复信号连接
                combo.blockSignals(False)

                # 禁止下拉框的滚轮事件
                combo.setFocusPolicy(Qt.StrongFocus)  # 确保只有获得焦点时才能键盘操作
                combo.wheelEvent = lambda event: None  # 禁用滚轮事件

    def public_server_map_save(self):
        '''对子类暴露保存接口'''
        return self.__save_world_data(True)

    def __setup_ui(self):
        """Initialize UI components"""
        # Set table properties
        self.choose_world_show.setColumnCount(6)  # 新增一列
        self.choose_world_show.setHorizontalHeaderLabels([
            "地图ID(Map ID)",
            "地图名称(Map Name)",
            "游戏端口(Game Port)",
            "RCON端口(RCON Port)",
            "是否启用(Enabled)",
            "世界配置(World Config)"  # 新增列标题
        ])

        # 设置表头居中
        header = self.choose_world_show.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignCenter)

        # 设置所有列内容居中
        for col in range(self.choose_world_show.columnCount()):
            self.choose_world_show.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        self.choose_world_show.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.choose_world_show.setSelectionMode(QTableWidget.SingleSelection)
        self.choose_world_show.setSelectionBehavior(QTableWidget.SelectRows)
        self.choose_world_show.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)

    def __connect_signals(self):
        """Connect UI signals to slots"""
        self.more_world_delete.clicked.connect(self.__delete_selected_world)
        self.more_world_save.clicked.connect(self.__save_world_data)
        self.more_world_add.clicked.connect(self.__add_new_world)

    def __load_world_data(self):
        """Load world data from ins_world_info and populate the table"""
        self.choose_world_show.setRowCount(0)  # Clear existing data

        for world_id, world_data in ins_world_info.get_all().items():
            row_position = self.choose_world_show.rowCount()
            self.choose_world_show.insertRow(row_position)

            # Add world key (not editable)
            key_item = QTableWidgetItem(world_id)
            key_item.setFlags(key_item.flags() & ~Qt.ItemIsEditable)
            key_item.setTextAlignment(Qt.AlignCenter)
            self.choose_world_show.setItem(row_position, 0, key_item)

            # Add world name (editable)
            name_item = QTableWidgetItem(world_data.get('name', ''))
            name_item.setTextAlignment(Qt.AlignCenter)
            self.choose_world_show.setItem(row_position, 1, name_item)

            # Add game port (editable)
            port_item = QTableWidgetItem(str(world_data.get('port', '')))
            port_item.setTextAlignment(Qt.AlignCenter)
            self.choose_world_show.setItem(row_position, 2, port_item)

            # Add RCON port (editable)
            rcon_item = QTableWidgetItem(str(world_data.get('rcon_port', '')))
            rcon_item.setTextAlignment(Qt.AlignCenter)
            self.choose_world_show.setItem(row_position, 3, rcon_item)

            # Add enabled checkbox
            enabled_item = QTableWidgetItem()
            enabled_item.setFlags(enabled_item.flags() | Qt.ItemIsUserCheckable)
            enabled_item.setTextAlignment(Qt.AlignCenter)
            enabled_item.setCheckState(Qt.Checked if world_data.get('open', False) else Qt.Unchecked)
            enabled_item.setFlags(enabled_item.flags() & ~Qt.ItemIsEditable)
            self.choose_world_show.setItem(row_position, 4, enabled_item)

            # Add world config combobox (新增列)
            combo = QComboBox()
            combo.addItems(self._world_config_options)

            # 禁止下拉框的滚轮事件
            combo.setFocusPolicy(Qt.StrongFocus)  # 确保只有获得焦点时才能键盘操作
            combo.wheelEvent = lambda event: None  # 禁用滚轮事件

            # 设置当前选中的配置
            current_config = world_data.get('world_set', 'default')
            index = combo.findText(current_config)
            if index >= 0:
                combo.setCurrentIndex(index)
            else:
                combo.setCurrentIndex(0)  # 默认选择default

            # 将combobox放入表格
            self.choose_world_show.setCellWidget(row_position, 5, combo)

    def __delete_selected_world(self):
        """Delete the selected world from the table (not saved until save button clicked)"""
        selected_rows = self.choose_world_show.selectionModel().selectedRows()

        if not selected_rows:
            self.message_box(
                "请先选择要删除的地图! (Please select a map to delete first!)",
                "警告(Warning)"
            )
            return

        selected_row = selected_rows[0].row()
        world_id = self.choose_world_show.item(selected_row, 0).text()
        world_name = self.choose_world_show.item(selected_row, 1).text()

        # Confirm deletion
        if self.message_box(
                f"确定要删除MapID为 '{world_id}' 的地图 '{world_name}' 吗? (Are you sure to delete map '{world_name}' with key '{world_id}'?)",
                "确认删除(Confirm Deletion)",
                "确定(Confirm)",
                "取消(Cancel)",
                QMessageBox.Question
        ):
            self.choose_world_show.removeRow(selected_row)
            self.message_box(
                f"已删除！保存生效！(Deleted! Please Save by yourself!)",
                "成功(Success)"
            )

    def __add_new_world(self):
        """Add a new empty row to the table"""
        row_position = self.choose_world_show.rowCount()
        self.choose_world_show.insertRow(row_position)

        # Add empty key (editable)
        key_item = QTableWidgetItem("")
        self.choose_world_show.setItem(row_position, 0, key_item)

        # Add empty name (editable)
        name_item = QTableWidgetItem("")
        self.choose_world_show.setItem(row_position, 1, name_item)

        # Add empty port (editable)
        port_item = QTableWidgetItem("")
        self.choose_world_show.setItem(row_position, 2, port_item)

        # Add empty RCON port (editable)
        rcon_item = QTableWidgetItem("")
        self.choose_world_show.setItem(row_position, 3, rcon_item)

        # Add disabled checkbox by default
        enabled_item = QTableWidgetItem()
        enabled_item.setFlags(enabled_item.flags() | Qt.ItemIsUserCheckable)
        enabled_item.setCheckState(Qt.Unchecked)
        enabled_item.setFlags(enabled_item.flags() & ~Qt.ItemIsEditable)
        self.choose_world_show.setItem(row_position, 4, enabled_item)

        # Add world config combobox for new row
        combo = QComboBox()
        combo.addItems(self._world_config_options)
        # 禁止下拉框的滚轮事件
        combo.setFocusPolicy(Qt.StrongFocus)  # 确保只有获得焦点时才能键盘操作
        combo.wheelEvent = lambda event: None  # 禁用滚轮事件
        combo.setCurrentIndex(0)  # 默认选择default
        combo.currentTextChanged.connect(lambda text, row=row_position: self.__update_world_config(text, row))
        self.choose_world_show.setCellWidget(row_position, 5, combo)

        self.message_box(
            "已添加新行，请填写信息后点击保存! (New row added, please fill in information and click save!)",
            "提示(Info)"
        )

    def __validate_world_data(self, world_id, port, rcon_port, existing_keys, existing_ports, existing_rcon_ports):
        """Validate world data before saving"""
        if not world_id:
            self.message_box(
                "Map ID不能为空! (Map ID cannot be empty!)",
                "错误(Error)",
                message_type=QMessageBox.Critical
            )
            return False

        if world_id in existing_keys:
            self.message_box(
                f"Map ID '{world_id}' 已存在! (Key '{world_id}' already exists!)",
                "错误(Error)",
                message_type=QMessageBox.Critical
            )
            return False

        try:
            port = int(port)
            if port in existing_ports:
                self.message_box(
                    f"游戏端口 {port} 已被使用! (Game port {port} is already in use!)",
                    "错误(Error)",
                    message_type=QMessageBox.Critical
                )
                return False
        except ValueError:
            self.message_box(
                "游戏端口必须为数字! (Game port must be a number!)",
                "错误(Error)",
                message_type=QMessageBox.Critical
            )
            return False

        try:
            rcon_port = int(rcon_port)
            if rcon_port in existing_rcon_ports:
                self.message_box(
                    f"RCON端口 {rcon_port} 已被使用! (RCON port {rcon_port} is already in use!)",
                    "错误(Error)",
                    message_type=QMessageBox.Critical
                )
                return False
        except ValueError:
            self.message_box(
                "RCON端口必须为数字! (RCON port must be a number!)",
                "错误(Error)",
                message_type=QMessageBox.Critical
            )
            return False

        return True

    def __save_world_data(self, ignore_success_tip=False):
        """Save changes from table back to ins_world_info"""
        try:
            # Create collections to check for duplicates
            existing_keys = set()
            existing_ports = set()
            existing_rcon_ports = set()

            # First pass: collect all data and validate
            updated_worlds = {}
            validation_errors = []

            for row in range(self.choose_world_show.rowCount()):
                world_id = self.choose_world_show.item(row, 0).text().strip()
                world_name = self.choose_world_show.item(row, 1).text().strip()
                port_str = self.choose_world_show.item(row, 2).text().strip()
                rcon_port_str = self.choose_world_show.item(row, 3).text().strip()
                enabled = self.choose_world_show.item(row, 4).checkState() == Qt.Checked

                # 获取世界配置
                combo = self.choose_world_show.cellWidget(row, 5)
                world_config = combo.currentText() if combo else "default"

                if not self.__validate_world_data(
                        world_id, port_str, rcon_port_str,
                        existing_keys, existing_ports, existing_rcon_ports
                ):
                    return False

                # Add to collections if validation passed
                existing_keys.add(world_id)
                port = int(port_str)
                existing_ports.add(port)
                rcon_port = int(rcon_port_str)
                existing_rcon_ports.add(rcon_port)

                updated_worlds[world_id] = {
                    'name': world_name,
                    'port': port,
                    'rcon_port': rcon_port,
                    'open': enabled,
                    'world_set': world_config  # 新增的世界配置字段
                }

            # Second pass: update ins_world_info if all validations passed
            ins_world_info.clear()
            ins_world_info.update(updated_worlds)

            if not ignore_success_tip:
                self.message_box(
                    "地图配置已保存! (Map configurations have been saved!)",
                    "成功(Success)"
                )
            return True

        except Exception as e:
            self.message_box(
                f"保存失败: {str(e)} (Save failed: {str(e)})",
                "错误(Error)",
                message_type=QMessageBox.Critical
            )
            return False
