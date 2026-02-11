from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot , Qt
from PyQt5.uic import loadUi
from os import path
import sys

def loadFile(file):
  base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
  return path.join(base_path, file)

class Teste(QMainWindow):
   def __init__(self):
      super().__init__()
      loadUi(loadFile("./teste.ui"), self)
      self.setWindowFlag(Qt.FramelessWindowHint)
      self.setAttribute(Qt.WA_TranslucentBackground)
      self.show()

if __name__ == "__main__":
    app = QApplication([])
    tela = Teste()
    app.exec_()