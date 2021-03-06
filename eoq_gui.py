# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eoq_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_d = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_d)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.lineEdit_h = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_h.setObjectName("lineEdit_h")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_h)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.lineEdit_k = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_k)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.lineEdit_l = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_l.setObjectName("lineEdit_l")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_l)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.lineEdit_c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c1.setObjectName("lineEdit_c1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEdit_c1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.lineEdit_c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c2.setObjectName("lineEdit_c2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lineEdit_c2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.lineEdit_q = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_q.setObjectName("lineEdit_q")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lineEdit_q)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.buttonCalc = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCalc.setObjectName("buttonCalc")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.buttonCalc)
        self.lineEdit_eoq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_eoq.setReadOnly(True)
        self.lineEdit_eoq.setObjectName("lineEdit_eoq")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lineEdit_eoq)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.lineEdit_rop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rop.setReadOnly(True)
        self.lineEdit_rop.setObjectName("lineEdit_rop")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lineEdit_rop)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EOQ Solver with Price Breaks"))
        self.label.setText(_translate("MainWindow", "Demand per time unit"))
        self.label_2.setText(_translate("MainWindow", "Holding Cost"))
        self.label_3.setText(_translate("MainWindow", "Setup Cost"))
        self.label_4.setText(_translate("MainWindow", "Lead Time"))
        self.label_5.setText(_translate("MainWindow", "Cost before bulk"))
        self.label_6.setText(_translate("MainWindow", "Cost after bulk"))
        self.label_7.setText(_translate("MainWindow", "Quantity price break point"))
        self.buttonCalc.setText(_translate("MainWindow", "Calculate EOQ"))
        self.label_8.setText(_translate("MainWindow", "Economic Order Quantity"))
        self.label_9.setText(_translate("MainWindow", "Reorder Point"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
