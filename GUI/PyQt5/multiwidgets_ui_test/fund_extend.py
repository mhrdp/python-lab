from fund import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui

class PageWindow(QtWidgets.QMainWindow):
    _signal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self._signal.emit(name)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Main Window')

        self.stackedWidget.addWidget(self.home)
        self.stackedWidget.addWidget(self.convert_gui)

        self.sidebr_btn_extract.clicked.connect(lambda: self.switch_page(self.convert_gui))
        self.sidebar_btn_home.clicked.connect(lambda: self.switch_page(self.home))
    
    def switch_page(self, widget):
        self.stackedWidget.setCurrentWidget(widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()

    ui.show()

    sys.exit(app.exec_())
