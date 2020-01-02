from ui import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import test


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self._test_thread = MyThread()
        self._test_thread.send.connect(self.display)
        self.onBindingUi()
        self._test_thread.start()
        #7self.btn_go.click.connect(self.action)
    def display(self,pix):
        self.label_8.setPixmap(pix)

    
    def onBindingUi(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
