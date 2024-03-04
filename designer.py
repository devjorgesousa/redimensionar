# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 465)
        icon = QIcon()
        icon.addFile(u"icones/icone.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.abrirArquivo = QAction(MainWindow)
        self.abrirArquivo.setObjectName(u"abrirArquivo")
        icon1 = QIcon()
        icon1.addFile(u"icones/abrir.svg", QSize(), QIcon.Normal, QIcon.On)
        self.abrirArquivo.setIcon(icon1)
        self.abrirArquivo.setIconVisibleInMenu(True)
        self.salvarArquivo = QAction(MainWindow)
        self.salvarArquivo.setObjectName(u"salvarArquivo")
        icon2 = QIcon()
        icon2.addFile(u"icones/salvar.svg", QSize(), QIcon.Normal, QIcon.On)
        self.salvarArquivo.setIcon(icon2)
        self.redimensionarImagem = QAction(MainWindow)
        self.redimensionarImagem.setObjectName(u"redimensionarImagem")
        icon3 = QIcon()
        icon3.addFile(u"icones/redimensionar.svg", QSize(), QIcon.Normal, QIcon.On)
        self.redimensionarImagem.setIcon(icon3)
        self.sobreProjeto = QAction(MainWindow)
        self.sobreProjeto.setObjectName(u"sobreProjeto")
        icon4 = QIcon()
        icon4.addFile(u"icones/sobre.svg", QSize(), QIcon.Normal, QIcon.On)
        self.sobreProjeto.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelLargura = QLabel(self.centralwidget)
        self.labelLargura.setObjectName(u"labelLargura")

        self.gridLayout.addWidget(self.labelLargura, 1, 0, 1, 1)

        self.inputAlturaImagem = QLineEdit(self.centralwidget)
        self.inputAlturaImagem.setObjectName(u"inputAlturaImagem")

        self.gridLayout.addWidget(self.inputAlturaImagem, 1, 3, 1, 1)

        self.labelAltura = QLabel(self.centralwidget)
        self.labelAltura.setObjectName(u"labelAltura")

        self.gridLayout.addWidget(self.labelAltura, 1, 2, 1, 1)

        self.inputLarguraImagem = QLineEdit(self.centralwidget)
        self.inputLarguraImagem.setObjectName(u"inputLarguraImagem")

        self.gridLayout.addWidget(self.inputLarguraImagem, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 487, 364))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelImg = QLabel(self.scrollAreaWidgetContents)
        self.labelImg.setObjectName(u"labelImg")

        self.gridLayout_2.addWidget(self.labelImg, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 21))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArquivo.addAction(self.abrirArquivo)
        self.menuArquivo.addAction(self.salvarArquivo)
        self.menuEditar.addAction(self.redimensionarImagem)
        self.menuAjuda.addAction(self.sobreProjeto)
        self.toolBar.addAction(self.abrirArquivo)
        self.toolBar.addAction(self.redimensionarImagem)
        self.toolBar.addAction(self.salvarArquivo)
        self.toolBar.addAction(self.sobreProjeto)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Redimensionar Imagem", None))
        self.abrirArquivo.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.abrirArquivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.salvarArquivo.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(shortcut)
        self.salvarArquivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.redimensionarImagem.setText(QCoreApplication.translate("MainWindow", u"Redimensionar", None))
#if QT_CONFIG(shortcut)
        self.redimensionarImagem.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.sobreProjeto.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
#if QT_CONFIG(shortcut)
        self.sobreProjeto.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.labelLargura.setText(QCoreApplication.translate("MainWindow", u"Largura:", None))
        self.labelAltura.setText(QCoreApplication.translate("MainWindow", u"Altura:", None))
        self.labelImg.setText("")
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

