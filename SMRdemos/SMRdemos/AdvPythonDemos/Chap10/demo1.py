# test
import sys
from PyQt4 import QtCore, QtGui

from demo1_ui import Ui_Form

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myform = MyForm()
    myform.show()
    sys.exit(app.exec_())