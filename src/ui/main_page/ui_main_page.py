# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(980, 750)
        MainPage.setMinimumSize(QSize(980, 750))
        MainPage.setMaximumSize(QSize(980, 750))
        self.gridLayout_3 = QGridLayout(MainPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_tabWidget = QTabWidget(MainPage)
        self.main_tabWidget.setObjectName(u"main_tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_12 = QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.choose_server_root = QPushButton(self.groupBox)
        self.choose_server_root.setObjectName(u"choose_server_root")
        self.choose_server_root.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.choose_server_root)

        self.server_root = QLineEdit(self.groupBox)
        self.server_root.setObjectName(u"server_root")
        self.server_root.setMinimumSize(QSize(132, 30))
        self.server_root.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")
        self.server_root.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.server_root)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"    border: none;               \n"
"    border-top: 1px solid black; \n"
"}")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.open_param_mworlds = QCheckBox(self.groupBox_5)
        self.open_param_mworlds.setObjectName(u"open_param_mworlds")

        self.horizontalLayout_5.addWidget(self.open_param_mworlds)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.cluster_id = QLineEdit(self.groupBox_5)
        self.cluster_id.setObjectName(u"cluster_id")
        self.cluster_id.setMinimumSize(QSize(132, 0))
        self.cluster_id.setMaximumSize(QSize(16777215, 16777215))
        self.cluster_id.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cluster_id)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.cluster_id_ask = QPushButton(self.groupBox_5)
        self.cluster_id_ask.setObjectName(u"cluster_id_ask")
        self.cluster_id_ask.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.cluster_id_ask)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout_5.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.cluster_path = QLineEdit(self.groupBox_5)
        self.cluster_path.setObjectName(u"cluster_path")
        self.cluster_path.setMaximumSize(QSize(16777215, 16777215))
        self.cluster_path.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}\n"
"")
        self.cluster_path.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.cluster_path)

        self.cluster_path_ask = QPushButton(self.groupBox_5)
        self.cluster_path_ask.setObjectName(u"cluster_path_ask")
        self.cluster_path_ask.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.cluster_path_ask)

        self.choose_cluster_path_btn = QPushButton(self.groupBox_5)
        self.choose_cluster_path_btn.setObjectName(u"choose_cluster_path_btn")
        self.choose_cluster_path_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_4.addWidget(self.choose_cluster_path_btn)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 9)
        self.horizontalLayout_4.setStretch(3, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_9)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"    border: none;               \n"
"    border-top: 1px solid black; \n"
"}")
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.gridLayout_11.addLayout(self.horizontalLayout_23, 2, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_2)

        self.server_pwd = QLineEdit(self.groupBox_6)
        self.server_pwd.setObjectName(u"server_pwd")
        self.server_pwd.setMinimumSize(QSize(132, 30))
        self.server_pwd.setMaximumSize(QSize(190, 16777215))
        self.server_pwd.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_18.addWidget(self.server_pwd)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_16)

        self.server_session_name = QLineEdit(self.groupBox_6)
        self.server_session_name.setObjectName(u"server_session_name")
        self.server_session_name.setMinimumSize(QSize(132, 30))
        self.server_session_name.setMaximumSize(QSize(190, 16777215))
        self.server_session_name.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_22.addWidget(self.server_session_name)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_24.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_24.addItem(self.verticalSpacer)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_3)

        self.admin_pwd = QLineEdit(self.groupBox_6)
        self.admin_pwd.setObjectName(u"admin_pwd")
        self.admin_pwd.setMinimumSize(QSize(132, 30))
        self.admin_pwd.setMaximumSize(QSize(190, 16777215))
        self.admin_pwd.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_19.addWidget(self.admin_pwd)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.open_param_be = QCheckBox(self.groupBox_6)
        self.open_param_be.setObjectName(u"open_param_be")

        self.horizontalLayout_21.addWidget(self.open_param_be)

        self.open_param_mods = QCheckBox(self.groupBox_6)
        self.open_param_mods.setObjectName(u"open_param_mods")

        self.horizontalLayout_21.addWidget(self.open_param_mods)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_24.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_24.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_4)

        self.max_player = QSpinBox(self.groupBox_6)
        self.max_player.setObjectName(u"max_player")
        self.max_player.setMinimumSize(QSize(32, 30))
        self.max_player.setMaximumSize(QSize(150, 16777215))
        self.max_player.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    font-size: 14px;\n"
"    min-width: 30px;\n"
"    background: white;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 1px solid #999;\n"
"}")
        self.max_player.setMaximum(10000)
        self.max_player.setValue(30)

        self.horizontalLayout_20.addWidget(self.max_player)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.save_set_input = QPushButton(self.groupBox_6)
        self.save_set_input.setObjectName(u"save_set_input")
        self.save_set_input.setMinimumSize(QSize(132, 40))
        self.save_set_input.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 12px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.verticalLayout_10.addWidget(self.save_set_input)


        self.horizontalLayout_24.addLayout(self.verticalLayout_10)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(2, 1)
        self.horizontalLayout_24.setStretch(4, 1)

        self.gridLayout_11.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 3)
        self.verticalLayout_8.setStretch(3, 3)

        self.gridLayout_12.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.choose_world_show = QTableWidget(self.groupBox_2)
        self.choose_world_show.setObjectName(u"choose_world_show")

        self.verticalLayout_3.addWidget(self.choose_world_show)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.more_world_delete = QPushButton(self.groupBox_2)
        self.more_world_delete.setObjectName(u"more_world_delete")

        self.horizontalLayout_9.addWidget(self.more_world_delete)

        self.more_world_save = QPushButton(self.groupBox_2)
        self.more_world_save.setObjectName(u"more_world_save")

        self.horizontalLayout_9.addWidget(self.more_world_save)

        self.more_world_add = QPushButton(self.groupBox_2)
        self.more_world_add.setObjectName(u"more_world_add")

        self.horizontalLayout_9.addWidget(self.more_world_add)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 2)

        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.run_button = QPushButton(self.tab)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setMinimumSize(QSize(252, 50))
        self.run_button.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 240px;\n"
"    background: white;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout.addWidget(self.run_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)

        self.main_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.wc_choose_config = QComboBox(self.groupBox_3)
        self.wc_choose_config.setObjectName(u"wc_choose_config")

        self.horizontalLayout_11.addWidget(self.wc_choose_config)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.horizontalLayout_11.setStretch(2, 9)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.wc_add_new_file = QPushButton(self.groupBox_3)
        self.wc_add_new_file.setObjectName(u"wc_add_new_file")

        self.horizontalLayout_12.addWidget(self.wc_add_new_file)

        self.wc_save_change = QPushButton(self.groupBox_3)
        self.wc_save_change.setObjectName(u"wc_save_change")

        self.horizontalLayout_12.addWidget(self.wc_save_change)

        self.wc_copy_config = QPushButton(self.groupBox_3)
        self.wc_copy_config.setObjectName(u"wc_copy_config")
        self.wc_copy_config.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.wc_copy_config)

        self.simple_config_btn = QPushButton(self.groupBox_3)
        self.simple_config_btn.setObjectName(u"simple_config_btn")

        self.horizontalLayout_12.addWidget(self.simple_config_btn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.wc_show_world_setting = QTableWidget(self.groupBox_3)
        self.wc_show_world_setting.setObjectName(u"wc_show_world_setting")

        self.verticalLayout_5.addWidget(self.wc_show_world_setting)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.wc_add_row = QPushButton(self.groupBox_3)
        self.wc_add_row.setObjectName(u"wc_add_row")

        self.horizontalLayout_14.addWidget(self.wc_add_row)

        self.wc_delete_row = QPushButton(self.groupBox_3)
        self.wc_delete_row.setObjectName(u"wc_delete_row")

        self.horizontalLayout_14.addWidget(self.wc_delete_row)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_5.addWidget(self.label_20)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 12)
        self.verticalLayout_5.setStretch(3, 1)

        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalLayout_4.setStretch(0, 5)

        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.save_mods_button = QPushButton(self.groupBox_4)
        self.save_mods_button.setObjectName(u"save_mods_button")
        self.save_mods_button.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_17.addWidget(self.save_mods_button)

        self.mods_install_crt = QPushButton(self.groupBox_4)
        self.mods_install_crt.setObjectName(u"mods_install_crt")
        self.mods_install_crt.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_17.addWidget(self.mods_install_crt)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)

        self.mods_show_table = QTableWidget(self.groupBox_4)
        self.mods_show_table.setObjectName(u"mods_show_table")

        self.gridLayout_9.addWidget(self.mods_show_table, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.mods_id = QLineEdit(self.groupBox_4)
        self.mods_id.setObjectName(u"mods_id")
        self.mods_id.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_16.addWidget(self.mods_id)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_6)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_13)

        self.mods_name = QLineEdit(self.groupBox_4)
        self.mods_name.setObjectName(u"mods_name")
        self.mods_name.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_16.addWidget(self.mods_name)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_7)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.mods_bak = QLineEdit(self.groupBox_4)
        self.mods_bak.setObjectName(u"mods_bak")
        self.mods_bak.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    min-width: 120px;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4a90e2;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #999;\n"
"}")

        self.horizontalLayout_16.addWidget(self.mods_bak)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_8)

        self.add_mods_button = QPushButton(self.groupBox_4)
        self.add_mods_button.setObjectName(u"add_mods_button")
        self.add_mods_button.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_16.addWidget(self.add_mods_button)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.gridLayout_9.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 9)
        self.gridLayout_9.setRowStretch(2, 1)

        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_7 = QGroupBox(self.tab_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_13 = QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.mp_show_logs = QTextEdit(self.groupBox_7)
        self.mp_show_logs.setObjectName(u"mp_show_logs")
        self.mp_show_logs.setStyleSheet(u"font-size: 12px;\n"
"font-weight: bold;")
        self.mp_show_logs.setReadOnly(True)

        self.gridLayout_13.addWidget(self.mp_show_logs, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.main_tabWidget.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.main_tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(MainPage)

        self.main_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"ARK ASCENDED - SERVER TOOL", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainPage", u"\u542f\u52a8\u53c2\u6570(Run Params)", None))
        self.choose_server_root.setText(QCoreApplication.translate("MainPage", u"\u70b9\u51fb\u9009\u62e9\u670d\u52a1\u5668\u6839\u76ee\u5f55\n"
"(Choose Server Root)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainPage", u"\u591a\u901a\u4e16\u754c(More Worlds)", None))
        self.open_param_mworlds.setText(QCoreApplication.translate("MainPage", u"\u5f00\u542f\u591a\u901a\u4e16\u754c(More World Open)", None))
        self.label_7.setText(QCoreApplication.translate("MainPage", u"\u591a\u901a\u5b58\u6863ID(Cluster ID)\uff1a", None))
        self.cluster_id.setPlaceholderText(QCoreApplication.translate("MainPage", u"\u552f\u4e00ID", None))
        self.cluster_id_ask.setText(QCoreApplication.translate("MainPage", u"?", None))
        self.label_8.setText(QCoreApplication.translate("MainPage", u"\u591a\u901a\u6570\u636e\u8def\u5f84(Cluster Path)\uff1a", None))
        self.cluster_path.setPlaceholderText(QCoreApplication.translate("MainPage", u"\u6570\u636e\u4e0a\u4e0b\u8f7d\u8def\u5f84", None))
        self.cluster_path_ask.setText(QCoreApplication.translate("MainPage", u"?", None))
        self.choose_cluster_path_btn.setText(QCoreApplication.translate("MainPage", u"\u9009\u62e9\u8def\u5f84\n"
"(Choose Save Path)", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainPage", u"\u901a\u7528\u914d\u7f6e(Common settings)", None))
        self.label_2.setText(QCoreApplication.translate("MainPage", u"\u670d\u52a1\u5668\u5bc6\u7801\uff1a\n"
"(Server Pwd)\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainPage", u"\u670d\u52a1\u5668\u540d\u79f0\uff1a\n"
"(ServerName)\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainPage", u"\u7ba1\u7406\u5458\u5bc6\u7801\uff1a\n"
"(Admin Pwd)\uff1a", None))
        self.open_param_be.setText(QCoreApplication.translate("MainPage", u"\u5f00\u542fBattlEye(Open BE)", None))
        self.open_param_mods.setText(QCoreApplication.translate("MainPage", u"\u5f00\u542f\u6a21\u7ec4(Open Mods)", None))
        self.label_4.setText(QCoreApplication.translate("MainPage", u"\u5355\u5730\u56fe\u6700\u5927\u4eba\u6570\uff1a\n"
"(MaxPlayer Count)\uff1a", None))
        self.save_set_input.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58\u6240\u6709\u914d\u7f6e\n"
"(Save All Config)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainPage", u"\u4e16\u754c\u9009\u62e9(Choose world)", None))
        self.more_world_delete.setText(QCoreApplication.translate("MainPage", u"\u5220\u9664\u9009\u4e2d(Delete Choose)", None))
        self.more_world_save.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58\u4fee\u6539(Save Change)", None))
        self.more_world_add.setText(QCoreApplication.translate("MainPage", u"\u6dfb\u52a0\u65b0\u4e16\u754c\u914d\u7f6e(Add New World)", None))
        self.run_button.setText(QCoreApplication.translate("MainPage", u"\u542f\u52a8(RUN)", None))
        self.label_17.setText(QCoreApplication.translate("MainPage", u"\u5f53\u4e16\u754c\u914d\u7f6e\u4e0d\u5b8c\u5168\u4e00\u6837\u65f6\uff0c\u9632\u6b62\u914d\u7f6e\u8986\u76d6\uff0c\u4fdd\u8bc1\u4e00\u4e2a\u4e16\u754c\u5c31\u7eea\u540e\u624d\u4f1a\u542f\u52a8\u4e0b\u4e00\u4e2a\u4e16\u754c\u3002\u514d\u8d39\u8f6f\u4ef6\u3002Git\u5730\u5740:https://github.com/hsLzw/ARKServerTool", None))
        self.label_18.setText(QCoreApplication.translate("MainPage", u"When world configurations are not identical, prevent configuration overwriting and ensure the next world is only started after the current one is ready.", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainPage", u"\u542f\u52a8\u9875\u9762(Run)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainPage", u"\u591a\u914d\u7f6e\u8bbe\u5b9a(\u8bbe\u5b9a\u90e8\u5206\u9879\uff0c\u672a\u5728\u6b64\u914d\u7f6e\u7684\u9879\u5c06\u4f7f\u7528\u6e38\u620f\u7684\u9ed8\u8ba4\u8bbe\u5b9a)", None))
        self.label_11.setText(QCoreApplication.translate("MainPage", u"\u9009\u62e9\u914d\u7f6e(Choose config):", None))
        self.wc_add_new_file.setText(QCoreApplication.translate("MainPage", u"\u65b0\u589e\u914d\u7f6e\u6587\u4ef6(Add Config)", None))
        self.wc_save_change.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58(Save Config/Change)", None))
        self.wc_copy_config.setText(QCoreApplication.translate("MainPage", u"\u590d\u5236\u5f53\u524d\u914d\u7f6e(Copy Current Config)", None))
        self.simple_config_btn.setText(QCoreApplication.translate("MainPage", u"\u7b80\u6613\u914d\u7f6e\u754c\u9762(Simple configuration interface)", None))
        self.wc_add_row.setText(QCoreApplication.translate("MainPage", u"\u65b0\u589e\u4e00\u884c(Add a row)", None))
        self.wc_delete_row.setText(QCoreApplication.translate("MainPage", u"\u5220\u9664\u884c(Delete row)", None))
        self.label_19.setText(QCoreApplication.translate("MainPage", u"\u6b64\u5904\u5e76\u975e\u5168\u90e8\u914d\u7f6e\uff0c\u800c\u662f\u90e8\u5206\u9700\u8981\u8c03\u6574\u7684\u914d\u7f6e\u3002\u914d\u7f6e\u6587\u4ef6\u4e2d\u672a\u4f53\u73b0\u7684\u914d\u7f6e\u5c06\u4f1a\u4f7f\u7528\u6e38\u620f\u7684\u9ed8\u8ba4\u914d\u7f6e\u3002\u4ec5\u8c03\u6574ServerSettings\u7684\u914d\u7f6e", None))
        self.label_20.setText(QCoreApplication.translate("MainPage", u"Only the configurations in the ServerSettings section will be adjusted. Configurations not specified in the file will use the game's default settings.", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainPage", u"\u4e16\u754c\u914d\u7f6e\u6587\u4ef6(WorldConfig)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u9009\u62e9(\u81ea\u884c\u524d\u5f80\u641c\u7d22\u6a21\u7ec4: https://www.curseforge.com/ark-survival-ascended/search?page=1&pageSize=20)", None))
        self.save_mods_button.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58\u6a21\u7ec4\u9009\u4e2d\n"
"(Save Config)", None))
        self.mods_install_crt.setText(QCoreApplication.translate("MainPage", u"\u4e00\u952e\u5b89\u88c5Mods\u8bc1\u4e66\n"
"(install AmazonRootCA2.crt)", None))
        self.label_12.setText(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4ID(Mods ID)\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u540d\u79f0(Name)\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainPage", u"\u5907\u6ce8(Desc)\uff1a", None))
        self.add_mods_button.setText(QCoreApplication.translate("MainPage", u"\u6dfb\u52a0(Add)", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u914d\u7f6e(ModsSettings)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainPage", u"\u5de5\u5177\u65e5\u5fd7(Tool Log)", None))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainPage", u"\u76d1\u63a7\u9762\u677f(MonitoringPanel)", None))
    # retranslateUi

