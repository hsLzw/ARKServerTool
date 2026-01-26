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
    QSpacerItem, QSpinBox, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.tabWidget = QTabWidget(MainPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(132, 30))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_6.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.open_param_be = QCheckBox(self.groupBox)
        self.open_param_be.setObjectName(u"open_param_be")

        self.horizontalLayout_3.addWidget(self.open_param_be)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.open_param_mods = QCheckBox(self.groupBox)
        self.open_param_mods.setObjectName(u"open_param_mods")

        self.horizontalLayout_3.addWidget(self.open_param_mods)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(5, 12)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(132, 30))
        self.lineEdit.setMaximumSize(QSize(132, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(132, 30))
        self.lineEdit_2.setMaximumSize(QSize(132, 16777215))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(30)

        self.horizontalLayout_5.addWidget(self.spinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 2)
        self.horizontalLayout_5.setStretch(8, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(132, 0))
        self.lineEdit_4.setMaximumSize(QSize(132, 16777215))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_7.addWidget(self.lineEdit_4)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_7.addItem(self.verticalSpacer_3)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(132, 16777215))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_7.addWidget(self.lineEdit_5)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 3)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 3)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 3)
        self.verticalLayout_2.setStretch(9, 1)

        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_9.addWidget(self.pushButton_6)

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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.run_button = QPushButton(self.tab)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setMinimumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.run_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
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

        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.horizontalLayout_11.setStretch(2, 9)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_12.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_12.addWidget(self.pushButton_9)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.tableView = QTableView(self.groupBox_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_5.addWidget(self.tableView)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_10 = QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_14.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.groupBox_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 30)
        self.verticalLayout_5.setStretch(3, 2)
        self.verticalLayout_5.setStretch(4, 1)

        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalLayout_4.setStretch(0, 5)

        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
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

        self.pushButton_13 = QPushButton(self.groupBox_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_17.addWidget(self.pushButton_13)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.groupBox_4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_9.addWidget(self.tableWidget_2, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.lineEdit_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_6)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_13)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.lineEdit_7)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_7)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.lineEdit_8 = QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.lineEdit_8)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_8)

        self.pushButton_12 = QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_16.addWidget(self.pushButton_12)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.gridLayout_9.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 9)
        self.gridLayout_9.setRowStretch(2, 1)

        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(MainPage)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"ARK ASCENDED - SERVER TOOL", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainPage", u"\u542f\u52a8\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainPage", u"*Tips: \u521a\u63a5\u89e6\uff0c\u5176\u4f59\u914d\u7f6e\u540e\u7eed\u8865\u5145", None))
        self.label_10.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainPage", u"\u70b9\u51fb\u9009\u62e9\u670d\u52a1\u5668\u6839\u76ee\u5f55", None))
        self.label_5.setText("")
        self.open_param_be.setText(QCoreApplication.translate("MainPage", u"\u5f00\u542fBattlEye", None))
        self.open_param_mods.setText(QCoreApplication.translate("MainPage", u"\u5f00\u542f\u6a21\u7ec4", None))
        self.checkBox.setText(QCoreApplication.translate("MainPage", u"\u591a\u901a\u4e16\u754c", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainPage", u"\u670d\u52a1\u5668\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainPage", u"\u7ba1\u7406\u5458\u5bc6\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainPage", u"\u5355\u5730\u56fe\u6700\u5927\u4eba\u6570\uff1a", None))
        self.label_9.setText("")
        self.label_7.setText(QCoreApplication.translate("MainPage", u"\u591a\u901a\u5b58\u6863ID\uff1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainPage", u"\u552f\u4e00ID", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainPage", u"?", None))
        self.label_8.setText(QCoreApplication.translate("MainPage", u"\u591a\u901a\u6570\u636e\u8def\u5f84\uff1a", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainPage", u"\u6570\u636e\u4e0a\u4e0b\u8f7d\u8def\u5f84", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPage", u"?", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainPage", u"\u591a\u901a\u4e16\u754c\u8bbe\u7f6e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPage", u"\u5220\u9664\u9009\u4e2d", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainPage", u"\u6dfb\u52a0\u65b0\u4e16\u754c\u914d\u7f6e", None))
        self.run_button.setText(QCoreApplication.translate("MainPage", u"\u542f\u52a8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainPage", u"\u542f\u52a8\u9875\u9762", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainPage", u"\u591a\u914d\u7f6e\u8bbe\u5b9a(\u8bbe\u5b9a\u90e8\u5206\u9879\uff0c\u672a\u5728\u6b64\u914d\u7f6e\u7684\u9879\u5c06\u4f7f\u7528\u6e38\u620f\u7684\u9ed8\u8ba4\u8bbe\u5b9a)", None))
        self.label_11.setText(QCoreApplication.translate("MainPage", u"\u9009\u62e9\u914d\u7f6e:", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainPage", u"\u65b0\u589e\u9ed8\u8ba4\u914d\u7f6e", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainPage", u"\u5bfc\u5165\u914d\u7f6e", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainPage", u"\u65b0\u589e\u4e00\u884c", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainPage", u"\u5220\u9664\u884c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainPage", u"\u670d\u52a1\u5668\u6e38\u620f\u914d\u7f6e", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u9009\u62e9(\u81ea\u884c\u524d\u5f80\u641c\u7d22\u6a21\u7ec4: https://www.curseforge.com/ark-survival-ascended/search?page=1&pageSize=20)", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainPage", u"\u4fdd\u5b58\u6a21\u7ec4\u9009\u4e2d", None))
        self.label_12.setText(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4ID\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u540d\u79f0\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainPage", u"\u5907\u6ce8\uff1a", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainPage", u"\u6dfb\u52a0\u6a21\u7ec4\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainPage", u"\u6a21\u7ec4\u914d\u7f6e", None))
    # retranslateUi

