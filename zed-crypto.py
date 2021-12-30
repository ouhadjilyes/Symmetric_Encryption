import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from crypto_gui import *

class Crypto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("zed-crypto")
        self.setFixedSize(838, 484)

        # Actions for encrypt tab
        self.ui.btn_box_encrypt.accepted.connect(self.Encrypt)

        # action for decrypt tab
        self.ui.btn_box_decrypt.accepted.connect(self.Decrypt)

        self.ui.btn_box_encrypt.rejected.connect(self.Rejected)
        self.ui.btn_box_decrypt.rejected.connect(self.Rejected)

        self.show()

    def Encrypt(self):
        #self.ui.self.centralwidget.close()
        print("Encrypted")
    
    def Decrypt(self):
        print("Decrypted")
    
    def Rejected(self):
        print("canceled !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Crypto()
    w.show()
    sys.exit(app.exec_())
