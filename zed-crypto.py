import sys
from PyQt5.QtWidgets import QMainWindow, QApplication , QFileDialog , QLabel
from enc_gui import *
import subprocess


class Crypto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Zed-Crypto")
        self.setFixedSize(838, 484)

        # Actions for encrypt tab
        self.ui.btn_box_encrypt.accepted.connect(self.Encrypt)

        # action for File upload
        self.ui.browse_encrypt.clicked.connect(self.Upload_File)
        self.ui.browse_decrypt.clicked.connect(self.Upload_File)

        # action for decrypt tab
        self.ui.btn_box_decrypt.accepted.connect(self.Decrypt)

        # close the window (cancel button)
        self.ui.btn_box_encrypt.rejected.connect(self.Rejected)
        self.ui.btn_box_decrypt.rejected.connect(self.Rejected)

        self.show()
        

    def Encrypt(self):
        args = ["openssl", "enc"]
        cipher = self.ui.cipher_encrypt.currentText()
        iters = self.ui.iters.currentText()
        args.append(cipher)
        args += ["-md" , "sha512", "-pbkdf2", "-iter"]
        args.append(iters)
        if self.ui.checkBox_salt.isChecked():
            args.append("-salt")
        args.append("-in")
        file_path = self.ui.lineEdit_file_encrypt.text()
        args.append(file_path)
        args.append("-out")
        output_file = self.ui.encrypt_output.text()
        args.append(output_file)
        enc_process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        enc_process.communicate()


    def Decrypt(self):
        args = ["openssl", "enc"]
        cipher = self.ui.cipher_decrypt.currentText()
        args.append(cipher)
        args += ["-md" , "sha512", "-pbkdf2" , "-in"]
        file_path = self.ui.lineEdit_file_dcrypt.text()
        args.append(file_path)
        args.append("-out")
        output_file = self.ui.decrypt_output.text()
        args.append(output_file)
        args.append("-d")
        dec_process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        dec_process.communicate()

    def Upload_File(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.ui.lineEdit_file_encrypt.setText(file[0])
        self.ui.lineEdit_file_dcrypt.setText(file[0])
    
    def Rejected(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Crypto()
    w.show()
    sys.exit(app.exec_())
