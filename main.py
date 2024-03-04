import sys
from designer import *
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap


class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.abrirArquivo.triggered.connect(self.abrir)
        self.salvarArquivo.triggered.connect(self.salvar)
        self.redimensionarImagem.triggered.connect(self.redimensionar_imagem)
        self.sobreProjeto.triggered.connect(self.sobre)

    def abrir(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            '',
        )
        self.imagem_original = QPixmap(imagem)
        self.labelImg.setPixmap(self.imagem_original)
        self.inputLarguraImagem.setText(str(self.imagem_original.width()))
        self.inputAlturaImagem.setText(str(self.imagem_original.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            '',
            'Arquivos PNG (*.png)'
        )
        if not imagem:
            return
        self.imagem_nova.save(imagem, 'PNG', -1)

    def redimensionar_imagem(self):
        largura = int(self.inputLarguraImagem.text())
        self.imagem_nova = self.imagem_original.scaledToWidth(largura)
        self.labelImg.setPixmap(self.imagem_nova)
        self.inputLarguraImagem.setText(str(self.imagem_nova.width()))
        self.inputAlturaImagem.setText(str(self.imagem_nova.height()))

    def sobre(self):
        QMessageBox.about(
            self,
            "Sobre o Projeto",
            "Copyright © 2024, Jorge Sousa.\n"
            "(https://github.com/devjorgesousa/redimensionar)"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    redimensionar = Redimensionar()
    redimensionar.show()
    app.exec()
