from PyQt5 import QtWidgets
from pages.convert_page import ConvertData

if __name__ == '__main__':
    from style.darkorange import StyleSheet
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Set CSS styling to the window
    app.setStyleSheet(StyleSheet)

    ui = ConvertData()
    ui.show()

    sys.exit(app.exec_())