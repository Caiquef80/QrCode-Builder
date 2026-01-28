from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from pyshorteners import Shortener
from notifypy import Notify
import qrcode 


def CREATE_SHORT_URL(url):
  link = Shortener()
  return link.tinyurl.short(url)

def CREATE_QRCODE(url):
  img = qrcode.make(url)
  return img.save("teste.png")
    
class QRCodeBuilder(QMainWindow):
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      loadUi("untitled.ui", self)
      self.show()
      
     
    
    def getURL(self):
      return self.txtUrl.text()
    
    def setURL(self , url):
      self.txtUrlShort.setText(url)
      
    @pyqtSlot()
    def on_btnGerar_clicked(self):
      valor = self.getURL()
      if valor:
        url = CREATE_SHORT_URL(valor)
        CREATE_QRCODE(url)
        self.setURL(url)
        self.img.setPixmap(QPixmap("teste.png"))
      else:
        self.showMessage("Erro URL" , "É esperado que você passe uma URL")
        
    def showMessage(self , title , message):
      QMessageBox.information(self, title , message)
      

if __name__ == "__main__":
    app = QApplication([])
    tela = QRCodeBuilder()
    app.exec_()