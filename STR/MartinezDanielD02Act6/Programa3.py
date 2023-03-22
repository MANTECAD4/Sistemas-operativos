'''
Sistemas Operativos

Integrantes:
    Saul Alejandro Castañeda Perez
    Daniel Martinez Martinez
    
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import random

#Variables Globales
Procesos=0
Lotes = []
LotesTerminados=0
SubLotesPendientes=[]
CantProcesosBloqueados=0
Pos_lote=0
ContadorGlobal=0
BanderaProcesos=True
BanderaEjecucion=False
Bandera_Error=False
Bandera_P_C=False
BanderaInterrupcion=False
mouse_click=0
grip=0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global grip
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_superior.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"border:2px solid rgb(225, 131, 0); \n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BotonMenu = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.BotonMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagenes/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMenu.setIcon(icon)
        self.BotonMenu.setIconSize(QtCore.QSize(38, 38))
        self.BotonMenu.setObjectName("BotonMenu")
        self.horizontalLayout.addWidget(self.BotonMenu)
        spacerItem = QtWidgets.QSpacerItem(544, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.BotonMinimizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMinimizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMinimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMinimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagenes/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMinimizar.setIcon(icon1)
        self.BotonMinimizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMinimizar.setObjectName("BotonMinimizar")
        self.horizontalLayout.addWidget(self.BotonMinimizar)
        self.BotonMaximizar = QtWidgets.QPushButton(self.frame_superior)
        self.BotonMaximizar.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonMaximizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonMaximizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Imagenes/maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonMaximizar.setIcon(icon2)
        self.BotonMaximizar.setIconSize(QtCore.QSize(38, 38))
        self.BotonMaximizar.setObjectName("BotonMaximizar")
        self.horizontalLayout.addWidget(self.BotonMaximizar)
        self.BotonSalir = QtWidgets.QPushButton(self.frame_superior)
        self.BotonSalir.setMinimumSize(QtCore.QSize(50, 40))
        self.BotonSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonSalir.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Imagenes/exportar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BotonSalir.setIcon(icon3)
        self.BotonSalir.setIconSize(QtCore.QSize(38, 38))
        self.BotonSalir.setObjectName("BotonSalir")
        self.horizontalLayout.addWidget(self.BotonSalir)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuDesplegable = QtWidgets.QFrame(self.frame_contenido)
        self.MenuDesplegable.setMinimumSize(QtCore.QSize(200, 0))
        self.MenuDesplegable.setMaximumSize(QtCore.QSize(0, 16777215))
        self.MenuDesplegable.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.034, y1:0.983364, x2:1, y2:0, stop:0.0795455 rgba(239, 187, 0, 248), stop:1 rgba(239, 99, 0, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}")
        self.MenuDesplegable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuDesplegable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuDesplegable.setObjectName("MenuDesplegable")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MenuDesplegable)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Asignar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Asignar.setMinimumSize(QtCore.QSize(135, 45))
        self.Asignar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Asignar.setObjectName("Asignar")
        self.verticalLayout.addWidget(self.Asignar)
        self.Procesos = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Procesos.setMinimumSize(QtCore.QSize(135, 45))
        self.Procesos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Procesos.setObjectName("Procesos")
        self.verticalLayout.addWidget(self.Procesos)
        self.Tiempos = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Tiempos.setMinimumSize(QtCore.QSize(135, 45))
        self.Tiempos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tiempos.setObjectName("Tiempos")
        self.verticalLayout.addWidget(self.Tiempos)
        spacerItem1 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.Ocultar = QtWidgets.QPushButton(self.MenuDesplegable)
        self.Ocultar.setMinimumSize(QtCore.QSize(135, 45))
        self.Ocultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ocultar.setObjectName("Ocultar")
        self.verticalLayout.addWidget(self.Ocultar)
        self.horizontalLayout_2.addWidget(self.MenuDesplegable)
        self.Contenido = QtWidgets.QFrame(self.frame_contenido)
        self.Contenido.setStyleSheet("")
        self.Contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Contenido.setObjectName("Contenido")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Contenido)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Contenido)
        self.stackedWidget.setStyleSheet("QFrame{\n"
"background-color: rgb(0,0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:rgb(0,0, 0);\n"
"font: 77 16pt \"Arial Black\";\n"
"color:rgb(225, 131, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"font: 77 12pt \"Arial Black\";\n"
"color:rgb(225,225,225);\n"
"border-bottom:2px solid rgb(225, 131, 0); \n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(0,0, 0);\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid#ff8300;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"background-color:rgb(0,0,0);\n"
"border-radius:20px;\n"
"color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid#ffffff;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0, 0);\n"
"gridline-color:rgb(225, 131, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:0px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color:rgb(0,0, 0);\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"border:2px solid rgb(225, 131, 0);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Asignar = QtWidgets.QWidget()
        self.page_Asignar.setObjectName("page_Asignar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_Asignar)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.page_Asignar)
        self.label_2.setStyleSheet("font: 77 20pt \"Arial Black\";")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_Asignar)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_Asignar)
        self.pushButton_2.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 104, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.page_Asignar)
        self.page_Procesos = QtWidgets.QWidget()
        self.page_Procesos.setStyleSheet("")
        self.page_Procesos.setObjectName("page_Procesos")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_Procesos)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.label = QtWidgets.QLabel(self.page_Procesos)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_21.setMaximumSize(QtCore.QSize(60, 35))
        self.lineEdit_21.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"")
        self.lineEdit_21.setText("")
        self.lineEdit_21.setMaxLength(30)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_12.addWidget(self.lineEdit_21)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(13, 266, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.page_Procesos)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_9.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_16 = QtWidgets.QLabel(self.page_Procesos)
        self.label_16.setMinimumSize(QtCore.QSize(60, 30))
        self.label_16.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.page_Procesos)
        self.label_17.setMinimumSize(QtCore.QSize(60, 30))
        self.label_17.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page_Procesos)
        self.label_20.setMinimumSize(QtCore.QSize(60, 30))
        self.label_20.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_13.setMaxLength(5)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 1, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_17.setMaxLength(30)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_25.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_25.setMaxLength(30)
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout.addWidget(self.lineEdit_25, 1, 2, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_14.setMaxLength(5)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 2, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_18.setMaxLength(30)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 2, 1, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_23.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_23.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_23.setMaxLength(30)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout.addWidget(self.lineEdit_23, 2, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_16.setMaxLength(5)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 3, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_19.setMaxLength(30)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout.addWidget(self.lineEdit_19, 3, 1, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_24.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_24.setMaxLength(30)
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout.addWidget(self.lineEdit_24, 3, 2, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_15.setMaxLength(5)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 4, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_20.setMaxLength(30)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout.addWidget(self.lineEdit_20, 4, 1, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(60, 30))
        self.lineEdit_26.setMaxLength(30)
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout.addWidget(self.lineEdit_26, 4, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem12)
        self.label_11 = QtWidgets.QLabel(self.page_Procesos)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_11.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_Procesos)
        self.tableWidget_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(197, 140))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(197, 140))
        self.tableWidget_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(True)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_2.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.tableWidget_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.page_Procesos)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_8.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.page_Procesos)
        self.label_10.setMinimumSize(QtCore.QSize(0, 35))
        self.label_10.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_7.setMaxLength(5)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_Procesos)
        self.label_12.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_9.setMaxLength(30)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_Procesos)
        self.label_13.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_10.setMaxLength(20)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page_Procesos)
        self.label_14.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_11.setMaxLength(20)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_Procesos)
        self.label_15.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(150, 35))
        self.lineEdit_12.setMaxLength(20)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 4, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.page_Procesos)
        self.label_19.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.page_Procesos)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(60, 35))
        self.lineEdit_22.setMaximumSize(QtCore.QSize(60, 35))
        self.lineEdit_22.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"")
        self.lineEdit_22.setText("")
        self.lineEdit_22.setMaxLength(30)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_10.addWidget(self.lineEdit_22)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.page_Procesos)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 34))
        self.label_18.setStyleSheet("border:2px solid rgb(225, 131, 0); \n"
"color: rgb(225,225,225);\n"
"")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        self.tableWidget = QtWidgets.QTableWidget(self.page_Procesos)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(287, 370))
        self.tableWidget.setMaximumSize(QtCore.QSize(287, 16777215))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_14.addWidget(self.tableWidget)
        spacerItem15 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem15)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        spacerItem16 = QtWidgets.QSpacerItem(13, 266, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.pushButton_9 = QtWidgets.QPushButton(self.page_Procesos)
        self.pushButton_9.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_11.addWidget(self.pushButton_9)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        spacerItem19 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem19)
        self.stackedWidget.addWidget(self.page_Procesos)
        self.page_Tiempos = QtWidgets.QWidget()
        self.page_Tiempos.setObjectName("page_Tiempos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_Tiempos)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem20 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem20)
        self.label_21 = QtWidgets.QLabel(self.page_Tiempos)
        self.label_21.setStyleSheet("font: 32pt \"Ink Free\";")
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_Tiempos)
        self.tableWidget_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(841, 300))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(841, 800))
        self.tableWidget_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_3.setAutoFillBackground(False)
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setAutoScrollMargin(16)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setTabKeyNavigation(True)
        self.tableWidget_3.setProperty("showDropIndicator", True)
        self.tableWidget_3.setDragEnabled(False)
        self.tableWidget_3.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_3.setAlternatingRowColors(False)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_3.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_3.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_3.setWordWrap(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(10)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_7.addWidget(self.tableWidget_3)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem23)
        self.pushButton_8 = QtWidgets.QPushButton(self.page_Tiempos)
        self.pushButton_8.setMinimumSize(QtCore.QSize(135, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(135, 45))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem24)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem25 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem25)
        self.stackedWidget.addWidget(self.page_Tiempos)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.horizontalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #De aqui empezamos
        self.MenuDesplegable.hide()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #Botones frameSuperior
        self.BotonMenu.clicked.connect(lambda: self.MostrarMenu())
        self.BotonMaximizar.clicked.connect(lambda: self.Maximizar())
        self.BotonMinimizar.clicked.connect(lambda: self.Minimizar())
        self.BotonSalir.clicked.connect(lambda: self.close())
        #Botones del menu
        self.Asignar.clicked.connect(lambda: self.MostrarPestañaAsignar())
        self.Procesos.clicked.connect(lambda: self.MostrarPestañaProcesos())
        self.Tiempos.clicked.connect(lambda: self.MostrarPestañaTiempos())
        self.Ocultar.clicked.connect(lambda: self.OcultarMenu())
        #PaginaAsignar
        self.lineEdit_2.textChanged.connect(lambda: self.EstadoInicial2())
        self.lineEdit_2.editingFinished.connect(lambda: self.lineEdit_2_Enter())
        self.pushButton_2.clicked.connect(lambda: self.PesstañaAsignar_Boton())
        #PaginaProcesos
        self.pushButton_9.clicked.connect(lambda: self.MostrarPestañaTiempos())
        #PaginaTiempos
        self.pushButton_8.clicked.connect(lambda: self.RestablecerValores())
        #CapturarEntradas
        MainWindow.keyPressEvent = self.CapturarTeclas
        self.tableWidget.keyPressEvent = self.CapturarTeclas
        #Mover ventana
        self.frame_superior.mouseMoveEvent = self.MoverVentana
        self.frame_superior.mousePressEvent = self.GetMousePos
        #Creacion de SizeGrip
        grip=QtWidgets.QSizeGrip(MainWindow)
        grip.resize(20, 20)
        #Acomodo de SizeGrip
        MainWindow.resizeEvent = self.RedimencionarVentana

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Asignar.setText(_translate("MainWindow", "Asignar"))
        self.Procesos.setText(_translate("MainWindow", "Procesos"))
        self.Tiempos.setText(_translate("MainWindow", "Tiempos"))
        self.Ocultar.setText(_translate("MainWindow", "Ocultar"))
        self.label_2.setText(_translate("MainWindow", "¿Cuantos procesos deseas realizar?"))
        self.pushButton_2.setText(_translate("MainWindow", "Continuar"))
        self.label.setText(_translate("MainWindow", "Nuevos: "))
        self.label_9.setText(_translate("MainWindow", "Listos"))
        self.label_16.setText(_translate("MainWindow", "ID"))
        self.label_17.setText(_translate("MainWindow", "TME"))
        self.label_20.setText(_translate("MainWindow", "TT"))
        self.label_11.setText(_translate("MainWindow", "Bloqueados"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TTB"))
        self.label_8.setText(_translate("MainWindow", "Proceso en ejecución"))
        self.label_10.setText(_translate("MainWindow", "ID: "))
        self.label_12.setText(_translate("MainWindow", "Operacion: "))
        self.label_13.setText(_translate("MainWindow", "TME: "))
        self.label_14.setText(_translate("MainWindow", "TT: "))
        self.label_15.setText(_translate("MainWindow", "TR: "))
        self.label_19.setText(_translate("MainWindow", "Contador global: "))
        self.label_18.setText(_translate("MainWindow", "Terminados"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Resultado"))
        self.pushButton_9.setText(_translate("MainWindow", "Continuar"))
        self.label_21.setText(_translate("MainWindow", "Informacion de Procesos"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TME"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "T.Llegada"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "T.Finalizacion"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T.Retorno"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T.Respuesta"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "T.Espera"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "T.Servicio"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Resultado"))
        self.pushButton_8.setText(_translate("MainWindow", "Restablecer"))

    #Funciones
    def MostrarMenu(self):
        if self.MenuDesplegable.isHidden():
            self.MenuDesplegable.show()
        else:
            self.MenuDesplegable.hide()
    def Maximizar(self):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
        else:
            MainWindow.showMaximized()
    def Minimizar(self):
        MainWindow.showMinimized()
    def close(self):
        MainWindow.close()
    
    #Funciones del menu
    def MostrarPestañaAsignar(self):
        self.stackedWidget.setCurrentWidget(self.page_Asignar)
    def MostrarPestañaProcesos(self):
        self.stackedWidget.setCurrentWidget(self.page_Procesos)
    def MostrarPestañaTiempos(self):
        self.stackedWidget.setCurrentWidget(self.page_Tiempos)
    def OcultarMenu(self):
        self.MenuDesplegable.hide()
    
    #PaginaAsignar
    def EstadoInicial2(self):
        self.lineEdit_2.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
    def lineEdit_2_Enter(self):
        self.pushButton_2.click()
    def PesstañaAsignar_Boton(self):
        global Procesos
        if Procesos!=0:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid red;")
            return
        try:
            Cebo=int(self.lineEdit_2.text())
        except:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid red;")
            return
        if Cebo<1 or Cebo>101:
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid yellow;")
            return
        Procesos=Cebo
        self.stackedWidget.setCurrentWidget(self.page_Procesos)
        self.lineEdit_2.setReadOnly(True)
        self.GeneradorDeMinioms()
    def GeneradorDeMinioms(self):
        global Procesos
        Operadores=['+','-','*','/','%']
        ID_Aleatorio=random.sample(range(1, 101),Procesos)
        for x in range(Procesos):
            SubLote=[ID_Aleatorio[x],random.randint(5, 16),0,0,0,-1,0,0,('{}{}{}'.format(random.randint(-100, 100),random.choice(Operadores),random.randint(1, 100)))]
            Lotes.append(SubLote)
        Lotes.sort()
        self.stackedWidget.setCurrentWidget(self.page_Procesos)
        self.LlenadoDeDatos()
        
    #PaginaProcesos
    def aMimir(self,time):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(time, loop.quit)
        loop.exec_()
        
    def ProcesarDatos(self,x):
        global BanderaEjecucion,Bandera_Error,Bandera_P_C,BanderaInterrupcion,ContadorGlobal
        BanderaEjecucion=True
        if Lotes[x][5]==-1:
            Lotes[x][5]=ContadorGlobal-Lotes[x][2]
        self.lineEdit_10.setText('{}'.format(Lotes[x][1]))
        self.lineEdit_11.setText('{}'.format(Lotes[x][7]))
        self.lineEdit_12.setText('{}'.format(Lotes[x][1]-Lotes[x][7]))
        self.aMimir(500)
        for i in range(Lotes[x][7],Lotes[x][1]):
            if Bandera_Error:
                break
            if Bandera_P_C:
                while True:
                    if not Bandera_P_C:
                        break
                    self.aMimir(50)
            if BanderaInterrupcion:
                self.lineEdit_7.clear()
                self.lineEdit_9.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()
                self.lineEdit_12.clear()
                BanderaInterrupcion=False
                return True
            self.lineEdit_7.setText('{}'.format(Lotes[x][0]))
            self.lineEdit_9.setText(Lotes[x][8])
            self.lineEdit_11.setText('{}'.format(i+1))
            self.lineEdit_12.setText('{}'.format(Lotes[x][1]-i-1))
            Lotes[x][7]+=1
            self.ContadorGlobal()
            self.DesbloquearProceso()
            self.aMimir(500)
        BanderaEjecucion=False
        Lotes[x][3]=ContadorGlobal
        Lotes[x][4]=Lotes[x][3]-Lotes[x][2]
        Lotes[x][6]=Lotes[x][4]-Lotes[x][7]
        self.aMimir(200)
        self.lineEdit_7.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.aMimir(100)
        self.ProcesosFinalizados(Lotes[x][0],Lotes[x][1],Lotes[x][2],Lotes[x][3],Lotes[x][4],Lotes[x][5],Lotes[x][6],Lotes[x][7],Lotes[x][8])
        self.aMimir(500)
        return False
    def BloquearProceso(self,x):
        global CantProcesosBloqueados
        self.tableWidget_2.setRowCount(CantProcesosBloqueados+1)
        item = QtWidgets.QTableWidgetItem('{}'.format(x))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(CantProcesosBloqueados, 0, item)
        item = QtWidgets.QTableWidgetItem('0')
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(CantProcesosBloqueados, 1, item)
        CantProcesosBloqueados+=1
        self.aMimir(500)
    def SalidaDelAnexo(self,paciente,x):
        if paciente==1:
            self.lineEdit_13.setText('{}'.format(Lotes[x][0]))
            self.lineEdit_17.setText('{}'.format(Lotes[x][1]))
            self.lineEdit_25.setText('{}'.format(Lotes[x][7]))
        elif paciente==2:
            self.lineEdit_14.setText('{}'.format(Lotes[x][0]))
            self.lineEdit_18.setText('{}'.format(Lotes[x][1]))
            self.lineEdit_23.setText('{}'.format(Lotes[x][7]))
        elif paciente==3:
            self.lineEdit_16.setText('{}'.format(Lotes[x][0]))
            self.lineEdit_19.setText('{}'.format(Lotes[x][1]))
            self.lineEdit_24.setText('{}'.format(Lotes[x][7]))
        else:
            self.lineEdit_15.setText('{}'.format(Lotes[x][0]))
            self.lineEdit_20.setText('{}'.format(Lotes[x][1]))
            self.lineEdit_26.setText('{}'.format(Lotes[x][7]))
        self.aMimir(500)
    def DesbloquearProceso(self):
        global CantProcesosBloqueados
        if CantProcesosBloqueados == 0:
            return
        i=0
        while i!=CantProcesosBloqueados:
            TTB=self.tableWidget_2.item(i,1)
            TTB=int(TTB.text())
            if TTB==8:
                ID=self.tableWidget_2.item(i,0)
                for x in range(len(SubLotesPendientes)):
                    if Lotes[SubLotesPendientes[x][1]][0]==int(ID.text()):
                        SubLotesPendientes[x][0]=SubLotesPendientes[x][0]*-1
                        self.tableWidget_2.removeRow(i)
                        self.SalidaDelAnexo(SubLotesPendientes[x][0],SubLotesPendientes[x][1])
                        CantProcesosBloqueados-=1
                        i-=1
                        break
            else:
                item = QtWidgets.QTableWidgetItem('{}'.format(TTB+1))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 1, item)
            i+=1
    def LlenadoDeDatos(self):
        global Procesos,BanderaProcesos,CantProcesosBloqueados,ContadorGlobal
        ContadorMinioms=0;
        BanderaProcesos=False
        self.lineEdit_21.setText('{}'.format(Procesos))
        self.lineEdit_22.setText('0')
        self.aMimir(500)
        if ContadorMinioms<Procesos:
            Lotes[ContadorMinioms][2]=ContadorGlobal
            self.lineEdit_13.setText('{}'.format(Lotes[ContadorMinioms][0]))
            self.lineEdit_17.setText('{}'.format(Lotes[ContadorMinioms][1]))
            self.lineEdit_25.setText('{}'.format(Lotes[ContadorMinioms][7]))
            catch=[1,ContadorMinioms,Lotes[ContadorMinioms][1]]
            SubLotesPendientes.append(catch)
            ContadorMinioms+=1
            self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
            self.aMimir(500)
            if ContadorMinioms<Procesos:
                Lotes[ContadorMinioms][2]=ContadorGlobal
                self.lineEdit_14.setText('{}'.format(Lotes[ContadorMinioms][0]))
                self.lineEdit_18.setText('{}'.format(Lotes[ContadorMinioms][1]))
                self.lineEdit_23.setText('{}'.format(Lotes[ContadorMinioms][7]))
                catch=[2,ContadorMinioms,Lotes[ContadorMinioms][1]]
                SubLotesPendientes.append(catch)
                ContadorMinioms+=1
                self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
                self.aMimir(500)
                if ContadorMinioms<Procesos:
                    Lotes[ContadorMinioms][2]=ContadorGlobal
                    self.lineEdit_16.setText('{}'.format(Lotes[ContadorMinioms][0]))
                    self.lineEdit_19.setText('{}'.format(Lotes[ContadorMinioms][1]))
                    self.lineEdit_24.setText('{}'.format(Lotes[ContadorMinioms][7]))
                    catch=[3,ContadorMinioms,Lotes[ContadorMinioms][1]]
                    SubLotesPendientes.append(catch)
                    ContadorMinioms+=1
                    self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
                    self.aMimir(500)
                    if ContadorMinioms<Procesos:
                        Lotes[ContadorMinioms][2]=ContadorGlobal
                        self.lineEdit_15.setText('{}'.format(Lotes[ContadorMinioms][0]))
                        self.lineEdit_20.setText('{}'.format(Lotes[ContadorMinioms][1]))
                        self.lineEdit_26.setText('{}'.format(Lotes[ContadorMinioms][7]))
                        catch=[4,ContadorMinioms,Lotes[ContadorMinioms][1]]
                        SubLotesPendientes.append(catch)
                        ContadorMinioms+=1
                        self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
                        self.aMimir(500)     
        while(len(SubLotesPendientes)!=0):
            SubLotesPendientes.sort(key=lambda x: x[2])
            self.lineEdit_13.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_17.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_25.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_14.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_18.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_23.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_16.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_19.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_24.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_15.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_20.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_26.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            if CantProcesosBloqueados==len(SubLotesPendientes):
                self.DesbloquearProceso()
                self.ContadorGlobal()
                self.aMimir(500)
            if SubLotesPendientes[0][0]==1:
                self.lineEdit_13.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_17.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_25.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.aMimir(250)
                self.lineEdit_13.clear()
                self.lineEdit_17.clear()
                self.lineEdit_25.clear()
                self.aMimir(250)
                if self.ProcesarDatos(SubLotesPendientes[0][1]):
                    self.BloquearProceso(Lotes[SubLotesPendientes[0][1]][0])
                    SubLotesPendientes[0][0]=-1
                    SubLotesPendientes.append(SubLotesPendientes[0])
                else:
                    if ContadorMinioms<Procesos:
                        Lotes[ContadorMinioms][2]=ContadorGlobal
                        self.lineEdit_13.setText('{}'.format(Lotes[ContadorMinioms][0]))
                        self.lineEdit_17.setText('{}'.format(Lotes[ContadorMinioms][1]))
                        self.lineEdit_25.setText('{}'.format(Lotes[ContadorMinioms][7]))
                        catch=[1,ContadorMinioms,Lotes[ContadorMinioms][1]]
                        SubLotesPendientes.append(catch)
                        ContadorMinioms+=1
                        self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
            elif SubLotesPendientes[0][0]==2:
                self.lineEdit_14.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_18.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_23.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.aMimir(250)
                self.lineEdit_14.clear()
                self.lineEdit_18.clear()
                self.lineEdit_23.clear()
                self.aMimir(250)
                if self.ProcesarDatos(SubLotesPendientes[0][1]):
                    self.BloquearProceso(Lotes[SubLotesPendientes[0][1]][0])
                    SubLotesPendientes[0][0]=-2
                    SubLotesPendientes.append(SubLotesPendientes[0])
                else:
                    if ContadorMinioms<Procesos:
                        Lotes[ContadorMinioms][2]=ContadorGlobal
                        self.lineEdit_14.setText('{}'.format(Lotes[ContadorMinioms][0]))
                        self.lineEdit_18.setText('{}'.format(Lotes[ContadorMinioms][1]))
                        self.lineEdit_23.setText('{}'.format(Lotes[ContadorMinioms][7]))
                        catch=[2,ContadorMinioms,Lotes[ContadorMinioms][1]]
                        SubLotesPendientes.append(catch)
                        ContadorMinioms+=1
                        self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
            elif SubLotesPendientes[0][0]==3:
                self.lineEdit_16.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_19.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_24.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.aMimir(250)
                self.lineEdit_16.clear()
                self.lineEdit_19.clear()
                self.lineEdit_24.clear()
                self.aMimir(250)
                if self.ProcesarDatos(SubLotesPendientes[0][1]):
                    self.BloquearProceso(Lotes[SubLotesPendientes[0][1]][0])
                    SubLotesPendientes[0][0]=-3
                    SubLotesPendientes.append(SubLotesPendientes[0])
                else:
                    if ContadorMinioms<Procesos:
                        Lotes[ContadorMinioms][2]=ContadorGlobal
                        self.lineEdit_16.setText('{}'.format(Lotes[ContadorMinioms][0]))
                        self.lineEdit_19.setText('{}'.format(Lotes[ContadorMinioms][1]))
                        self.lineEdit_24.setText('{}'.format(Lotes[ContadorMinioms][7]))
                        catch=[3,ContadorMinioms,Lotes[ContadorMinioms][1]]
                        SubLotesPendientes.append(catch)
                        ContadorMinioms+=1
                        self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
            elif SubLotesPendientes[0][0]==4:
                self.lineEdit_15.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_20.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_26.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.aMimir(250)
                self.lineEdit_15.clear()
                self.lineEdit_20.clear()
                self.lineEdit_26.clear()
                self.aMimir(250)
                if self.ProcesarDatos(SubLotesPendientes[0][1]):
                    self.BloquearProceso(Lotes[SubLotesPendientes[0][1]][0])
                    SubLotesPendientes[0][0]=-4
                    SubLotesPendientes.append(SubLotesPendientes[0])
                else:
                    if ContadorMinioms<Procesos:
                        Lotes[ContadorMinioms][2]=ContadorGlobal
                        self.lineEdit_15.setText('{}'.format(Lotes[ContadorMinioms][0]))
                        self.lineEdit_20.setText('{}'.format(Lotes[ContadorMinioms][1]))
                        self.lineEdit_26.setText('{}'.format(Lotes[ContadorMinioms][7]))
                        catch=[4,ContadorMinioms,Lotes[ContadorMinioms][1]]
                        SubLotesPendientes.append(catch)
                        ContadorMinioms+=1
                        self.lineEdit_21.setText('{}'.format(Procesos-ContadorMinioms))
            else:
                SubLotesPendientes.append(SubLotesPendientes[0])
            if SubLotesPendientes[0][0]==-1:
                self.lineEdit_13.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_17.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_25.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
            if SubLotesPendientes[0][0]==-2:
                self.lineEdit_14.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_18.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_23.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
            if SubLotesPendientes[0][0]==-3:
                self.lineEdit_16.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_19.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_24.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
            if SubLotesPendientes[0][0]==-4:
                self.lineEdit_15.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_20.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
                self.lineEdit_26.setStyleSheet("border-bottom:2px solid rgb(0, 255, 0);")
            SubLotesPendientes.pop(0)
            self.aMimir(500)
        BanderaProcesos=True
        self.pushButton_8.setStyleSheet("QPushButton{border:2px solid#ff8300}\nQPushButton:Hover{border:2px solid#ffffff}")
        self.lineEdit_22.setStyleSheet("border:2px solid rgb(0, 255, 0);")
        self.lineEdit_13.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_17.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_25.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_14.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_18.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_23.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_16.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_19.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_24.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_15.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_20.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
        self.lineEdit_26.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
    #PaginaFinalizados
    def ProcesosFinalizados(self,ID,TME,TL,TF,TRo,TRa,TE,TS,Operacion):
        global LotesTerminados,Pos_lote,Bandera_Error
        self.tableWidget.setRowCount(Pos_lote+1)
        self.tableWidget_3.setRowCount(Pos_lote+1)
        #Terminados
        item = QtWidgets.QTableWidgetItem('{}'.format(ID))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        if Bandera_Error:
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.FDiagPattern)
            item.setBackground(brush)
        self.tableWidget.setItem(Pos_lote, 0, item)
        item = QtWidgets.QTableWidgetItem(Operacion)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        if Bandera_Error:
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.FDiagPattern)
            item.setBackground(brush)
        self.tableWidget.setItem(Pos_lote, 1, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(int(eval(Operacion))))
        if Bandera_Error:
            item = QtWidgets.QTableWidgetItem('ERROR')
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.FDiagPattern)
            item.setBackground(brush)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(Pos_lote, 2, item)
        #Tiempos
        item = QtWidgets.QTableWidgetItem('{}'.format(ID))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 0, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TME))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 1, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TL))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 2, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TF))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 3, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TRo))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 4, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TRa))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 5, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TE))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 6, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(TS))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 7, item)
        item = QtWidgets.QTableWidgetItem('{}'.format(Operacion))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 8, item)
        if Bandera_Error:
            item = QtWidgets.QTableWidgetItem('ERROR')
        else:
            item = QtWidgets.QTableWidgetItem('{}'.format(int(eval(Operacion)))) 
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(Pos_lote, 9, item)
        Bandera_Error=False
        Pos_lote+=1
    def ContadorGlobal(self):
        global ContadorGlobal
        ContadorGlobal+=1
        self.lineEdit_22.setText('{}'.format(ContadorGlobal))
    def RestablecerValores(self):
        global Procesos,ContadorGlobal,BanderaProcesos,LotesTerminados,Pos_lote,BanderaEjecucion,Bandera_Error,Bandera_P_C,BanderaInterrupcion,CantidadLotesTerminados
        if BanderaProcesos:
            Procesos=0
            ContadorGlobal=0
            LotesTerminados=0
            Pos_lote=0
            CantidadLotesTerminados=0
            BanderaEjecucion=False
            Bandera_Error=False
            Bandera_P_C=False
            BanderaInterrupcion=False
            for x in range(len(Lotes)):
                Lotes.pop()
            self.lineEdit_2.clear()
            self.lineEdit_2.setStyleSheet("border-bottom:2px solid rgb(225, 131, 0);")
            self.lineEdit_2.setReadOnly(False)
            
            self.lineEdit_21.clear()
            
            self.tableWidget.setRowCount(0)
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_3.setRowCount(0)
            self.lineEdit_22.clear()
            self.lineEdit_22.setStyleSheet("border:2px solid rgb(225, 131, 0);")
            
            self.stackedWidget.setCurrentWidget(self.page_Asignar)
        else:
            self.pushButton_8.setStyleSheet("border:2px solid red")
    
    def CapturarTeclas(self,event):
        global BanderaEjecucion,Bandera_Error,Bandera_P_C,BanderaInterrupcion
        if BanderaEjecucion:
            if event.text()=='e' or event.text()=='E':
                if not Bandera_P_C:
                    Bandera_Error=True
            elif event.text()=='p' or event.text()=='P':
                Bandera_P_C=True
            elif event.text()=='c' or event.text()=='C':
                Bandera_P_C=False
            elif event.text()=='i' or event.text()=='I':
                if not Bandera_P_C:
                    BanderaInterrupcion=True
    def GetMousePos(self,event):
        global mouse_click
        mouse_click = event.globalPos()
    def MoverVentana(self,event):
        global mouse_click
        if not MainWindow.isMaximized():
            if event.buttons() == QtCore.Qt.LeftButton:
                MainWindow.move(MainWindow.pos() + event.globalPos() - mouse_click)
                mouse_click = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            MainWindow.showMaximized()
        else:
            MainWindow.showNormal()
    def RedimencionarVentana(self,event):
        global grip
        rect = MainWindow.rect()
        grip.move(rect.right()-20, rect.bottom()-20)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
