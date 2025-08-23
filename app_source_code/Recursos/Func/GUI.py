##                                                              ##
## ░░      ░░░        ░░  ░░░░░░░░        ░░░      ░░░░      ░░ ##
## ▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒ ##
## ▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓      ▓▓▓▓      ▓▓ ##
## █        █████  █████  ███████████  ███████████  ████████  █ ##
## █  ████  ██        ██        ██        ███      ████      ██ ##
## ████████████████████████████████████████████████████████████ ##
##                                                              ##
##                      @ 2024 - Presente                       ##
##           byAd12.pages.dev | aili-ss.pages.dev               ##
##                                                              ##
## ____________________________________________________________ ##

import sys, os, json
from string import Template
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QIcon, QFont
from PySide6.QtCore import QSize
import Recursos.Func.main as FuncMainPY

if getattr(sys, 'frozen', False): RUTA_RECURSOS = os.path.join(sys._MEIPASS, "Recursos") # Windows .exe
else: RUTA_RECURSOS = "Recursos" # Código .py

def conseguir_RUTA_DIR_USUARIO_():
    if os.name == "nt": RUTA_DIR_USUARIO = os.path.join(os.environ.get("USERPROFILE", os.path.expanduser("~")), "AILISS_v2")
    else: RUTA_DIR_USUARIO = os.path.join(os.path.expanduser("~"), "AILISS_v2")

    return RUTA_DIR_USUARIO

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# TRADUCCIÓN AJUSTADA

with open(os.path.join(RUTA_RECURSOS, "TRANSLATE.json"), "r", encoding="utf-8") as TR_FILE_:
    TRADUCCIONES_COMPLETAS = json.load(TR_FILE_)

def __TR__(STRING):
    try:
        texto_base = TRADUCCIONES_COMPLETAS[FuncMainPY.obt_json_("IDIOMA")]["main.py"][STRING]
    except:
        FuncMainPY.ERR_REG_(f"[__TR__] Faltó variable para sustituir: {STRING}\n\n")
        return "Error_Idioma"
    
    ####

    plantilla = Template(texto_base)

    variables = {
        "version": FuncMainPY.obt_aili_json_(0),
        "FuncMainPY_obt_json_0": FuncMainPY.obt_json_(0),
        "FuncMainPY_obt_json_1": FuncMainPY.obt_json_(1),
        "FuncMainPY_obt_json_2": FuncMainPY.obt_json_(2),
        "FuncMainPY_obt_json_3": FuncMainPY.obt_json_(3),
        "FuncMainPY_obt_json_4": FuncMainPY.obt_json_(4),
        "FuncMainPY_obt_json_5": FuncMainPY.obt_json_(5),
        "FuncMainPY_obt_json_6": FuncMainPY.obt_json_(6),
        "FuncMainPY_obt_json_7": FuncMainPY.obt_json_(7),
        "FuncMainPY_obt_json_8": FuncMainPY.obt_json_(8),
        "NMAP_VERSION": FuncMainPY.version_nmap(),
    }

    try:
        return plantilla.substitute(variables)
    except KeyError as e:
        print(f"[__TR__] Faltó variable para sustituir: {e}")
        return texto_base

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def crear_boton_(text, icon_path, callback, bloquear_terminos, en_centro=False):
    button = QPushButton(text)
    button.clicked.connect(callback)
    
    if bloquear_terminos == True and FuncMainPY.obt_json_(8) != True:
        button.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "IconoX.png")))
    else:
        button.setIcon(QIcon(icon_path))
    
    button.setIconSize(QSize(30, 30))
    button.setProperty("tipo", "button1")

    button.setMinimumHeight(50)
    button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    font = QFont()
    font.setPointSize(12)
    button.setFont(font)

    if en_centro == False:
        button.setStyleSheet("text-align: left; padding-left: 10px;")
    else:
        button.setStyleSheet("text-align: center;")
    return button

def agregar_fila_botones(main_layout, botones):
    layout = QHBoxLayout()
    for boton in botones:
        layout.addWidget(boton)
    main_layout.addLayout(layout)
    return layout

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def ocultar_elemento_(elemento):
    if isinstance(elemento, QWidget):
        elemento.hide()
    elif isinstance(elemento, QLayoutItem):
        if elemento.widget():
            elemento.widget().hide()

def mostrar_elemento_(elemento):
    if isinstance(elemento, QWidget):
        elemento.show()
    elif isinstance(elemento, QLayoutItem):
        if elemento.widget():
            elemento.widget().show()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def centrar_ventana_(ventana):
    qr = ventana.frameGeometry()
    cp = QApplication.primaryScreen().availableGeometry().center()
    qr.moveCenter(cp)
    ventana.move(qr.topLeft())

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

# no se usa pero está :)
def refrescar_ico_boton_(boton):
    if boton.text() in [f"{__TR__('ESCANEO_REDES_WIFI')}", f"{__TR__('MONITORIZAR_RED')}", f"{__TR__('ESCANEO_HOSTS')}", f"{__TR__('ESCANEO_PUERTOS')}", f"{__TR__('ESCANEO_VULNERABILIDADES')}"] and FuncMainPY.obt_json_(8) != True:
        boton.setIcon(QIcon("Recursos/Logos/IconoX.png"))
    else:
        if boton.text() == f"{__TR__('MONITORIZAR_RED')}":
            boton.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoNPCAP.png")))

        elif boton.text() == f"{__TR__('ESCANEO_REDES_WIFI')}":
            boton.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "Logo.png")))
        else:
            boton.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoNMAP.png")))

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~