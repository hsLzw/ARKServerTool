from PySide6.QtWidgets import (
    QMessageBox,
    QTableWidgetItem,
    QAbstractItemView,
    QCheckBox,
    QWidget,
    QHBoxLayout,
    QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from app.models.json_setting import ins_mods_setting
from app.ui_utils.base_page.base_page import BasePage
from src.ui.main_page.ui_main_page import Ui_MainPage


class MainPage_ModsSet(BasePage, Ui_MainPage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def ins_init(self):
        self.__setup_ui()
        self.__load_data()
        self.__bind_events()

    def __setup_ui(self):
        """初始化UI控件状态"""
        # 设置表格为4列
        self.mods_show_table.setColumnCount(4)
        self.mods_show_table.setHorizontalHeaderLabels(["模组ID(Mods ID)", "模组名称(Mods Name)", "备注(Mods Desc)", "启用(Enabled)"])

        # 表格行为设置
        self.mods_show_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mods_show_table.setEditTriggers(QAbstractItemView.DoubleClicked)

        # 列宽设置
        self.mods_show_table.setColumnWidth(0, 100)  # ID列
        self.mods_show_table.setColumnWidth(1, 150)  # Name列
        self.mods_show_table.setColumnWidth(3, 80)  # 复选框列
        self.mods_show_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    def __bind_events(self):
        """绑定所有UI控件的事件"""
        self.add_mods_button.clicked.connect(self.__on_add_mods)
        self.save_mods_button.clicked.connect(self.__on_save_mods)
        self.mods_show_table.cellDoubleClicked.connect(self.__on_edit_cell)

    def __load_data(self):
        """从配置加载数据到表格"""
        self.mods_show_table.setRowCount(0)

        for mod_id in ins_mods_setting:
            mod_data = ins_mods_setting[mod_id]
            self.__add_row_to_table(
                mod_id,
                mod_data.get("name", ""),
                mod_data.get("bak", ""),
                mod_data.get("open", False)
            )

    def __add_row_to_table(self, mod_id: str, name: str, description: str, enabled: bool):
        """添加一行数据到表格"""
        row_pos = self.mods_show_table.rowCount()
        self.mods_show_table.insertRow(row_pos)

        # ID列（不可编辑）
        id_item = QTableWidgetItem(mod_id)
        id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
        id_item.setBackground(QColor(240, 240, 240))
        self.mods_show_table.setItem(row_pos, 0, id_item)

        # Name列
        name_item = QTableWidgetItem(name)
        self.mods_show_table.setItem(row_pos, 1, name_item)

        # Description列
        desc_item = QTableWidgetItem(description)
        self.mods_show_table.setItem(row_pos, 2, desc_item)

        # Checkbox列
        checkbox_widget = QWidget()
        checkbox_layout = QHBoxLayout(checkbox_widget)
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_layout.setAlignment(Qt.AlignCenter)

        checkbox = QCheckBox()
        checkbox.setChecked(enabled)
        checkbox_layout.addWidget(checkbox)
        self.mods_show_table.setCellWidget(row_pos, 3, checkbox_widget)

    def __on_add_mods(self):
        """添加新模组"""
        mod_id = self.mods_id.text().strip()
        mod_name = self.mods_name.text().strip()
        mod_bak = self.mods_bak.text().strip()

        if not mod_id:
            self.message_box(content="Mod ID cannot be empty!", title="错误")
            return

        if mod_id in ins_mods_setting:
            self.message_box(content=f"Mod ID {mod_id} already exists!", title="错误")
            return

        # 添加到表格
        self.__add_row_to_table(mod_id, mod_name, mod_bak, False)

        # 清空输入框
        self.mods_id.clear()
        self.mods_name.clear()
        self.mods_bak.clear()

        # 自动保存
        # self.__on_save_mods()

    def __on_save_mods(self):
        """保存所有修改（全量更新）"""
        try:
            # 清空原有配置
            ins_mods_setting.clear()

            # 遍历表格所有行，重新构建配置
            for row in range(self.mods_show_table.rowCount()):
                mod_id_item = self.mods_show_table.item(row, 0)
                if not mod_id_item:
                    continue

                mod_id = mod_id_item.text()

                # 获取复选框状态
                checkbox_widget = self.mods_show_table.cellWidget(row, 3)
                if not checkbox_widget:
                    continue

                checkbox = checkbox_widget.findChild(QCheckBox)
                if not checkbox:
                    continue

                # 更新配置
                ins_mods_setting[mod_id] = {
                    "name": self.mods_show_table.item(row, 1).text() if self.mods_show_table.item(row, 1) else "",
                    "bak": self.mods_show_table.item(row, 2).text() if self.mods_show_table.item(row, 2) else "",
                    "open": checkbox.isChecked()
                }

            self.message_box(content=f"全部修改已保存!(All changes saved successfully!)", title="Success")

        except Exception as e:
            self.message_box(content=f"保存失败！Save failed: {str(e)}", title="Error")

    def __on_edit_cell(self, row, column):
        """表格单元格双击编辑处理"""
        if column == 0:  # ID列不可编辑
            return
        self.mods_show_table.editItem(self.mods_show_table.item(row, column))

