from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
# from pySide import QtCore, QtGui

from views import credenciais
from views import dash

# if __name__ == "__main__":
# 	import sys
# 	app = QtGui.QApplication(sys.argv)
# 	MainWindow = QtGui.QMainWindow()
# 	ui = dash.Ui_mainWindow()
# 	ui.setupUi(MainWindow)
# 	MainWindow.show()
# 	sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dash.Ui_mainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())