# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 598)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(890, 500, 121, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(750, 300, 121, 41))
        self.btn_all.setObjectName("btn_all")
        self.path_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.path_dir.setGeometry(QtCore.QRect(240, 30, 491, 20))
        self.path_dir.setObjectName("path_dir")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(740, 30, 121, 23))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_gen_inf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_inf.setGeometry(QtCore.QRect(750, 350, 121, 41))
        self.btn_gen_inf.setObjectName("btn_gen_inf")
        self.btn_pro_loss = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pro_loss.setGeometry(QtCore.QRect(750, 400, 121, 41))
        self.btn_pro_loss.setObjectName("btn_pro_loss")
        self.btn_cashflow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cashflow.setGeometry(QtCore.QRect(750, 450, 121, 41))
        self.btn_cashflow.setObjectName("btn_cashflow")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(240, 90, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_info.setFont(font)
        self.label_info.setAutoFillBackground(False)
        self.label_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(740, 70, 121, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(230, 60, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.btn_b_sheet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_b_sheet.setGeometry(QtCore.QRect(750, 500, 121, 41))
        self.btn_b_sheet.setObjectName("btn_b_sheet")
        self.table_pd = QtWidgets.QTableView(self.centralwidget)
        self.table_pd.setGeometry(QtCore.QRect(240, 120, 491, 421))
        self.table_pd.setObjectName("table_pd")
        self.btn_table = QtWidgets.QPushButton(self.centralwidget)
        self.btn_table.setGeometry(QtCore.QRect(750, 230, 121, 41))
        self.btn_table.setObjectName("btn_table")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_all.setText(_translate("MainWindow", "ALL"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_gen_inf.setText(_translate("MainWindow", "General Inf."))
        self.btn_pro_loss.setText(_translate("MainWindow", "Profit/Loss"))
        self.btn_cashflow.setText(_translate("MainWindow", "Cashflow"))
        self.label_info.setText(_translate("MainWindow", "Waiting for input"))
        self.label_status.setText(_translate("MainWindow", "Status"))
        self.btn_b_sheet.setText(_translate("MainWindow", "B. Sheet"))
        self.btn_table.setText(_translate("MainWindow", "GENERATE TABLE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())