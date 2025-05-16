import shutil  
import sys     
import os      
from PySide6.QtWidgets import *  
from PySide6.QtGui import QIcon  
from teste_qt_ui import Ui_MainWindow 


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("File Organizer")
        appIcon = QIcon("bulbasaur.jgp")
        self.setWindowIcon(appIcon)
        
        self.btn_abrir.clicked.connect(self.open_path)
        self.pushButton.clicked.connect(self.organize)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str('folder with files'), '/home', QFileDialog.ShowDirsOnly | 
                                                    QFileDialog.DontResolveSymlinks)
        self.lineEdit.setText(self.path)
        self.path = str(self.path)

        
    def organize(self):
        path = self.path  
        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)  
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path + '/' + extension) 
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText('Files Organized')
        msg.exec()  
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    windown = MainWindow()
    windown.show()
    app.exec()