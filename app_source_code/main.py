##                                                              ##
## ░░      ░░░        ░░  ░░░░░░░░        ░░░      ░░░░      ░░ ##
## ▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒ ##
## ▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓      ▓▓▓▓      ▓▓ ##
## █        █████  █████  ███████████  ███████████  ████████  █ ##
## █  ████  ██        ██        ██        ███      ████      ██ ##
## ████████████████████████████████████████████████████████████ ##
##                                                              ##
##                      @ 2024 - Presente                       ##
##                         MIT LICENSE                          ##
##           byAd12.pages.dev | aili-ss.pages.dev               ##
##                                                              ##
## ____________________________________________________________ ##


import datetime, os

global TIEMPO_INICIO; TIEMPO_INICIO = datetime.datetime.now()
global IDIOMA_ELEGIDO; IDIOMA_ELEGIDO = False

import sys, os, json
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
from string import Template

# En LINUX se fuerza buscar los paquetes de Qt en esa ruta
if os.name != "nt":
    if hasattr(sys, "_MEIPASS"):
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(sys._MEIPASS, "platforms")

from Recursos.Func.main import crear_directorios_

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ruta de ejecución

crear_directorios_()

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
        "ruta_usuario_carpeta": os.path.abspath(conseguir_RUTA_DIR_USUARIO_()),
        "NMAP_VERSION": FuncMainPY.version_nmap(),
    }

    try:
        return plantilla.substitute(variables)
    except KeyError as e:
        print(f"[__TR__] Faltó variable para sustituir: {e}")
        return texto_base

# __TR__('')

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# 

def listar_archivos_directorio(directorio):
    for carpeta, subcarpetas, archivos in os.walk(directorio):
        nivel = carpeta.replace(directorio, '').count(os.sep)
        indentacion = ' ' * 4 * (nivel)
        print(f"{indentacion}{os.path.basename(carpeta)}/")
        subindentacion = ' ' * 4 * (nivel + 1)
        for archivo in archivos:
            print(f"{subindentacion}{archivo}")

# listar_archivos_directorio(RUTA_RECURSOS)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Primero instalar las dependencias

import time, requests, webbrowser, socket, nmap, ipaddress, ping3
import whois as whois_lib
from urllib.parse import urlparse
from scapy.all import *
from bs4 import BeautifulSoup
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QKeySequence, QIcon, QTextCursor, QAction, QShortcut
from PySide6.QtCore import Qt, QTimer, QSize, Signal, QObject, QEventLoop, QThreadPool, QRunnable
import dns.resolver

import Recursos.Func.main as FuncMainPY
import Recursos.Func.GUI as FuncGuiPY

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla de carga (Solo logo)

def p_carga_():
    VENTANA_carga = QMainWindow()
    VENTANA_carga.setFixedSize(200, 200)
    FuncGuiPY.centrar_ventana_(VENTANA_carga)
    VENTANA_carga.setWindowTitle(f"{__TR__('CARGAR_SOFTWARE')}")
    VENTANA_carga.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.CustomizeWindowHint)

    label = QLabel(VENTANA_carga)
    label.setGeometry(0, 0, VENTANA_carga.width(), VENTANA_carga.height())
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    label.setPixmap(pixmap.scaled(VENTANA_carga.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
    
    global TIEMPO_CARGA_LOGO; TIEMPO_CARGA_LOGO = datetime.now()

    return VENTANA_carga

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla de los términos de uso

def p_idioma_():
    VENTANA0 = QMainWindow()
    VENTANA0.setFixedSize(425, 150)
    FuncGuiPY.centrar_ventana_(VENTANA0)
    VENTANA0.setWindowTitle("AILI-SS")
    VENTANA0.setStyleSheet(FuncMainPY.estilos_())
    main_layout = QVBoxLayout()

    ############

    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"Idioma / Language")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def cambiar_idioma_(idioma):
        FuncMainPY.gua_json_(FuncMainPY.obt_json_(0),
                            FuncMainPY.obt_json_("01"),
                            FuncMainPY.obt_json_(1),
                            FuncMainPY.obt_json_(2),
                            FuncMainPY.obt_json_(3),
                            FuncMainPY.obt_json_(4),
                            FuncMainPY.obt_json_(5),
                            FuncMainPY.obt_json_(6),
                            FuncMainPY.obt_json_(7),
                            FuncMainPY.obt_json_(8),
                            idioma)

        if FuncMainPY.r_gr_(2): p_principal_(VENTANA0)
        else: p_terminos_(VENTANA0) # Si no hay archivo con clave,-1

    ############

    # Botones
    button1 = QPushButton(f"es-ESPAÑA")
    button1.clicked.connect(lambda: cambiar_idioma_("es-ESPAÑA"))
    button1.setProperty("tipo", "button1")

    button2 = QPushButton(f"en-UNITED_KINGDOM")
    button2.clicked.connect(lambda: cambiar_idioma_("en-UNITED_KINGDOM"))
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"gl-GALICIA")
    button3.clicked.connect(lambda: cambiar_idioma_("gl-GALICIA"))
    button3.setProperty("tipo", "button1")

    ############

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA0.setCentralWidget(widget_principal)

    global IDIOMA_ELEGIDO; IDIOMA_ELEGIDO = True

    VENTANA0.show()
    return VENTANA0

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla de los términos de uso

def p_terminos_(ventana=None):
    if ventana != None:
        ventana.close()

    VENTANA1 = QMainWindow()
    VENTANA1.setFixedSize(700, 400)
    FuncGuiPY.centrar_ventana_(VENTANA1)
    VENTANA1.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA1.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_TERMINOS_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setHtml(FuncMainPY.terminos_())
    text_edit.setReadOnly(True)
    text_edit.setObjectName("TerminosText")
    text_edit.setFixedHeight(250)
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    # Agregar el QTextEdit al layout principal
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def mirar_():
        if FuncMainPY.r_gr_(2): p_principal_(VENTANA1)
        else: p_REGISTRAR_licencia_(VENTANA1) # Si no hay archivo con clave,-1

    # Botones
    button1 = QPushButton(f"{__TR__('ACEPTAR')}")
    button1.clicked.connect(mirar_)
    button1.setShortcut("Return")
    button1.setProperty("tipo", "button1")

    button2 = QPushButton(f"{__TR__('CANCELAR')}")
    button2.clicked.connect(lambda: sys.exit())
    button2.setShortcut("Escape")
    button2.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA1.setCentralWidget(widget_principal)

    VENTANA1.show()
    return VENTANA1

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla de errores

def p_error_(ventana_, err, excp=None):
    if excp != 1 and excp != 3 and excp != 5:
        ventana_.close()

    global VENTANA2
    VENTANA2 = QMainWindow()

    ############

    if excp == 5:
        VENTANA2.setFixedSize(450, 115)
    else:
        VENTANA2.setFixedSize(450, 100)
    
    FuncGuiPY.centrar_ventana_(VENTANA2)
    
    ############

    VENTANA2.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA2.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    label = QLabel(err)
    label.setTextFormat(Qt.TextFormat.RichText) # HTML
    label.setWordWrap(True)
    main_layout.addWidget(label)
    
    ############

    if "versión" in str(err):
        button3 = QPushButton(f"{__TR__('DESCARGAR')}")
        button3.setProperty("tipo", "button1")
        button3.clicked.connect(lambda: webbrowser.open("https://aili-ss.pages.dev/Descargar"))


    button4 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button4.setProperty("tipo", "button2")
    button4.setShortcut("Escape")

    if excp == 1:
        button4.clicked.connect(lambda: VENTANA2.close())
        button4.setText(f"{__TR__('CERRAR')}")
    elif excp == 2: # p_licencia_
        button4.clicked.connect(lambda: p_principal_(VENTANA2, "IrALicencia"))
    elif excp == 3: # p_sobre_aili_ ERROR ARCHIVO
        button4.clicked.connect(lambda: VENTANA2.close())
    elif excp == 4: # p_sobre_aili_ ERROR ARCHIVO
        button4.clicked.connect(lambda: p_REGISTRAR_licencia_(VENTANA2))
    elif excp == 5: # ERROR TERMINOS RECHAZADOS
        def cerrar_excp_5():
            ventana_.close()
            p_configuracion_(VENTANA2)
        button4.clicked.connect(cerrar_excp_5)
        button4.setText(f"{__TR__('IR_CONFIG')}")
    elif excp == 6: # ERROR ENVIAR DHCP DISCOVERY POR INTERFAZ
        button4.clicked.connect(lambda: p_configuracion_(VENTANA2))
        button4.setText(f"{__TR__('IR_CONFIG')}")
    elif excp == 7: # ERROR ENVIAR DHCP DISCOVERY POR DEPENDENCIAS
        button4.clicked.connect(lambda: p_principal_(VENTANA2, "IrADependencias"))
        button4.setText(f"{__TR__('IR_CONFIG')}")
    elif excp == 8:
        button4.clicked.connect(lambda: p_configuracion_(VENTANA2))
        button4.setText(f"{__TR__('IR_CONFIG')}")
    elif excp == 9:
        button4.clicked.connect(lambda: p_principal_(VENTANA2, "IrADependencias"))
        button4.setText(f"{__TR__('INSTALAR_NPCAP')}")
    elif excp == "EXPORTAR":
        button4.setText(f"{__TR__('ABRIR')}")
        button4.setProperty("tipo", "button1")
        button4.setShortcut("Return")

        def abrir():
            if str(err).endswith(".html"):
                webbrowser.open(err)
            else:
                try:
                    subprocess.run(["notepad.exe", err])
                except:
                    try:
                        subprocess.run(["gedit", err])
                    except Exception as e:
                        FuncMainPY.ERR_REG_(f"[p_error_] No se encuentra el archivo de exportación ({err}).\n\n")

        button4.clicked.connect(abrir)
        
    else:
        button4.clicked.connect(lambda: p_REGISTRAR_licencia_(VENTANA2))

    ############

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    if f"{__TR__('NUEVA_VERSION')}" in str(err):
        button_layout.addWidget(button3)
    button_layout.addWidget(button4)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA2.setCentralWidget(widget_principal)

    VENTANA2.show()
    return VENTANA2

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla de la licencia

def p_REGISTRAR_licencia_(ventana):
    # Cerrar ventana anterior
    if ventana != None:
        ventana.close()
    
    # Crear nueva ventana
    global VENTANA3
    VENTANA3 = QMainWindow()
    VENTANA3.setFixedSize(665, 300)
    FuncGuiPY.centrar_ventana_(VENTANA3)
    VENTANA3.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA3.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

     # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('REGISTRE_CLAVE_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    # Establecer el layout al widget principal
    VENTANA3.setLayout(main_layout)

    ############

    spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    label = QLabel(f"{__TR__('EXPLICACION_REGISTRAR_CLAVE')}")
    label.setWordWrap(True)
    main_layout.addWidget(label)

    ############
    
    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    entrada_clave = QLineEdit()
    entrada_clave.setPlaceholderText(f"0000000000")
    entrada_clave.setText(f"9991979139 {__TR__('LICENCIA_GRATUITA')}")
    main_layout.addWidget(entrada_clave)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    workers_activos = []

    class WorkerSignals(QObject):
        finished = Signal(dict)
        error = Signal(str)
        especial = Signal(str)

    # Trabajador que corre en segundo plano
    class RegistrarWorker(QRunnable):
        def __init__(self, clave):
            super().__init__()
            self.clave = clave
            self.signals = WorkerSignals()

        def run(self):
            try:
                res = FuncMainPY.registrar_clave_(self.clave)

                if res == "Vacio" or res == "NoInternet":
                    self.signals.especial.emit(res)
                else:
                    self.signals.finished.emit(res)

            except Exception as e:
                self.signals.error.emit(str(e))

    # Función que lanza el proceso en hilo
    def iniciar_registrar_():
        clave = entrada_clave.text()

        # Desactivar botones y UI
        for i in [button1, button3, button4]:
            i.setEnabled(False)
            i.setStyleSheet("background-color: transparent; color: transparent; border: 0px solid transparent;")
        
        button2.setEnabled(False)
        button2.setText(f"{__TR__('ESPERAR')}")
        button2.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        QApplication.processEvents()

        # Crear y lanzar el trabajador
        worker = RegistrarWorker(clave)
        workers_activos.append(worker)

        worker.signals.finished.connect(manejar_resultado)
        worker.signals.error.connect(mostrar_error)
        worker.signals.especial.connect(manejar_errores_especiales)

        QThreadPool.globalInstance().start(worker)

    # Manejo del resultado exitoso
    def manejar_resultado(res):
        try:
            if res["existe"]:
                FuncMainPY.r_gu_(entrada_clave.text())
                p_principal_(VENTANA3)
            else:
                p_error_(VENTANA3, f"{__TR__('CLAVE_NO_REGISTRADA')}")
        except:
            if res.get("error") == "AILI_ERR_ClaveLetra":
                p_error_(VENTANA3, f"{__TR__('CLAVE_SOLO_NUMEROS')}")

        restaurar_estilo_botones()

    # Manejo de errores tipo "Vacio", "NoInternet"
    def manejar_errores_especiales(res):
        if res == "Vacio":
            p_error_(VENTANA3, __TR__('P_LICENCLA_8'), 4)
        elif res == "NoInternet":
            p_error_(VENTANA3, __TR__('P_LICENCLA_7'), 4)
        restaurar_estilo_botones()

    # Manejo de errores generales
    def mostrar_error(msg):
        FuncMainPY.ERR_REG_(f"[Thread Error] {msg}")
        p_error_(VENTANA3, f"{__TR__('ERROR_INESPERADO')}")
        restaurar_estilo_botones()

    # Restaurar botones y estilo
    def restaurar_estilo_botones():
        with open(FuncMainPY.obtener_ruta_config(), "r") as f:
            data = json.load(f)

        for i in [button1, button3, button4]:
            i.setEnabled(True)
            i.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']}; border: 1px solid {data['BACKG_BASE']};")
        
        button2.setEnabled(True)
        button2.setText(f"{__TR__('REGISTRAR')}")
        button2.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
        
        QApplication.processEvents()

    ############

    # Botones
    button1 = QPushButton(f"{__TR__('COMPRA_LICENCIA')}")
    button1.clicked.connect(lambda: webbrowser.open("https://aili-ss.pages.dev/Productos#Precios"))
    button1.setProperty("tipo", "button1")

    button2 = QPushButton(f"{__TR__('REGISTRAR')}")
    button2.clicked.connect(iniciar_registrar_)
    QShortcut(QKeySequence("Return"), button2).activated.connect(iniciar_registrar_)
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('APOYA_PROYECTO')}")
    button3.clicked.connect(lambda: p_apoya_proyecto_(VENTANA3, 2))
    button3.setProperty("tipo", "button1")

    button4 = QPushButton(f"{__TR__('CERRAR')}")
    button4.clicked.connect(lambda: sys.exit())
    button4.setShortcut("Escape")
    button4.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button1)
    button_layout.addWidget(button3)
    button_layout.addWidget(button4)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA3.setCentralWidget(widget_principal)

    VENTANA3.show()
    return VENTANA3

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla principal

global TIEMPO_CARGA_V_PRINCIPAL
TIEMPO_CARGA_V_PRINCIPAL = ""
try:
    cuando_se_registro_licencia = FuncMainPY.r_gr_(3).split('.')[0]
except:
    cuando_se_registro_licencia = None

############

def p_principal_(ventana, es_movil=False):       
    # Cerrar ventana anterior
    if ventana != None:
        ventana.close()

    if es_movil == "VolverAConfig": return p_configuracion_()
    
    # Crear nueva ventana
    global VENTANA4
    VENTANA4 = QMainWindow()
    
    VENTANA4.setFixedSize(665, 315)
    FuncGuiPY.centrar_ventana_(VENTANA4)
    VENTANA4.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA4.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    ############

    menu_bar = QMenuBar()

    menu_principal = QMenu("☰", VENTANA4)
    menu_bar.addMenu(menu_principal)

    accion_principal = QAction(f"{__TR__('INICIO')}", VENTANA4)
    accion_principal.setShortcut("Ctrl+0")

    accion_config = QAction(f"{__TR__('CONFIG_APARIENCIA')}", VENTANA4)
    accion_config.setShortcut("Ctrl+1")
    accion_config.triggered.connect(lambda: p_configuracion_(VENTANA4))

    accion_dependencias = QAction(f"{__TR__('INSTALAR_DEPENDENCIAS')}", VENTANA4)
    accion_dependencias.setShortcut("Ctrl+2")

    accion_licencia = QAction(f"{__TR__('ADMINISTRAR_LICENCIA')}", VENTANA4)
    accion_licencia.setShortcut("Ctrl+3")

    accion_infotecn = QAction(f"{__TR__('INFO_TECNICA')}", VENTANA4)
    accion_infotecn.setShortcut("Ctrl+4")

    accion_salir = QAction(f"{__TR__('CERRAR')}", VENTANA4)
    accion_salir.setShortcut("Escape")
    accion_salir.triggered.connect(lambda: sys.exit())


    menu_principal.addAction(accion_principal)
    menu_principal.addAction(accion_config)
    menu_principal.addAction(accion_dependencias)
    menu_principal.addAction(accion_licencia)
    menu_principal.addAction(accion_infotecn)
    menu_principal.addSeparator()
    menu_principal.addAction(accion_salir)

    VENTANA4.setMenuBar(menu_bar)

    ############

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"AILI-<span style='color: {FuncMainPY.obt_json_(6)};'>SS</span>. {__TR__('P_PRINCIPAL_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    VENTANA4.setLayout(main_layout)

    ############

    spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    ACTUALIZACION = ""

    try:
        soup = BeautifulSoup(requests.get("https://aili-ss.pages.dev/App").text, 'html.parser')
        primer_h1 = soup.find("h1")
        if primer_h1:
            if FuncMainPY.obt_aili_json_(0) == primer_h1.text:
                pass
            else:
                ACTUALIZACION = f". {__TR__('NUEVA_ACTUALIZACION')}: <b>{primer_h1.text}</b>"
    except:
        pass

    label = QLabel(f"{__TR__('P_PRINCIPAL_EXPLICACION')}" + ACTUALIZACION)
    label.setWordWrap(True)
    main_layout.addWidget(label)
    
    ############

    spacer_x1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer_x1)

    ############
    ############

    apoya1 = QPushButton("")
    apoya1.setStyleSheet("padding: 10px;")
    apoya1.clicked.connect(lambda: webbrowser.open("https://www.patreon.com/c/byAd12"))
    apoya1.setIconSize(QSize(50, 50))
    apoya1.setCursor(Qt.CursorShape.PointingHandCursor)
    apoya1.setObjectName("buttonNOESTILOS")
    apoya1.setToolTip("Apóyanos en Patreon")

    apoya2 = QPushButton("")
    apoya2.setStyleSheet("padding: 10px;")
    apoya2.clicked.connect(lambda: webbrowser.open("https://paypal.me/byAd112"))
    apoya2.setCursor(Qt.CursorShape.PointingHandCursor)
    apoya2.setIconSize(QSize(50, 50))
    apoya2.setObjectName("buttonNOESTILOS")

    apoya3 = QPushButton("")
    apoya3.setStyleSheet("padding: 10px;")
    apoya3.clicked.connect(lambda: webbrowser.open("https://ko-fi.com/byad12"))
    apoya3.setCursor(Qt.CursorShape.PointingHandCursor)
    apoya3.setIconSize(QSize(50, 50))
    apoya3.setObjectName("buttonNOESTILOS")

    GRID = QGridLayout()

    GRID.setColumnStretch(0, 1)
    GRID.setColumnStretch(1, 1)
    GRID.setColumnStretch(2, 1)

    GRID.addWidget(apoya1, 0, 0)
    GRID.addWidget(apoya2, 0, 1)
    GRID.addWidget(apoya3, 0, 2)

    main_layout.addLayout(GRID)
    FuncGuiPY.ocultar_elemento_(apoya1)
    FuncGuiPY.ocultar_elemento_(apoya2)
    FuncGuiPY.ocultar_elemento_(apoya3)

    ############
    ############

    def mostrar_p_OTRAS_HERRAMIENTAS_(): # SERVIDORES LINUX
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # VENTANA
        VENTANA4.setFixedSize(665, 364)
        # TEXTO
        title_label.setText(f"{__TR__('P_HERRAMIENTAS_server_TITULO')}")
        # BOTONES
        button1.setText(f"?")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(lambda: p_ayuda_msg_(VENTANA4, 4))
        button3.clicked.connect(mostrar_p_herramientas_otras_)
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(button2)
        FuncGuiPY.ocultar_elemento_(label)
        FuncGuiPY.ocultar_elemento_(spacer_x1)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # MOSTRAR ELEMENTOS
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.mostrar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
    
    ############
    ############

    icon_logo = QIcon(os.path.join(RUTA_RECURSOS, "Logos", "Logo.png"))
    icon_nmap = QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoNMAP.png"))
    icon_npcap = QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoNPCAP.png"))

    ############

    botones_fila1 = [
        FuncGuiPY.crear_boton_(f"{__TR__('INTERFACES_ACTIVAS')}", icon_logo, lambda: pF_interfaces_red_(VENTANA4), False),
        FuncGuiPY.crear_boton_(f"{__TR__('CALCULAR_IP')}", icon_logo, lambda: pF_calcular_direcciones_(VENTANA4), False)
    ]

    botones_fila2 = [
        FuncGuiPY.crear_boton_(f"{__TR__('DETECCION_ARP_SPOOF')}", icon_logo, lambda: pF_deteccion_arp_spoofing_(VENTANA4), False),
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_BLE')}", icon_logo, lambda: pF_dispositivos_bluetooth_(VENTANA4), False)
    ]

    botones_fila3 = [
        FuncGuiPY.crear_boton_(f"{__TR__('PING_GRAFICO')}", icon_logo, lambda: pF_ping_grafica_(VENTANA4), False),
        FuncGuiPY.crear_boton_(f"{__TR__('CALCULAR_TIEMPOS')}", icon_logo, lambda: pF_tiempos_respuesta(VENTANA4), False)
    ]

    botones_fila4 = [
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_REDES_WIFI')}", icon_logo, lambda: pF_escaneo_redes_WiFi_(VENTANA4), True),
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_DOMINIO_WORDLIST')}", icon_logo, lambda: pF_escaneo_TLD_wordlist_(VENTANA4), True),
    ]

    botones_fila5 = [
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_HOSTS')}", icon_nmap, lambda: pF_escaneo_dispositivos_(VENTANA4), True),
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_PUERTOS')}", icon_nmap, lambda: pF_escaneo_puertos_(VENTANA4), True)
    ]

    botones_fila6 = [
        FuncGuiPY.crear_boton_(f"{__TR__('ESCANEO_VULNERABILIDADES')}", os.path.join(RUTA_RECURSOS, "Logos", "LogoNMAP.png"), lambda: pF_escaneo_vulnerabilidades_(VENTANA4), True),
        FuncGuiPY.crear_boton_(f"{__TR__('MONITORIZAR_RED')}", icon_npcap, lambda: pF_monitorizacion_trafico_red_(VENTANA4), True),
    ]

    botones_fila7 = [
        FuncGuiPY.crear_boton_(f"{__TR__('CRIPTOGRAFIA_HASH')}", icon_logo, lambda: pF_hashing_(VENTANA4), False),
        FuncGuiPY.crear_boton_(f"{__TR__('CRIPTOGRAFIA_AES')}", icon_logo, lambda: pF_cifrado_AES_random_(VENTANA4), False),
    ]

    botones_fila8 = [
        FuncGuiPY.crear_boton_(f"{__TR__('DIAGNOSTICO_REPORTE_DE')}", icon_logo, lambda: pF_reporte_equipo_(VENTANA4), False),
    ]

    botones_fila9 = [
        FuncGuiPY.crear_boton_(f"{__TR__('SERVIDORES_LINUX')}", icon_logo, mostrar_p_OTRAS_HERRAMIENTAS_, False),
    ]

    botones_fila10 = [
        FuncGuiPY.crear_boton_(f"DHCP - isc-dhcp-server", icon_logo, lambda: pF_control_servidores_(VENTANA4, "isc-dhcp-server"), False),
        FuncGuiPY.crear_boton_(f"DNS - bind9", icon_logo, lambda: pF_control_servidores_(VENTANA4, "bind9"), False),
    ]

    botones_fila11 = [
        FuncGuiPY.crear_boton_(f"HTTP - apache2", icon_logo, lambda: pF_control_servidores_(VENTANA4, "apache2"), False),
        FuncGuiPY.crear_boton_(f"FTP - vsftpd", icon_logo, lambda: pF_control_servidores_(VENTANA4, "vsftpd"), False),
    ]

    botones_fila12 = [
        FuncGuiPY.crear_boton_(f"SMTP - postfix", icon_logo, lambda: pF_control_servidores_(VENTANA4, "postfix"), False),
    ]

    # Agregar a layout principal
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila1)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila2)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila3)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila4)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila5)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila6)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila7)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila8)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila9)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila10)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila11)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila12)

    for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
        for z in i:
            FuncGuiPY.ocultar_elemento_(z)

    ############
    ############

    global PAG_ACTUAL
    PAG_ACTUAL = 0

    text_edit_blog = QTextEdit()
    text_edit_blog.setText(FuncMainPY.blog_())
    text_edit_blog.setReadOnly(True)
    text_edit_blog.setObjectName("BlogText")
    text_edit_blog.setFixedHeight(450)
    text_edit_blog.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA4.resizeEvent = lambda event: adjust_text_edit_height(VENTANA4, text_edit_blog)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))

    # Agregar el QTextEdit al layout principal
    main_layout.addWidget(text_edit_blog)
    FuncGuiPY.ocultar_elemento_(text_edit_blog)

    ###########

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ###########

    blog_funcs = [
        FuncMainPY.blog_,
        FuncMainPY.blog_2_,
        FuncMainPY.blog_3_,
        FuncMainPY.blog_4_,
        FuncMainPY.blog_5_,
        FuncMainPY.blog_6_
    ]

    def actualizar_pagina():
        text_edit_blog.setText(blog_funcs[PAG_ACTUAL]())

    def antes_():
        global PAG_ACTUAL
        if PAG_ACTUAL > 0:
            PAG_ACTUAL -= 1
            actualizar_pagina()
        
        # EASTER EGGG 🥚🥚
        if PAG_ACTUAL == 5: FuncGuiPY.mostrar_elemento_(button4) # 5 es 6
        else:               FuncGuiPY.ocultar_elemento_(button4)

    def siguiente_():
        global PAG_ACTUAL
        if PAG_ACTUAL < len(blog_funcs) - 1:
            PAG_ACTUAL += 1
            actualizar_pagina()
        
        # EASTER EGGG 🥚🥚
        if PAG_ACTUAL == 5: FuncGuiPY.mostrar_elemento_(button4) # 5 es 6
        else:               FuncGuiPY.ocultar_elemento_(button4)

    ############
    ############

    def eliminar_linea_():
        # DETECTAR ARCHIVO
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
        PASE = False

        with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "r", encoding="utf-8") as f:
            data = f.read()

        # COMPROBAR SI ESTÁ
        PASE = False
        try:
            if data.split("\n")[1].startswith("AILI_Data"):
                DATA_DEF = data.split("\n")[1].split(",-")
                PASE = True
        except:
            pass

        # ELIMINARLA
        if PASE == True:
            with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "w", encoding="utf-8") as f:
                f.write(data.split("\n")[0])
            
            button7.setText(f"{__TR__('ELIMINADA')}")
            button7.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
            print("")
            QApplication.processEvents()

        else:
            button7.setText(f"{__TR__('NO_ELIMINADA')}")

            QApplication.processEvents()

            # ESPERAR
            time.sleep(0.2)
            
            # BOTÓN A NORMAL
            button7.setText(f"{__TR__('ELIMINAR_LINEA')}")
            QApplication.processEvents()
        

    def cargar_licencia_():
        # HABILITAR BOTONES
        for i in [button1, button2, button4, button5, button6, button7]:
            i.setDisabled(True)

        try: button7.clicked.disconnect()
        except: pass

        title_label.setText(f"{__TR__('P_LICENCLA_6')} <span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('ESPERAR')}</span>")
        label.setText(f"""{__TR__('P_LICENCLA_1')}<br>
    <ul>
    <li>{__TR__('P_LICENCLA_2X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('ESPERAR')}</span></li>
    <li>{__TR__('P_LICENCLA_3X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('ESPERAR')}</span></li>
    <li>{__TR__('P_LICENCLA_4')} <span style='color: {FuncMainPY.obt_json_(7)};'>{FuncMainPY.r_gr_(3).split('.')[0]}</span>.</li>
    </ul>""")
        
        # DESHABILITAR EL BOTÓN
        try:
            button7.setText(f"{__TR__('CONTACTANDO_CON_AILI')}")
            button7.setEnabled(False)
            button7.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        except:
            pass
            
        print("")
        # OBTENER LOS RESULTADOS
        try:
            RESULTADOS = FuncMainPY.Conseguir_Datos_LLave()
        except:
            FuncMainPY.ERR_REG_(f"[cargar_] No hay conexión a internet.\n\n")

            p_error_(VENTANA4, f"{__TR__('P_LICENCLA_7')}", 2)
            return
        
        print("")
        # COGER LOS DATOS
        if RESULTADOS:
            for item in RESULTADOS:
                ### DEFINIR VARIABLES
                caducidad = item.get('CADUCIDAD')
                tipo = item.get('TIPO')
                cliente = item.get('CLIENTE')
            
        print("")

        # GUARDAR EN TEMP
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
        if PASE == False:
            with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "a", encoding="utf-8") as f:
                f.write(f"\nAILI_Data,-{caducidad},-{tipo},-{cliente}")
                f.close()

        print("")
        ### PREPARAR Y ENSEÑAR EN TEXTO FINAL

        label.setText(f"""{__TR__('P_LICENCLA_1')}<br>
<ul>
<li>{__TR__('P_LICENCLA_2X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{caducidad}</span>.</li>
<li>{__TR__('P_LICENCLA_3X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{tipo}</span>.</li>
<li>{__TR__('P_LICENCLA_4')} <span style='color: {FuncMainPY.obt_json_(7)};'>{FuncMainPY.r_gr_(3).split('.')[0]}</span>.</li>
</ul>""")
        
        print("")
        title_label.setText(f"{__TR__('P_LICENCLA_6')} <span style='color: {FuncMainPY.obt_json_(6)};'>{cliente}</span>")

        print("")
        # HABILITAR EL BOTÓN
        button7.setEnabled(True)
        with open(FuncMainPY.obtener_ruta_config(), "r") as f: data = json.load(f)
        button7.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
        button7.setText(f"{__TR__('ELIMINAR_LINEA')}")
        button7.clicked.disconnect()
        button7.clicked.connect(eliminar_linea_)
        FuncGuiPY.mostrar_elemento_(button7)
        QApplication.processEvents()
        # HABILITAR BOTONES
        for i in [button1, button2, button3, button4, button5, button6, button7]:
            i.setDisabled(False)

    
    def start_thread_licencia_():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=cargar_licencia_)
        thread.start()
    
    def cerrar_sesion_():
        FuncMainPY.r_bu_()
        p_REGISTRAR_licencia_(VENTANA4)

    ############
    ############

    def limpiar():
        FuncMainPY.ERR_REG_("--Limpiar--")
        RES = obt_()
        return text_edit_blog.setText(f"{__TR__('SIN_ERRORES')}" if RES == None or RES == '' else RES)
  
    def obt_():
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

        if os.path.exists(os.path.join(RUTA_DIR_USUARIO, "Errores.log")):
            with open(os.path.join(RUTA_DIR_USUARIO, "Errores.log"), "r", encoding="utf-8") as f:
                return f.read()

    ############
    ############

    # Botones
    button1 = QPushButton(f"{__TR__('HERRAMIENTAS_RED')}")
    #button1.clicked.connect(lambda: p_herramientas_red_(VENTANA4))
    button1.setProperty("tipo", "button1")

    button2 = QPushButton(f"{__TR__('OTRAS_HERRAMIENTAS')}")
    #button2.clicked.connect(lambda: p_herramientas_otras_(VENTANA4))
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('BLOG_SEGURIDAD')}")
    #button3.clicked.connect(lambda: p_blog_(VENTANA4))
    button3.setProperty("tipo", "button1")

    button4 = QPushButton(f"{__TR__('TIEMPO_CARGA')}")
    #button4.clicked.connect(lambda: p_tiempos_carga_(VENTANA4))
    button4.setProperty("tipo", "button1")

    button5 = QPushButton(f"{__TR__('ERRORES')}")
    #button5.clicked.connect(lambda: pF_errores_app_(VENTANA4))
    button5.setProperty("tipo", "button1")

    button6 = QPushButton(f"{__TR__('APOYA')}")
    #button6.clicked.connect(lambda: p_apoya_proyecto_(VENTANA4, 1))
    button6.setProperty("tipo", "button1")

    button7 = QPushButton(f"{__TR__('CARGAR')}")
    button7.setProperty("tipo", "button1")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)
    button_layout.addWidget(button4)
    button_layout.addWidget(button5)
    button_layout.addWidget(button6)
    button_layout.addWidget(button3)

    FuncGuiPY.ocultar_elemento_(button4)
    FuncGuiPY.ocultar_elemento_(button5)
    FuncGuiPY.ocultar_elemento_(button6)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    button_layout.addWidget(button7)
    FuncGuiPY.ocultar_elemento_(button7)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA4.setCentralWidget(widget_principal)

    ############
    ############

    def mostrar_todos_elementos_():
        FuncGuiPY.mostrar_elemento_(button1)
        FuncGuiPY.mostrar_elemento_(button2)
        FuncGuiPY.mostrar_elemento_(button3)
        FuncGuiPY.mostrar_elemento_(label)
        FuncGuiPY.mostrar_elemento_(spacer_x1)
        button1.setShortcut("")
        button2.setShortcut("")

    ############
    ############

    with open(os.path.join(RUTA_RECURSOS, "AILI_info.json"), "r", encoding="utf-8") as f: datos = f.read(); datos_json = json.loads(datos)
    
    def comprobar_actualizaciones_():
        soup = BeautifulSoup(requests.get("https://aili-ss.pages.dev/App").text, 'html.parser')
        primer_h1 = soup.find("h1")
        if primer_h1:
            if datos_json['App']['Version'] == primer_h1.text:
                return [f"{__TR__('ULTIMA_VERSION')}", primer_h1.text, datos_json['App']['Version']]
            else:
                return [f"{__TR__('NUEVA_VERSION')}: <b><span style='color: {FuncMainPY.obt_json_(7)};'>{primer_h1.text}</span></b>", primer_h1.text, datos_json['App']['Version']]
        else:
            return [f"{__TR__('NO_PODER_COMPROBAR_ACTUALIZACION')}", "None", datos_json['App']['Version']]

    ############
    ############

    global ESTA_EN_TERMINOS
    ESTA_EN_TERMINOS = False

    ############
    ############

    def mostrar_p_principal_(mover=False):
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # VENTANA
        VENTANA4.setFixedSize(665, 315)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if mover: FuncGuiPY.centrar_ventana_(VENTANA4)
        if mover: FuncGuiPY.centrar_ventana_(VENTANA4)
        # TEXTO
        title_label.setText(f"AILI-<span style='color: {FuncMainPY.obt_json_(6)};'>SS</span>. {__TR__('P_PRINCIPAL_TITULO')}")
        label.setText(f"{__TR__('P_PRINCIPAL_EXPLICACION')}" + ACTUALIZACION)
        # BOTONES
        button1.setText(f"{__TR__('HERRAMIENTAS_RED')}")
        button2.setText(f"{__TR__('OTRAS_HERRAMIENTAS')}")
        button3.setText(f"{__TR__('BLOG_SEGURIDAD')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("Alt+1")
        button2.setShortcut("Alt+2")
        button3.setShortcut("Alt+4")
        button1.clicked.connect(mostrar_p_herramientas_red_)
        button2.clicked.connect(mostrar_p_herramientas_otras_)
        button3.clicked.connect(mostrar_p_blog_)
        accion_salir.triggered.connect(lambda: sys.exit())
        # SHORTCUT
        accion_salir.setShortcut("Escape")
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)

    accion_principal.triggered.connect(mostrar_p_principal_)

    ############
    ############

    def mostrar_p_dependencias_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # VENTANA
        VENTANA4.setFixedSize(665, 315)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        # TEXTO
        title_label.setText(f"{__TR__('P_DEPENDENCIAS_TITULO')}")
        label.setText(f"{__TR__('P_DEPENDENCIAS_EXPLICACION')}")
        # FUNCIONES
        def mirar_dep_():
            texto_label_final = f"{__TR__('P_DEPENDENCIAS_EXPLICACION')}"
            if os.name != "nt":
                texto_label_final = texto_label_final.replace("Npcap", "Libpcap")

            # Nmap
            res1 = FuncMainPY.mirar_dependencias_instaladas_(1)

            if res1[0] == True: FuncGuiPY.ocultar_elemento_(button1)
            ver = ""
            if res1[0] != False:
                ver = f"(<span style='color: {FuncMainPY.obt_json_(6)};'>{res1[2]}</span>)"
            texto_label_final = texto_label_final.replace(f"{__TR__('ESPERE__')}", f"{res1[1]} {ver}")

            label.setText(texto_label_final)
            QApplication.processEvents()

            # Npcap O libpcap
            res2 = FuncMainPY.mirar_dependencias_instaladas_(2)
            
            if res2[0] == True and os.name == "nt": FuncGuiPY.ocultar_elemento_(button2)
            texto_label_final = texto_label_final.replace(f"{__TR__('AGUARDA__')}", f"{res2[1]}")
            
            label.setText(texto_label_final)
            QApplication.processEvents()

        def start_thread():
            global stop_thread, thread
            stop_thread = False
            thread = threading.Thread(target=mirar_dep_)
            thread.start()

        start_thread()
        # BOTONES
        button1.setText(f"{__TR__('INSTALAR_NMAP')}")
        button2.setText(f"{__TR__('INSTALAR_NPCAP')}")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(lambda: webbrowser.open("https://nmap.org/download"))
        button2.clicked.connect(lambda: webbrowser.open("https://npcap.com/"))
        button3.clicked.connect(mostrar_p_principal_)
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)

    accion_dependencias.triggered.connect(mostrar_p_dependencias_)

    ############
    ############

    def mostrar_p_apoyanos_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # VENTANA
        VENTANA4.setFixedSize(665, 315)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        # TEXTO
        title_label.setText(f"{__TR__('P_APOYA_TITULO')}")
        label.setText(f"{__TR__('P_APOYA_DESC')}")
        # BOTONES
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button3.clicked.disconnect()
        button3.setShortcut("")
        button3.clicked.connect(mostrar_p_info_tecnica_)

        apoya1.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoPATREON.png")))
        apoya2.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoPAYPAL.png")))
        apoya3.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoKOFI.png")))

        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button1, button2, button4, button5, button6, button7]:
            FuncGuiPY.ocultar_elemento_(i)
        for i in [apoya1, apoya2, apoya3, label]:
            FuncGuiPY.mostrar_elemento_(i)

    button6.clicked.connect(mostrar_p_apoyanos_)

    ############
    ############

    def mostrar_p_blog_():
        # MOSTRAR ELEMENTOS
        global ESTA_EN_TERMINOS
        mostrar_todos_elementos_()
        # TEXTO
        title_label.setText(f"{__TR__('BLOG_SEGURIDAD_TITULO')}")
        actualizar_pagina()
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # BOTONES
        button1.setText(f"«")
        button2.setText(f"»")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button4.setText(f"")
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.setShortcut("Left")
        button2.setShortcut("Right")
        button3.setShortcut("Escape")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button4.clicked.disconnect()
        button1.clicked.connect(antes_)
        button2.clicked.connect(siguiente_)
        button3.clicked.connect(mostrar_p_principal_)
        button4.clicked.connect(p_easter_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = True
        # OCULTAR ELEMENTOS
        FuncGuiPY.mostrar_elemento_(text_edit_blog)
        FuncGuiPY.ocultar_elemento_(label)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        # VENTANA
        VENTANA4.setMinimumSize(0, 0)
        VENTANA4.setFixedSize(0, 0)
        VENTANA4.setMinimumSize(1000, 700)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FuncGuiPY.centrar_ventana_(VENTANA4)
        FuncGuiPY.centrar_ventana_(VENTANA4)

    button3.clicked.connect(mostrar_p_blog_)

    ############
    ############

    def mostrar_p_errores_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # TEXTO
        title_label.setText(f"{__TR__('P_REGISTRO_ERRORES_TITULO')}")
        RES = obt_()
        text_edit_blog.setText(f"{__TR__('SIN_ERRORES')}" if RES == None or RES == '' else RES)
        # QTEXTEDIT
        text_edit_blog.setFixedHeight(290)
        # BOTONES
        button1.setText(f"{__TR__('_LIMPIAR_')}")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(limpiar)
        button3.clicked.connect(mostrar_p_info_tecnica_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = True
        # OCULTAR ELEMENTOS
        FuncGuiPY.mostrar_elemento_(text_edit_blog)
        FuncGuiPY.ocultar_elemento_(label)
        FuncGuiPY.ocultar_elemento_(button2)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # VENTANA
        VENTANA4.setMinimumSize(665, 500)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)

    button5.clicked.connect(mostrar_p_errores_)

    ############
    ############

    def mostrar_p_actualizaciones_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # DATOS
        with open(os.path.join(RUTA_RECURSOS, "AILI_info.json"), "r", encoding="utf-8") as f: datos = f.read(); datos_json = json.loads(datos)
        # TEXTO
        title_label.setText(f"<span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('COMROBAR_ACTUALIZACION')}</span>")
        label.setText(f"{__TR__('ESPERE')}<br><br><br><br><br><br><br><br><br><br><br><br><br><br><span style='color: rgba(0,0,0,0);'>.</span>")
        # FUNCION PRINCIPAL
        def label_():
            try:
                res = comprobar_actualizaciones_()
            except:
                res = [f"{__TR__('NO_PODER_COMPROBAR_ACTUALIZACION')}", "None", FuncMainPY.obt_aili_json_(0)]
            label.setText(f"""
                            {__TR__('COMROBAR_ACTUALIZACION_DESC_0')}<br><br>
                        <span style='color:{FuncMainPY.obt_json_(7)};'>{res[0]}</span> (Actual: <span style='color:{FuncMainPY.obt_json_(7)};'>{res[2]}</span>)<br>

                        <hr><br>

                            {__TR__('COMROBAR_ACTUALIZACION_DESC_1')}<br><br>
                        <span style='color:{FuncMainPY.obt_json_(6)};'>https://aili-ss.pages.dev/App</span><br><br>
                        
                        {__TR__('COMROBAR_ACTUALIZACION_DESC_2')}<br><br>
                        <span style='color:{FuncMainPY.obt_json_(6)};'>https://aili-ss.pages.dev/Descargar</span>""")
        
            if f"{__TR__('ULTIMA_VERSION')}" != res[0]:
                button1.setText(f"{__TR__('DESCARGAR')}")
                button1.clicked.disconnect()
                button1.clicked.connect(lambda: webbrowser.open("https://aili-ss.pages.dev/Descargar"))
                FuncGuiPY.mostrar_elemento_(button1)
            else:
                FuncGuiPY.ocultar_elemento_(button1)

        def start_thread():
            global stop_thread, thread
            stop_thread = False
            thread = threading.Thread(target=label_)
            thread.start()

        start_thread()
        # BOTONES
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button3.clicked.connect(mostrar_p_info_tecnica_)

        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = True
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        FuncGuiPY.ocultar_elemento_(button4)
        FuncGuiPY.mostrar_elemento_(label)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button5, button6]:
            FuncGuiPY.mostrar_elemento_(i)
        for i in [button2, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        # VENTANA
        VENTANA4.setMinimumSize(665, 500)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)


    ############
    ############

    def mostrar_p_licencia_():
        # VENTANA
        global ESTA_EN_TERMINOS
        VENTANA4.setMinimumSize(665, 315)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4) # 2 sino no va
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        button7.setText(f"{__TR__('CARGAR')}")
        button7.setEnabled(True)
        button7.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        with open(FuncMainPY.obtener_ruta_config(), "r") as f: data = json.load(f)
        # DEESHABILITAR BOTONES
        for i in [button1, button2, button3, button4, button5, button6, button7]:
            i.setDisabled(True)
        # TEXTO
        res = FuncMainPY.r_gr_(3).split('.')[0]
        title_label.setText(f"{__TR__('HOLA_USUARIO')}")
        label.setText(f"""{__TR__('P_LICENCLA_1')}<br> 
<ul>
    <li>{__TR__('P_LICENCLA_2')}</li>
    <li>{__TR__('P_LICENCLA_3')}</li>
    <li>{__TR__('P_LICENCLA_4')} <span style='color: {FuncMainPY.obt_json_(7)};'>{res if res != None else FuncMainPY.r_gr_(3).split('.')[0]}</span>.</li>
</ul>""")
        ############
        # MIRAR SI YA CARGO LOS DATOS
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
        global PASE
        PASE = False

        with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "r", encoding="utf-8") as f:
            data = f.read()
        
        try:
            if data.split("\n")[1].startswith("AILI_Data"):
                DATA_DEF = data.split("\n")[1].split(",-")
                PASE = True
        except:
            pass
    
        if PASE == True:
            RESULTADOS = [{'CADUCIDAD': DATA_DEF[1], 'CLIENTE': DATA_DEF[3], 'LLAVE': "-", 'TIPO': DATA_DEF[2]}]
        
            # COGER LOS DATOS
            if RESULTADOS:
                for item in RESULTADOS:
                    ### DEFINIR VARIABLES
                    caducidad = item.get('CADUCIDAD')
                    tipo = item.get('TIPO')
                    cliente = item.get('CLIENTE')

            ### PREPARAR Y ENSEÑAR EN TEXTO FINAL
            title_label.setText(f"{__TR__('P_LICENCLA_6')} <span style='color: {FuncMainPY.obt_json_(6)};'>{cliente}</span>")
            label.setText(f"""{__TR__('P_LICENCLA_1')}<br>
        <ul>
        <li>{__TR__('P_LICENCLA_2X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{caducidad}</span>.</li>
        <li>{__TR__('P_LICENCLA_3X')} <span style='color: {FuncMainPY.obt_json_(7)};'>{tipo}</span>.</li>
        <li>{__TR__('P_LICENCLA_4')} <span style='color: {FuncMainPY.obt_json_(7)};'>{FuncMainPY.r_gr_(3).split('.')[0]}</span>.</li>
        </ul><br>
        {__TR__('P_LICENCLA_5')}<br>
        - Adrián L. G. P.""")


            button7.setText(f"{__TR__('ELIMINAR_LINEA')}")
            button7.clicked.connect(eliminar_linea_)
            FuncGuiPY.mostrar_elemento_(button7)
        else:
            button7.clicked.connect(start_thread_licencia_)
            FuncGuiPY.mostrar_elemento_(button7)
        
        with open(FuncMainPY.obtener_ruta_config(), "r") as f: data = json.load(f)
        button7.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")


        ############
        # BOTONES
        button1.setText(f"?")
        button2.setText(f"{__TR__('CERRAR_SESION')}")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(lambda: p_ayuda_licencia_(VENTANA4))
        button2.clicked.connect(cerrar_sesion_)
        button3.clicked.connect(mostrar_p_principal_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        FuncGuiPY.mostrar_elemento_(label)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button1, button2, button5, button6]:
            FuncGuiPY.mostrar_elemento_(i)
        for i in [button4, button5, button6, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        # HABILITAR BOTONES
        for i in [button1, button2, button3, button4, button5, button6, button7]:
            i.setDisabled(False)

    accion_licencia.triggered.connect(mostrar_p_licencia_)

    ############
    ############

    def mostrar_p_app_licencias_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # DATOS
        with open(os.path.join(RUTA_RECURSOS, "LICENSE.txt"), "r", encoding="utf-8") as f:
            datos = f.read()

            datos2 = datos.replace("AILI-SS · Licencias de Uso y Créditos", f"<span style='color:{FuncMainPY.obt_json_(6)};'>AILI-SS</span> · <span style='color:{FuncMainPY.obt_json_(7)};'>Licencias de Uso y Créditos</span>")
            datos2 = datos2.replace("MIT License", f"<span style='color:{FuncMainPY.obt_json_(6)};'>MIT License</span>")
            datos2 = datos2.replace("ISC License", f"<span style='color:{FuncMainPY.obt_json_(6)};'>ISC License</span>")
            datos2 = datos2.replace("Apache License 2.0", f"<span style='color:{FuncMainPY.obt_json_(6)};'>Apache License 2.0</span>")
            datos2 = datos2.replace("PSF-based", f"<span style='color:{FuncMainPY.obt_json_(6)};'>PSF-based</span>")
            datos2 = datos2.replace("LGPLv3", f"<span style='color:{FuncMainPY.obt_json_(6)};'>LGPLv3</span>")
            datos2 = datos2.replace("GPLv3", f"<span style='color:{FuncMainPY.obt_json_(6)};'>GPLv3</span>")
            datos2 = datos2.replace("BSD 3-Clause License", f"<span style='color:{FuncMainPY.obt_json_(6)};'>BSD 3-Clause License</span>")
            datos2 = datos2.replace("GPLv2", f"<span style='color:{FuncMainPY.obt_json_(6)};'>GPLv2</span>")
            datos2 = datos2.replace("Python Software Foundation License (PSF)", f"<span style='color:{FuncMainPY.obt_json_(6)};'>Python Software Foundation License (PSF)</span>")
            datos2 = datos2.replace("LICENCIAS DE BIBLIOTECAS (Python3):", f"<span style='color:{FuncMainPY.obt_json_(6)};'>LICENCIAS DE BIBLIOTECAS (Python3)</span>:")
            datos2 = datos2.replace("CRÉDITOS:", f"<span style='color:{FuncMainPY.obt_json_(6)};'>CRÉDITOS</span>:")
            datos2 = datos2.replace("Idioma: Español", f"Idioma: <span style='color:{FuncMainPY.obt_json_(7)};'>Español</span>")
            datos2 = datos2.replace("Adrián Leonardo Giménez Payo", f"<span style='color:{FuncMainPY.obt_json_(7)};'>Adrián Leonardo Giménez Payo</span>")
            datos2 = datos2.replace("Cheque", f"<span style='color:{FuncMainPY.obt_json_(7)};'>Cheque</span>")
            datos2 = datos2.replace("Cerca", f"<span style='color:{FuncMainPY.obt_json_(7)};'>Cerca</span>")
            datos2 = datos2.replace("Esperar", f"<span style='color:{FuncMainPY.obt_json_(7)};'>Esperar</span>")
            datos2 = datos2.replace("\n", f"<br>")

            for i in ["https://aili-ss.pages.dev", "https://byad12.pages.dev", "https://docs.python.org/3/license.html", "https://github.com/giampaolo/psutil/blob/master/LICENSE", "https://bitbucket.org/xael/python-nmap/src/master/gpl-3.0.txt", "https://github.com/al45tair/netifaces/blob/master/LICENSE", "https://github.com/kyan001/ping3/blob/master/LICENSE", "https://github.com/secdev/scapy/blob/master/LICENSE", "https://github.com/mongodb/mongo-python-driver/blob/master/LICENSE", "https://github.com/pyside/PySide", "https://github.com/matplotlib/matplotlib/blob/main/LICENSE/LICENSE", "https://github.com/hbldh/bleak/blob/develop/LICENSE", "https://github.com/psf/requests/blob/main/LICENSE", "https://docs.python.org/3/library/webbrowser.html", "https://docs.python.org/3/library/ipaddress.html", "https://www.crummy.com/software/BeautifulSoup/#Download", "https://github.com/rthalley/dnspython/blob/master/LICENSE", "https://github.com/awkman/pywifi/blob/master/LICENSE", "https://github.com/enthought/comtypes/blob/master/LICENSE.txt", "https://github.com/chardet/chardet/blob/main/LICENSE", "https://www.flaticon.es/icono-gratis/cheque_3285799", "https://www.flaticon.es/autores/freepik", "https://www.flaticon.es/icono-gratis/cerca_2919559", "https://www.flaticon.es/icono-gratis/esperar_1686925", "https://github.com/richardpenman/whois/blob/master/LICENSE.txt"]:
                datos2 = datos2.replace(i, f"<span style='color:{FuncMainPY.obt_json_(6)};'>{i}</span>")

            for i in range(19, -1, -1):
                datos2 = datos2.replace(f"{i}. ", f"<span style='color:{FuncMainPY.obt_json_(7)};'>{i}</span>. ")

        # TEXTO
        title_label.setText(f"{__TR__('P_LICENCIA_CREDITOS_TITULO')}")
        text_edit_blog.setHtml(str(datos2) + "<br><br>" + str(os.path.abspath(os.path.join(RUTA_RECURSOS, "LICENSE.txt"))))
        # BOTONES
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button3.clicked.disconnect()
        button3.clicked.connect(mostrar_p_info_tecnica_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = True
        # OCULTAR ELEMENTOS
        FuncGuiPY.mostrar_elemento_(text_edit_blog)
        FuncGuiPY.ocultar_elemento_(label)
        FuncGuiPY.ocultar_elemento_(button2)
        FuncGuiPY.ocultar_elemento_(button1)
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button4, button5, button6, button7]:
            FuncGuiPY.ocultar_elemento_(i)
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # VENTANA
        VENTANA4.setMinimumSize(1000, 700)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FuncGuiPY.centrar_ventana_(VENTANA4)
        FuncGuiPY.centrar_ventana_(VENTANA4)


    ############
    ############

    def mostrar_p_tiempos_carga_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # DATOS
        with open(os.path.join(RUTA_RECURSOS, "AILI_info.json"), "r", encoding="utf-8") as f: datos = f.read(); datos_json = json.loads(datos)
        # TEXTO
        title_label.setText(f"{__TR__('P_TIEMPOS_CARGA_TITULO')}")
        label.setText(f"""<p>{__TR__('P_INFO_TECNICA_DESC')}</p>
                        <p><b>{__TR__('ARRANQUE_APP')}</b>:</p>

                            <ul>
                                <li>{TIEMPO_INICIO}</li>
                            </ul>

                            <p><b>{__TR__('CARGA_DEPENDENCIAS')}</b>:</p>

                            <ul>
                                <li><span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('FECHA')}</span>: {TIEMPO_CARGA_LOGO}</li>
                                <li><span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('DESDE_INICIO')}</span>: {TIEMPO_CARGA_LOGO - TIEMPO_INICIO}</li>
                            </ul>

                            <p><b>{__TR__('TIEMPO_VENTANA_PRINCIPAL')}</b>:</p>

                            <ul>
                                <li><span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('FECHA')}</span>: {TIEMPO_CARGA_V_PRINCIPAL}</li>
                                <li><span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('DESDE_INICIO')}</span>: {TIEMPO_CARGA_V_PRINCIPAL - TIEMPO_INICIO}</li>
                            </ul>""")

        # BOTONES
        button1.setText(f"{__TR__('COMROBAR_ACTUALIZACION')}")
        button2.setText(f"{__TR__('LICENCIA_CREDITOS')}")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(comprobar_actualizaciones_)
        button2.clicked.connect(mostrar_p_app_licencias_)
        button3.clicked.connect(mostrar_p_info_tecnica_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        FuncGuiPY.ocultar_elemento_(button4)
        FuncGuiPY.mostrar_elemento_(label)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [button5, button6]:
            FuncGuiPY.mostrar_elemento_(i)
        for i in [button1, button2, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        # VENTANA
        VENTANA4.setMinimumSize(665, 500)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)


    button4.clicked.connect(mostrar_p_tiempos_carga_)

    ############
    ############

    def mostrar_p_info_tecnica_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        FuncGuiPY.ocultar_elemento_(button7)
        global ESTA_EN_TERMINOS
        # DATOS
        with open(os.path.join(RUTA_RECURSOS, "AILI_info.json"), "r", encoding="utf-8") as f: datos = f.read(); datos_json = json.loads(datos)
        # TEXTO
        title_label.setText(f"{__TR__('INFO_TECNICA_TITULO')}")
        label.setText(f"""<p><b>{__TR__('APP')}</b>:</p>

                            <ul>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('VERSION')}</span>: {datos_json['App']['Version']}</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('TECNOLOGIA')}</span>: {datos_json['App']['Tecnologia']}.</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('GUI')}</span>: {datos_json['App']['GUI']}.</li>
                            </ul>

                            <p><b>{__TR__('SOPORTE')}</b>:</p>

                            <ul>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('WEB')}</span>: {datos_json['Pro']['Web']}</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('TWITTER')}</span>: {datos_json['Pro']['Twitter']}</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('INSTAGRAM')}</span>: {datos_json['Pro']['Instagram']}</li>
                            </ul>

                            <p><b>{__TR__('CREDITOS')}</b>:</p>

                            <ul>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('CEO')}</span>: {datos_json['Emp']['Programadores']}</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('BETA')}</span>: {datos_json['Emp']['BetaTester']}</li>
                                <li><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('INSPIRACION')}</span>: <span style='color: {FuncMainPY.obt_json_(7)};'>{datos_json['Emp']['Inspiracion']}</span> 🙏</li>
                            </ul>""")

        # BOTONES
        button1.setText(f"{__TR__('COMROBAR_ACTUALIZACION')}")
        button2.setText(f"{__TR__('LICENCIA_CREDITOS')}")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button4.setText(f"{__TR__('TIEMPO_CARGA')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button4.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        #button1.clicked.connect(comprobar_actualizaciones_)
        button1.clicked.connect(mostrar_p_actualizaciones_)
        button2.clicked.connect(mostrar_p_app_licencias_)
        button3.clicked.connect(mostrar_p_principal_)
        button4.clicked.connect(mostrar_p_tiempos_carga_)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = True
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        FuncGuiPY.mostrar_elemento_(label)
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6, botones_fila7, botones_fila8, botones_fila9, botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)
        for i in [button1, button2, button4, button5, button6]:
            FuncGuiPY.mostrar_elemento_(i)
        # VENTANA
        VENTANA4.setMinimumSize(665, 500)
        VENTANA4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        FuncGuiPY.centrar_ventana_(VENTANA4)
        FuncGuiPY.centrar_ventana_(VENTANA4) # no va si no hay 2

    accion_infotecn.triggered.connect(mostrar_p_info_tecnica_)

    ############
    ############

    global index_ico_1
    index_ico_1 = 0

    def mostrar_p_herramientas_red_():
        global index_ico_1
        index_ico_1 += 1
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        # VENTANA
        VENTANA4.setFixedSize(665, 510)
        FuncGuiPY.centrar_ventana_(VENTANA4)
        FuncGuiPY.centrar_ventana_(VENTANA4)
        # TEXTO
        title_label.setText(f"{__TR__('P_HERRAMIENTAS_RED_TITULO')}")
        # BOTONES
        button1.setText(f"?")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(lambda: p_ayuda_msg_(VENTANA4, 2))
        button3.clicked.connect(mostrar_p_principal_)
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(button2)
        FuncGuiPY.ocultar_elemento_(label)
        FuncGuiPY.ocultar_elemento_(spacer_x1)
        FuncGuiPY.ocultar_elemento_(text_edit_blog)
        # CAMBIAR VARIABLES
        global ESTA_EN_TERMINOS
        ESTA_EN_TERMINOS = True
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # MOSTRAR ELEMENTOS
        for i in [botones_fila1, botones_fila2, botones_fila3, botones_fila4, botones_fila5, botones_fila6]:
            for z in i:
                FuncGuiPY.mostrar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)

    button1.clicked.connect(mostrar_p_herramientas_red_)

    ############
    ############

    def mostrar_p_herramientas_otras_():
        # MOSTRAR ELEMENTOS
        mostrar_todos_elementos_()
        global ESTA_EN_TERMINOS
        # VENTANA
        VENTANA4.setFixedSize(665, 364)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        if ESTA_EN_TERMINOS: FuncGuiPY.centrar_ventana_(VENTANA4)
        # TEXTO
        title_label.setText(f"{__TR__('P_HERRAMIENTAS_OTRAS_TITULO')}")
        # BOTONES
        button1.setText(f"?")
        button3.setText(f"{__TR__('VOLVER_ATRAS')}")
        button1.clicked.disconnect()
        button2.clicked.disconnect()
        button3.clicked.disconnect()
        button1.setShortcut("")
        button2.setShortcut("")
        button3.setShortcut("")
        button1.clicked.connect(lambda: p_ayuda_msg_(VENTANA4, 3))
        button3.clicked.connect(mostrar_p_principal_)
        # OCULTAR ELEMENTOS
        FuncGuiPY.ocultar_elemento_(button2)
        FuncGuiPY.ocultar_elemento_(label)
        FuncGuiPY.ocultar_elemento_(spacer_x1)
        # CAMBIAR VARIABLES
        ESTA_EN_TERMINOS = False
        # SHORTCUT
        accion_salir.setShortcut("")
        button3.setShortcut("Escape")
        # MOSTRAR ELEMENTOS
        for i in [botones_fila10, botones_fila11, botones_fila12]:
            for z in i:
                FuncGuiPY.ocultar_elemento_(z)
        for i in [botones_fila7, botones_fila8, botones_fila9]:
            for z in i:
                FuncGuiPY.mostrar_elemento_(z)
        for i in [button4, button5, button6, button7, apoya1, apoya2, apoya3]:
            FuncGuiPY.ocultar_elemento_(i)

    button2.clicked.connect(mostrar_p_herramientas_otras_)

    ############
    ############

    if es_movil == "IrAHerramientasRed": mostrar_p_herramientas_red_()
    if es_movil == "IrAHerramientasOtras": mostrar_p_herramientas_otras_()
    if es_movil == "IrASobreAili": mostrar_p_info_tecnica_()
    if es_movil == "IrALicencia": mostrar_p_licencia_()
    if es_movil == "IrADependencias": mostrar_p_dependencias_()
    button1.setShortcut("Alt+1")
    button2.setShortcut("Alt+2")
    button3.setShortcut("Alt+4")

    global TIEMPO_CARGA_V_PRINCIPAL
    if TIEMPO_CARGA_V_PRINCIPAL == "":
        TIEMPO_CARGA_V_PRINCIPAL = datetime.now()

    VENTANA4.show()
    FuncGuiPY.centrar_ventana_(VENTANA4)
    return VENTANA4

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla para la ayuda de la configuracion

def p_ayuda_msg_(ventana=None, tipo=1):

    global VENTANA9
    VENTANA9 = QMainWindow()
    
    if tipo == 3:
        VENTANA9.setFixedSize(650, 110)
    elif tipo == 4:
        VENTANA9.setFixedSize(650, 100)
    else:
        VENTANA9.setFixedSize(650, 250)
    
    VENTANA9.setWindowTitle("AILI-SS")
    FuncGuiPY.centrar_ventana_(VENTANA9)

    # Estilo general
    VENTANA9.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    if tipo == 1:
        label = QLabel(f"{__TR__('P_AYUDA_EXPLICACION')}")
    elif tipo == 2:
        label = QLabel(f"{__TR__('P_AYUDA_EXPLICACION_2')}")
    elif tipo == 3:
        label = QLabel(f"{__TR__('P_AYUDA_EXPLICACION_3')}")
    elif tipo == 4:
        label = QLabel(f"{__TR__('P_AYUDA_EXPLICACION_4')}")
    else:
        pass

    label.setTextFormat(Qt.TextFormat.RichText) # HTML
    label.setWordWrap(True)
    main_layout.addWidget(label)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    # Botones
    def abrir_p_dependencias():
        ventana.close()
        p_principal_(VENTANA9, "IrADependencias")

    button1 = QPushButton(f"{__TR__('INSTALAR_DEPENDENCIAS')}")
    button1.clicked.connect(abrir_p_dependencias)
    button1.setProperty("tipo", "button1")

    button2 = QPushButton(f"{__TR__('COLORES')}")
    button2.clicked.connect(lambda: webbrowser.open("https://htmlcolorcodes.com/"))
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('CERRAR')}")
    button3.clicked.connect(lambda: VENTANA9.close())
    QShortcut(QKeySequence("Escape"), button3).activated.connect(lambda: VENTANA9.close())
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    if tipo == 1:
        button_layout.addWidget(button2)
    else:
        if tipo != 4:
            button_layout.addWidget(button1)
    
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA9.setCentralWidget(widget_principal)

    VENTANA9.show()
    return VENTANA9

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla para la ayuda de la licencia

def p_ayuda_licencia_(ventana):
    global VENTANA10
    VENTANA10 = QMainWindow()
    VENTANA10.setFixedSize(680, 330)
    FuncGuiPY.centrar_ventana_(VENTANA10)
    VENTANA10.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA10.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    label = QLabel(f"""{__TR__('TIPO_CLAVE')}:
<ul>
<li><span style='color: {FuncMainPY.obt_json_(7)};'>PREMIUM</span>: {__TR__('BENEFICIO_1_CLAVE')}</li>
<li><span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('ESTANDAR')}</span>: {__TR__('BENEFICIO_2_CLAVE')}</li>
</ul><br>
{__TR__('PREGUNTA_SOBRE_APP')}
<ul>
<li>{__TR__('RESPUESTA_PREGUNTA_SOBRE_APP')}</li>
</ul><br>
{__TR__('QUE_ES_ELIMINAR_LOCAL_PRE')}
<ul>
<li>{__TR__('QUE_ES_ELIMINAR_LOCAL_RES')}</li>
</ul>
""")
    label.setTextFormat(Qt.TextFormat.RichText) # HTML
    label.setWordWrap(True)
    main_layout.addWidget(label)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    # Botones
    button2 = QPushButton(f"{__TR__('AMPLIE_LICENCIA')}")
    button2.clicked.connect(lambda: webbrowser.open("https://aili-ss.pages.dev/Productos#Precios"))
    button2.setProperty("tipo", "button1")
    QShortcut(QKeySequence("Return"), button2).activated.connect(lambda: webbrowser.open("https://aili-ss.pages.dev/Productos#Precios"))
    
    button3 = QPushButton(f"{__TR__('CERRAR')}")
    button3.clicked.connect(lambda: VENTANA10.close())
    button3.setShortcut("Return")
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA10.setCentralWidget(widget_principal)

    VENTANA10.show()
    return VENTANA10

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla para la configuracion

def p_configuracion_(ventana=None):
    global VENTANA11
    VENTANA11 = QMainWindow()
    VENTANA11.showMaximized()
    VENTANA11.setFixedSize(VENTANA11.size())

    ############
    
    overlay = QWidget(VENTANA11)
    overlay.setWindowFlags(Qt.FramelessWindowHint)
    overlay.setAttribute(Qt.WA_TransparentForMouseEvents)
    layout = QVBoxLayout(overlay)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignCenter)
    loading_label = QLabel(f"{__TR__('CARGANDO_RECURSOS')}")
    layout.addWidget(loading_label)
    overlay.show()

    def fix_overlay():
        VENTANA11.setFixedSize(VENTANA11.size())
        overlay.setGeometry(VENTANA11.rect())
        overlay.show()
        overlay.raise_()
        QTimer.singleShot(300, overlay.close)

    QTimer.singleShot(0, fix_overlay)

    ############

    elementos_visibles, elementos_visibles_2, elementos_visibles_3 = [], [], []

    VENTANA11.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA11.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles_2.append(spacer)
    elementos_visibles_3.append(spacer)

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label__0 = QLabel(f"{__TR__('CONFIG_GUI_TITULO')}")
    title_label__0.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label__0)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    label = QLabel(f"{__TR__('P_CONFIG_COLORES_EXPLICACION')}")
    label.setTextFormat(Qt.TextFormat.RichText) # HTML
    label.setWordWrap(True)
    main_layout.addWidget(label)
    elementos_visibles.append(label)

    ############

    grid_layout = QGridLayout()
    elementos_visibles.append(grid_layout)

    grid_layout.setColumnStretch(0, 1)
    grid_layout.setColumnStretch(1, 1)

    ############
    
    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    label = QLabel(f"{__TR__('COLOR_BASE_APP')}")
    elementos_visibles.append(label)
    config_entrada0 = QLineEdit()
    elementos_visibles.append(config_entrada0)

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    ############
    
    label = QLabel(f"{__TR__('COLOR_BASE_LETRAS')}")
    elementos_visibles.append(label)
    config_entrada01 = QLineEdit()
    elementos_visibles.append(config_entrada01)

    grid_layout.addWidget(label, 0, 1)
    grid_layout.addWidget(config_entrada01, 1, 1)
    
    ############
    
    label = QLabel(f"{__TR__('COLOR_FONDO_BT1')}")
    elementos_visibles.append(label)
    config_entrada1 = QLineEdit()
    elementos_visibles.append(config_entrada1)

    grid_layout.addWidget(label, 2, 0)
    grid_layout.addWidget(config_entrada1, 3, 0)
    
    ############

    label = QLabel(f"{__TR__('COLOR_TEXTO_BT')}")
    elementos_visibles.append(label)
    config_entrada2 = QLineEdit()
    elementos_visibles.append(config_entrada2)

    grid_layout.addWidget(label, 2, 1)
    grid_layout.addWidget(config_entrada2, 3, 1)
    
    ############
    
    label = QLabel(f"{__TR__('COLOR_HOVER_BT1')}")
    elementos_visibles.append(label)
    config_entrada3 = QLineEdit()
    elementos_visibles.append(config_entrada3)

    grid_layout.addWidget(label, 4, 0)
    grid_layout.addWidget(config_entrada3, 5, 0)
    
    ############

    label = QLabel(f"{__TR__('COLOR_HOVER_BT2')}")
    config_entrada4 = QLineEdit()
    elementos_visibles.append(label)
    elementos_visibles.append(config_entrada4)

    grid_layout.addWidget(label, 4, 1)
    grid_layout.addWidget(config_entrada4, 5, 1)
    
    ############

    label = QLabel(f"{__TR__('COLOR_RESALTE_TIT')}")
    config_entrada5 = QLineEdit()
    elementos_visibles.append(label)
    elementos_visibles.append(config_entrada5)

    grid_layout.addWidget(label, 6, 0)
    grid_layout.addWidget(config_entrada5, 7, 0)
        
    ############

    label = QLabel(f"{__TR__('COLOR_RESALTE_TEXTO')}")
    config_entrada6 = QLineEdit()
    elementos_visibles.append(label)
    elementos_visibles.append(config_entrada6)

    grid_layout.addWidget(label, 6, 1)
    grid_layout.addWidget(config_entrada6, 7, 1)
   
    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles.append(spacer)

    ############

    main_layout.addLayout(grid_layout)

    ############
    ############

    # Layout 
    header_layout = QHBoxLayout()
    elementos_visibles.append(header_layout)

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    title_label__1 = QLabel(f"{__TR__('CONFIG_PARAM_TITULO')}")
    title_label__1.setStyleSheet("font-size: 24px; font-weight: bold;")

    header_layout.addWidget(title_label__1)
    main_layout.addLayout(header_layout)
    elementos_visibles.append(title_label__1)

    ############
    
    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles.append(spacer)

    ############

    grid2 = QGridLayout()
    elementos_visibles.append(grid2)

    grid2.setColumnStretch(0, 1)
    grid2.setColumnStretch(1, 1)

    ############

    label__interfaz_ = QLabel(f"{__TR__('INTERFAZ_RED')}({FuncMainPY.obt_json_(5) if FuncMainPY.obt_json_(5) not in [None, ''] else __TR__('NINGUNA_ELEGIDA')})")
    elementos_visibles.append(label__interfaz_)
    grid2.addWidget(label__interfaz_, 0, 0)

    config_param0 = QComboBox()
    elementos_visibles.append(config_param0)

    if FuncMainPY.obt_json_(5) not in [None, '']:
        config_param0.addItems([FuncMainPY.obt_json_(5), ""])

        ii = FuncMainPY.INTERFACES_()
        ii.remove(FuncMainPY.obt_json_(5))

        config_param0.addItems(ii)
    else:
        config_param0.addItem("")
        config_param0.addItems(FuncMainPY.INTERFACES_())

    grid2.addWidget(config_param0, 1, 0)
    QTimer.singleShot(0, lambda: config_param0.setCurrentIndex(0)) # No va sino

    ############

    label = QLabel(f"{__TR__('IDIOMA')}")
    grid2.addWidget(label, 0, 1)
    elementos_visibles.append(label)

    config_param7 = QComboBox()
    elementos_visibles.append(config_param7)

    def anadir_items_idioma_():
        if FuncMainPY.obt_json_("IDIOMA") == "es-ESPAÑA":
            config_param7.addItems(["es-ESPAÑA", "en-UNITED_KINGDOM", "gl-GALICIA"])
        elif FuncMainPY.obt_json_("IDIOMA") == "gl-GALICIA":
            config_param7.addItems(["gl-GALICIA", "es-ESPAÑA", "en-UNITED_KINGDOM"])
        else:
            config_param7.addItems(["en-UNITED_KINGDOM", "es-ESPAÑA", "gl-GALICIA"])
    
    threading.Thread(target=anadir_items_idioma_).start()

    grid2.addWidget(config_param7, 1, 1)
    
    ############

    main_layout.addLayout(grid2)

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles.append(spacer)

    ############
    ############

    # Layout 
    header_layout = QHBoxLayout()
    elementos_visibles.append(header_layout)

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    title_label__2 = QLabel(f"{__TR__('P_CONFIG_TITULO_3')}")
    title_label__2.setStyleSheet("font-size: 24px; font-weight: bold;")

    header_layout.addWidget(title_label__2)
    main_layout.addLayout(header_layout)
    elementos_visibles.append(title_label__2)

    ############
    
    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles.append(spacer)

    ############

    grid2 = QGridLayout()
    elementos_visibles.append(grid2)

    ############

    label = QLabel(f"{__TR__('PELIGRO_EXPLICACION')}")
    elementos_visibles.append(label)
    grid2.addWidget(label, 0, 0)

    config_param1 = QComboBox()
    elementos_visibles.append(config_param1)
    config_param1.addItem(__TR__('SI_ACEPTO'), userData=True)
    config_param1.addItem(__TR__('NO_ACEPTO'), userData=False)

    def anadir_items_terminos_():
        valor_actual = FuncMainPY.obt_json_(8)
        if valor_actual in [True, "SI", "YES", __TR__('SI_ACEPTO')]:
            config_param1.setCurrentIndex(0)
        else:
            config_param1.setCurrentIndex(1)
    
    threading.Thread(target=anadir_items_terminos_).start()

    grid2.addWidget(config_param1, 1, 0)
    
    ############

    main_layout.addLayout(grid2)

    ############
    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles.append(spacer)

    ############

    def reiniciar_estilos_titulos_():
        title_label__0.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")
        title_label__1.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label__2.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label__0.setText(f"{__TR__('CONFIG_GUI_TITULO')}")
        title_label__1.setText(f"{__TR__('CONFIG_PARAM_TITULO')}")
        title_label__2.setText(f"{__TR__('P_CONFIG_TITULO_3')}")

    ############

    def eliminar_todos_campos_():
        for elemento in elementos_visibles:
            if isinstance(elemento, QWidget):
                elemento.hide()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().hide()
    
    ############

    def eliminar_campos_copia_seguridad_():
        for elemento in elementos_visibles_2:
            if isinstance(elemento, QWidget):
                elemento.hide()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().hide()

    ############

    def eliminar_campos_tema_personalizado_():
        for elemento in elementos_visibles_3:
            if isinstance(elemento, QWidget):
                elemento.hide()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().hide()
    
    ############

    def mostrar_elementos_():
        title_label__0.setText(f"{__TR__('CONFIG_GUI_TITULO')}")

        for elemento in elementos_visibles:
            if isinstance(elemento, QWidget):
                elemento.show()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().show()
    
    ############

    def mostrar_elementos_copia_seguridad_():
        QTimer.singleShot(50, camb_)

        for elemento in elementos_visibles_2:
            if isinstance(elemento, QWidget):
                elemento.show()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().show()
                    
    ############

    def mostrar_elementos_tema_personalizado_():
        for elemento in elementos_visibles_3:
            if isinstance(elemento, QWidget):
                elemento.show()
            elif isinstance(elemento, QLayoutItem):
                if elemento.widget():
                    elemento.widget().show()
    
    ############

    def mostrar_p_copia_seguridad_():
        button10.clicked.disconnect()
        button10.setText(f"{__TR__('IR_CONFIG')}")
        button10.clicked.connect(mostrar_p_configuracion_)
        eliminar_todos_campos_()
        mostrar_elementos_copia_seguridad_()
        title_label__0.setText(f"{__TR__('P_COPIA_SEGURIDAD_TITULO')}")
    
    ############

    def mostrar_p_tema_personalizado_():
        button10.clicked.disconnect()
        button10.setText(f"{__TR__('IR_CONFIG')}")
        button10.clicked.connect(mostrar_p_configuracion_)
        eliminar_todos_campos_()
        mostrar_elementos_tema_personalizado_()
        text_edit.setText(f"{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO')} <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO_1')}</span><br><br>{__TR__('TEMA_PERSONALIZADO_DESC')}<br><br>{__TR__('TEMA_ACTUAL_GUARDAR')}<br>" + f"""<ul>
            <li>{__TR__('COLOR_BASE_APP')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(0)}</span></li>
            <li>{__TR__('COLOR_BASE_LETRAS')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_("01")}</span></li>
            <li>{__TR__('COLOR_FONDO_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(1)}</span></li>
            <li>{__TR__('COLOR_TEXTO_BT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(2)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(3)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT2')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(4)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TIT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(6)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TEXTO')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(7)}</span></li>
        </ul>""")
        title_label__0.setText(f"<span style='color: $FuncMainPY_obt_json_6;'>{__TR__('TEMA_PERSONALIZADO_TIT')}</span>")
    
    ############

    def mostrar_p_configuracion_():
        button9.clicked.disconnect()
        button10.clicked.disconnect()

        button9.setText(f"{__TR__('TEMA_PERSONALIZADO')}")
        button10.setText(f"{__TR__('COPIA_SEGURIDAD')}")

        button9.clicked.connect(mostrar_p_tema_personalizado_)
        button10.clicked.connect(mostrar_p_copia_seguridad_)
        
        eliminar_campos_copia_seguridad_()
        eliminar_campos_tema_personalizado_()
        mostrar_elementos_()
        reiniciar_estilos_titulos_()

    ############

    def actualizar_campos_():
        config_entrada0.setText(FuncMainPY.obt_json_(0))
        config_entrada01.setText(FuncMainPY.obt_json_("01"))
        config_entrada1.setText(FuncMainPY.obt_json_(1))
        config_entrada2.setText(FuncMainPY.obt_json_(2))
        config_entrada3.setText(FuncMainPY.obt_json_(3))
        config_entrada4.setText(FuncMainPY.obt_json_(4))
        config_entrada5.setText(FuncMainPY.obt_json_(6))
        config_entrada6.setText(FuncMainPY.obt_json_(7))

        valor_actual = FuncMainPY.obt_json_(8)
        if valor_actual in [True, "SI", "YES", __TR__('SI_ACEPTO')]:
            config_param1.setCurrentIndex(0)
        else:
            config_param1.setCurrentIndex(1)
        
        config_param7.clear()
        if FuncMainPY.obt_json_("IDIOMA") == "es-ESPAÑA":
            config_param7.addItems(["es-ESPAÑA", "en-UNITED_KINGDOM", "gl-GALICIA"])
        elif FuncMainPY.obt_json_("IDIOMA") == "gl-GALICIA":
            config_param7.addItems(["gl-GALICIA", "es-ESPAÑA", "en-UNITED_KINGDOM"])
        else:
            config_param7.addItems(["en-UNITED_KINGDOM", "es-ESPAÑA", "gl-GALICIA"])


        label__interfaz_.setText(f"{__TR__('INTERFAZ_RED')}({FuncMainPY.obt_json_(5) if FuncMainPY.obt_json_(5) not in [None, ''] else __TR__('NINGUNA_ELEGIDA')})")
        config_param0.clear()
        if FuncMainPY.obt_json_(5) not in [None, '']:
            config_param0.addItems([FuncMainPY.obt_json_(5), ""])

            ii = FuncMainPY.INTERFACES_()
            ii.remove(FuncMainPY.obt_json_(5))

            config_param0.addItems(ii)
        else:
            config_param0.addItem("")
            config_param0.addItems(FuncMainPY.INTERFACES_())
        
        ############
        ############

    ################################################
    ################################################
    ################################################

    buttonxx4 = QPushButton(f"{__TR__('GUARDAR_BACKUP')}")
    buttonxx4.setProperty("tipo", "button1")
    elementos_visibles_2.append(buttonxx4)

    buttonxx5 = QPushButton(f"{__TR__('RESTAURAR_BACKUP')}")
    buttonxx5.setProperty("tipo", "button1")
    elementos_visibles_2.append(buttonxx5)

    ################################################

    buttonxxx4 = QPushButton(f"{__TR__('GUARDAR_MAYUS')}")
    buttonxxx4.setProperty("tipo", "button1")
    elementos_visibles_3.append(buttonxxx4)
    FuncGuiPY.ocultar_elemento_(buttonxxx4)

    buttonxxx5 = QPushButton(f"{__TR__('RESTAURAR_MAYUS')}")
    buttonxxx5.setProperty("tipo", "button1")
    elementos_visibles_3.append(buttonxxx5)
    FuncGuiPY.ocultar_elemento_(buttonxxx5)

    ############

    def guardar_():
       ############

        try:
            shutil.copy2(FuncMainPY.obtener_ruta_config(), os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'config.json'))

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            camb_("1", False)
        except:
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            camb_("1", True)
        
        actualizar_campos_()
        

        ############

    ############

    def restaurar_():
        PASE_IDIOMA = False
       ############
        try:
            with open(os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'config.json'), "r") as f:
                data = json.load(f)
            
            if data["IDIOMA"] != FuncMainPY.obt_json_('IDIOMA'):
                PASE_IDIOMA = True

        except:
            pass
       ############
        try:
            shutil.copy2(os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'config.json'), FuncMainPY.obtener_ruta_config())
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            camb_("2", False)
        except:
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            camb_("2", True)
        
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            actualizar_campos_()

        ############

    ############

    buttonxx4.clicked.connect(guardar_)
    buttonxx5.clicked.connect(restaurar_)
    
    ############

    def camb_(nuevo=False, err=False):
        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)

        if err == False:
            subrayar_1, subrayar_2 = "", ""
        else:
            subrayar_1, subrayar_2 = "<span style='text-decoration: line-through;'>", "</span>"

        if nuevo == False:
            texto_n = ""
        if nuevo == "1":
            texto_n = f"<span style='color: {'yellow' if err == False else 'red'};'>{subrayar_1}{__TR__('COPIA_SEGURIDAD')} - {__TR__('GUARDADA')}</span>{subrayar_2} <br><br>"
        if nuevo == "2":
            texto_n = f"<span style='color: {'yellow' if err == False else 'red'};'>{subrayar_1}{__TR__('COPIA_SEGURIDAD')} - {__TR__('RESTAURADA')}</span>{subrayar_2} <br><br>"

        
        ############

        texto_poner_ = f"{texto_n}<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('COPIA_SEGURIDAD')}</span> - {__TR__('GUARDAR_MAYUS')} <br><br>"

        texto_poner_ += f"{__TR__('COPIA_SEGURIDAD_DESC')}<br><br>"
        texto_poner_ += f"{__TR__('RUTA_A_GUARDAR')} <span style='color: {'yellow' if nuevo in ['1', '2'] else FuncMainPY.obt_json_(6)};'>{os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'), 'config.json')}</span><br><br>"
        texto_poner_ += f"{__TR__('COPIA_SEGURIDAD_DESC_2')}<br>"
        texto_poner_ += f"""<ul>
            <li>{__TR__('COLOR_BASE_APP')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(0)}</span></li>
            <li>{__TR__('COLOR_BASE_LETRAS')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_("01")}</span></li>
            <li>{__TR__('COLOR_FONDO_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(1)}</span></li>
            <li>{__TR__('COLOR_TEXTO_BT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(2)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(3)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT2')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(4)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TIT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(6)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TEXTO')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(7)}</span></li>
            <br style='font-size: 8px;'>
            <li>{__TR__('INTERFAZ_RED')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(5)}</span></li>
            <li>{__TR__('IDIOMA')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_('IDIOMA')}</span></li>
            <br style='font-size: 8px;'>
            <li>{__TR__('P_TERMINOS_TITULO')}<span style='color: {FuncMainPY.obt_json_(6)};'>: {FuncMainPY.obt_json_(8)}</span></li>
        </ul>"""

                ############

        texto_poner_ += f"<br><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('COPIA_SEGURIDAD')}</span> - {__TR__('RESTAURAR_MAYUS')} <br><br>"

        texto_poner_ += f"{__TR__('COPIA_SEGURIDAD_DESC_3')}"

        ############

        text_edit.setText(texto_poner_)

        ############
        ############

    ############

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    elementos_visibles_2.append(text_edit)
    elementos_visibles_3.append(text_edit)

    def temp_ajustar_():
        VENTANA11.resizeEvent = lambda event: adjust_text_edit_height(VENTANA11, text_edit)
        def adjust_text_edit_height(window, text_edit):
            text_edit.setFixedHeight(int(window.height() * 0.75))
    
    threading.Thread(target=temp_ajustar_).start()

    main_layout.addWidget(text_edit)

    ############

    threading.Thread(target=eliminar_campos_copia_seguridad_).start()

    ################################################
    ################################################
    ################################################

    def reg_valores_():
        FuncMainPY.gen_json_(config_param7.currentText())

        VENTANA11.setStyleSheet(FuncMainPY.estilos_())
        actualizar_campos_()
        reiniciar_estilos_titulos_()

    ############

    def gua_valores_():
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_(config_entrada0.text(),
                             config_entrada01.text(),
                             config_entrada1.text(),
                             config_entrada2.text(),
                             config_entrada3.text(),
                             config_entrada4.text(),
                             config_param0.currentText(),
                             config_entrada5.text(),
                             config_entrada6.text(),
                             config_param1.currentData(),
                             config_param7.currentText())

        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()

    ############

    def gua_tema1_(): # Tema base
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_("#2A3139",
                             "white",
                             "#4a4a4a",
                             "white",
                             "#008fff",
                             "red",
                             config_param0.currentText(),
                             "#008fff",
                             "orange",
                             config_param1.currentData(),
                             config_param7.currentText())
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()

    ############

    def gua_tema2_(): # Tema claro
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_("white",
                             "black",
                             "lightgray",
                             "black",
                             "blue",
                             "#e15757",
                             config_param0.currentText(),
                             "blue",
                             "orange",
                             config_param1.currentData(),
                             config_param7.currentText())
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()

    ############

    def gua_tema3_(): # Tema profesional
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_("black",
                             "white",
                             "rgba(144, 238, 144, 0.3)",
                             "white",
                             "rgba(144, 238, 144, 0.3)",
                             "darkgreen",
                             config_param0.currentText(),
                             "rgba(144, 238, 144, 0.7)",
                             "rgba(144, 238, 144, 0.7)",
                             config_param1.currentData(),
                             config_param7.currentText())
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()
    
    ############

    def gua_tema4_(): # Tema oscuro elegante
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_("#1e1e2e",
                             "#cdd6f4",
                             "#313244",
                             "#ffffff",
                             "#89b4fa",
                             "#c1204d",
                             config_param0.currentText(),
                             "#89b4fa",
                             "#fab387",
                             config_param1.currentData(),
                             config_param7.currentText())
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()

    ############

    def gua_tema5_(): # Tema océano
        PASE_IDIOMA = False
        if FuncMainPY.obt_json_("IDIOMA") != config_param7.currentText():
            PASE_IDIOMA = True

        FuncMainPY.gua_json_("#1E2A38",
                             "#E0F2F1",
                             "#016359",
                             "#FFFFFF",
                             "#26A69A",
                             "#EF5350",
                             config_param0.currentText(),
                             "#00BFA5",
                             "#FFD54F",
                             config_param1.currentData(),
                             config_param7.currentText())
        if PASE_IDIOMA:
            p_configuracion_(VENTANA11)
        else:
            VENTANA11.setStyleSheet(FuncMainPY.estilos_())
            button3.setText(f"{__TR__('VOLVER_ATRAS')}")
            actualizar_campos_()
            reiniciar_estilos_titulos_()
    
    ############

    threading.Thread(target=actualizar_campos_).start()

    ############

    def gua_tema_personalizado_(ELECCION):
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

        if ELECCION == 'GUARDAR':
            FuncMainPY.gua_tema_personalizado_JSON_(config_entrada0.text(),
                                                config_entrada01.text(),
                                                config_entrada1.text(),
                                                config_entrada2.text(),
                                                config_entrada3.text(),
                                                config_entrada4.text(),
                                                config_entrada5.text(),
                                                config_entrada6.text())
        else:
            if os.path.exists(os.path.join(RUTA_DIR_USUARIO, "ConfigTemaPers.json")):
                with open(os.path.join(RUTA_DIR_USUARIO, "ConfigTemaPers.json"), "r", encoding="utf-8") as f:
                    data = json.load(f)

                FuncMainPY.gua_json_(data["APP_BASE"],
                                    data["APP_LETRA_BASE"],
                                    data["BACKG_BASE"],
                                    data["LETRA_BASE"],
                                    data["BOTON1_BASE"],
                                    data["BOTON2_BASE"],
                                    config_param0.currentText(),
                                    data["COLOR_RESALTE_TITULO"],
                                    data["COLOR_IMPORT_LICENCIA"],
                                    config_param1.currentText(),
                                    config_param7.currentText())
            
        if ELECCION == 'GUARDAR':
            text_edit.setText(f"{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO')} <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO_2')}</span><br><br>{__TR__('TEMA_PERSONALIZADO_DESC')}<br><br>{__TR__('TEMA_ACTUAL_GUARDADO')}<br>" + f"""<ul>
            <li>{__TR__('COLOR_BASE_APP')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(0)}</span></li>
            <li>{__TR__('COLOR_BASE_LETRAS')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_("01")}</span></li>
            <li>{__TR__('COLOR_FONDO_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(1)}</span></li>
            <li>{__TR__('COLOR_TEXTO_BT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(2)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT1')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(3)}</span></li>
            <li>{__TR__('COLOR_HOVER_BT2')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(4)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TIT')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(6)}</span></li>
            <li>{__TR__('COLOR_RESALTE_TEXTO')}<span style='color: {FuncMainPY.obt_json_(6)};'>{FuncMainPY.obt_json_(7)}</span></li>
        </ul>""")
        else:
            text_edit.setText(f"{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO')} <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('TEMA_PERSONALIZADO_DESC_ESTADO_3')}</span><br><br>{__TR__('TEMA_PERSONALIZADO_DESC')}")
        actualizar_campos_()
        
        VENTANA11.setStyleSheet(FuncMainPY.estilos_())
        title_label__0.setText(f"<span style='color: $FuncMainPY_obt_json_6;'>{__TR__('TEMA_PERSONALIZADO_TIT')}</span>")

    buttonxxx4.clicked.connect(lambda: gua_tema_personalizado_('GUARDAR'))
    buttonxxx5.clicked.connect(lambda: gua_tema_personalizado_('RESTAURAR'))

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    elementos_visibles_2.append(spacer)

    ############

    # Botones
    button1 = QPushButton(f"{__TR__('GUARDAR')}")
    button1.clicked.connect(gua_valores_)
    button1.setShortcut("Return")
    button1.setProperty("tipo", "button1")
    elementos_visibles.append(button1)

    button4 = QPushButton(f"{__TR__('REINICIAR_VALORES')}")
    button4.clicked.connect(reg_valores_)
    button4.setProperty("tipo", "button2")
    elementos_visibles.append(button4)

    button2 = QPushButton(f"{__TR__('AYUDA')}")
    button2.clicked.connect(lambda: p_ayuda_msg_(None, 1))
    button2.setProperty("tipo", "button1")
    elementos_visibles.append(button2)

    button6 = QPushButton(f"{__TR__('TEMA_BASE')}")
    button6.clicked.connect(gua_tema1_)
    button6.setProperty("tipo", "button1")
    elementos_visibles.append(button6)

    button5 = QPushButton(f"{__TR__('TEMA_CLARO')}")
    button5.clicked.connect(gua_tema2_)
    button5.setProperty("tipo", "button1")
    elementos_visibles.append(button5)

    button7 = QPushButton(f"{__TR__('TEMA_PRO')}")
    button7.clicked.connect(gua_tema3_)
    button7.setProperty("tipo", "button1")
    elementos_visibles.append(button7)

    button8 = QPushButton(f"{__TR__('TEMA_OSC_ELEGANTE')}")
    button8.clicked.connect(gua_tema4_)
    button8.setProperty("tipo", "button1")
    elementos_visibles.append(button8)

    button8_1 = QPushButton(f"{__TR__('TEMA_OCEANO')}")
    button8_1.clicked.connect(gua_tema5_)
    button8_1.setProperty("tipo", "button1")
    elementos_visibles.append(button8_1)

    button9 = QPushButton(f"{__TR__('TEMA_PERSONALIZADO')}")
    #button9.clicked.connect(lambda: gua_tema_personalizado_("RESTAURAR"))
    button9.clicked.connect(mostrar_p_tema_personalizado_)
    button9.setProperty("tipo", "button1")
    elementos_visibles.append(button9)

    button10 = QPushButton(f"{__TR__('COPIA_SEGURIDAD')}")
    button10.clicked.connect(mostrar_p_copia_seguridad_)
    button10.setProperty("tipo", "button1")

    ############

    def volver_():
        if ventana != None:
            ventana.close()
        p_principal_(VENTANA11, True)
        VENTANA11.close()

    ############

    button3 = QPushButton(f"{__TR__('CANCELAR')}")
    button3.clicked.connect(volver_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")
    button3.setStyleSheet("margin-right: 20px;")
    elementos_visibles.append(button3)

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(buttonxx4)
    button_layout.addWidget(buttonxx5)
    button_layout.addWidget(buttonxxx4)
    button_layout.addWidget(buttonxxx5)

    button_layout.addWidget(button1)
    button_layout.addWidget(button4)
    button_layout.addWidget(button3)
    button_layout.addWidget(button2)
    button_layout.addWidget(button10)


    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    #
    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button6)
    button_layout.addWidget(button5)
    button_layout.addWidget(button7)
    button_layout.addWidget(button8)
    button_layout.addWidget(button8_1)
    button_layout.addWidget(button9)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA11.setCentralWidget(widget_principal)

    VENTANA11.show()
    # overlay
    if ventana != None:
        ventana.hide()
    return VENTANA11

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para ver las interfaces de red y su información

def pF_interfaces_red_(ventana):
    global VENTANA13
    VENTANA13 = QMainWindow()
    VENTANA13.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA13)
    VENTANA13.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA13.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_INTERFACES_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def camb_(pase=False):
        print(1)
        if pase == False:
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
    
        texto_poner0_ = f"{__TR__('INTERFACES_DETECTADAS')} {FuncMainPY.INTERFACES_()}<br><br>{__TR__('PROCESO')}<br>"
        texto_poner_ = f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('INTERFACES_DE')}</span> '<span style='color: {FuncMainPY.obt_json_(7)};'>{socket.gethostname()}</span>'<br>"
        
        indice = 0

        for i in FuncMainPY.INTERFACES_():
            texto_poner0_ += f"{'<br>' if indice != 0 else ''}<br>---- <span style='color: {FuncMainPY.obt_json_(6)};'>{i}</span> ----"

            indice += 1

            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            texto_poner0_ += f"<br>{__TR__('RECOPILANDO_IP_MASC')} {i}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            res1 = FuncMainPY.get_network_data(i)

            texto_poner0_ += f"<br>{__TR__('RECOPILANDO_MAC')} {i}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            res2 = FuncMainPY.get_network_data(i, 1)

            texto_poner0_ += f"<br>{__TR__('CALC_DIREC_RED')} {i}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            DIREC_RED = FuncMainPY.CALCULAR_DIRECCION_RED__(i)

            texto_poner0_ += f"<br>{__TR__('CALC_DIREC_DIF')} {i}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            DIREC_DIF = FuncMainPY.CALCULAR_DIRECCION_DIFUSION__(i)

            texto_poner0_ += f"<br>{__TR__('CALC_TIPO_IP')} {i}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            TIPO_IP = FuncMainPY.tipo_ip_(str(res1[0]))

            texto_poner0_ += f"<br>{__TR__('DETECTANDO_GATEWAY_EN_RED')}"
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            try:
                GATEWAY = FuncMainPY.get_network_data(None, 2)
                GATEWAY_SI = ipaddress.ip_address(GATEWAY) in ipaddress.ip_network(DIREC_RED)
            except:
                GATEWAY_SI, GATEWAY = False, None

            if GATEWAY_SI:
                texto_poner0_ += f"<br>{__TR__('PING_GATEWAY_EN_RED')}"
                GATEWAY_PING = ""

                if pase == False:
                    text_edit.setText(texto_poner0_); QApplication.processEvents()

                try:
                    ping = ping3.ping(GATEWAY, timeout=0.5)
                    if ping != None:
                        GATEWAY_PING = f"(Ping: <span style='color: {FuncMainPY.obt_json_(7)};'>{round(ping, 6)} ms</span>)"
                except:
                    pass

            texto_poner0_ += f"<br>{__TR__('DETECTANDO_DNS_EN_RED')} "
            if pase == False:
                text_edit.setText(texto_poner0_); QApplication.processEvents()

            resolver = dns.resolver.Resolver()
            default_dns_server = resolver.nameservers
            DNS_FIN_ = None
            for dns_ in default_dns_server:
                if ipaddress.ip_address(dns_) in ipaddress.ip_network(DIREC_RED):
                    DNS_FIN_ = str(dns_)
                    break

            ########

            texto_poner_ += f"""<p><span style='color: {FuncMainPY.obt_json_(6)};'>{i}</span>:</p>
<ul>
    <li>MAC: <span style='color: {FuncMainPY.obt_json_(7)};'>{res2[0]}</span></li>
    <br style='font-size: 8px;'>
    <li>{__TR__('IP_ACTUAL')}: <span style='color: {FuncMainPY.obt_json_(7)};'>{res1[0]}</span></li>
    <li>{__TR__('MASCARA')}: <span style='color: {FuncMainPY.obt_json_(7)};'>/{DIREC_RED.split('/')[1]}</span>  •  <span style='color: {FuncMainPY.obt_json_(7)};'>{res1[1]}</span></li>
    <li>{__TR__('TIPO_IP')}: <span style='color: {FuncMainPY.obt_json_(7)};'>{TIPO_IP}</span></li>
    <br style='font-size: 8px;'>
    <li>{__TR__('DIREC_RED_2')}<span style='color: {FuncMainPY.obt_json_(7)};'>{DIREC_RED}</span></li>
    <li>{__TR__('DIREC_DIF_2')}<span style='color: {FuncMainPY.obt_json_(7)};'>{DIREC_DIF}</span></li>
    
    {f"<br style='font-size: 8px;'><li>Gateway: <span style='color: {FuncMainPY.obt_json_(7)};'>{GATEWAY}</span> {GATEWAY_PING}</li>" if GATEWAY_SI == True else ""}
    {f"<li>{__TR__('SERVER_DNS')}<span style='color: {FuncMainPY.obt_json_(7)};'>{DNS_FIN_}</span></li>" if DNS_FIN_ != None else ""}

</ul>"""
        ############

        if pase == True:
            return texto_poner_

        text_edit.setText(texto_poner_)

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)

        ############

        try: button4.clicked.disconnect()
        except: pass
        button4.setEnabled(True)
        button4.setText(f"{__TR__('EXPORTAR')}")
        button4.clicked.connect(lambda: pF_exportar_res_(VENTANA13, texto_poner_, 6))

        ############
    ############

    if ventana == "Pase1":
        res = camb_(True)

        try: VENTANA13.destroy()
        except: pass

        return res
    else:
        QTimer.singleShot(0, camb_)

    ############

    text_edit = QTextEdit()
    text_edit.setReadOnly(True)
    text_edit.setText(f"{__TR__('CALCULANDO')}")
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA13.resizeEvent = lambda event: adjust_text_edit_height(VENTANA13, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    button4 = QPushButton(f"{__TR__('ESPERAR')}")
    button4.setProperty("tipo", "button1")
    button4.setEnabled(False)

    def hide_show_():
        VENTANA13.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    button_layout = QHBoxLayout()

    button_layout.addWidget(button4)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA13.setCentralWidget(widget_principal)

    VENTANA13.show()
    ventana.hide()
    return VENTANA13

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para ver las interfaces de red y su información

def pF_deteccion_arp_spoofing_(ventana):
    global VENTANA14
    VENTANA14 = QMainWindow()
    VENTANA14.timer = QTimer()

    VENTANA14.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA14)
    VENTANA14.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA14.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_ARP_SPOOF_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    text_edit = QTextEdit()
    try:
        MAC = FuncMainPY.get_network_data(FuncMainPY.obt_json_(5), 1)[0]
        text_edit.setText(f"<span style='color: {FuncMainPY.obt_json_(6)};'>!! {__TR__('IMPORTANTE')} !!</span><br><br>{__TR__('NO_FUNCIONA_MAS_INTERFACES')} (<span style='color: {FuncMainPY.obt_json_(7)};'>{FuncMainPY.obt_json_(5)}</span>) [<span style='color: {FuncMainPY.obt_json_(7)};'>{MAC}</span>].<br><br><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('COMO_FUNCIONA')}</span><br><br>{__TR__('FILTROS_SEGUIR')}<br><ol> <li>{__TR__('FILTROS_SEGUIR_1')}</li> <li>{__TR__('FILTROS_SEGUIR_2')}</li> <li>{__TR__('FILTROS_SEGUIR_3')}</li> <li>{__TR__('FILTROS_SEGUIR_4')}</li>  </ol><br>{__TR__('PULSAR_EMPEZAR')}")
    except:
        FuncMainPY.ERR_REG_(f"[pF_deteccion_arp_spoofing_] Interfaz no configurada.\n\n")

        MAC = "NO"
        text_edit.setText(F"Error:<br><br>{__TR__('COMPROBAR_INTERFAZ_EN_CONFIG')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA14.resizeEvent = lambda event: adjust_text_edit_height(VENTANA14, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def SCAPY_ARP_Spoofing_zz():
        button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        
        e = FuncMainPY.SCAPY_ARP_Spoofing_()
        try:
            if e[1] == "DIREC_RED_ERROR": text_edit.setText(e[0])
        except: pass

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(SCAPY_ARP_Spoofing_zz)
    button0.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA14.close()
        ventana.show()


    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA14))
    button1.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    if MAC == "NO":
        button_layout.addWidget(button1)
    else:
        button_layout.addWidget(button0)

    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA14.setLayout(main_layout)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA14.setCentralWidget(widget_principal)

    VENTANA14.show()
    ventana.hide()
    return VENTANA14

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para monitorizar el tráfico de red

def pF_monitorizacion_trafico_red_(ventana):
    global VENTANA15
    VENTANA15 = QMainWindow()
    VENTANA15.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA15.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA15.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA15)
    VENTANA15.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA15.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_MONITORIZAR_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    ############
    
    label = QLabel(f"{__TR__('FILTRO_A_MONITORIZAR')}")
    config_entrada0 = QLineEdit()

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    config_entrada0.setText("tcp or udp")
    config_entrada0.setPlaceholderText("tcp or udp")
    
    ############
    
    label = QLabel(f"{__TR__('TIEMPO_ENTRE_PAQUETES')}")
    config_entrada1 = QLineEdit()

    grid_layout.addWidget(label, 0, 1)
    grid_layout.addWidget(config_entrada1, 1, 1)
    
    config_entrada1.setText("0.5")
    config_entrada1.setPlaceholderText("0.00")

    ############

    main_layout.addLayout(grid_layout)

    ############

    GUIA = f"""<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('CONFIG_FILTROS')}</span>  <br><br>
<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('TIPO_FILTROS')}</span>  <br>
tcp, udp, icmp, arp, dns, dot11, bootp, tls, ssl  <br><br>

{__TR__('EJ')}  <br>
>> tcp  <br><br>

<span style='color: {FuncMainPY.obt_json_(6)};'>HOSTS:</span>  <br>
host (IP_HOST)  <br><br>

{__TR__('EJ')}  <br>
>> host 192.168.1.1  <br>
?? {__TR__('PAQUETES_INVOLUCRAN_IP')}  <br><br>

<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('ORIGEN_')}</span>  <br>
src ({__TR__('ORIGEN')}), dst ({__TR__('DESTINO')})  <br><br>

<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('OPERADORES')}</span>  <br>
and, or, not  <br><br>
                      
{__TR__('EJS')}  <br>
>> tcp and src port 443  <br>
?? {__TR__('TODO_PAQ_TCP_PUERTO')} 443  <br><br>
                      
>> udp and dst port 80  <br>
?? {__TR__('TODO_PAQ_UDP_PUERTO_80')}  <br><br>

>> net 192.168.0.0/24 not host 192.168.1.1  <br>
?? {__TR__('SOBRE_RED_SIN_HOST')}

<br><br> <span style='color: {FuncMainPY.obt_json_(7)}; font-size: 12px;'>{__TR__('DEBES_TENER_NPCAP')}</span>
"""
    
    ############

    text_edit = QTextEdit()
    text_edit.setHtml(GUIA)
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA15.resizeEvent = lambda event: adjust_text_edit_height(VENTANA15, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############
    
    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def check_(e=None):
        FuncGuiPY.ocultar_elemento_(button1)

        if FuncMainPY.obt_json_(5) == None or FuncMainPY.obt_json_(5) == "":
            text_edit.setHtml(f"Error:<br><br>{__TR__('COMPROBAR_INTERFAZ_EN_CONFIG')}")

            FuncGuiPY.ocultar_elemento_(button1)
            FuncGuiPY.ocultar_elemento_(button0)
            FuncGuiPY.ocultar_elemento_(button2)
            FuncGuiPY.ocultar_elemento_(button4)
            FuncGuiPY.mostrar_elemento_(button3)
            FuncGuiPY.mostrar_elemento_(button1)

            return
    
        with open(FuncMainPY.obtener_ruta_config(), "r") as f:
            data = json.load(f)
            if e == False:
                button2.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
            else:
                button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                button2.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
            
            QApplication.processEvents()
            time.sleep(0.2)

            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                button2.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")

        
        QApplication.processEvents()

        ###
        FuncMainPY.Monitorizar_Paquetes_(config_entrada0.text(), e, config_entrada1.text())
        ###
    

    def enviar_dhcp():
        FuncGuiPY.ocultar_elemento_(button1)
        FuncGuiPY.ocultar_elemento_(button5)

        res = FuncMainPY.enviar_dhcp_discovery()

        if res == f"{__TR__('NPCAP_NO_INSTALADO')}":
            button4.setStyleSheet("background-color: rgba(128, 0, 0, 0.3); color: white;")
            FuncGuiPY.mostrar_elemento_(button5)
            p_error_(VENTANA15, f"{__TR__('NPCAP_NO_INSTALADO')}", 9)
        
        elif res == f"{__TR__('COMPROBAR_INTERFAZ_EN_CONFIG')}":
            button4.setStyleSheet("background-color: rgba(128, 0, 0, 0.3); color: white;")
            FuncGuiPY.mostrar_elemento_(button1)
            p_error_(VENTANA15, f"{__TR__('COMPROBAR_INTERFAZ_EN_CONFIG')}", 8)

        else:
            button4.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
            QApplication.processEvents()
            time.sleep(0.2)

            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button4.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
        
        QApplication.processEvents()

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA15))
    button1.setProperty("tipo", "button1")

    ############

    button5 = QPushButton(f"{__TR__('INSTALAR_NPCAP')}")
    button5.clicked.connect(lambda: p_principal_(VENTANA15, "IrADependencias"))
    button5.setProperty("tipo", "button1")

    ############

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(check_)
    button0.setProperty("tipo", "button1")

    ############

    button2 = QPushButton(f"{__TR__('EMPEZAR_SIMPLE')}")
    button2.clicked.connect(lambda: check_(1))
    button2.setProperty("tipo", "button1")

    ############

    button4 = QPushButton(f"{__TR__('ENVIAR_PAQ_DHCP')}")
    button4.clicked.connect(enviar_dhcp)
    button4.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA15.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button1)
    button_layout.addWidget(button5)
    button_layout.addWidget(button2)
    button_layout.addWidget(button4)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    FuncGuiPY.ocultar_elemento_(button1)
    FuncGuiPY.ocultar_elemento_(button5)

    ############

    # Establecer el layout al widget principal
    VENTANA15.setLayout(main_layout)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA15.setCentralWidget(widget_principal)

    VENTANA15.show()
    ventana.hide()
    return VENTANA15

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para ver las interfaces de red y su información

def pF_escaneo_dispositivos_(ventana):
    global VENTANA16
    VENTANA16 = QMainWindow()
    VENTANA16.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA16.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)
        

    VENTANA16.setMinimumSize(700, 600)
    VENTANA16.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA16.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_HOSTS_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    ############
    
    label = QLabel(f"{__TR__('RANGO_IP')}")
    config_entrada0 = QLineEdit()

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    config_entrada0.setPlaceholderText(f"{__TR__('RANGO_IP_2')}")

    ############

    main_layout.addLayout(grid_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setText(f"""{__TR__('P_HOSTS_EXPLICACION')}  <span style='color: {FuncMainPY.obt_json_(6)};'>-n -sP -PE -PA21,23,80,3389</span> <span style='color: {FuncMainPY.obt_json_(7)};'>(+ {__TR__('EVASION')})</span>

<br><br> <span style='color: {FuncMainPY.obt_json_(7)}; font-size: 12px;'>{__TR__('DEBES_TENER_NMAP')}</span>""")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA16.resizeEvent = lambda event: adjust_text_edit_height(VENTANA16, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_():
        def parar():
            try: button0.setText(f"{__TR__('EMPEZAR')}")
            except: pass
            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
            
        
        buttonX.setEnabled(False)
        button0.setText(f"{__TR__('ESPERAR')}")
        button0.setStyleSheet(f"background-color: rgba(0, 128, 0, 0.3); color: white;")

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
    
        button0.setEnabled(False)
        actualizar_texto(f"{__TR__('NMAP_CALCULANDO')}")

        texto_poner_ = ""

        if stop_thread:
            return parar()
        
        DESTINO_ = ""
        if config_entrada0.text() != None or config_entrada0.text() != "":
            DESTINO_ = config_entrada0.text()

        RESULTADO_ESCANEO_ = FuncMainPY.NMAP_detectar_dispositivos_(MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS, DESTINO_)

        if stop_thread:
            return parar()

        actualizar_texto(f"{__TR__('NMAP_CALCULANDO')}<br>{__TR__('AILI_ANALIZANDO')}")
        time.sleep(0.3)

        if stop_thread:
            return parar()

        if RESULTADO_ESCANEO_[1] == "BIEN":
            texto_poner_ += f"{__TR__('ESCANEADO_EN')} {RESULTADO_ESCANEO_[3]}s<br><br>"
            texto_poner_ += f"{RESULTADO_ESCANEO_[2]}<br><br><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('DISPOSITIVOS_ACTIVOS')}</span><br><br>"
            texto_poner_ += RESULTADO_ESCANEO_[0]

        elif RESULTADO_ESCANEO_[1] == "DIREC_RED_ERROR":
            texto_poner_ = RESULTADO_ESCANEO_[0]
            button_layout.addWidget(button1)
        
        elif RESULTADO_ESCANEO_[1] == "NMAP_ERR_INSTALADO":
            texto_poner_ = RESULTADO_ESCANEO_[0]
            button_layout.addWidget(button2)
            QApplication.processEvents()
            print("")
        
        elif RESULTADO_ESCANEO_[1] == "ARG_MAL":
            texto_poner_ = RESULTADO_ESCANEO_[0]
            buttonX.setStyleSheet("background-color: rgba(128, 0, 0, 0.3); color: white;")
        
        else:
            texto_poner_ = f"{__TR__('ERROR_DESCONOCIDO')}"
        
        if stop_thread:
            return parar()

        actualizar_texto(texto_poner_)

        button0.setEnabled(True)

        if RESULTADO_ESCANEO_[1] == "BIEN":
            parar()

            try: button0.clicked.disconnect()
            except: pass
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.clicked.connect(lambda: pF_exportar_res_(VENTANA16, texto_poner_, 1))

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            buttonX.setEnabled(True)
            
            return 
        
        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
        buttonX.setEnabled(True)

        parar()

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    ############

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
    MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = "", "", ""
    
    ############

    def conseguir_params_evasion_():
        global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
        EVASION = pF_evasion_ids_(MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

        if EVASION[0] != None and EVASION[1] != None and EVASION[2] != None:
            MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = EVASION[0], EVASION[1], EVASION[2]
            buttonX.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        
        if MAC_FALSIFICADA == None and PUERTO_FALSIFICADO == None and OTRAS_FALSIFICADAS == None or MAC_FALSIFICADA == "" and PUERTO_FALSIFICADO == "" and OTRAS_FALSIFICADAS == "":
            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                buttonX.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")


    buttonX = QPushButton(f"{__TR__('EVASION')}")
    buttonX.clicked.connect(conseguir_params_evasion_)
    buttonX.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA16.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button2 = QPushButton(f"{__TR__('INSTALAR_NMAP')}")
    button2.clicked.connect(lambda: p_principal_(VENTANA16, "IrADependencias"))
    button2.setProperty("tipo", "button1")

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA16))
    button1.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(buttonX)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA16.setCentralWidget(widget_principal)

    VENTANA16.show()
    ventana.hide()
    return VENTANA16

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para escanear puertos

def pF_escaneo_puertos_(ventana):
    global VENTANA17
    VENTANA17 = QMainWindow()
    VENTANA17.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA17.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA17.setMinimumSize(700, 600)
    VENTANA17.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA17.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_PUERTOS_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    grid_layout.setColumnStretch(0, 1)
    grid_layout.setColumnStretch(1, 1)

    ############
    
    label0 = QLabel("IPv4 / DNS:")
    config_entrada0 = QLineEdit()
    config_entrada0.setPlaceholderText(f"127.0.0.1")
    config_entrada0.setText("127.0.0.1")

    label1 = QLabel(f"{__TR__('RUIDO')}")
    config_entrada_ruido = QComboBox()
    config_entrada_ruido.addItems(["0 (Paranoid)", "1", "2", "3 (Normal)", "4", "5 (Insane)"])

    container0 = QWidget()
    h_layout0 = QHBoxLayout(container0)
    h_layout0.setContentsMargins(0, 0, 0, 0)
    h_layout0.addWidget(label0, 1)
    h_layout0.addWidget(label1, 1)

    container1 = QWidget()
    h_layout1 = QHBoxLayout(container1)
    h_layout1.setContentsMargins(0, 0, 0, 0)
    h_layout1.addWidget(config_entrada0, 1)
    h_layout1.addWidget(config_entrada_ruido, 1)

    grid_layout.addWidget(container0, 0, 0)
    grid_layout.addWidget(container1, 1, 0)
    
    ############
    
    label = QLabel(f"{__TR__('PUERTOS_')} (1-65535 ; 1-22,25-50 ; 22): ")
    config_entrada1 = QLineEdit()

    grid_layout.addWidget(label, 0, 1)
    grid_layout.addWidget(config_entrada1, 1, 1)
    
    ############

    config_entrada0.setText("127.0.0.1")
    config_entrada0.setPlaceholderText("127.0.0.1")

    config_entrada1.setText("1-1024")
    config_entrada1.setPlaceholderText("1-1024")

    main_layout.addLayout(grid_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setHtml(f"""{__TR__('P_PUERTOS_EXPLICACION')} <span style='color: {FuncMainPY.obt_json_(6)};'>-sT -sV -T [...]</span> <span style='color: {FuncMainPY.obt_json_(7)};'>(+ {__TR__('EVASION')})</span>

<br><br> <span style='color: {FuncMainPY.obt_json_(7)}; font-size: 12px;'>{__TR__('DEBES_TENER_NMAP')}</span>""")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA17.resizeEvent = lambda event: adjust_text_edit_height(VENTANA17, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def hide_show_():
        VENTANA17.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button2 = QPushButton(f"{__TR__('INSTALAR_NMAP')}")
    button2.clicked.connect(lambda: p_principal_(VENTANA17, "IrADependencias"))
    button2.setProperty("tipo", "button1")

    ############

    def start_thread(e=None):
        global stop_thread, thread
        stop_thread = False
        if e == "raw":
            thread = threading.Thread(target=lambda: camb_("raw"))
        else:
            thread = threading.Thread(target=camb_)
        thread.start()
    
    ############
    
    button0 = QPushButton(f"{__TR__('ESCANEAR')}")
    button0.clicked.connect(lambda: start_thread())
    button0.setProperty("tipo", "button1")

    ############

    button01 = QPushButton(f"{__TR__('ESCANEAR_RAW')}")
    button01.clicked.connect(lambda: start_thread("raw"))
    button01.setProperty("tipo", "button1")

    ############

    global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
    MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = "", "", ""
    
    ############

    def conseguir_params_evasion_():
        global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
        EVASION = pF_evasion_ids_(MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

        if EVASION[0] != None and EVASION[1] != None and EVASION[2] != None:
            MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = EVASION[0], EVASION[1], EVASION[2]
            buttonX.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        
        if MAC_FALSIFICADA == None and PUERTO_FALSIFICADO == None or MAC_FALSIFICADA == "" and PUERTO_FALSIFICADO == "":
            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                buttonX.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")


    buttonX = QPushButton(f"{__TR__('EVASION')}")
    buttonX.clicked.connect(conseguir_params_evasion_)
    buttonX.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button01)
    button_layout.addWidget(buttonX)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA17.setLayout(main_layout)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True
        

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_(e=None):
        def parar():
            if e == "raw":
                button01.setText(f"{__TR__('ESCANEAR_RAW')}")
                with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                    data = json.load(f)
                    button01.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
            else:
                button0.setText(f"{__TR__('ESCANEAR')}")
                with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                    data = json.load(f)
                    button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")      


        buttonX.setEnabled(False)

        if e != "raw":
            button0.setText(f"{__TR__('ESPERAR')}")
            button0.setStyleSheet(f"background-color: rgba(0, 128, 0, 0.3); color: white;")
        else:
            button01.setText(f"{__TR__('ESPERAR')}")
            button01.setStyleSheet(f"background-color: rgba(0, 128, 0, 0.3); color: white;")

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)

        if e != "raw":
            button0.setEnabled(False)
            button01.setEnabled(False)
            button01.setStyleSheet("background-color: rgba(255,255,255,0); border: 0; color: rgba(255,255,255,0);")
            button_layout.removeWidget(button01)
        else:
            button0.setEnabled(False)
            button01.setEnabled(False)
            button0.setStyleSheet("background-color: rgba(255,255,255,0); border: 0; color: rgba(255,255,255,0);")
            button_layout.removeWidget(button0)

        actualizar_texto(f"{__TR__('NMAP_ESCANEA_PUERTOS_ESPERAR')}")

        if stop_thread:
            return parar()

        texto_poner_ = ""

        RESULTADO_ESCANEO_ = FuncMainPY.NMAP_detectar_puertos_(config_entrada0.text(), config_entrada1.text(), e, False, str(config_entrada_ruido.currentText()).split(" ")[0], MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

        if stop_thread:
            return parar()

        if RESULTADO_ESCANEO_[1] == "BIEN":
            texto_poner_ += f"{__TR__('ESCANEADO_EN')} {RESULTADO_ESCANEO_[2]}s<br><br>"
            texto_poner_ += f"{__TR__('PUERTOS_A_ESCANEAR')}: <span style='color: {FuncMainPY.obt_json_(7)};'>{config_entrada1.text()}</span><br><br>"
            texto_poner_ += f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('PUERTOS_ACTIVOS')}</span> '<span style='color: {FuncMainPY.obt_json_(7)};'>{config_entrada0.text()}</span>'<br><br>{RESULTADO_ESCANEO_[0]}"

        elif RESULTADO_ESCANEO_[1] == "NMAP_ERR_INSTALADO":
            texto_poner_ = RESULTADO_ESCANEO_[0]
            button_layout.addWidget(button2)
        
        elif RESULTADO_ESCANEO_[1] == "ARG_MAL":
            texto_poner_ = RESULTADO_ESCANEO_[0]
            buttonX.setStyleSheet("background-color: rgba(128, 0, 0, 0.3); color: white;")

        else:
            texto_poner_ = RESULTADO_ESCANEO_[0]
        
        if stop_thread:
            return parar()

        actualizar_texto(texto_poner_)

        if e != "raw":
            button0.setEnabled(True)

        else: button01.setEnabled(True)

        parar()

        if RESULTADO_ESCANEO_[1] == "BIEN":

            if e != "raw":
                try: button0.clicked.disconnect()
                except: pass
                button0.setText(f"{__TR__('EXPORTAR')}")
                button0.clicked.connect(lambda: pF_exportar_res_(VENTANA17, texto_poner_, 2))

            else:
                try: button01.clicked.disconnect()
                except: pass
                button01.setText(f"{__TR__('EXPORTAR')}")
                button01.clicked.connect(lambda: pF_exportar_res_(VENTANA17, texto_poner_, 2))
            
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            buttonX.setEnabled(True)
            return 
        
        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
        buttonX.setEnabled(True)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA17.setCentralWidget(widget_principal)

    VENTANA17.show()
    ventana.hide()
    return VENTANA17

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para escanear vulnerabilidades

stop_thread, thread = False, None

def pF_escaneo_vulnerabilidades_(ventana):
    global VENTANA18
    VENTANA18 = QMainWindow()
    VENTANA18.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA18.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA18.setMinimumSize(700, 600)
    VENTANA18.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA18.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_VULNERABILIDADES_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    grid_layout.setColumnStretch(0, 1)
    grid_layout.setColumnStretch(1, 1)

    ############
    
    label0 = QLabel("IPv4 / DNS:")
    config_entrada0 = QLineEdit()
    config_entrada0.setPlaceholderText(f"127.0.0.1")
    config_entrada0.setText("127.0.0.1")

    label1 = QLabel(f"{__TR__('RUIDO')}")
    config_entrada_ruido = QComboBox()
    config_entrada_ruido.addItems(["0 (Paranoid)", "1", "2", "3 (Normal)", "4", "5 (Insane)"])

    container0 = QWidget()
    h_layout0 = QHBoxLayout(container0)
    h_layout0.setContentsMargins(0, 0, 0, 0)
    h_layout0.addWidget(label0, 1)
    h_layout0.addWidget(label1, 1)

    container1 = QWidget()
    h_layout1 = QHBoxLayout(container1)
    h_layout1.setContentsMargins(0, 0, 0, 0)
    h_layout1.addWidget(config_entrada0, 1)
    h_layout1.addWidget(config_entrada_ruido, 1)

    grid_layout.addWidget(container0, 0, 0)
    grid_layout.addWidget(container1, 1, 0)

    ############

    central_widget = QWidget()
    VENTANA18.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    label = QLabel(f"{__TR__('CONJUNTO_VULNERABILIDADES')}")

    boton = QPushButton(f"{__TR__('SELECCIONAR')}")
    boton.setProperty("tipo", "button1")

    # Crear el menú
    config_entrada1 = QMenu()

    # Opciones para el menú
    opciones = [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}", "VULN", "DOCKER", "HTTP", "HTTP_Brute", "SSL", "RSTP", "RSTP_Brute", "IMAP", "SMTP", "SMTP_Brute", "MySQL", "POP3", "SMB", "FTP", "DNS", "DNS_Brute", "SSH", "SSH_Brute", "Vulnerabilidad_DoS_IIS", "Vulnerabilidad_DoS_SMTP"]

    # Crear acciones en el menú
    acciones = []
    for texto in opciones:
        accion = QAction(texto)

        if FuncMainPY.obt_json_(8) == f"{__TR__('NO_ACEPTO')}" and texto in ["HTTP_Brute", "SMTP_Brute", "RSTP_Brute", "DNS_Brute", "SSH_Brute", "Vulnerabilidad_DoS_IIS", "Vulnerabilidad_DoS_SMTP"]:
            accion.setCheckable(False)
            accion.setChecked(False)
        else:
            accion.setCheckable(True)
        
        config_entrada1.addAction(accion)
        acciones.append(accion)

    global scripts_seleccionados
    scripts_seleccionados = []

    def actualizar_texto_2_(*args, **kwargs):
        global scripts_seleccionados
        scripts_seleccionados = []

        for accion in acciones:
            if accion.isChecked():
                texto = accion.text()
                if texto == f"{__TR__('_LIMPIAR_')}":
                    for a in acciones:
                        a.setChecked(False)
                    boton.setText(f"{__TR__('SELECCIONAR')}")
                    return
                elif texto == f"{__TR__('_TODOS_')}":
                    for a in acciones:
                        if a.text() != f"{__TR__('_LIMPIAR_')}":
                            a.setChecked(True)
                        if a.text() == f"{__TR__('_TODOS_')}":
                            a.setChecked(False)
                    scripts_seleccionados = [a.text() for a in acciones if a.text() not in [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}"]]
                    boton.setText(f"{__TR__('SELECCIONAR')} ({len(acciones) - 2})")
                    return

        scripts_seleccionados = [a.text() for a in acciones if a.isChecked() and a.text() not in [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}"]]

        if scripts_seleccionados:
            boton.setText(f"{__TR__('SELECCIONAR')} ({len(scripts_seleccionados)})")
        else:
            boton.setText(f"{__TR__('SELECCIONAR')}")

    # Conectar la señal de selección
    for accion in acciones:
        accion.triggered.connect(actualizar_texto_2_)
        if accion.isCheckable():
            accion.toggled.connect(actualizar_texto_2_)

    # Función para mostrar el menú cuando el botón es presionado
    def mostrar_menu():
        config_entrada1.popup(boton.mapToGlobal(boton.rect().bottomLeft()))

    def menu_oculto():
        QTimer.singleShot(50, actualizar_texto_2_)  # Da tiempo a que .isChecked() se actualice

    config_entrada1.aboutToHide.connect(menu_oculto)

    # Conectar la acción del botón al menú
    boton.clicked.connect(mostrar_menu)

    # Agregar los widgets al layout
    layout.addWidget(label)
    layout.addWidget(boton)

    ############

    def obtener_scripts_():
        lista_total = []

        for i in scripts_seleccionados:
            if i == "DOCKER":
                for ii in ["docker-version"]:
                    lista_total.append(ii)
            if i == "VULN":
                for ii in ["vuln"]:
                    lista_total.append(ii)
            if i == "HTTP":
                for ii in ["http-title","http-headers","http-methods", "https-redirect", "ip-https-discover", "http-enum","http-vuln-cve2006-3392","http-auth","http-robots.txt","http-server-header","http-php-version","http-wordpress-enum","http-security-headers","http-feed","http-ls","http-stored-xss","http-backup-finder","http-cakephp-version","http-comments-displayer","http-config-backup","http-cookie-flags","http-form-fuzzer","http-generator","http-git","http-gitweb-projects-enum","http-google-malware","http-useragent-tester","http-userdir-enum","http-vhosts","http-vuln-cve2009-3960","http-vuln-cve2010-0738","http-vuln-cve2010-2861","http-vuln-cve2011-3192","http-vuln-cve2011-3368","http-vuln-cve2015-1427","http-vuln-cve2015-1635","http-vuln-cve2017-1001000","http-vuln-cve2017-5638","http-vuln-cve2017-5689","http-vuln-cve2017-8917","http-waf-detect","http-waf-fingerprint","http-webdav-scan"]:
                    lista_total.append(ii)
            if i == "HTTP_Brute":
                for ii in ["http-brute","http-form-brute","http-iis-short-name-brute"]:
                    lista_total.append(ii)
            if i == "RSTP":
                for ii in ["rtsp-methods"]:
                    lista_total.append(ii)
            if i == "RSTP_Brute":
                for ii in ["rtsp-url-brute"]:
                    lista_total.append(ii)
            if i == "SSL":
                for ii in ["ssl-ccs-injection", "ssl-cert", "ssl-cert-intaddr", "ssl-date", "ssl-dh-params", "ssl-enum-ciphers", "ssl-heartbleed", "ssl-known-key", "sslv2", "ssl-poodle", "sslv2-drown"]:
                    lista_total.append(ii)
            if i == "IMAP":
                for ii in ["imap-capabilities", "imap-ntlm-info", "imap-user-enum", "imap-vuln-cve2007-5195", "imap-vuln-cve2009-3555"]:
                    lista_total.append(ii)
            if i == "SMTP":
                for ii in ["smtp-commands", "smtp-enum-users", "smtp-ntlm-info", "smtp-open-relay", "smtp-strangeport", "smtp-vuln-cve2010-4344", "smtp-vuln-cve2011-1720", "smtp-vuln-cve2011-1764"]:
                    lista_total.append(ii)
            if i == "SMTP_Brute":
                for ii in ["smtp-brute"]:
                    lista_total.append(ii)
            if i == "MySQL":
                for ii in ["mysql-info", "mysql-dump-hash", "mysql-empty-password", "mysql-query", "mysql-root-login", "mysql-users", "mysql-version", "mysql-variables", "mysql-ssl-ccs-injection"]:
                    lista_total.append(ii)
            if i == "POP3":
                for ii in ["pop3-capabilities", "pop3-ntlm-info", "pop3-user-enum", "pop3-vuln-cve2007-5195", "pop3-vuln-cve2009-3555"]:
                    lista_total.append(ii)
            if i == "SMB":
                for ii in ["smb-os-fingerprint", "smb-ls", "smb-enum-shares", "smb-enum-users", "smb-vuln-ms17-010", "smb-vuln-ms08-067", "smb-vuln-cve2009-3103", "smb-vuln-cve2017-7494", "smb-vuln-cve2020-0796"]:
                    lista_total.append(ii)
            if i == "FTP":
                for ii in ["ftp-anon", "ftp-bounce", "ftp-syst", "ftp-vsftpd-backdoor", "ftp-ntlm-info", "ftp-ssl", "ftp-enum"]:
                    lista_total.append(ii)
            if i == "DNS":
                for ii in ["dns-cache-snooping", "dns-zone-transfer", "dns-nsid", "dns-unknown-type", "dns-recursion", "dns-fingerprint", "dns-service-discovery", "dns-tcp"]:
                    lista_total.append(ii)
            if i == "DNS_Brute":
                for ii in ["dns-brute"]:
                    lista_total.append(ii)
            if i == "SSH":
                for ii in ["ssh-auth-methods", "ssh-hostkey", "ssh-publickey-acceptance", "ssh2-enum-algos", "sshv1"]:
                    lista_total.append(ii)
            if i == "SSH_Brute":
                for ii in ["ssh-brute"]:
                    lista_total.append(ii)
            if i == "Vulnerabilidad_DoS_IIS":
                for ii in ["dos-ms10-065"]:
                    lista_total.append(ii)
            if i == "Vulnerabilidad_DoS_SMTP":
                for ii in ["snmpdos"]:
                    lista_total.append(ii)
        
        if lista_total == []: lista_total.append("default")
        elif "--Limpiar--" in lista_total or "--Clean--" in lista_total or "--Limpar--" in lista_total: lista_total.remove(f"{__TR__('_LIMPIAR_')}")
        print(lista_total)
        return lista_total

    ############

    grid_layout.addWidget(label, 0, 1)
    grid_layout.addWidget(boton, 1, 1)

    main_layout.addLayout(grid_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setText(f"""{__TR__('P_VULNERABILIDADES_EXPLICACION')}<br><br>{__TR__('IP_LEGAL_SCANME')}
<br><br> <span style='color: {FuncMainPY.obt_json_(7)}; font-size: 12px;'>{__TR__('DEBES_TENER_NMAP')}</span>""")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA18.resizeEvent = lambda event: adjust_text_edit_height(VENTANA18, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def hide_show_():
        VENTANA18.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button2 = QPushButton(f"{__TR__('INSTALAR_NMAP')}")
    button2.clicked.connect(lambda: p_principal_(VENTANA18, "IrADependencias"))
    button2.setProperty("tipo", "button1")

    ############

    def start_thread():
        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
    
        button0.setEnabled(False)
        button1.setEnabled(True)
        button1.setText(f"{__TR__('PARAR_ESPERAR')}")
        button2.setEnabled(False)
        button3.setEnabled(False)

        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    ############

    global FIN_FINAL; FIN_FINAL = False

    ############

    def stop_thread_func():
        global stop_thread
        stop_thread = True

        FuncGuiPY.ocultar_elemento_(button1)
        FuncGuiPY.ocultar_elemento_(button2)
        FuncGuiPY.ocultar_elemento_(buttonX2)
        print("")
        QApplication.processEvents()

        button1.setEnabled(False)
        with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                button1.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
        
        print("")
        button0.setEnabled(True)
        button2.setEnabled(True)
        button3.setEnabled(True)
        buttonX2.setEnabled(True)
        print("")

    ############

    button0 = QPushButton(f"{__TR__('ESCANEAR')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
    MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = "", "", ""

    ############

    def conseguir_params_evasion_():
        global MAC_FALSIFICADA; global PUERTO_FALSIFICADO; global OTRAS_FALSIFICADAS
        EVASION = pF_evasion_ids_(MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

        if EVASION[0] != None and EVASION[1] != None and EVASION[2] != None:
            MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS = EVASION[0], EVASION[1], EVASION[2]
            button2.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        
        if MAC_FALSIFICADA == None and PUERTO_FALSIFICADO == None or MAC_FALSIFICADA == "" and PUERTO_FALSIFICADO == "":
            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button2.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")


    button2 = QPushButton(f"{__TR__('EVASION')}")
    button2.clicked.connect(conseguir_params_evasion_)
    button2.setProperty("tipo", "button1")

    ############

    global OPCIONES_SELECCIONADAS
    OPCIONES_SELECCIONADAS = []

    def conseguir_partes_a_evitar_():
        global OPCIONES_SELECCIONADAS
        opc = pF_evitar_partes_()

        if opc[0] != None: # 0 es una lista
            buttonX2.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
            OPCIONES_SELECCIONADAS = opc[0]

        else:
            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                buttonX2.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")


    buttonX2 = QPushButton(f"{__TR__('P_EVITAR_PARTES')}")
    buttonX2.clicked.connect(conseguir_partes_a_evitar_)
    buttonX2.setProperty("tipo", "button1")

    ############

    button1 = QPushButton(f"{__TR__('PARAR')}")
    button1.clicked.connect(stop_thread_func)
    button1.setEnabled(False)
    button1.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button2)
    button_layout.addWidget(button1)
    button_layout.addWidget(buttonX2)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA18.setLayout(main_layout)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()
    updater.signal_actualizar.connect(lambda html: (
        text_edit.setHtml(html),
        text_edit.moveCursor(QTextCursor.End)
    ))

    def actualizar_texto(html):
        try:
            updater.signal_actualizar.emit(html)
        except:
            pass

    ############

    def camb_(e=None):
        SCRIPTS = obtener_scripts_()

        button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        button0.setText(f"{__TR__('ESPERAR')}")
        button1.setEnabled(True)
        buttonX2.setEnabled(False)

        ############

        def ESCANEO_DETENIDO_POR_USUARIO(TEXTO):
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            try:
                actualizar_texto(TEXTO)
            except:
                pass

            with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                data = json.load(f)
                button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                button1.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")

            if FIN_FINAL == False:
                button0.setEnabled(True)

                with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                    data = json.load(f)
                    button1.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                
                button1.setText(f"{__TR__('PARAR')}")
                button3.setEnabled(True)
                buttonX2.setEnabled(True)
        
        ############

        def no_tener_nmap_():
            button0.setText(f"{__TR__('INSTALAR_NMAP')}")
            button0.setEnabled(True)
            button0.clicked.disconnect()
            button0.clicked.connect(lambda: p_principal_(VENTANA18, "IrADependencias"))

        ############

        global stop_thread

        while not stop_thread:
            ############
            texto_poner_ = ""
            ############

            try:
                FuncMainPY.ocultar_consola_en_scan()
                PRUEBA = nmap.PortScanner()
            except:
                FuncMainPY.ERR_REG_(f"[camb_] Nmap no está instalado.\n\n")

                actualizar_texto(f"{__TR__('NMAP_NO_INSTALADO_')}")
                no_tener_nmap_()

                button2.setEnabled(True)

                with open(FuncMainPY.obtener_ruta_config(), "r") as f:
                    data = json.load(f)
                    button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
                    button1.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")

                return stop_thread_func()

            ############

            if f"{__TR__('INFO_EQUIPO_EV')}" in OPCIONES_SELECCIONADAS:

                actualizar_texto(f"{__TR__('DETECTNADO_PARAMS')}")

                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br><br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

                RESULTADO_INFO_HOST = FuncMainPY.NMAP_detectar_parametros_(config_entrada0.text(), str(config_entrada_ruido.currentText()).split(" ")[0], MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

                if RESULTADO_INFO_HOST[1] == "ARG_MAL":
                    texto_poner_ = RESULTADO_INFO_HOST[0]
                    actualizar_texto(texto_poner_)
                    
                    stop_thread_func()
                    button1.setText(f"{__TR__('PARAR')}")
                    break

                texto_poner_ += f"""<span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('INFO_EQUIPO')}</span>
                <br>
                <ul>
                    <li>Hostname: <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[0]}</span></li>
                    <li>{__TR__('SO')} <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[1]}</span></li>
                    <li>{__TR__('PRECISION')} <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[2]}</span></li>
                    <li>{__TR__('ESTADO')} <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[4]}</span></li>
                    {f''' <li>{__TR__('UP-TIME')} <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[5]}</span></li> ''' if RESULTADO_INFO_HOST[5] != '' else ''}
                    {f''' <li>{__TR__('LAST-BOOT')} <span style='color: {FuncMainPY.obt_json_(7)};'>{RESULTADO_INFO_HOST[6]}</span></li> ''' if RESULTADO_INFO_HOST[6] != '' else ''}
                </ul>
                ({__TR__('ESCANEADO_EN')} {RESULTADO_INFO_HOST[3]}s)
                <br>"""

                texto_poner_ += "_"*50 + "<br><br>"
                actualizar_texto(texto_poner_)

                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

            ############

            if f"{__TR__('PUERTOS_TCP_EV')}" in OPCIONES_SELECCIONADAS:

                texto_poner_2 = texto_poner_ + f"{__TR__('ESCANEANDO_PUERTOS_IMPORTANTES')}"
                actualizar_texto(texto_poner_2)

                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br><br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

                puertos = "19,20,21,22,23,25,42,80,88,110,115,135,139,143,179,389,443,445,465,554,587,636,873,990,993,995,1080,1194,1352,1433,1521,1645,1646,1723,2049,2082,2083,2483,2484,24800,27015,27017,27018,27019,27020,28017,3000,3128,3306,3389,5000,5001,5004,5005,50070,50075,50090,5432,5601,5800,5900,5984,6000,6001,61616,6379,64738,6667,7000,8000,8008,8080,8081,8082,8443,8888,9000,9042,9100,9200,9201,10000,10050,10051,1080,11211,11214,15672,25565,27015,49152,49153"
                RESULTADO_ESCANEO_ = FuncMainPY.NMAP_detectar_puertos_(config_entrada0.text(), puertos, e, False, str(config_entrada_ruido.currentText()).split(" ")[0], MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

                if RESULTADO_ESCANEO_[1] == "NMAP_ERR_INSTALADO":
                    button_layout.addWidget(button2)
                    button1.setText(f"{__TR__('PARAR')}")

                    texto_poner_ += RESULTADO_ESCANEO_[0]
                    actualizar_texto(texto_poner_)
                    stop_thread_func()
                    no_tener_nmap_()
                    break

                if RESULTADO_ESCANEO_[1] == "ARG_MAL":
                    stop_thread_func()
                    button1.setText(f"{__TR__('PARAR')}")

                    texto_poner_ += RESULTADO_ESCANEO_[0]
                    actualizar_texto(texto_poner_)
                    break 

                texto_poner_ += f"<span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('PUERTOS_IMPORTANTES_ACTIVOS')}</span>:<br><br>{RESULTADO_ESCANEO_[0]}<br>({__TR__('ESCANEADO_EN')} {RESULTADO_ESCANEO_[2]}s)<br>"
                texto_poner_ += "_"*50 + "<br><br>"
                actualizar_texto(texto_poner_)

                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

            ############

            if f"{__TR__('PUERTOS_UDP_EV')}" in OPCIONES_SELECCIONADAS:

                texto_poner_2 = texto_poner_ + f"{__TR__('ESCANEANDO_PUERTOS_IMPORTANTES_2')}"
                actualizar_texto(texto_poner_2)
                
                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br><br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

                puertos = "53,67,68,69,123,137,138,161,162,500,514,520,623,1434,1900,4500,5353,1701,33434"
                RESULTADO_ESCANEO_ = FuncMainPY.NMAP_detectar_puertos_(config_entrada0.text(), puertos, e, True, str(config_entrada_ruido.currentText()).split(" ")[0], MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

                if RESULTADO_ESCANEO_[1] == "ARG_MAL":
                    stop_thread_func()
                    button1.setText(f"{__TR__('PARAR')}")

                    texto_poner_ += RESULTADO_ESCANEO_[0]
                    actualizar_texto(texto_poner_)
                    break 

                texto_poner_ += f"<span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('PUERTOS_IMPORTANTES_ACTIVOS_2')}</span>:<br><br>{RESULTADO_ESCANEO_[0]}<br>({__TR__('ESCANEADO_EN')} {RESULTADO_ESCANEO_[2]}s)<br>"
                texto_poner_ += "_"*50 + "<br><br>"
                actualizar_texto(texto_poner_)
                
                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

            ############

            for i in SCRIPTS:

                texto_poner_2 = texto_poner_ + f"{__TR__('ESCANEANDO_CON_SCRIPT')}'{i}'..."
                actualizar_texto(texto_poner_2)

                if stop_thread:
                    ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br><br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")
                    break

                RESULTADO_SCRIPT_1_ = FuncMainPY.NMAP_detectar_scripts_(config_entrada0.text(), i, str(config_entrada_ruido.currentText()).split(" ")[0], MAC_FALSIFICADA, PUERTO_FALSIFICADO, OTRAS_FALSIFICADAS)

                texto_poner_ += f"<span style='color:{FuncMainPY.obt_json_(6)};'>{__TR__('RESULTADO_SCRIPT')}'{i}'</span> {RESULTADO_SCRIPT_1_[0]}<br><br>({__TR__('ESCANEADO_EN')} {RESULTADO_SCRIPT_1_[2]}s)<br>"

                texto_poner_ += "_"*50 + "<br><br>"
                actualizar_texto(texto_poner_)

            ############ TEXTO FINAL REPORTE

            texto_poner_ += f"{__TR__('ESCANEO_FINALIZADO')} - AILI-SS"
            actualizar_texto(texto_poner_)

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            
            if stop_thread:
                ESCANEO_DETENIDO_POR_USUARIO(texto_poner_ + "<br><br>" + f"{__TR__('ESCANEO_DETENIDO_POR_USUARIO')}")

            ############ EXPORTAR RESULTADOS

            button0.setEnabled(True)
            try: button0.clicked.disconnect()
            except: pass
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.clicked.connect(lambda: pF_exportar_res_(VENTANA18, texto_poner_, 3))
            print("")
            QApplication.processEvents()

            button1.setStyleSheet("background-color: rgba(255,255,255,0); border: 0; color: rgba(255,255,255,0);")
            button_layout.removeWidget(button1)

            global FIN_FINAL; FIN_FINAL = True

            ############ CERRAR FUNCION

            stop_thread_func()
            button1.setText(f"{__TR__('PARAR')}")
            break
    ############
    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA18.setCentralWidget(widget_principal)

    VENTANA18.show()
    ventana.hide()
    return VENTANA18

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular el direccionamiento IP

def pF_calcular_direcciones_(ventana=None, IP=None, MASC=None, DIREC_RED=None, Fue_de_calcular_lista=False):
    global VENTANA19
    VENTANA19 = QMainWindow()
    VENTANA19.setFixedSize(750, 500)
    FuncGuiPY.centrar_ventana_(VENTANA19)
    VENTANA19.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA19.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_DIRECCIONAMIENTO_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    GRID = QGridLayout()

    GRID.setColumnStretch(0, 1)
    GRID.setColumnStretch(1, 1)

    ############

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label1 = QLabel(f"{__TR__('BITS_RED_HOST')}")
    label2 = QLabel("Hosts:")

    label_layout.addWidget(label1)
    label_layout.addWidget(label2)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 9, 1)

    ############
    ############

    label_ip = QLabel(f"IPv4:")
    config_entrada0 = QLineEdit()
    config_entrada0.setPlaceholderText("127.0.0.1")
    if IP != None:
        config_entrada0.setText(IP)
    
    GRID.addWidget(label_ip, 0, 0)
    GRID.addWidget(config_entrada0, 1, 0)

    ############
    
    label_entry_mascara = QLabel(f"{__TR__('MASCARA_CON_EJ')}")
    config_entrada01 = QLineEdit()
    config_entrada01.setPlaceholderText("255.255.255.0")
    if MASC != None:
        config_entrada01.setText(MASC)
    
    GRID.addWidget(label_entry_mascara, 0, 1)
    GRID.addWidget(config_entrada01, 1, 1)

    ############

    GRID.addWidget(QLabel(f""), 2, 0, 1, 2)

    ############
    
    label = QLabel(f"{__TR__('MASCARA_BIN')}")
    GRID.addWidget(label, 3, 0)

    label_ensenar_mascara = QLabel("")
    label_ensenar_mascara.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_ensenar_mascara, 4, 0)

    ############
    
    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label_poner_que_otra_mascara = QLabel(f"{__TR__('MASCARA_INVERSA')}")
    label_poner_mascara_wildcard = QLabel(f"{__TR__('MASCARA_WILDCARD')}")

    label_layout.addWidget(label_poner_que_otra_mascara)
    label_layout.addWidget(label_poner_mascara_wildcard)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 3, 1)

    # ---

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label_ensenar_mascara_cidr_dot = QLabel("")
    label_ensenar_mascara_cidr_dot.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    label_ensenar_mascara_wildcard = QLabel("")
    label_ensenar_mascara_wildcard.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")

    label_layout.addWidget(label_ensenar_mascara_cidr_dot)
    label_layout.addWidget(label_ensenar_mascara_wildcard)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 4, 1)

    ############

    GRID.addWidget(QLabel(f""), 5, 0, 1, 2)

    ############

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label1 = QLabel(f"{__TR__('DIREC_RED_2')}")
    label2 = QLabel(f"{__TR__('DIREC_DIF_2')}")

    label_layout.addWidget(label1)
    label_layout.addWidget(label2)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 6, 0)

    ############

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label_direc_red = QLabel("")
    label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    label_direc_dif = QLabel("")
    label_direc_dif.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")

    label_layout.addWidget(label_direc_red)
    label_layout.addWidget(label_direc_dif)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 7, 0)

    ############ zzz

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label_arpa = QLabel(f"<span style='color: {FuncMainPY.obt_json_(7)};'>(__)</span>.in-addr.arpa: ")
    label2 = QLabel(f"{__TR__('CLASE_IP')}")

    label_layout.addWidget(label_arpa)
    label_layout.addWidget(label2)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 6, 1)

    ############

    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label_ensenar_in_addr_arpa = QLabel("")
    label_ensenar_in_addr_arpa.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    label_ensenar_clase_ip = QLabel("")
    label_ensenar_clase_ip.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")

    label_layout.addWidget(label_ensenar_in_addr_arpa)
    label_layout.addWidget(label_ensenar_clase_ip)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 7, 1)

    ############

    GRID.addWidget(QLabel(f""), 8, 0, 1, 2)

    ############
    
    label = QLabel(f"{__TR__('PARTE_RED_HOST')}")
    GRID.addWidget(label, 9, 0)

    label_ensenar_parte_red_y_host = QLabel("")
    label_ensenar_parte_red_y_host.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_ensenar_parte_red_y_host, 10, 0)

    ############
    
    label_container = QWidget()
    label_layout = QHBoxLayout()
    label_layout.setContentsMargins(0, 0, 0, 0)
    label_layout.setSpacing(10)

    label1 = QLabel(f"{__TR__('BITS_RED_HOST')}")
    label2 = QLabel("Hosts:")

    label_layout.addWidget(label1)
    label_layout.addWidget(label2)

    label_container.setLayout(label_layout)
    GRID.addWidget(label_container, 9, 1)

    # === Valores (fila 10, columna 1) ===
    value_container = QWidget()
    value_layout = QHBoxLayout()
    value_layout.setContentsMargins(0, 0, 0, 0)
    value_layout.setSpacing(10)

    bits_red_y_host = QLabel("")
    bits_red_y_host.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")

    formula_host = QLabel("")
    formula_host.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")

    value_layout.addWidget(bits_red_y_host)
    value_layout.addWidget(formula_host)

    value_container.setLayout(value_layout)
    GRID.addWidget(value_container, 10, 1)

    ############

    main_layout.addLayout(GRID)

    ############

    def calcular_direcciones_(x=None):

        ############
        ############

        def cidr_a_mascara(cidr):
            try:
                red = ipaddress.IPv4Network("0.0.0.0" + cidr, strict=False)
                return str(red.netmask)
            except:
                return ""
        
        ############

        def mascara_a_cidr(mascara):
            red = ipaddress.IPv4Network(f"0.0.0.0/{mascara}", strict=False)
            return f"/{red.prefixlen}"
        
        ############
        ############

        mascara, mascara_punteada = "", ""

        if config_entrada01.text() != "":

            if str(config_entrada01.text()).__contains__("."): # DOT A CIDR
                mascara = config_entrada01.text()
                mascara_punteada = config_entrada01.text()

                label_poner_que_otra_mascara.setText(f"{__TR__('MASCARA_CON_2')}")
                label_entry_mascara.setText(f"{__TR__('MASCARA_CON_1')}")

                try: label_ensenar_mascara_cidr_dot.setText(str(mascara_a_cidr(config_entrada01.text())))
                except: label_ensenar_mascara_cidr_dot.setText("")
            
            else: # CIDR A DOT
                mascara = cidr_a_mascara(f"{'' if config_entrada01.text().startswith('/') else '/'}{config_entrada01.text()}")
                mascara_punteada = mascara

                label_poner_que_otra_mascara.setText(f"{__TR__('MASCARA_CON_1')}")
                label_entry_mascara.setText(f"{__TR__('MASCARA_CON_2')}")

                try: label_ensenar_mascara_cidr_dot.setText(mascara)
                except: label_ensenar_mascara_cidr_dot.setText("")

        else:
            label_poner_que_otra_mascara.setText(f"{__TR__('MASCARA_INVERSA')}")
            label_ensenar_mascara_cidr_dot.setText(f"{__TR__('MASCARA_INVALIDA')}")
            label_entry_mascara.setText(f"{__TR__('MASCARA_CON_EJ')}")
            label2.setText("Hosts:")
            formula_host.setText("")
        
        ############
        ############

        if config_entrada01.text() in ["", None]:
            config_entrada01.setPlaceholderText("255.255.255.0 • /24")
        else:
            config_entrada01.setPlaceholderText("")
        
        ############

        label_ip.setText(f"IPv4 - <span style='color: {FuncMainPY.obt_json_(7)};'>{FuncMainPY.tipo_ip_(config_entrada0.text())}</span>:")

        label_ensenar_clase_ip.setText(str(FuncMainPY.calcular_clase_IP(config_entrada0.text())))
        
        label_ensenar_in_addr_arpa.setText(str(FuncMainPY.invertir_ip_(config_entrada0.text())))

        label_ensenar_mascara_wildcard.setText(str(FuncMainPY.calcular_mascara_wildcard_(mascara_punteada)))

        ############

        DIREC_RED = FuncMainPY.CALCULAR_DIRECCION_RED__(None, config_entrada0.text(), mascara, True)
        label_direc_red.setText(DIREC_RED)

        DIREC_DIF = FuncMainPY.CALCULAR_DIRECCION_DIFUSION__(None, config_entrada0.text(), mascara, True)
        label_direc_dif.setText(DIREC_DIF)

        LABEL_PARTES = FuncMainPY.CALCULAR_PARTES__(None, config_entrada0.text(), str(mascara), True)
        label_ensenar_parte_red_y_host.setText(str(LABEL_PARTES))

        LABEL_MASCARA = FuncMainPY.CALCULAR_MASCARA_BINARIA__(str(mascara), True)
        label_ensenar_mascara.setText(str(LABEL_MASCARA))

        BITS_IP = FuncMainPY.CALCULAR_BITS__(str(mascara))
        if BITS_IP == "Error":
            bits_red_y_host.setText("")
        else:
            bits_red_y_host.setText(f"<span style='color: {FuncMainPY.obt_json_(6)}'>{BITS_IP[0]}</span> / <span style='color: {FuncMainPY.obt_json_(7)}'>{BITS_IP[1]}</span> (Max. 32)")
        
        if config_entrada01.text() != "":
            label2.setText(f"Hosts (2<sup><span style='color: {FuncMainPY.obt_json_(7)}'>{BITS_IP[1]}</span></sup> - 2):")

        try: formula_host.setText(f"{(2 ** int(BITS_IP[1])) - 2}")
        except: formula_host.setText("")

        ############
        ############

        if x != None:
            VENTANA19.timer.stop()
            VENTANA19.destroy()
            return pF_hosts_red_disponibles_(VENTANA19, config_entrada0.text(), mascara)

        ############
        ############
    
    VENTANA19.timer = QTimer()
    VENTANA19.timer.timeout.connect(calcular_direcciones_)
    VENTANA19.timer.start(1000)

    ############

    def abrir_host_por_mascara_():
        def cidr_a_mascara(cidr):
            try:
                red = ipaddress.IPv4Network("0.0.0.0" + cidr, strict=False)
                return str(red.netmask)
            except:
                return ""
    
        ###########

        ESTILOS = """<style>
            * {
                font-family: Arial;
                background-color: FuncMainPY.obt_json_(0);
                color: FuncMainPY.obt_json_(2);
            }
            th {
                color: FuncMainPY.obt_json_(6);
                padding: 0 20px 10px 20px;
            }
            td:hover {
                background-color: #555 !important;
                color: white;
            }
        </style>"""

        ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(0)", FuncMainPY.obt_json_(0))
        ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(2)", FuncMainPY.obt_json_(2))
        ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(6)", FuncMainPY.obt_json_(6))

        ###########

        with open(os.path.join(os.path.abspath(conseguir_RUTA_DIR_USUARIO_()), "MaskHosts.html"), "w", encoding="UTF-8") as file:

            tabla = f"""<tr>
                \n<th>{__TR__('MASCARA_CON_2').replace(': ', '')}</th>
                \n<th>{__TR__('MASCARA_CON_1').replace(': ', '')}</th>
                \n<th>HOSTS - Total</th>
                \n<th>HOSTS - Usable</th>
            \n</tr>"""

            ###########

            for i in range(33): # es 32
                tabla += f"""\n<tr>
                    \n<td style='border: 1px solid gray; padding: 5px;'>/{i}</td>
                    \n<td style='border: 1px solid gray; padding: 5px;'>{cidr_a_mascara(f"/{i}")}</td>
                    \n<td style='border: 1px solid gray; padding: 5px;'>{2 ** (32-i):,}</td>
                    \n<td style='border: 1px solid gray; padding: 5px;'>{0 if i == 32 else 2 ** (32-i) - 2:,}</td>
                \n</tr>"""

            ###########
            
            html = f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MASK - HOSTS</title>
        {ESTILOS}
    </head>

    <body style='font-size: 20px;'>
        <p><a target='_bank' href='https://aili-ss.pages.dev' style='color: {FuncMainPY.obt_json_(6)};'>AILI-SS</a> • {FuncMainPY.obt_json_('IDIOMA')} • {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}</p>
        <br>
        <table>
        {tabla}
        </table>
    </body>
</html>"""
            ###########

            file.write(html)
            webbrowser.open(os.path.join(os.path.abspath(conseguir_RUTA_DIR_USUARIO_()), "MaskHosts.html"))

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    # Botones
    def volver_():
        def hide_show_():
            if Fue_de_calcular_lista:
                return p_principal_(VENTANA19, "IrAHerramientasRed")
            VENTANA19.close()
            ventana.show()

        VENTANA19.timer.stop()
        hide_show_()
    
    ############

    button2 = QPushButton(f"{__TR__('MAX_HOSTS')}")
    button2.clicked.connect(lambda: calcular_direcciones_(1))
    button2.setProperty("tipo", "button1")

    button2_1 = QPushButton(f"{__TR__('MAPA_MASK_HOST')}")
    button2_1.clicked.connect(abrir_host_por_mascara_)
    button2_1.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(volver_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button2_1)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA19.setCentralWidget(widget_principal)

    VENTANA19.show()
    ventana.hide()
    return VENTANA19


####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular el direccionamiento IP

def pF_ping_grafica_(ventana=None):
    global VENTANA20
    VENTANA20 = QMainWindow()
    VENTANA20.setFixedSize(690, 300)
    FuncGuiPY.centrar_ventana_(VENTANA20)
    VENTANA20.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA20.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_PING_GRAFICA_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    label = QLabel(f"{__TR__('IP_DNS_HOST')}")
    main_layout.addWidget(label)
    config_entrada0 = QLineEdit()
    config_entrada0.setText("cloudflare.com")
    config_entrada0.setPlaceholderText("aili-ss.pages.dev")
    main_layout.addWidget(config_entrada0)

    ############
    
    label = QLabel(f"{__TR__('PINGS_A_REALIZAR')}")
    main_layout.addWidget(label)
    config_entrada1 = QLineEdit()
    config_entrada1.setText("5")
    config_entrada1.setPlaceholderText("00")
    main_layout.addWidget(config_entrada1)

    ############

    text_edit_RESULTADO = QTextEdit()
    text_edit_RESULTADO.setReadOnly(True)
    text_edit_RESULTADO.setObjectName("BlogText")
    text_edit_RESULTADO.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA20.resizeEvent = lambda event: adjust_text_edit_height(VENTANA20, text_edit_RESULTADO)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.40))
    
    main_layout.addWidget(text_edit_RESULTADO)
    FuncGuiPY.ocultar_elemento_(text_edit_RESULTADO)

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def empezar_():
        def func_pr_():
            CANTIDAD, OBJETIVO = config_entrada1.text(), config_entrada0.text()

            # HACER PING
            indices = []
            tiempos = []
            RESULTADO_STR = ""

            VENTANA20.setFixedSize(690, 510)
            FuncGuiPY.centrar_ventana_(VENTANA20)
            FuncGuiPY.mostrar_elemento_(text_edit_RESULTADO)

            for i in range(int(CANTIDAD)):
                t = ping3.ping(OBJETIVO)
                indices.append(i)
                tiempos.append(t)
                RESULTADO_STR += f"{i} - {t} ms{'<br>' if i != (int(CANTIDAD) - 1) else ''}"

                text_edit_RESULTADO.setText(RESULTADO_STR)
                QApplication.processEvents()

            RESULTADO = (indices, tiempos)

            # GRÁFICO
            FuncMainPY.PING_generar_gráfico(OBJETIVO, CANTIDAD, RESULTADO)

        QTimer.singleShot(50, func_pr_)

        button2.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")

    ############

    # Botones
    button2 = QPushButton(f"{__TR__('GENERAR_GRAFICO')}")
    button2.clicked.connect(empezar_)
    button2.setProperty("tipo", "button1")

    def hide_show_():
        VENTANA20.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA20.setCentralWidget(widget_principal)

    VENTANA20.show()
    ventana.hide()
    return VENTANA20

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para obtener tiempos de respuesta

def pF_tiempos_respuesta(ventana):
    global VENTANA21
    VENTANA21 = QMainWindow()
    VENTANA21.timer = QTimer()

    VENTANA21.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA21)
    VENTANA21.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA21.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_TIEMPOS_RESPUESTA_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    ############
    
    label = QLabel(f"{__TR__('IP_DNS_HOST')}")
    config_entrada0 = QLineEdit()

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    config_entrada0.setText("cloudflare.com")
    config_entrada0.setPlaceholderText("aili-ss.pages.dev")

    ############

    main_layout.addLayout(grid_layout)
    
    ############

    text_edit = QTextEdit()
    text_edit.setHtml(f"{__TR__('RELLENAR_HOST_LUEGO_OBTENER')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA21.resizeEvent = lambda event: adjust_text_edit_height(VENTANA21, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA21))
    button1.setProperty("tipo", "button1")

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_():
        try: button0.clicked.disconnect()
        except: pass
        button0.clicked.connect(camb_)

        button0.setEnabled(False)
        button0.setText(f"{__TR__('ESPERAR')}")
        button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        QApplication.processEvents()

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
    
        ##

        HOST = config_entrada0.text()

        respuesta = f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('PING_HACIA_HOST')} '{HOST}'</span>"
        actualizar_texto(respuesta + f"<br><br>{__TR__('PEALIZAR_PING3')}")

        if stop_thread: return

        try:
            ping = round(ping3.ping(HOST, unit="ms"), 4)
            respuesta += f"<br><br>Ping: <span style='color: {FuncMainPY.obt_json_(7)};'>{ping} ms</span>"
        except:
            FuncMainPY.ERR_REG_(f"[camb_] No se puedo hacer ping a {HOST}.\n\n")

            respuesta += f"<br><br>Ping: <span style='color: {FuncMainPY.obt_json_(7)};'>0.00 ms</span>"

        ##

        random_dns = random.choice(["google.com", "cloudflare.com", "marca.es", "amazon.com", "whatsapp.com", "steamcommunity.com", "drive.google.com", "github.com", "patreon.com", "render.com", "gmail.com", "mega.nz", "discord.com", "alienwarearena.com", "dell.com", "msi.com", "asus.com", "vercel.com", "wireshark.org", "nmap.org", "npcap.org"])
        actualizar_texto(respuesta + f"<br><br>{__TR__('RESOLVIENDO_DNS_')} '{random_dns}'...")
        respuesta += f"<br><br><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('RESOLUCIÓN_DNS')} - '{random_dns}' ({__TR__('ALEATORIO')})</span>"

        try:
            if stop_thread: return

            while True:
                global dns_time
                start_dns = time.time()
                socket.gethostbyname("cloudflare.com")
                end_dns = time.time()
                dns_time = round((end_dns - start_dns) * 1000, 5)
                if dns_time == 0: pass
                else: break
            
            respuesta += f"<br><br>{__TR__('RESOLUCIÓN_DNS')}: <span style='color: {FuncMainPY.obt_json_(7)};'>{dns_time} ms</span>"
        except:
            FuncMainPY.ERR_REG_(f"[camb_] No hay conexión a internet.\n\n")

            respuesta += f"<br><br>ERROR>> {__TR__('COMPROBAR_INTERNET')}"

        actualizar_texto(respuesta)

        ##

        GATEWAY = FuncMainPY.get_network_data(None, 2)

        respuesta += f"<br><br><span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('PING_HACIA_GATEWAY')} '{GATEWAY}'</span>"
        actualizar_texto(respuesta + f"<br><br>{__TR__('PEALIZAR_PING3')}")

        if stop_thread: return

        ping = "0.00"
        intentos = 0
        while True:
            intentos += 1
            if intentos >= 4:
                break

            try:
                ping = round(ping3.ping(GATEWAY, unit="ms"), 4)
            except:
                break

            if ping == 0: pass
            else: break
        
        respuesta += f"<br><br>Ping: <span style='color: {FuncMainPY.obt_json_(7)};'>{ping} ms</span>"
        actualizar_texto(respuesta)

        ##

        respuesta += f"<br><br><span style='color: {FuncMainPY.obt_json_(6)};'>Tiempo de contacto con el servidor de AILI-SS</span>"
        actualizar_texto(respuesta + f"<br><br>{__TR__('ESPERAR')}")

        if stop_thread: return

        try:
            start = datetime.now()
            response = requests.get(f"https://aili-mongodb.onrender.com/")
            FIN = datetime.now()

            try:
                res2 = response.json()
            except:
                res2 = response.text
            
        except:
            respuesta += f"<br><br>ERROR>> {__TR__('COMPROBAR_INTERNET')}"
            actualizar_texto(respuesta)


        try:
            ping = round(ping3.ping(HOST, unit="ms"), 4)
            respuesta += f"<br><br>{__TR__('TIEMPO')}: <span style='color: {FuncMainPY.obt_json_(7)};'>{FIN - start}</span>  <br>{__TR__('RESPUESTA_')} <span style='color: {FuncMainPY.obt_json_(7)};'>{res2}</span>"
        except:
            FuncMainPY.ERR_REG_(f"[camb_] No se puedo contactar con el servidor de AILI-SS.\n\n")

            respuesta += f"<br><br>Respuesta: <span style='color: {FuncMainPY.obt_json_(7)};'>{__TR__('NO_PODER_CONTACTAR_SERVER')}</span>"

        actualizar_texto(respuesta)

        ##

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)

        ##

        button0.setEnabled(True)
        button0.setText(f"{__TR__('OBTENER')}")
        with open(FuncMainPY.obtener_ruta_config(), "r") as f:
            data = json.load(f)
            button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")
        
        QApplication.processEvents()
        
        #3

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    button0 = QPushButton(f"{__TR__('OBTENER')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA21.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA21.setLayout(main_layout)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA21.setCentralWidget(widget_principal)

    VENTANA21.show()
    ventana.hide()
    return VENTANA21

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Pantalla sobre los tiempos de carga

def p_apoya_proyecto_(ventana, e=None):
    global VENTANA23
    VENTANA23 = QMainWindow()
    VENTANA23.setFixedSize(305, 180)
    FuncGuiPY.centrar_ventana_(VENTANA23)
    VENTANA23.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA23.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_APOYA_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############
    
    button1 = QPushButton("")
    button1.setStyleSheet("padding: 10px;")
    button1.clicked.connect(lambda: webbrowser.open("https://www.patreon.com/c/byAd12"))
    button1.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoPATREON.png")))
    button1.setIconSize(QSize(50, 50))
    button1.setCursor(Qt.CursorShape.PointingHandCursor)
    button1.setObjectName("buttonNOESTILOS")

    button2 = QPushButton("")
    button2.setStyleSheet("padding: 10px;")
    button2.clicked.connect(lambda: webbrowser.open("https://paypal.me/byAd112"))
    button2.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoPAYPAL.png")))
    button2.setCursor(Qt.CursorShape.PointingHandCursor)
    button2.setIconSize(QSize(50, 50))
    button2.setObjectName("buttonNOESTILOS")

    button3 = QPushButton("")
    button3.setStyleSheet("padding: 10px;")
    button3.clicked.connect(lambda: webbrowser.open("https://ko-fi.com/byad12"))
    button3.setIcon(QIcon(os.path.join(RUTA_RECURSOS, "Logos", "LogoKOFI.png")))
    button3.setCursor(Qt.CursorShape.PointingHandCursor)
    button3.setIconSize(QSize(50, 50))
    button3.setObjectName("buttonNOESTILOS")

    ############

    GRID = QGridLayout()

    GRID.setColumnStretch(0, 1)
    GRID.setColumnStretch(1, 1)
    GRID.setColumnStretch(2, 1)

    GRID.addWidget(button1, 0, 0)
    GRID.addWidget(button2, 0, 1)
    GRID.addWidget(button3, 0, 2)

    main_layout.addLayout(GRID)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA23.setCentralWidget(widget_principal)

    VENTANA23.show()
    return VENTANA23

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para escanear dispositivos bluetooth

def pF_dispositivos_bluetooth_(ventana):
    global VENTANA24
    VENTANA24 = QMainWindow()
    VENTANA24.timer = QTimer()

    VENTANA24.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA24)
    VENTANA24.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA24.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('OBTENER_TITULO')} <span style='color: {FuncMainPY.obt_json_(6)};'>Bluetooth Low Energy</span>")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    text_edit = QTextEdit()
    text_edit.setText(f"{__TR__('ERROR_INICIAR_BLUETOOTH')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA24.resizeEvent = lambda event: adjust_text_edit_height(VENTANA24, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    
    main_layout.addWidget(text_edit)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_():
        try: button0.clicked.disconnect()
        except: pass
        button0.clicked.connect(camb_)

        button0.setEnabled(False)
        button0.setText(f"{__TR__('ESPERAR')}")
        button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")

        def stop_():
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            button0.setEnabled(True)
            return
        
        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)
    
        actualizar_texto(f"{__TR__('AILI_ESCANEANDO_BLE')}")

        if stop_thread: stop_()

        RESULTADO_ESCANEO_ = FuncMainPY.dispositivos_bluetooth_()

        if stop_thread: stop_()

        actualizar_texto(f"{__TR__('AILI_ESCANEANDO_BLE')}<br>{__TR__('AILI_ANALIZANDO')}")
        time.sleep(0.3)

        if stop_thread: stop_()

        res1 = f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('DISPOSITIVOS_BLE')}</span> <br><br>" + RESULTADO_ESCANEO_
        actualizar_texto(res1)

        if RESULTADO_ESCANEO_ == __TR__("SE_NECESITA_BLUETOOTH"):
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
            button0.setText(f"{__TR__('EMPEZAR')}")
        else:
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            try: button0.clicked.disconnect()
            except: pass
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.clicked.connect(lambda: pF_exportar_res_(VENTANA24, str(__TR__('DISPOSITIVOS_BLE')) + "<br><br>" + RESULTADO_ESCANEO_, 5))
        
        button0.setEnabled(True)
        with open(FuncMainPY.obtener_ruta_config(), "r") as f:
            data = json.load(f)
            button0.setStyleSheet(f"background-color: {data['BACKG_BASE']}; color: {data['LETRA_BASE']};")

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA24.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button2 = QPushButton(f"{__TR__('INSTALAR_NMAP')}")
    button2.clicked.connect(lambda: p_principal_(VENTANA24, "IrADependencias"))
    button2.setProperty("tipo", "button1")

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA24))
    button1.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addStretch()


    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA24.setCentralWidget(widget_principal)

    VENTANA24.show()
    ventana.hide()
    return VENTANA24

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para escanear dispositivos bluetooth

def pF_hosts_red_disponibles_(ventana, IP_RED_DADA, MASCARA_DADA):
    ventana.close()

    global VENTANA25
    VENTANA25 = QMainWindow()
    VENTANA25.timer = QTimer()

    VENTANA25.setFixedSize(700, 600)
    FuncGuiPY.centrar_ventana_(VENTANA25)
    VENTANA25.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA25.setStyleSheet(FuncMainPY.estilos_())

    ############

    # Layout principal
    main_layout = QVBoxLayout()

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('CALCULAR_IPS_LISTA')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    text_edit = QTextEdit()
    text_edit.setText("")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA25.resizeEvent = lambda event: adjust_text_edit_height(VENTANA25, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    
    main_layout.addWidget(text_edit)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_():
        actualizar_texto(f"{__TR__('ESPERA_AILI_CALCULANDO_IP')}")

        if stop_thread: return
        
        DIREC_RED = FuncMainPY.CALCULAR_DIRECCION_RED__(None, IP_RED_DADA, MASCARA_DADA)

        RESULTADO_ESCANEO_ = ""
        RESULTADO_ESCANEO_exportado_ = ""

        index = 0
        try:
            RESULTADO_ESCANEO_0 = list( ipaddress.ip_network(DIREC_RED).hosts() )
            SUMA = len(RESULTADO_ESCANEO_0)

            RESULTADO_ESCANEO_exportado_ = f"{__TR__('IP_HOSTS_RED')}\n\n{__TR__('RED_')} {DIREC_RED}\n\n{__TR__('IPS_TOTALES')}{SUMA}\n\nIPv4:\n\n"
            for i in RESULTADO_ESCANEO_0:
                index += 1
                if index > 500:
                    pass
                else:
                    RESULTADO_ESCANEO_ += f"{i}<br>"
            
            for i in RESULTADO_ESCANEO_0:
                RESULTADO_ESCANEO_exportado_ += f"{i}\n"
            
            RESULTADO_ESCANEO_exportado_ += "\n\n© AILI-SS (aili-ss.pages.dev)"

        except Exception as e:
            print(e)
            FuncMainPY.ERR_REG_(f"[camb_] No se puede calcular los host disponibles - Parámetros incorrectos.\n\n")

            SUMA = 0
            RESULTADO_ESCANEO_ = f"{__TR__('NO_PUEDE_CALCULAR')}"

        if stop_thread: return

        actualizar_texto(f"{__TR__('ESPERA_AILI_CALCULANDO_IP')}<br>{__TR__('AILI_ANALIZANDO')}")
        time.sleep(0.3)

        if stop_thread: return

        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

        with open(os.path.join(RUTA_DIR_USUARIO, "DireccionamientoIP.txt"), "w", encoding="UTF-8") as f:
            f.write(RESULTADO_ESCANEO_exportado_)
        
        with open(os.path.join(RUTA_DIR_USUARIO, "DireccionamientoIP.html"), "w", encoding="UTF-8") as f:
            ESTILOS = """<style>* {font-family: Arial; background-color: FuncMainPY.obt_json_(0); color: FuncMainPY.obt_json_(2);}</style>"""

            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(0)", FuncMainPY.obt_json_(0))
            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(2)", FuncMainPY.obt_json_(2))
            
            RESULTADO_ESCANEO_exportado_2_ =  "<html> <body>" + RESULTADO_ESCANEO_exportado_ + ESTILOS + "</body> </html>"

            RESULTADO_ESCANEO_exportado_2_ = RESULTADO_ESCANEO_exportado_2_.replace(f"{__TR__('IP_HOSTS_RED')}", f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('IP_HOSTS_RED')}</span>")
            RESULTADO_ESCANEO_exportado_2_ = RESULTADO_ESCANEO_exportado_2_.replace(f"{__TR__('RED_')}", f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('RED_')}</span>")
            RESULTADO_ESCANEO_exportado_2_ = RESULTADO_ESCANEO_exportado_2_.replace(f"{__TR__('IPS_TOTALES')}", f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('IPS_TOTALES')}</span>")
            RESULTADO_ESCANEO_exportado_2_ = RESULTADO_ESCANEO_exportado_2_.replace(f"IPv4:", f"<span style='color: {FuncMainPY.obt_json_(6)};'>IPv4:</span>")
            RESULTADO_ESCANEO_exportado_2_ = RESULTADO_ESCANEO_exportado_2_.replace(f"aili-ss.pages.dev", f"<u><a href='https://aili-ss.pages.dev' target=_blank style='color: {FuncMainPY.obt_json_(6)};'>aili-ss.pages.dev</a></u>")

            f.write(str(RESULTADO_ESCANEO_exportado_2_).replace("\n", "<br>"))
        
        try:
            FORMULA = f"2<sup>{32 - int(str(DIREC_RED).split('/')[1])}</sup> - 2"
        except:
            FORMULA = "Error"

        res1 = f"""<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('IP_HOSTS_RED')}</span>
        <br><br>{__TR__('RESULTADO_EXPORTADO_A')}<br>
        <span style='color: {FuncMainPY.obt_json_(7)};'> {os.path.join(RUTA_DIR_USUARIO, 'DireccionamientoIP.txt')} </span>
        <br> <span style='color: {FuncMainPY.obt_json_(7)};'> {os.path.join(RUTA_DIR_USUARIO, 'DireccionamientoIP.html')} </span>
        <br><br>{__TR__('RED_')}<span style='color: {FuncMainPY.obt_json_(7)};'>{DIREC_RED}</span>
        <br><br>{__TR__('ENSEÑANDO_')}{index if index < 500 else 500}/({__TR__('500_PRIMEROS')})
        <br><br>{__TR__('IPS_TOTALES')}<span style='color: {FuncMainPY.obt_json_(7)};'>{SUMA}</span> • (<span style='color: {FuncMainPY.obt_json_(7)};'>{FORMULA}</span>)
        <br><br>""" + RESULTADO_ESCANEO_
        actualizar_texto(res1)
        print("Debug: Completado")

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    ############

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(lambda: pF_calcular_direcciones_(VENTANA25, IP_RED_DADA, MASCARA_DADA, FuncMainPY.CALCULAR_DIRECCION_RED__(None, IP_RED_DADA, MASCARA_DADA), True))
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button3)
    button_layout.addStretch()


    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA25.setCentralWidget(widget_principal)

    start_thread()

    VENTANA25.show()
    return VENTANA25

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ver registro de errores

def pF_exportar_res_(ventana, EXPORTAR, CUAL):
    global VENTANA27
    VENTANA27 = QMainWindow()
    VENTANA27.setFixedSize(400, 125)
    FuncGuiPY.centrar_ventana_(VENTANA27)
    VENTANA27.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA27.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_EXPORTAR_RESULTADOS')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def exportar_txt_(EXPORTAR, FORMATO):
        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

        if FORMATO != "HTML": # TXT

            EXPORTAR = str(EXPORTAR).replace("<br>", "\n")
            EXPORTAR = str(EXPORTAR).replace("<br style='font-size: 8px;'>", "\n")
            EXPORTAR = str(EXPORTAR).replace(f"<span style=", "")
            EXPORTAR = str(EXPORTAR).replace("</span>", "")
            EXPORTAR = str(EXPORTAR).replace("<p>", "")
            EXPORTAR = str(EXPORTAR).replace("</p>", "")
            EXPORTAR = str(EXPORTAR).replace("<ul>", "")
            EXPORTAR = str(EXPORTAR).replace("</ul>", "")
            EXPORTAR = str(EXPORTAR).replace("<li>", "")
            EXPORTAR = str(EXPORTAR).replace("</li>", "")
            EXPORTAR = str(EXPORTAR).replace(f"<b style='color: {FuncMainPY.obt_json_(7)};'>", "")
            EXPORTAR = str(EXPORTAR).replace("</b>", "")

            EXPORTAR = str(EXPORTAR).replace("                    ", "")
            EXPORTAR = str(EXPORTAR).replace("                        ", "")

            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(1)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(2)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(3)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(4)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(5)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(6)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(7)};'>", "")
            EXPORTAR = str(EXPORTAR).replace(f"'color: {FuncMainPY.obt_json_(8)};'>", "")

            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(1)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(2)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(3)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(4)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(5)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(6)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(7)};">', "")
            EXPORTAR = str(EXPORTAR).replace(f'"color: {FuncMainPY.obt_json_(8)};">', "")
        
        else: # HTML
            EXPORTAR = f"<p><a target='_bank' href='https://aili-ss.pages.dev' style='color: {FuncMainPY.obt_json_(6)};'>AILI-SS</a> • {FuncMainPY.obt_json_('IDIOMA')} • {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}</p><br>" + str(EXPORTAR).replace("_"*50, "<hr>")

            ESTILOS = """<br>
            <style>
                * {
                    font-family: Arial;
                    background-color: FuncMainPY.obt_json_(0);
                    color: FuncMainPY.obt_json_(2);
                }
            </style>"""

            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(0)", FuncMainPY.obt_json_(0))
            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(2)", FuncMainPY.obt_json_(2))

            EXPORTAR += ESTILOS

        if CUAL == 1 and FORMATO == "TXT":  archivo = "HostsRED.txt"
        if CUAL == 1 and FORMATO == "HTML": archivo = "HostsRED.html"
        
        if CUAL == 2 and FORMATO == "TXT":  archivo = "PuertosHOST.txt"
        if CUAL == 2 and FORMATO == "HTML": archivo = "PuertosHOST.html"

        if CUAL == 3 and FORMATO == "TXT":  archivo = "VulnerabilidadesHOST.txt"
        if CUAL == 3 and FORMATO == "HTML": archivo = "VulnerabilidadesHOST.html"

        if CUAL == 4 and FORMATO == "TXT":  archivo = "RedesWIFI.txt"
        if CUAL == 4 and FORMATO == "HTML": archivo = "RedesWIFI.html"

        if CUAL == 5 and FORMATO == "TXT":  archivo = "DispositivosBLE.txt"
        if CUAL == 5 and FORMATO == "HTML": archivo = "DispositivosBLE.html"

        if CUAL == 6 and FORMATO == "TXT":  archivo = "InterfacesEQUIPO.txt"
        if CUAL == 6 and FORMATO == "HTML": archivo = "InterfacesEQUIPO.html"

        if CUAL == 7 and FORMATO == "TXT":  archivo = "Hardware.txt"
        if CUAL == 7 and FORMATO == "HTML": archivo = "Hardware.html"

        if CUAL == 8 and FORMATO == "TXT":  archivo = "EscaneoTLD.txt"
        if CUAL == 8 and FORMATO == "HTML": archivo = "EscaneoTLD.html"

        with open(os.path.join(RUTA_DIR_USUARIO, archivo), "w", encoding="UTF-8") as f:
            f.write(EXPORTAR)
        
        p_error_(VENTANA27, str(os.path.join(RUTA_DIR_USUARIO, archivo)), "EXPORTAR")

    ############

    button2 = QPushButton(f"{__TR__('TEXTO_PLANO')} (.TXT)")
    button2.clicked.connect(lambda: exportar_txt_(EXPORTAR, "TXT"))
    button2.setProperty("tipo", "button1")

    button3 = QPushButton("HTML")
    button3.clicked.connect(lambda: exportar_txt_(EXPORTAR, "HTML"))
    button3.setProperty("tipo", "button1")

    button_layout = QHBoxLayout()
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)
    button_layout.addStretch()
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA27.setCentralWidget(widget_principal)

    VENTANA27.show()
    return VENTANA27

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Escaneo redes Wi-Fi

def pF_escaneo_redes_WiFi_(ventana):
    global VENTANA28
    VENTANA28 = QMainWindow()
    VENTANA28.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA28.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA28.setMinimumSize(700, 600)
    VENTANA28.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA28.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_WIFI_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    text_edit = QTextEdit()
    text_edit.setText(f"{__TR__('P_WIFI_EXPLICACION')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA28.resizeEvent = lambda event: adjust_text_edit_height(VENTANA28, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    
    main_layout.addWidget(text_edit)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    def camb_():
        try: button0.clicked.disconnect()
        except: pass
        button0.clicked.connect(camb_)

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)


        button0.setEnabled(False)
        texto_poner_ = ""

        RESULTADO_ESCANEO_ = FuncMainPY.devolver_redes_wifi_()

        if stop_thread: return

        actualizar_texto(f"{__TR__('AILI_ANALIZANDO')}".replace('<br>',''))
        time.sleep(0.3)

        if stop_thread: return

        texto_poner_ += f"<span style='color: {FuncMainPY.obt_json_(6)};'>{__TR__('REDES_ACTIVOS')}</span> ({RESULTADO_ESCANEO_[1]})<br>"
        texto_poner_ += RESULTADO_ESCANEO_[0]
        if str(RESULTADO_ESCANEO_[1]) == "0":
            texto_poner_ += f"<br>{__TR__('WLAN_0_DETECTADAS')}"
        
        if stop_thread: return

        actualizar_texto(texto_poner_)

        if RESULTADO_ESCANEO_[0] != "" and "Error" not in RESULTADO_ESCANEO_[0]:
            button0.setEnabled(True)
            try: button0.clicked.disconnect()
            except: pass
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.clicked.connect(lambda: pF_exportar_res_(VENTANA28, texto_poner_, 4))

            cursor = text_edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            text_edit.setTextCursor(cursor)

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)
        else:
            button0.setEnabled(True)

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    ############

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA28.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA28))
    button1.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA28.setCentralWidget(widget_principal)

    VENTANA28.show()
    ventana.hide()
    return VENTANA28

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Opciones extra para cambiar más parámetros para IDS a firewall

def pF_evasion_ids_(IP_F, PUERTO_F, OTRAS_F):
    global VENTANA29
    VENTANA29 = QMainWindow()
    VENTANA29.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        return p_error_(VENTANA29, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA29.setFixedSize(700, 280)
    FuncGuiPY.centrar_ventana_(VENTANA29)
    VENTANA29.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA29.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_EVASION_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    grid_layout.setColumnStretch(0, 1)
    grid_layout.setColumnStretch(1, 1)

    ############
    
    label = QLabel(f"{__TR__('FALSIFICAR_MAC_')}: ")
    config_entrada0 = QLineEdit(IP_F)
    config_entrada0.setPlaceholderText("01:02:03:04:05:06")

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    ############
    
    label = QLabel(f"{__TR__('FALSIFICAR_PUERTO_ORIGEN_')}: ")
    config_entrada1 = QLineEdit(PUERTO_F)

    grid_layout.addWidget(label, 0, 1)
    grid_layout.addWidget(config_entrada1, 1, 1)
    
    ############
    
    label = QLabel(f"{__TR__('OTRAS_OPCIONES_NMAP_')}: ")
    config_entrada2 = QLineEdit(OTRAS_F)

    grid_layout.addWidget(label, 2, 0, 1, 2)
    grid_layout.addWidget(config_entrada2, 3, 0, 1, 2)
    
    ############

    main_layout.addLayout(grid_layout)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
        
    ############

    loop = QEventLoop()
    result = {}

    def aceptar():
        result['data'] = [config_entrada0.text(), config_entrada1.text(), config_entrada2.text()]
        loop.quit()
        VENTANA29.close()

    def cancelar():
        result['data'] = [None, None]
        loop.quit()
        VENTANA29.close()

    
    ############

    button0 = QPushButton(f"{__TR__('ACEPTAR')}")
    button0.clicked.connect(aceptar)
    button0.setProperty("tipo", "button1")

    ############

    button2 = QPushButton(f"Manual")
    button2.clicked.connect(lambda: webbrowser.open("https://nmap.org/docs.html"))
    button2.setProperty("tipo", "button1")

    ############

    button3 = QPushButton(f"{__TR__('CANCELAR')}")
    button3.clicked.connect(cancelar)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addWidget(button2)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA29.setLayout(main_layout)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA29.setCentralWidget(widget_principal)

    VENTANA29.show()
    loop.exec()
    return result['data']

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para crear hash de texto o archivos

def pF_hashing_(ventana):
    ventana.close()

    global VENTANA30
    VENTANA30 = QMainWindow()
    VENTANA30.timer = QTimer()

    VENTANA30.setFixedSize(355, 170)
    FuncGuiPY.centrar_ventana_(VENTANA30)
    VENTANA30.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA30.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_HASHING_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    text_edit = QTextEdit()
    text_edit.setPlaceholderText(f"{__TR__('ESCRIBA_AQUI')}")

    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA30.resizeEvent = lambda event: adjust_text_edit_height(VENTANA30, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.75))
    main_layout.addWidget(text_edit)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def conseguir_ruta_archivo_():
        archivo, _ = QFileDialog.getOpenFileName(
            VENTANA30,
            "Seleccionar archivo",
            "",
            "Todos los archivos (*);;Archivos de texto (*.txt);;Imágenes (*.png *.jpg)"
        )
        if archivo:
            pantalla = p_error_(VENTANA30, f"{__TR__('ESPERE')}", 1)
            time.sleep(0.1)
            QApplication.processEvents()
            FuncMainPY.Hashear_(OPC, archivo)
            QApplication.processEvents()
            pantalla.close()

    ############

    def Hashear_a_():
        button0.setStyleSheet("background-color: rgba(0, 128, 0, 0.3); color: white;")
        
        FuncMainPY.Hashear_(OPC, text_edit.toPlainText())

    ############

    button00 = QPushButton(f"{__TR__('SELECCIONAR')}")
    button00.clicked.connect(conseguir_ruta_archivo_)
    button00.setProperty("tipo", "button1")
    
    ############

    button0 = QPushButton(f"{__TR__('ACEPTAR')}")
    button0.clicked.connect(Hashear_a_)
    button0.setProperty("tipo", "button1")

    ############

    buttonx3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    buttonx3.clicked.connect(lambda: elegir_opc_(0))
    buttonx3.setShortcut("Escape")
    buttonx3.setProperty("tipo", "button2")
    
    ############

    button3 = QPushButton(f"{__TR__('CERRAR')}")
    button3.clicked.connect(lambda: p_principal_(VENTANA30, "IrAHerramientasOtras"))
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    global OPC
    OPC = None

    def elegir_opc_(opc):
        global OPC
        OPC = opc

        for i in [text_edit, button0, button00, buttonx1, buttonx2, buttonx3, button3]:
            FuncGuiPY.ocultar_elemento_(i)

        if OPC == 0:
            VENTANA30.setFixedSize(355, 170)

            for i in [buttonx1, buttonx2, button3]:
                FuncGuiPY.mostrar_elemento_(i)

        elif OPC == 1:
            VENTANA30.setMinimumSize(700, 600)

            for i in [text_edit, button0, buttonx3]:
                FuncGuiPY.mostrar_elemento_(i)

        else:
            for i in [button00, buttonx3]:
                FuncGuiPY.mostrar_elemento_(i)
            
        # Centrar ventana
        frameGm = VENTANA30.frameGeometry()
        screen = VENTANA30.screen().availableGeometry().center()
        frameGm.moveCenter(screen)
        VENTANA30.move(frameGm.topLeft())

    ############

    buttonx1 = QPushButton(f"{__TR__('TEXTO_HASH')}")
    buttonx1.clicked.connect(lambda: elegir_opc_(1))
    buttonx1.setProperty("tipo", "button1")
    
    ############

    buttonx2 = QPushButton(f"{__TR__('ARCHIVO_HASH')}")
    buttonx2.clicked.connect(lambda: elegir_opc_(2))
    buttonx2.setProperty("tipo", "button1")

    ############

    button_layout0 = QHBoxLayout()

    button_layout0.addWidget(buttonx1)
    button_layout0.addWidget(buttonx2)
    button_layout0.addWidget(button3)
    button_layout0.addWidget(button0)
    button_layout0.addWidget(button00)
    button_layout0.addWidget(buttonx3)
    
    for i in [buttonx3, button0, button00, text_edit]:
        FuncGuiPY.ocultar_elemento_(i)

    button_layout0.addStretch()
    
    main_layout.addLayout(button_layout0)

    ############

    # Establecer el layout al widget principal
    VENTANA30.setLayout(main_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA30.setCentralWidget(widget_principal)
    
    # Centrar ventana
    frameGm = VENTANA30.frameGeometry()
    screen = VENTANA30.screen().availableGeometry().center()
    frameGm.moveCenter(screen)
    VENTANA30.move(frameGm.topLeft())

    VENTANA30.show()
    return VENTANA30

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para des/cifrar texto con claves aleatorias

def pF_cifrado_AES_random_(ventana):
    global VENTANA33
    VENTANA33 = QMainWindow()
    VENTANA33.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA33.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA33.setMinimumSize(700, 600)
    VENTANA33.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA33.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_CIFRADO_AES')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    label_config_entrada1 = QLabel(f"{__TR__('CLAVE_ALEATORIA')}: ")
    config_entrada1 = QLineEdit()
    config_entrada1.setPlaceholderText(f"{__TR__('SOLO_CLAVE_RELLENE_CAMPO_INFERIOR')}")

    FuncGuiPY.ocultar_elemento_(label_config_entrada1)
    FuncGuiPY.ocultar_elemento_(config_entrada1)

    grid_layout.addWidget(label_config_entrada1, 0, 0)
    grid_layout.addWidget(config_entrada1, 1, 0)

    main_layout.addLayout(grid_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setHtml(f"{__TR__('CIFRAR_AES_DESC')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    text_edit.setPlaceholderText(f"{__TR__('INTRODUZCA_TEXTO_CIFRADO')}")

    text_edit.setFixedHeight(int(VENTANA33.height() * 0.76))
    
    main_layout.addWidget(text_edit)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def hide_show_():
        VENTANA33.close()
        ventana.show()
    
    ############
    
    def camb_(tipo):
        button0.clicked.disconnect()
        button01.clicked.disconnect()
        button3.clicked.disconnect()

        button0.clicked.connect(lambda: camb_(1))
        button01.clicked.connect(lambda: camb_(2))
        button3.clicked.connect(lambda: camb_(0))

        text_edit.setFixedHeight(int(VENTANA33.height() * 0.65))
        
        FuncGuiPY.mostrar_elemento_(label_config_entrada1)
        FuncGuiPY.mostrar_elemento_(config_entrada1)

        config_entrada1.setReadOnly(False)

        if tipo == 0: # MENÚ PRINCIPAL
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            FuncGuiPY.mostrar_elemento_(button0)
            FuncGuiPY.mostrar_elemento_(button01)
            FuncGuiPY.ocultar_elemento_(label_config_entrada1)
            FuncGuiPY.ocultar_elemento_(config_entrada1)

            text_edit.setFixedHeight(int(VENTANA33.height() * 0.76))
            text_edit.setReadOnly(True)
            text_edit.setHtml(f"{__TR__('CIFRAR_AES_DESC')}")
            config_entrada1.setText("")
            button3.clicked.disconnect()
            button3.clicked.connect(hide_show_)


        elif tipo == 1: # CIFRAR
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            def cifrar_():
                res = FuncMainPY.cifrado_AES_(1,
                                              text_edit.toPlainText())
            
                if "Error" in str(res[0]):
                    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
                    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    img_label.setPixmap(pixmap)

                    text_edit.setHtml(str(res[0]) + str(res[1]))
                else:
                    text_edit.setHtml(res[0].decode('utf-8'))
                    config_entrada1.setText(res[1].decode('utf-8'))

                    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
                    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    img_label.setPixmap(pixmap)
                
            button0.clicked.disconnect()
            button0.clicked.connect(cifrar_)

            FuncGuiPY.mostrar_elemento_(button0)
            FuncGuiPY.ocultar_elemento_(button01)
            text_edit.setReadOnly(False)
            text_edit.setHtml("")
            text_edit.setPlaceholderText(f"{__TR__('INTRODUZCA_TEXTO_CIFRADO')}")

            label_config_entrada1.setText(f"{__TR__('CLAVE_ALEATORIA')}")

            config_entrada1.setText("")
            config_entrada1.setPlaceholderText(f"{__TR__('SOLO_CLAVE_RELLENE_CAMPO_INFERIOR')}")

        else: # DESCIFRAR
            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            def descifrar_():
                res = FuncMainPY.cifrado_AES_(2,
                                              text_edit.toPlainText().encode('utf-8'),
                                              config_entrada1.text().encode('utf-8'))
            
                if "Error" in res:
                    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
                    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    img_label.setPixmap(pixmap)

                    p_error_(VENTANA33, res, 1)
                else:
                    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
                    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    img_label.setPixmap(pixmap)

                    text_edit.setHtml(res)

            button01.clicked.disconnect()
            button01.clicked.connect(descifrar_)

            FuncGuiPY.ocultar_elemento_(button0)
            FuncGuiPY.mostrar_elemento_(button01)
            text_edit.setReadOnly(False)
            text_edit.setHtml("")
            text_edit.setPlaceholderText(f"{__TR__('INTRODUZCA_TEXTO_DESCIFRADO')}")

            label_config_entrada1.setText(f"{__TR__('CLAVE')}")

            config_entrada1.setText("")
            config_entrada1.setPlaceholderText(f"{__TR__('INSERTE_SU_CLAVE')}")
    
    ############
    
    button0 = QPushButton(f"{__TR__('CIFRAR')}")
    button0.clicked.connect(lambda: camb_(1))
    button0.setProperty("tipo", "button1")

    ############

    button01 = QPushButton(f"{__TR__('DESCIFRAR')}")
    button01.clicked.connect(lambda: camb_(2))
    button01.setProperty("tipo", "button1")

    ############

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button01)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA33.setLayout(main_layout)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True
        

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        updater.signal_actualizar.emit(html)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA33.setCentralWidget(widget_principal)

    VENTANA33.show()
    ventana.hide()
    return VENTANA33

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Opción para evitar partes en pf_escaneo_vulnerabilidades

def pF_evitar_partes_():
    global VENTANA34
    VENTANA34 = QMainWindow()
    VENTANA34.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        return p_error_(VENTANA34, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA34.setFixedSize(500, 200)
    FuncGuiPY.centrar_ventana_(VENTANA34)
    VENTANA34.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA34.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_EVITAR_PARTES_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    ############
    
    central_widget = QWidget()
    VENTANA34.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    boton = QPushButton(f"{__TR__('SELECCIONAR')}")
    boton.setProperty("tipo", "button1")

    # Crear el menú
    config_entrada1 = QMenu()

    # Opciones para el menú
    opciones = [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}", f"{__TR__('INFO_EQUIPO_EV')}", f"{__TR__('PUERTOS_TCP_EV')}", f"{__TR__('PUERTOS_UDP_EV')}"]

    # Crear acciones en el menú
    acciones = []
    for texto in opciones:
        accion = QAction(texto)
        accion.setCheckable(True)
        config_entrada1.addAction(accion)
        acciones.append(accion)

    global scripts_seleccionados_2
    scripts_seleccionados_2 = []

    def actualizar_texto__():
        global scripts_seleccionados_2
        scripts_seleccionados_2 = []

        for accion in acciones:
            if accion.isChecked():
                texto = accion.text()
                if texto == f"{__TR__('_LIMPIAR_')}":
                    for a in acciones:
                        a.setChecked(False)
                    boton.setText(f"{__TR__('SELECCIONAR')}")
                    return
                elif texto == f"{__TR__('_TODOS_')}":
                    for a in acciones:
                        if a.text() != f"{__TR__('_LIMPIAR_')}":
                            a.setChecked(True)
                        if a.text() == f"{__TR__('_TODOS_')}":
                            a.setChecked(False)
                    scripts_seleccionados_2 = [a.text() for a in acciones if a.text() not in [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}"]]
                    boton.setText(f"{__TR__('SELECCIONAR')} ({len(acciones) - 2})")
                    return

        scripts_seleccionados_2 = [a.text() for a in acciones if a.isChecked() and a.text() not in [f"{__TR__('_LIMPIAR_')}", f"{__TR__('_TODOS_')}"]]

        if scripts_seleccionados_2:
            boton.setText(f"{__TR__('SELECCIONAR')} ({len(scripts_seleccionados_2)})")
        else:
            boton.setText(f"{__TR__('SELECCIONAR')}")

    def obtener_scripts_():
        lista_total = []

        for i in scripts_seleccionados_2:
            lista_total.append(i)
        
        return lista_total


    # Conectar la señal de selección
    for accion in acciones:
        accion.triggered.connect(actualizar_texto__)
        if accion.isCheckable():
            accion.toggled.connect(actualizar_texto__)


    # Función para mostrar el menú cuando el botón es presionado
    def mostrar_menu():
        config_entrada1.popup(boton.mapToGlobal(boton.rect().bottomLeft()))

    def menu_oculto():
        QTimer.singleShot(50, actualizar_texto__)  # Da tiempo a que .isChecked() se actualice

    config_entrada1.aboutToHide.connect(menu_oculto)

    # Conectar la acción del botón al menú
    boton.clicked.connect(mostrar_menu)

    # Agregar los widgets al layout
    layout.addWidget(boton)

    grid_layout.addWidget(boton, 0, 0)
    
    ############

    main_layout.addLayout(grid_layout)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
        
    ############

    loop = QEventLoop()
    result = {}

    def aceptar():
        result['data'] = [obtener_scripts_()]
        loop.quit()
        VENTANA34.close()

    def cancelar():
        result['data'] = [None]
        loop.quit()
        VENTANA34.close()
    
    ############

    button0 = QPushButton(f"{__TR__('ACEPTAR')}")
    button0.clicked.connect(aceptar)
    button0.setProperty("tipo", "button1")

    ############

    button3 = QPushButton(f"{__TR__('CANCELAR')}")
    button3.clicked.connect(cancelar)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    # Establecer el layout al widget principal
    VENTANA34.setLayout(main_layout)

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA34.setCentralWidget(widget_principal)

    VENTANA34.show()
    loop.exec()
    return result['data']

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Reporte completo de el equipo

def pF_reporte_equipo_(ventana):
    global VENTANA35
    VENTANA35 = QMainWindow()
    VENTANA35.setFixedSize(500, 200)
    FuncGuiPY.centrar_ventana_(VENTANA35)
    VENTANA35.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA35.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_REPORTE_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def camb_():
        print("camb_ se ejecuta")
        ############ PREPARAR

        RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
        button4.setText(f"{__TR__('ESPERAR')}")
        QApplication.processEvents()

        ############ INTERFACES DE RED

        button4.setText(f"1/4")
        QApplication.processEvents()
        CONTENIDO1 = pF_interfaces_red_("Pase1")

        ############ HARDWARE Y SOFTWARE

        button4.setText(f"2/4")
        QApplication.processEvents()
        CONTENIDO2 = FuncMainPY.ReporteEquipo()

        ############ GUARDAR CONTENIDOS

        button4.setText(f"3/4")
        QApplication.processEvents()

        with open(os.path.join(RUTA_DIR_USUARIO, "ReporteEquipo.html"), "w") as f:
            TITULO = f"<p><a target='_bank' href='https://aili-ss.pages.dev' style='color: {FuncMainPY.obt_json_(6)};'>AILI-SS</a> • {FuncMainPY.obt_json_('IDIOMA')} • {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}</p><br>"

            ESTILOS = """<style>* {font-family: Arial; background-color: FuncMainPY.obt_json_(0); color: FuncMainPY.obt_json_(2);}</style>"""
            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(0)", FuncMainPY.obt_json_(0))
            ESTILOS = ESTILOS.replace("FuncMainPY.obt_json_(2)", FuncMainPY.obt_json_(2))

            f.write(str(ESTILOS) + "\n\n" + str(TITULO) + str(CONTENIDO1) + f"<br><hr>" + "\n\n <br><br>\n" + str(CONTENIDO2).replace('_'*50, '<hr>'))

        ############ 

        button4.setText(f"{__TR__('ABRIR')}")
        button4.setEnabled(True)
        button4.clicked.connect(lambda: webbrowser.open(os.path.join(RUTA_DIR_USUARIO, "ReporteEquipo.html")))
        
        QApplication.processEvents()

        ############ FIN :)
    ############

    QTimer.singleShot(0, camb_)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    button4 = QPushButton(f"{__TR__('ESPERAR')}")
    button4.setProperty("tipo", "button1")
    button4.setEnabled(False)

    def hide_show_():
        VENTANA35.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    button_layout = QHBoxLayout()

    button_layout.addWidget(button4)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA35.setCentralWidget(widget_principal)

    VENTANA35.show()
    ventana.hide()
    return VENTANA35

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Easter egg - KIRAA AGGJ

def p_easter_():
    global VENTANA36
    VENTANA36 = QMainWindow()
    VENTANA36.setFixedSize(400, 400)
    FuncGuiPY.centrar_ventana_(VENTANA36)
    VENTANA36.setWindowTitle(" ")

    label = QLabel(VENTANA36)
    label.setGeometry(0, 0, VENTANA36.width(), VENTANA36.height())
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/DeusKira.jpg")
    label.setPixmap(pixmap.scaled(VENTANA36.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
    
    global TIEMPO_CARGA_LOGO; TIEMPO_CARGA_LOGO = datetime.now()

    VENTANA36.show()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para instalar y controlar servidores

def pF_control_servidores_(ventana, SERVER_ELEGIDO):
    global VENTANA37
    VENTANA37 = QMainWindow()
    VENTANA37.setFixedSize(500, 385)
    FuncGuiPY.centrar_ventana_(VENTANA37)
    VENTANA37.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA37.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"Server - <span style='color: {FuncMainPY.obt_json_(6)};'>{SERVER_ELEGIDO}</span>")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    label = QLabel(f"")
    label.setTextFormat(Qt.TextFormat.RichText) # HTML
    label.setWordWrap(True)
    main_layout.addWidget(label)

    def cambiar_estado():
        label.setText(str(FuncMainPY.estado_servidor_(SERVER_ELEGIDO)))

    QTimer.singleShot(0, cambiar_estado)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    botones_fila1 = [
        FuncGuiPY.crear_boton_(f"{__TR__('INICIAR')}", "NINGUNO", lambda: FuncMainPY.manejar_1_servidor_(SERVER_ELEGIDO, "start", label), True, True),
        FuncGuiPY.crear_boton_(f"{__TR__('REINICIAR')}", "NINGUNO", lambda: FuncMainPY.manejar_1_servidor_(SERVER_ELEGIDO, "restart", label), True, True),
        FuncGuiPY.crear_boton_(f"{__TR__('PARAR')}", "NINGUNO", lambda: FuncMainPY.manejar_1_servidor_(SERVER_ELEGIDO, "stop", label), True, True),
    ]

    botones_fila2 = [
        FuncGuiPY.crear_boton_(f"{__TR__('REGISTROS')}", "NINGUNO", lambda: FuncMainPY.abrir_registros_servidor_(SERVER_ELEGIDO, label), True, True),
        FuncGuiPY.crear_boton_(f"{__TR__('CONFIGURAR')}", "NINGUNO", lambda: FuncMainPY.configurar_servidor_(SERVER_ELEGIDO, label), True, True),
        FuncGuiPY.crear_boton_(f"{__TR__('GUÍA')}", "NINGUNO", lambda: webbrowser.open("https://byad12.pages.dev/guides"), True, True),
    ]

    botones_fila3 = [
        FuncGuiPY.crear_boton_(f"{__TR__('INSTALAR_SERVICIO')}", "NINGUNO", lambda: pF_instalar_servidor_(SERVER_ELEGIDO), True, True),
        FuncGuiPY.crear_boton_(f"{__TR__('DESINSTALAR_SERVICIO')}", "NINGUNO", lambda: pF_desinstalar_servidor_(SERVER_ELEGIDO), True, True),
    ]

    # Agregar a layout principal
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila1)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila2)
    FuncGuiPY.agregar_fila_botones(main_layout, botones_fila3)


    ############

    def hide_show_():
        VENTANA37.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    button_layout = QHBoxLayout()

    button_layout.addWidget(button3)
    button_layout.addStretch()

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA37.setCentralWidget(widget_principal)

    VENTANA37.show()
    ventana.hide()
    return VENTANA37

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para instalar un servidor

def pF_instalar_servidor_(SERVIDOR):
    global VENTANA38
    VENTANA38 = QMainWindow()
    VENTANA38.setFixedSize(500, 385)
    FuncGuiPY.centrar_ventana_(VENTANA38)
    VENTANA38.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA38.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_INSTALAR_SERVER_TITULO')} - <span style='color: {FuncMainPY.obt_json_(6)};'>{SERVIDOR}</span>")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    spacer = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    GRID = QGridLayout()

    GRID.setColumnStretch(0, 1)

    ############

    GRID.addWidget(QLabel(f""), 2, 0, 1, 2)

    ############
    
    label = QLabel(f"1.")
    GRID.addWidget(label, 0, 0)

    label_ensenar_mascara = QLabel("sudo apt-get update")
    label_ensenar_mascara.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_ensenar_mascara, 1, 0)

    ############

    label = QLabel(f"2.")
    GRID.addWidget(label, 2, 0)

    label_direc_red = QLabel("")

    if SERVIDOR == "isc-dhcp-server": label_direc_red.setText("sudo apt-get install isc-dhcp-server")
    if SERVIDOR == "bind9": label_direc_red.setText("sudo apt-get install bind9")
    if SERVIDOR == "apache2": label_direc_red.setText("sudo apt-get install apache2 apache2-utils")
    if SERVIDOR == "vsftpd": label_direc_red.setText("sudo apt-get install vsftpd")
    if SERVIDOR == "postfix": label_direc_red.setText("sudo apt-get install postfix")

    label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_direc_red, 3, 0)

    ############

    if SERVIDOR == "isc-dhcp-server":
        label = QLabel(f"3.")
        GRID.addWidget(label, 4, 0)

        label_direc_red = QLabel("sudo ufw allow 67")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 5, 0)

    if SERVIDOR == "bind9":
        label = QLabel(f"3.")
        GRID.addWidget(label, 4, 0)

        label_direc_red = QLabel("sudo ufw allow 53")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 5, 0)

    if SERVIDOR == "apache2":
        label = QLabel(f"3.")
        GRID.addWidget(label, 4, 0)

        label_direc_red = QLabel("sudo ufw allow 80")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 5, 0)

    if SERVIDOR == "vsftpd":
        label = QLabel(f"3.")
        GRID.addWidget(label, 4, 0)

        label_direc_red = QLabel("sudo ufw allow 21")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 5, 0)

    if SERVIDOR == "postfix":
        label = QLabel(f"3.")
        GRID.addWidget(label, 4, 0)

        label_direc_red = QLabel("sudo ufw allow 25")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 5, 0)

    ############

    main_layout.addLayout(GRID)

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    
    ############
    
    def ejec_():
        res = FuncMainPY.instalar_servidor_(SERVIDOR)
        if res == "ok":
            return
        elif res == "win":
            p_error_(None, f"{__TR__('NO_DISPONILBE_WIN')}", 3)
        else:
            p_error_(None, res, 3)
        
    ############

    button2 = QPushButton(f"{__TR__('EJECUTAR')}")
    button2.clicked.connect(ejec_)
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('CERRAR')}")
    button3.clicked.connect(VENTANA38.close)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA38.setCentralWidget(widget_principal)

    VENTANA38.show()
    return VENTANA38

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Función para DESinstalar un servidor

def pF_desinstalar_servidor_(SERVIDOR):
    global VENTANA39
    VENTANA39 = QMainWindow()
    VENTANA39.setFixedSize(500, 385)
    FuncGuiPY.centrar_ventana_(VENTANA39)
    VENTANA39.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA39.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('P_DESINSTALAR_SERVER_TITULO')} - <span style='color: {FuncMainPY.obt_json_(6)};'>{SERVIDOR}</span>")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)

    ############

    spacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    GRID = QGridLayout()

    GRID.setColumnStretch(0, 1)

    ############

    GRID.addWidget(QLabel(f""), 2, 0, 1, 2)

    ############

    label = QLabel(f"1.")
    GRID.addWidget(label, 0, 0)

    label_direc_red = QLabel("")

    if SERVIDOR == "isc-dhcp-server": label_direc_red.setText("sudo apt-get remove isc-dhcp-server")
    if SERVIDOR == "bind9": label_direc_red.setText("sudo apt remove bind9")
    if SERVIDOR == "apache2": label_direc_red.setText("sudo apt remove apache2 apache2-utils")
    if SERVIDOR == "vsftpd": label_direc_red.setText("sudo apt remove vsftpd")
    if SERVIDOR == "postfix": label_direc_red.setText("sudo apt remove postfix")

    label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_direc_red, 1, 0)

    ############

    if SERVIDOR == "isc-dhcp-server":
        label = QLabel(f"2.")
        GRID.addWidget(label, 2, 0)

        label_direc_red = QLabel("sudo ufw deny 67")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 3, 0)

    if SERVIDOR == "bind9":
        label = QLabel(f"2.")
        GRID.addWidget(label, 2, 0)

        label_direc_red = QLabel("sudo ufw deny 53")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 3, 0)

    if SERVIDOR == "apache2":
        label = QLabel(f"2.")
        GRID.addWidget(label, 2, 0)

        label_direc_red = QLabel("sudo ufw deny 80")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 3, 0)

    if SERVIDOR == "vsftpd":
        label = QLabel(f"2.")
        GRID.addWidget(label, 2, 0)

        label_direc_red = QLabel("sudo ufw deny 21")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 3, 0)

    if SERVIDOR == "postfix":
        label = QLabel(f"2.")
        GRID.addWidget(label, 2, 0)

        label_direc_red = QLabel("sudo ufw deny 25")

        label_direc_red.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
        GRID.addWidget(label_direc_red, 3, 0)

    ############
    
    label = QLabel(f"3.")
    GRID.addWidget(label, 4, 0)

    label_ensenar_mascara = QLabel(":)")
    label_ensenar_mascara.setStyleSheet("border: 1px solid white; font-weight: bold; padding: 10px; border-radius: 10px; text-align: center;")
    GRID.addWidget(label_ensenar_mascara, 5, 0)

    ############

    main_layout.addLayout(GRID)

    ############

    spacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)
    
    ############

    def ejec_():
        res = FuncMainPY.desinstalar_servidor_(SERVIDOR)
        if res == "ok":
            return
        elif res == "win":
            p_error_(None, f"{__TR__('NO_DISPONILBE_WIN')}", 3)
        else:
            p_error_(None, res, 3)
        
    ############

    button2 = QPushButton(f"{__TR__('EJECUTAR')}")
    button2.clicked.connect(ejec_)
    button2.setProperty("tipo", "button1")

    button3 = QPushButton(f"{__TR__('CERRAR')}")
    button3.clicked.connect(VENTANA39.close)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    # Layout para los botones
    button_layout = QHBoxLayout()

    # Agregar los botones al layout 
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Botones a la derecha
    button_layout.addStretch()

    # Agregar el layout
    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA39.setCentralWidget(widget_principal)

    VENTANA39.show()
    return VENTANA39

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Escaneo de dominios - WORDLIST, WHOIS, etc

def pF_escaneo_TLD_wordlist_(ventana):
    global VENTANA40
    VENTANA40 = QMainWindow()
    VENTANA40.timer = QTimer()

    if FuncMainPY.obt_json_(8) != True:
        VENTANA40.close()
        return p_error_(ventana, f"{__TR__('ACEPTAR_TERMINOS')}", 5)

    VENTANA40.setMinimumSize(700, 600)
    VENTANA40.setWindowTitle("AILI-SS")

    # Estilo general
    VENTANA40.setStyleSheet(FuncMainPY.estilos_())

    # Layout principal
    main_layout = QVBoxLayout()

    ############

    # Layout 
    header_layout = QHBoxLayout()

    # Imagen
    global img_label
    img_label = QLabel()
    pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/Logo.png")
    pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    img_label.setPixmap(pixmap)

    # Título
    title_label = QLabel(f"{__TR__('ESCANEO_DOMINIO_WORDLIST_TITULO')}")
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding-left: 10px;")

    header_layout.addWidget(img_label)
    header_layout.addWidget(title_label)
    header_layout.addStretch()

    main_layout.addLayout(header_layout)
    
    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    grid_layout = QGridLayout()

    ############
    
    label = QLabel(f"URL:")
    config_entrada0 = QLineEdit()

    grid_layout.addWidget(label, 0, 0)
    grid_layout.addWidget(config_entrada0, 1, 0)
    
    config_entrada0.setPlaceholderText(f"https://aili-ss.pages.dev")

    ############

    main_layout.addLayout(grid_layout)

    ############

    text_edit = QTextEdit()
    text_edit.setText(f"{__TR__('P_TLD_EXPLICACION')}")
    text_edit.setReadOnly(True)
    text_edit.setObjectName("BlogText")
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

    VENTANA40.resizeEvent = lambda event: adjust_text_edit_height(VENTANA40, text_edit)
    def adjust_text_edit_height(window, text_edit):
        text_edit.setFixedHeight(int(window.height() * 0.65))
    
    main_layout.addWidget(text_edit)

    ############

    class TextoUpdater(QObject):
        signal_actualizar = Signal(str)

    updater = TextoUpdater()

    def manejar_html(html):
        try:
            text_edit.setHtml(html)
            text_edit.moveCursor(QTextCursor.End)
            QApplication.processEvents()
        except Exception:
            global stop_thread
            stop_thread = True

    updater.signal_actualizar.connect(manejar_html)

    def actualizar_texto(html):
        bar = text_edit.verticalScrollBar()
        pos = bar.value()

        updater.signal_actualizar.emit(html)
        bar.setValue(pos)

    ############

    def camb_():
        try: button0.clicked.disconnect()
        except: pass
        button0.clicked.connect(camb_)

        pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoReloj.png")
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        img_label.setPixmap(pixmap)

        button0.setEnabled(False)

        ############

        texto_poner_ = ""
        URL = config_entrada0.text()
        if URL.endswith("/"): URL = URL[:-1]

        if stop_thread: return

        ############ DETECTAR SI LA URL ES ALCANZABLE

        try:
            SOLICITUD = requests.get(URL)
        except:
            button0.setEnabled(True)

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoX.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

            actualizar_texto(f"{__TR__('URL_INVALIDO')}")
            return

        ############ DETECTAR DOMINIO

        actualizar_texto(f"{__TR__('AILI_ANALIZANDO')} - DNS")
        if stop_thread: return

        parsed_url = urlparse(URL)
        HOSTNAME = parsed_url.hostname
        IP_DETECTADA = socket.gethostbyname(HOSTNAME)

        if str(HOSTNAME) == str(IP_DETECTADA):
            texto_poner_ = f"HOST: <span style='color: {FuncMainPY.obt_json_(7)};'>{IP_DETECTADA}</span> / <span style='color: red;'>{__TR__('NO_PUDO_DETECTAR_DNS')}</span>"
        else:
            texto_poner_ = f"HOST: <span style='color: {FuncMainPY.obt_json_(7)};'>{IP_DETECTADA}</span> / <span style='color: {FuncMainPY.obt_json_(7)};'>{HOSTNAME}</span>"
        
        actualizar_texto(texto_poner_)

        if stop_thread: return

        ############ WHOIS
        
        actualizar_texto(f"{texto_poner_} <br> {__TR__('AILI_ANALIZANDO')} - WHOIS")
        if stop_thread: return

        texto_poner_ += f"<br><br> {'_'*50} <br><br> <span style='color: {FuncMainPY.obt_json_(6)};'>WHOIS</span>:"
        
        try:
            WHOIS_resultado = whois_lib.whois(URL)

            texto_poner_ += f""" <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.domain_name}</span> <br>
            <br>
            Registrar: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.registrar}</span> <br>
            Registrar URL: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.registrar_url}</span> <br>
            Reseller: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.reseller}</span> <br>
            <br>
            WHOIS Server: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.whois_server}</span> <br>
            Referral URL: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.referral_url}</span> <br>
            <br>
            Updated date: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.updated_date}</span> <br>
            Creation date: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.creation_date}</span> <br>
            Expiration date: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.expiration_date}</span> <br>
            <br>
            Name servers: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.name_servers}</span> <br>
            <br>
            Status: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.status}</span> <br>
            <br>
            E-Mails: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.emails}</span> <br>
            <br>
            DNSSEC: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.dnssec}</span> <br>
            <br>
            Name: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.name}</span> <br>
            ORG: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.org}</span> <br>
            <br>
            Address: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.address}</span> <br>
            City: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.city}</span> <br>
            State: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.state}</span> <br>
            Registrant postal code: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.registrant_postal_code}</span> <br>
            Country: <span style='color: {FuncMainPY.obt_json_(7)};'>{WHOIS_resultado.country}</span> <br>

            """

        except:
            texto_poner_ += f" {__TR__('SIN_INFO_WHOIS')}"
        
        actualizar_texto(texto_poner_)
        if stop_thread: return

        ############ WORDLIST

        texto_poner_ += f"""<br> {'_'*50} <br><br> <span style='color: {FuncMainPY.obt_json_(6)};'>WORDLIST</span>: <br>"""
        actualizar_texto(texto_poner_ + f"<br>{__TR__('CONTACTANDO')}")

        if os.path.exists(os.path.join(conseguir_RUTA_DIR_USUARIO_(), "wordlist.txt")):
            with open(os.path.join(conseguir_RUTA_DIR_USUARIO_(), "wordlist.txt"), "r") as f:
                PALABRAS = str(f.read()).split("\n")

            for i in PALABRAS:
                try:
                    SOLICITUD = requests.get(f"{URL}/{i}")

                    if str(SOLICITUD.status_code) != "404":
                        texto_poner_ += f"""<br> {SOLICITUD.elapsed} • <span style='color: {FuncMainPY.obt_json_(7)};'>{URL}/{i}</span> • {SOLICITUD.reason} ({SOLICITUD.status_code})"""
                        actualizar_texto(texto_poner_ + f"<br><br>{__TR__('CONTACTANDO')}")

                except Exception as Error_e:
                    texto_poner_ += f"""<br> ERROR • <span style='color: {FuncMainPY.obt_json_(7)};'>{URL}/{i}</span> • {Error_e}"""
                    actualizar_texto(texto_poner_ + f"<br><br>{__TR__('CONTACTANDO')}")

        else:
            texto_poner_ += f"""<br> ERROR • <span style='color: {FuncMainPY.obt_json_(7)};'>{os.path.join(conseguir_RUTA_DIR_USUARIO_(), "wordlist.txt")}</span>"""
            actualizar_texto(texto_poner_)

        texto_poner_ += f"<br><br> {'_'*50}"

        actualizar_texto(texto_poner_)

        ############ FINAL

        if True: # siempre :)
            button0.setEnabled(True)
            try: button0.clicked.disconnect()
            except: pass
            button0.setText(f"{__TR__('EXPORTAR')}")
            button0.clicked.connect(lambda: pF_exportar_res_(VENTANA40, texto_poner_, 8))

            cursor = text_edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            text_edit.setTextCursor(cursor)

            pixmap = QPixmap(f"{RUTA_RECURSOS}/Logos/IconoV.png")
            pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            img_label.setPixmap(pixmap)

    ############

    spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    main_layout.addItem(spacer)

    ############

    def start_thread():
        global stop_thread, thread
        stop_thread = False
        thread = threading.Thread(target=camb_)
        thread.start()
    
    ############

    button0 = QPushButton(f"{__TR__('EMPEZAR')}")
    button0.clicked.connect(start_thread)
    button0.setProperty("tipo", "button1")

    ############

    def hide_show_():
        VENTANA40.close()
        ventana.show()

    button3 = QPushButton(f"{__TR__('VOLVER_ATRAS')}")
    button3.clicked.connect(hide_show_)
    button3.setShortcut("Escape")
    button3.setProperty("tipo", "button2")

    ############

    button1 = QPushButton(f"{__TR__('IR_CONFIG')}")
    button1.clicked.connect(lambda: p_configuracion_(VENTANA40))
    button1.setProperty("tipo", "button1")

    ############

    button_layout = QHBoxLayout()

    button_layout.addWidget(button0)
    button_layout.addWidget(button3)
    button_layout.addStretch()

    ############

    main_layout.addLayout(button_layout)

    ############

    widget_principal = QWidget()
    widget_principal.setLayout(main_layout)
    VENTANA40.setCentralWidget(widget_principal)

    VENTANA40.show()
    ventana.hide()
    return VENTANA40

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# (Las que por alguna razón se eliminaron)

# LIBRE - VENTANA5, VENTANA6, VENTANA7, VENTANA8, VENTANA12, VENTANA22, 
#         VENTANA26, VENTANA31, VENTANA32

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

print(f"\nAILI-SS • Por Adrián L. G. P.\n")
print(f"Inicio:\t\t\t{TIEMPO_INICIO.strftime('%d/%m/%Y, %H:%M:%S')}")
print(f"Ejecutándose desde:\t{os.path.abspath('.')}")
print(f"Recursos en:\t\t{os.path.abspath(RUTA_RECURSOS)}")
print(f"Carpeta del usuario:\t{os.path.abspath(conseguir_RUTA_DIR_USUARIO_())}\n")
print("="*28)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def main(e=None):
    
    # Función para descargar las dependencias
    def cargar_dependencias():
        time.sleep(1)
        w.close()


        global VENTANA99 # Solo se referencia, sino se cierra
        if FuncMainPY.r_gr_(2): VENTANA99 = p_principal_(None)
        else:
            if IDIOMA_ELEGIDO == True:
                VENTANA99 = p_terminos_()
            else:
                VENTANA99 = p_idioma_()
    
    global app
    app = QApplication(sys.argv)
    
    #QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    #QGuiApplication.highDpiScaleFactorRoundingPolicy()

    app.setWindowIcon(QIcon(f"{RUTA_RECURSOS}/Logos/Logo.ico"))
    w = p_carga_()
    w.show()
    QTimer.singleShot(100, lambda: cargar_dependencias())

    sys.exit(app.exec())


if __name__ == "__main__": main()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

# C:\Users\USER\AILISS_v2
# /etc/AILISS_v2

# C:\Users\USER\AILISS_v2\Temp\
# /etc/AILISS_v2/Temp/

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~