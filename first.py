# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1454, 1040)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(690, 940, 75, 41))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(30, 300, 1401, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 1311, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2D_E_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2D_E_2.sizePolicy().hasHeightForWidth())
        self.label_2D_E_2.setSizePolicy(sizePolicy)
        self.label_2D_E_2.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_2D_E_2.setText("")
        self.label_2D_E_2.setObjectName("label_2D_E_2")
        self.horizontalLayout_2.addWidget(self.label_2D_E_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2D_H_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2D_H_2.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_2D_H_2.setText("")
        self.label_2D_H_2.setObjectName("label_2D_H_2")
        self.horizontalLayout_2.addWidget(self.label_2D_H_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(230, 20, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 161, 21))
        self.label.setObjectName("label")
        self.label_2D_E_3 = QtWidgets.QLabel(self.widget)
        self.label_2D_E_3.setGeometry(QtCore.QRect(380, 40, 629, 469))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2D_E_3.sizePolicy().hasHeightForWidth())
        self.label_2D_E_3.setSizePolicy(sizePolicy)
        self.label_2D_E_3.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_2D_E_3.setText("")
        self.label_2D_E_3.setObjectName("label_2D_E_3")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3D_EH = QtWidgets.QLabel(self.tab_2)
        self.label_3D_EH.setGeometry(QtCore.QRect(380, 50, 629, 469))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3D_EH.sizePolicy().hasHeightForWidth())
        self.label_3D_EH.setSizePolicy(sizePolicy)
        self.label_3D_EH.setStyleSheet("QLabel{\n"
"    border-color: rgb(255, 170,0);\n"
"     border-width: 1px;\n"
"     border-style: solid;\n"
"}")
        self.label_3D_EH.setText("")
        self.label_3D_EH.setObjectName("label_3D_EH")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(620, 40, 741, 211))
        self.groupBox.setObjectName("groupBox")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 241, 59))
        self.label_15.setObjectName("label_15")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 110, 321, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setIndent(-1)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_4.setProperty("value", 1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(400, 110, 321, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setIndent(-1)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.spinBox_7 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_7.setProperty("value", 1)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_8.addWidget(self.spinBox_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.spinBox_8 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_8.setProperty("value", 20)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_9.addWidget(self.spinBox_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(270, 30, 61, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.spinBox_9 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_9.setMaximum(1000)
        self.spinBox_9.setSingleStep(1)
        self.spinBox_9.setProperty("value", 100)
        self.spinBox_9.setObjectName("spinBox_9")
        self.horizontalLayout_13.addWidget(self.spinBox_9)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(80, 160, 291, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 20, 541, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 231, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 30, 391, 31))
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.openimage)
        self.comboBox_2.currentIndexChanged['QString'].connect(Form.slot1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "电磁场实验3"))
        self.pushButton.setText(_translate("Form", "运行"))
        self.comboBox.setCurrentText(_translate("Form", "独立显示"))
        self.comboBox.setItemText(0, _translate("Form", "独立显示"))
        self.comboBox.setItemText(1, _translate("Form", "合并显示"))
        self.label.setText(_translate("Form", "电场磁场的显示方式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "2D 显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "3D 显示"))
        self.groupBox.setTitle(_translate("Form", "仿真参数（为保证仿真连续性，请勿在仿真结束前修改此参数）"))
        self.label_15.setText(_translate("Form", "磁场放大倍数 (便于可视化)"))
        self.label_13.setText(_translate("Form", "介质1参数"))
        self.label_8.setText(_translate("Form", "u1 = _ u0"))
        self.label_5.setText(_translate("Form", "e1 = _ e0"))
        self.label_14.setText(_translate("Form", "介质2参数"))
        self.label_11.setText(_translate("Form", "u2 = _ u0"))
        self.label_12.setText(_translate("Form", "e2 = _ e0"))
        self.groupBox_2.setTitle(_translate("Form", "作者信息"))
        self.groupBox_3.setTitle(_translate("Form", "仿真内容选择"))
        self.label_3.setText(_translate("Form", "运行结束前请勿更改此选项！！！"))
        self.comboBox_2.setItemText(0, _translate("Form", "平面波对理想导体平面边界的垂直入射"))
        self.comboBox_2.setItemText(1, _translate("Form", "平面波对理想介质的垂直入射"))
