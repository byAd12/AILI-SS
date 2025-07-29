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

import os, subprocess, json, psutil, socket, datetime, struct, nmap, netifaces, asyncio, requests, sys, hashlib, pywifi, ipaddress, platform
from scapy.all import *
from scapy.all import (
    IP, ARP, Ether, sniff, TCP, UDP, ICMP, DNS,
    send, sr, hexdump, Raw, wrpcap, rdpcap, ls
)
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, RandMAC
from cryptography.fernet import Fernet

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, QThread
import matplotlib.pyplot as plt
from bleak import BleakScanner
from string import Template

from pywifi import const

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ruta de ejecución

if getattr(sys, 'frozen', False): RUTA_RECURSOS = os.path.join(sys._MEIPASS, "Recursos") # Windows .exe
else: RUTA_RECURSOS = "Recursos" # Código .py

def conseguir_RUTA_DIR_USUARIO_():
    if os.name == "nt":
        RUTA_DIR_USUARIO = os.path.join(os.environ.get("USERPROFILE", os.path.expanduser("~")), "AILISS_v2")
    else:
        RUTA_DIR_USUARIO = os.path.join(os.path.expanduser("~"), "AILISS_v2")
    
    return RUTA_DIR_USUARIO

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Registrar errores

def ERR_REG_(error):
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
    
    if error == "--Limpiar--":
        with open(os.path.join(RUTA_DIR_USUARIO, "Errores.log"), "w", encoding="utf-8") as f:
            f.write("")
        return
    
    with open(os.path.join(RUTA_DIR_USUARIO, "Errores.log"), "a", encoding="utf-8") as f:
        f.write(str(datetime.now()) + "  -  " + str(error))
    
    return

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Obtener texto del JSON

def obt_json_(opc):
    ruta_config = obtener_ruta_config()
    with open(ruta_config, "r") as json_final: cont = json.load(json_final)

    if opc == 0: return cont["APP_BASE"]
    if opc == "01": return cont["APP_LETRA_BASE"]
    if opc == 1: return cont["BACKG_BASE"]
    if opc == 2: return cont["LETRA_BASE"]
    if opc == 3: return cont["BOTON1_BASE"]
    if opc == 4: return cont["BOTON2_BASE"]
    if opc == 5: return cont["INTERFAZ"]
    if opc == 6: return cont["COLOR_RESALTE_TITULO"]
    if opc == 7: return cont["COLOR_IMPORT_LICENCIA"]
    if opc == 8: return cont["TERMINOS"]
    if opc == "IDIOMA": return cont["IDIOMA"]

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ruta de configuración (cross-platform y sin permisos)

def obtener_ruta_config():
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

    os.makedirs(RUTA_DIR_USUARIO, exist_ok=True)
    os.makedirs(os.path.join(RUTA_DIR_USUARIO, "Temp"), exist_ok=True)

    for i in [os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), os.path.join(RUTA_DIR_USUARIO, "Errores.log"), os.path.join(RUTA_DIR_USUARIO, "Config.json"), os.path.join(RUTA_DIR_USUARIO, "ConfigTemaPers.json")]:
        if not os.path.exists(i):
            with open(i, "w", encoding="utf-8") as f:
                pass

    return os.path.join(RUTA_DIR_USUARIO, "Config.json")

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# TRADUCCIÓN AJUSTADA

with open(os.path.join(RUTA_RECURSOS, "TRANSLATE.json"), "r", encoding="utf-8") as TR_FILE_:
    TRADUCCIONES_COMPLETAS = json.load(TR_FILE_)



def __TR__(STRING, ES_TERMINOS=False, ES_BLOG=False):
    if ES_TERMINOS == True:
        try:
            texto_base = TRADUCCIONES_COMPLETAS[obt_json_("IDIOMA")]["terminos"][STRING]
        except:
            ERR_REG_(f"[__TR__] Faltó variable para sustituir: {STRING}\n\n")
            return "Error_Idioma"
        
    elif ES_BLOG == True:
        try:
            texto_base = TRADUCCIONES_COMPLETAS[obt_json_("IDIOMA")]["blog"][STRING]
        except:
            ERR_REG_(f"[__TR__] Faltó variable para sustituir: {STRING}\n\n")
            return "Error_Idioma"
    
    else:
        try:
            texto_base = TRADUCCIONES_COMPLETAS[obt_json_("IDIOMA")]["Recursos/Func/main.py"][STRING]
        except:
            ERR_REG_(f"[__TR__] Faltó variable para sustituir: {STRING}\n\n")
            return "Error_Idioma"
    
    ####

    plantilla = Template(texto_base)

    variables = {
        "version": obt_aili_json_(0),
        "FuncMainPY_obt_json_0": obt_json_(0),
        "FuncMainPY_obt_json_1": obt_json_(1),
        "FuncMainPY_obt_json_2": obt_json_(2),
        "FuncMainPY_obt_json_3": obt_json_(3),
        "FuncMainPY_obt_json_4": obt_json_(4),
        "FuncMainPY_obt_json_5": obt_json_(5),
        "FuncMainPY_obt_json_6": obt_json_(6),
        "FuncMainPY_obt_json_7": obt_json_(7),
        "FuncMainPY_obt_json_8": obt_json_(8),
        "Dolar": "$",
        "NMAP_VERSION": version_nmap(),
    }

    try:
        return plantilla.substitute(variables)
    except KeyError as e:
        return texto_base

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Estilos CSS

def estilos_():
    finales = """
QWidget {background-color: APP_BASE; font-family: Arial; font-size: 17px;}

QLabel, QLineEdit {color: APP_LETRA_BASE;}

QMenu{border: 1px solid APP_LETRA_BASE;}
QMenuBar::item {font-size: 10px; background-color: BACKG_BASE; color: APP_LETRA_BASE; border-bottom-right-radius: 10px; padding: 5px 10px; border-bottom: 1px solid BACKG_BASE; border-right: 1px solid BACKG_BASE;}
QMenuBar::item::selected {background-color: APP_BASE; color: APP_LETRA_BASE; border-bottom: 1px solid APP_LETRA_BASE; border-right: 1px solid APP_LETRA_BASE;}

QMenu::item {background-color: APP_BASE; color: APP_LETRA_BASE;}
QMenu::item::selected {background-color: lightblue; color: black;}
QMenu::separator {background-color: lightblue; height: 1px; margin: 5px 10% 5px 10%;}

QTextEdit#TerminosText {font-size: 16px; padding: 10px; color: APP_LETRA_BASE;}
QTextEdit#BlogText {font-size: 19px; padding: 10px; color: APP_LETRA_BASE; font-family: Arial;}

QScrollBar:vertical {border: 1px solid APP_LETRA_BASE;  background: APP_BASE; width: 8px; margin: 0; border-radius: 6px;}
QScrollBar::handle:vertical {background: #2A3139; min-height: 20px;}
QScrollBar::handle:vertical:hover {background: #555;}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {height: 0px;}

QComboBox, QComboBox QAbstractItemView {color: APP_LETRA_BASE; border: 1.4px solid APP_LETRA_BASE;}

QPushButton                 {background-color: BACKG_BASE; border: 1px solid BACKG_BASE; color: LETRA_BASE; font-size: 14px; padding: 5px 15px; border-radius: 0; border-top-left-radius: 10px; border-bottom-right-radius: 10px;}
QPushButton[tipo="button3"] {background-color: lightblue; color: black; border: 1px solid lightblue;}
QPushButton:hover           {background-color: blue; color: LETRA_BASE;}

QPushButton[tipo="button1"]:hover {border: 1px solid BOTON1_BASE; background-color: rgba(255,255,255,0); color: LETRA_BASE;}
QPushButton[tipo="button2"]:hover {background-color: BOTON2_BASE; color: LETRA_BASE;}
QPushButton[tipo="button3"]:hover {border: 1px solid BOTON1_BASE; background-color: rgba(255,255,255,0); color: LETRA_BASE;}

QPushButton#buttonNOESTILOS {background: none; border: none; border-radius: 0px;}
QPushButton#buttonNOESTILOS:hover {background: none; border: 1px solid BOTON1_BASE; border-radius: 10px;}
"""
    with open(obtener_ruta_config(), "r") as f: data = json.load(f)

    finales = finales.replace("APP_BASE", data["APP_BASE"])
    finales = finales.replace("APP_LETRA_BASE", data["APP_LETRA_BASE"])
    finales = finales.replace("BACKG_BASE", data["BACKG_BASE"])
    finales = finales.replace("LETRA_BASE", data["LETRA_BASE"])
    finales = finales.replace("BOTON1_BASE", data["BOTON1_BASE"])
    finales = finales.replace("BOTON2_BASE", data["BOTON2_BASE"])

    placeholders = ["APP_BASE", "APP_LETRA_BASE", "BACKG_BASE", "LETRA_BASE", "BOTON1_BASE", "BOTON2_BASE"]

    for ph in placeholders:
        if ph not in data:
            print(f"Falta definir el color para {ph}")

    return finales

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Cambiar valores de la configuración

def config_cambiar_(a1=None, a2=None, a3=None, a4=None):
    with open(obtener_ruta_config(), "r") as f: data = json.load(f)
    if a1 != None: data["BACKG_BASE"] = a1
    if a2 != None: data["LETRA_BASE"] = a2
    if a3 != None: data["BOTON1_BASE"] = a3
    if a4 != None: data["BOTON2_BASE"] = a4
    with open(obtener_ruta_config(), "w") as f: data = json.dump(data, f)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 1

def blog_():
    return f"""1/6 • <span style='color: {obt_json_(7)};'>10/05/2025</span> • AILI-SS<br><br>
{__TR__('T1',False,True)}<br><br>
{__TR__('T1.1',False,True)}<br><br>
{__TR__('P1.1',False,True)}<br><br>
{__TR__('T1.2',False,True)}<br><br>
{__TR__('P1.2',False,True)}<br><br>
{__TR__('T1.3',False,True)}<br><br>
{__TR__('P1.3',False,True)}<br><br>
{__TR__('T1.4',False,True)}<br><br>
{__TR__('P1.4',False,True)}<br><br>
{__TR__('T1.5',False,True)}<br><br>
{__TR__('P1.5',False,True)}
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 2

def blog_2_():
    return f"""2/6 • <span style='color: {obt_json_(7)};'>18/06/2025</span> • AILI-SS<br><br>
{__TR__('T2',False,True)}<br><br>
{__TR__('T2.1',False,True)}<br><br>
{__TR__('P2.1',False,True)}<br><br>
{__TR__('T2.2',False,True)}<br><br>
{__TR__('P2.2',False,True)}
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 3

def blog_3_():
    return f"""3/6 • <span style='color: {obt_json_(7)};'>18/06/2025</span> • AILI-SS<br><br>
{__TR__('T3',False,True)}<br><br>
{__TR__('T3.1',False,True)}<br><br>
{__TR__('P3.1',False,True)}
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 4

def blog_4_():
    return f"""4/6 • <span style='color: {obt_json_(7)};'>21/06/2025</span> • AILI-SS<br><br>
{__TR__('T4',False,True)}<br><br>
{__TR__('T4.1',False,True)}<br><br>
{__TR__('P4.1',False,True)}<br><br>
{__TR__('T4.2',False,True)}<br><br>
{__TR__('P4.2',False,True)}<br><br>
{__TR__('T4.3',False,True)}<br><br>
{__TR__('P4.3',False,True)}<br><br>
{__TR__('T4.4',False,True)}<br><br>
{__TR__('P4.4',False,True)}<br><br>
{__TR__('T4.5',False,True)}<br><br>
{__TR__('P4.5',False,True)}
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 4

def blog_5_():
    return f"""5/6 • <span style='color: {obt_json_(7)};'>28/07/2025</span> • AILI-SS<br><br>
{__TR__('T5',False,True)}<br><br>
{__TR__('T5.1',False,True)}<br><br>
{__TR__('P5.1',False,True)}
{__TR__('T5.2',False,True)}<br><br>
{__TR__('P5.2',False,True)}<br><br>
{__TR__('T5.3',False,True)}<br><br>
{__TR__('P5.3',False,True)}<br><br>
{__TR__('T5.4',False,True)}<br><br>
{__TR__('P5.4',False,True)}<br><br>
{__TR__('T5.5',False,True)}<br><br>
{__TR__('P5.5',False,True)}<br><br>
{__TR__('T5.6',False,True)}<br><br>
{__TR__('P5.6',False,True)}
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Blog - 6

def blog_6_():
    return f"""6/6 • <span style='color: {obt_json_(7)};'>© 2024 - {datetime.now().strftime('%Y')}</span> • AILI-SS<br><br>
Adrián L. G. P.<br>
adgimenezp@gmail.com<br>
byad12.pages.dev<br><br>
aili-ss.pages.dev
"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Contenido Términos

def terminos_():  #### NO TRADUCIR
    return f"""<span style='color: {obt_json_(7)};'>03/05/2025</span> • AILI-SS<br><br>

1. <span style='color: {obt_json_(6)};'>{__TR__('T1', True)}</span><br><br>

{__TR__('P1', True)}<br><br><br>


2. <span style='color: {obt_json_(6)};'>{__TR__('T2', True)}</span><br><br>

{__TR__('P2', True)}<br><br><br>


3. <span style='color: {obt_json_(6)};'>{__TR__('T3', True)}</span><br><br>

{__TR__('P3', True)}<br>
{__TR__('P32', True)}<br><br><br>


4. <span style='color: {obt_json_(6)};'>{__TR__('T4', True)}</span><br><br>

{__TR__('P4', True)}<br><br><br>


5. <span style='color: {obt_json_(6)};'>{__TR__('T5', True)}</span><br><br>

{__TR__('P5', True)}"""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Crear directorios (usando carpeta segura)

def crear_directorios_():
    ruta_config = obtener_ruta_config()

    if os.path.exists(ruta_config):
        try:
            with open(ruta_config, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "APP_BASE" not in data:
                return gen_json_()
        except json.JSONDecodeError:
            return gen_json_()
        return False

    return gen_json_()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Generar JSON

def gen_json_(IDIOMA_=False):
    basico = {
        "APP_BASE": "#2A3139",
        "APP_LETRA_BASE": "white",
        "BACKG_BASE": "#4a4a4a",
        "LETRA_BASE": "white",
        "BOTON1_BASE": "#008fff",
        "BOTON2_BASE": "red",
        "COLOR_RESALTE_TITULO": "#008fff",
        "COLOR_IMPORT_LICENCIA": "orange",
        "INTERFAZ": None,
        "TERMINOS": "No acepto.",
        "IDIOMA": "es-ESPAÑA"if IDIOMA_ == False else IDIOMA_
    }

    ruta_config = obtener_ruta_config()

    with open(ruta_config, "w") as json_final:
        json.dump(basico, json_final)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Obtener texto de AILI_info.json

def obt_aili_json_(opc):
    try:
        with open(os.path.join(RUTA_RECURSOS, "AILI_info.json"), "r") as json_final: cont = json.load(json_final)
        if opc == 0: return cont["App"]["Version"]
    except:
        return f"2.0 ({__TR__('ERROR_CARGANDO_AILI_JSON')})"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Guardar texto en el JSON

def gua_json_(opc0, opc01, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, opc9):
    cambios = {
        "APP_BASE": opc0,
        "APP_LETRA_BASE": opc01,
        "BACKG_BASE": opc1,
        "LETRA_BASE": opc2,
        "BOTON1_BASE": opc3,
        "BOTON2_BASE": opc4,
        "COLOR_RESALTE_TITULO": opc6,
        "COLOR_IMPORT_LICENCIA": opc7,
        "INTERFAZ": opc5,
        "TERMINOS": opc8,
        "IDIOMA": opc9
    }

    ruta_config = obtener_ruta_config()

    with open(ruta_config, "w") as json_final:
        json.dump(cambios, json_final)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Conseguir de la BB.DD datos

def Conseguir_Datos_LLave(): # Solo si hay llave registrada
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()

    with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "r", encoding="utf-8") as f: clave = f.read()
    llave = int(clave.split(",-")[0])

    response = requests.get(f"https://aili-mongodb.onrender.com/data/{llave}")

    if response.status_code == 200:
        try:   return response.json()
        except: ERR_REG_(f"[Conseguir_Datos_LLave] Request código de error {response.status_code}\n\n")

    return "Error."

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Registrar la clave en el sistema

def registrar_clave_(clave):
    if clave == None or clave == "":
        return "Vacio"
    
    try:
        response = requests.get(f"https://aili-mongodb.onrender.com/registrar/{clave}")
    except:
        return "NoInternet"

    try:
        return response.json()
    except:
        return response.text

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Guardar la clave registrada

def r_gu_(clave): 
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
    with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "w", encoding="utf-8") as f: f.write(f"{clave},-1,-{datetime.now()}")
    return True

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Borrar la clave registrada

def r_bu_(): 
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
    with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "w", encoding="utf-8") as f: f.write("")
    return True

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Mirar si la clave ya fue registrada

def r_gr_(tipo):               # Se llama primero
    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
   
    with open(os.path.join(RUTA_DIR_USUARIO, "Temp", "Temp.txt"), "r", encoding="utf-8") as f: cont = f.read()

    try:
        if tipo == 1: # Clave
            return str(cont.split(",-")[0])
    except:
        return False
    try:
        if tipo == 2: # Si fue registrado correctamente (True/False)
            if str(cont.split(",-")[1]) == "1":
                return True
    except:
        return False
    try:
        if tipo == 3: # Cuando se registró
            return str(cont.split(",-")[2])
    except:
        return False

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Coger las interfaces activas

def INTERFACES_():
    interfaces_activas = []
    interfaces = psutil.net_if_addrs()

    for interfaz, direcciones in interfaces.items():
        for direccion in direcciones:
            if direccion.family == socket.AF_INET and direccion.address != "127.0.0.1" and not interfaz.startswith("Conexión"):
                interfaces_activas.append(interfaz)

    return interfaces_activas

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Coger IP y máscara

def get_network_data(interfaz_config, e=None):
    net_if_addrs = psutil.net_if_addrs()
    net_if_stats = psutil.net_if_stats()

    if interfaz_config not in net_if_addrs and e != 2:
        return None  # Interfaz no encontrada

    if e is None: # IPv4 y máscara
        for addr in net_if_addrs[interfaz_config]:
            if addr.family == socket.AF_INET:
                return [addr.address, addr.netmask]

    elif e == 1: # MAC
        for addr in net_if_addrs[interfaz_config]:
            try:
                if addr.family == psutil.AF_LINK or addr.family == socket.AF_PACKET:
                    return [str(addr.address).replace("-", ":")]
            except: 
                return "-"

    elif e == 2: # Gateway 
        gateways = netifaces.gateways()
        default_gateway = gateways.get('default', {}).get(netifaces.AF_INET)
        if default_gateway:
            gateway_ip = default_gateway[0]
            return gateway_ip
        return None

    return None

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular las partes de la IP

def CALCULAR_PARTES__(INTERFAZ_DADA_, ip=None, mascara=None):
    try:
        def FUNCION_GUAPA_(ip_decimal):
            bin_ip = ""
            partes = ip_decimal.split(".")
            for i, parte in enumerate(partes):
                binario = bin(int(parte))[2:].zfill(8)
                bin_ip += binario + ("." if i < 3 else "")
            return bin_ip

        if ip is None:
            ip_bin = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[0])
        else:
            ip_bin = FUNCION_GUAPA_(ip)

        if mascara is None:
            mascara_bin = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[1])
        else:
            mascara_bin = FUNCION_GUAPA_(mascara)

        bits_red = mascara_bin.replace(".", "").count("1")
        ip_bin_sin_puntos = ip_bin.replace(".", "")

        resultado_coloreado = ""
        for i, bit in enumerate(ip_bin_sin_puntos):
            color = str(obt_json_(6)) if i < bits_red else str(obt_json_(7))
            resultado_coloreado += f"<span style='color: {color};'>{bit}</span>"
            if (i + 1) % 8 == 0 and i < 31:
                resultado_coloreado += "."

        return resultado_coloreado

    except Exception as e:
        return "Error"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular máscara binaria

def CALCULAR_MASCARA_BINARIA__(mascara=None):
    try:
        #################################################
        def FUNCION_GUAPA_(oplk):
            ip_bin = ""
            ip2 = oplk.split(".")

            z = 0
            for i in ip2:
                z += 1
                ip_bin += str(bin(int(i))).replace("0b","") + ("." if z < 4 else "")

            salida_definita_sexy_perra_si_qwerty = ""
            zxzxzxzx = 0

            for i in ip_bin.split("."):
                
                zxzxzxzx += 1
                salida, zz1 = "", 0
                if len(i) < 8:
                    while zz1 < int(str(int(len(i))-8).replace("-","")):
                        zz1 += 1
                        salida += "0"
                    salida += str(i)
                    salida_definita_sexy_perra_si_qwerty += f"{salida}." + ("." if zxzxzxzx < 4 else "")
                else:
                    salida_definita_sexy_perra_si_qwerty += f"{i}" + ("." if zxzxzxzx < 4 else "")

            return salida_definita_sexy_perra_si_qwerty.replace("..",".")


        masc_final_sexy = str(FUNCION_GUAPA_(mascara)) # decimal a binario

        #################################################

        pr_gr_mm = masc_final_sexy.split(".")[0]
        se_gr_mm = masc_final_sexy.split(".")[1]
        te_gr_mm = masc_final_sexy.split(".")[2]
        cu_gr_mm = masc_final_sexy.split(".")[3]

        return(f"{pr_gr_mm}.{se_gr_mm}.{te_gr_mm}.{cu_gr_mm}")

        #################################################
    
    except:
        return "Error"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular bits de red y host

def CALCULAR_BITS__(mascara=None):
    try:
        #################################################
        def FUNCION_GUAPA_(oplk):
            ip_bin = ""
            ip2 = oplk.split(".")

            z = 0
            for i in ip2:
                z += 1
                ip_bin += str(bin(int(i))).replace("0b","") + ("." if z < 4 else "")

            salida_definita_sexy_perra_si_qwerty = ""
            zxzxzxzx = 0

            for i in ip_bin.split("."):
                
                zxzxzxzx += 1
                salida, zz1 = "", 0
                if len(i) < 8:
                    while zz1 < int(str(int(len(i))-8).replace("-","")):
                        zz1 += 1
                        salida += "0"
                    salida += str(i)
                    salida_definita_sexy_perra_si_qwerty += f"{salida}." + ("." if zxzxzxzx < 4 else "")
                else:
                    salida_definita_sexy_perra_si_qwerty += f"{i}" + ("." if zxzxzxzx < 4 else "")

            return salida_definita_sexy_perra_si_qwerty.replace("..",".")


        masc_final_sexy = str(FUNCION_GUAPA_(mascara)) # decimal a binario

        #################################################

        masc_pura = masc_final_sexy.replace(".", "")
        bits_red = masc_pura.count("1")
        bits_host = masc_pura.count("0")
        return [bits_red, bits_host]

        #################################################
    
    except:
        return "Error"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular dirección de red

def CALCULAR_DIRECCION_RED__(INTERFAZ_DADA_, ip=None, mascara=None):
    try:
        #################################################
        def FUNCION_GUAPA_(oplk):
            ip_bin = ""
            ip2 = oplk.split(".")

            z = 0
            for i in ip2:
                z += 1
                ip_bin += str(bin(int(i))).replace("0b","") + ("." if z < 4 else "")

            salida_definita_sexy_perra_si_qwerty = ""
            zxzxzxzx = 0

            for i in ip_bin.split("."):
                
                zxzxzxzx += 1
                salida, zz1 = "", 0
                if len(i) < 8:
                    while zz1 < int(str(int(len(i))-8).replace("-","")):
                        zz1 += 1
                        salida += "0"
                    salida += str(i)
                    salida_definita_sexy_perra_si_qwerty += f"{salida}." + ("." if zxzxzxzx < 4 else "")
                else:
                    salida_definita_sexy_perra_si_qwerty += f"{i}" + ("." if zxzxzxzx < 4 else "")

            return salida_definita_sexy_perra_si_qwerty.replace("..",".")

        print("="*60)

        if ip == None:
            ip_final_sexy = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[0])
        else:
            ip_final_sexy = FUNCION_GUAPA_(ip) # decimal a binario
        
        if mascara == None:
            masc_final_sexy = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[1])
        else:
            masc_final_sexy = str(FUNCION_GUAPA_(mascara)) # decimal a binario

        #################################################

        pr_gr_ip = ip_final_sexy.split(".")[0]
        se_gr_ip = ip_final_sexy.split(".")[1]
        te_gr_ip = ip_final_sexy.split(".")[2]
        cu_gr_ip = ip_final_sexy.split(".")[3]

        pr_gr_mm = masc_final_sexy.split(".")[0]
        se_gr_mm = masc_final_sexy.split(".")[1]
        te_gr_mm = masc_final_sexy.split(".")[2]
        cu_gr_mm = masc_final_sexy.split(".")[3]

        #################################################

        def CALCULAR_DIRECCIO_SEXY_RED_(asadasd1, asadasd2):
            ip_num = int(asadasd1, 2)
            mm_num = int(asadasd2, 2)
            result = ip_num & mm_num
            ip_bin = str(bin(result)).replace("0b", "")
            zxzxzxzx, salida_definita_sexy_perra_si_qwerty = 0, ""

            for i in ip_bin.split("."):
                
                zxzxzxzx += 1
                salida, zz1 = "", 0
                if len(i) < 8:
                    while zz1 < int(str(int(len(i))-8).replace("-","")):
                        zz1 += 1
                        salida += "0"
                    salida += str(i)
                    salida_definita_sexy_perra_si_qwerty += f"{salida}." + ("." if zxzxzxzx < 4 else "")
                else:
                    salida_definita_sexy_perra_si_qwerty += f"{i}" + ("." if zxzxzxzx < 4 else "")
            
            return str(salida_definita_sexy_perra_si_qwerty).replace("..", ".")


        salida_final_definitiva_hungahunga_pepinillo_IP_ = f"{CALCULAR_DIRECCIO_SEXY_RED_(pr_gr_ip,pr_gr_mm)}{CALCULAR_DIRECCIO_SEXY_RED_(se_gr_ip, se_gr_mm)}{CALCULAR_DIRECCIO_SEXY_RED_(te_gr_ip, te_gr_mm)}{CALCULAR_DIRECCIO_SEXY_RED_(cu_gr_ip, cu_gr_mm)}"

        #################################################

        print(ip_final_sexy)
        print(masc_final_sexy)
        print(salida_final_definitiva_hungahunga_pepinillo_IP_)
        print("-"*60, "\n\n")

        #################################################
        #################################################
        # CALCULAR EL DECIMAL

        grups_binarios_ = salida_final_definitiva_hungahunga_pepinillo_IP_.split(".")
        resultado_decimal_ = ""

        salida_decimal1 = 0
        salida_decimal2 = 0
        salida_decimal3 = 0
        salida_decimal4 = 0

        zzzzxds = 0

        for i in grups_binarios_:
            print("-"*10, i)
            zzzzxds += 1
            if i and zzzzxds == 1:
                if i[0] == "1": salida_decimal1 += 128; print(128)
                if i[1] == "1": salida_decimal1 += 64; print(64)
                if i[2] == "1": salida_decimal1 += 32; print(32)
                if i[3] == "1": salida_decimal1 += 16; print(16)
                if i[4] == "1": salida_decimal1 += 8; print(8)
                if i[5] == "1": salida_decimal1 += 4; print(4)
                if i[6] == "1": salida_decimal1 += 2; print(2)
                if i[7] == "1": salida_decimal1 += 1; print(1)
            if i and zzzzxds == 2:
                if i[0] == "1": salida_decimal2 += 128; print(128)
                if i[1] == "1": salida_decimal2 += 64; print(64)
                if i[2] == "1": salida_decimal2 += 32; print(32)
                if i[3] == "1": salida_decimal2 += 16; print(16)
                if i[4] == "1": salida_decimal2 += 8; print(8)
                if i[5] == "1": salida_decimal2 += 4; print(4)
                if i[6] == "1": salida_decimal2 += 2; print(2)
                if i[7] == "1": salida_decimal2 += 1; print(1)
            if i and zzzzxds == 3:
                if i[0] == "1": salida_decimal3 += 128; print(128)
                if i[1] == "1": salida_decimal3 += 64; print(64)
                if i[2] == "1": salida_decimal3 += 32; print(32)
                if i[3] == "1": salida_decimal3 += 16; print(16)
                if i[4] == "1": salida_decimal3 += 8; print(8)
                if i[5] == "1": salida_decimal3 += 4; print(4)
                if i[6] == "1": salida_decimal3 += 2; print(2)
                if i[7] == "1": salida_decimal3 += 1; print(1)
            if i and zzzzxds == 4:
                if i[0] == "1": salida_decimal4 += 128; print(128)
                if i[1] == "1": salida_decimal4 += 64; print(64)
                if i[2] == "1": salida_decimal4 += 32; print(32)
                if i[3] == "1": salida_decimal4 += 16; print(16)
                if i[4] == "1": salida_decimal4 += 8; print(8)
                if i[5] == "1": salida_decimal4 += 4; print(4)
                if i[6] == "1": salida_decimal4 += 2; print(2)
                if i[7] == "1": salida_decimal4 += 1; print(1)
            
        print("\n" + "="*60)

        def subnet_to_cidr(subnet):
            subnet_int = struct.unpack("!I", socket.inet_aton(subnet))[0]
            return bin(subnet_int).count('1')
        
        if ip == None and mascara == None:
            DIREC_RED_FINAL = str(salida_decimal1) + "." + str(salida_decimal2) + "." + str(salida_decimal3) + "." + str(salida_decimal4) + "/" + str(subnet_to_cidr(get_network_data(INTERFAZ_DADA_)[1]))
        else:
            DIREC_RED_FINAL = str(salida_decimal1) + "." + str(salida_decimal2) + "." + str(salida_decimal3) + "." + str(salida_decimal4) + "/" + str(subnet_to_cidr(mascara))
        return DIREC_RED_FINAL
    
        # hecho en 2h y 15 minutos
    except:
        if INTERFAZ_DADA_ != None: ERR_REG_(f"[CALCULAR_DIRECCION_RED__] No se pudo detectar la dirección de red.\n\n")

        return f"{__TR__('NO_PUDO_DETECTAR')}"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Calcular dirección de difusión

def CALCULAR_DIRECCION_DIFUSION__(INTERFAZ_DADA_, ip=None, mascara=None):
    try:
        #################################################
        def FUNCION_GUAPA_(oplk):
            ip_bin = ""
            ip2 = oplk.split(".")

            z = 0
            for i in ip2:
                z += 1
                ip_bin += str(bin(int(i))).replace("0b","") + ("." if z < 4 else "")

            salida_definita_sexy_perra_si_qwerty = ""
            zxzxzxzx = 0

            for i in ip_bin.split("."):
                
                zxzxzxzx += 1
                salida, zz1 = "", 0
                if len(i) < 8:
                    while zz1 < int(str(int(len(i))-8).replace("-","")):
                        zz1 += 1
                        salida += "0"
                    salida += str(i)
                    salida_definita_sexy_perra_si_qwerty += f"{salida}." + ("." if zxzxzxzx < 4 else "")
                else:
                    salida_definita_sexy_perra_si_qwerty += f"{i}" + ("." if zxzxzxzx < 4 else "")

            return salida_definita_sexy_perra_si_qwerty.replace("..",".")

        print("="*60)

        if ip == None:
            ip_final_sexy = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[0])
        else:
            ip_final_sexy = FUNCION_GUAPA_(ip) # decimal a binario
        
        if mascara == None:
            masc_final_sexy = FUNCION_GUAPA_(get_network_data(INTERFAZ_DADA_)[1])
        else:
            masc_final_sexy = FUNCION_GUAPA_(mascara) # decimal a binario

        #################################################

        pr_gr_ip = ip_final_sexy.split(".")[0]
        se_gr_ip = ip_final_sexy.split(".")[1]
        te_gr_ip = ip_final_sexy.split(".")[2]
        cu_gr_ip = ip_final_sexy.split(".")[3]

        pr_gr_mm = masc_final_sexy.split(".")[0]
        se_gr_mm = masc_final_sexy.split(".")[1]
        te_gr_mm = masc_final_sexy.split(".")[2]
        cu_gr_mm = masc_final_sexy.split(".")[3]

        #################################################

        def CALCULAR_DIRECCIO_SEXY_DIFUSION_(asadasd1, asadasd2):
            ip_num = int(asadasd1, 2)
            mm_num = int(asadasd2, 2)
            result = (ip_num & mm_num) | (~mm_num & 0xFF)
            ip_bin = f"{result:08b}"
            return ip_bin + "."

        #################################################

        salida_final_definitiva_hungahunga_pepinillo_IP_ = f"{CALCULAR_DIRECCIO_SEXY_DIFUSION_(pr_gr_ip, pr_gr_mm)}{CALCULAR_DIRECCIO_SEXY_DIFUSION_(se_gr_ip, se_gr_mm)}{CALCULAR_DIRECCIO_SEXY_DIFUSION_(te_gr_ip, te_gr_mm)}{CALCULAR_DIRECCIO_SEXY_DIFUSION_(cu_gr_ip, cu_gr_mm)}"

        #################################################

        print(ip_final_sexy)
        print(masc_final_sexy)
        print("= ", salida_final_definitiva_hungahunga_pepinillo_IP_)
        print("-"*60, "\n\n")

        #################################################
        #################################################
        # CALCULAR EL DECIMAL

        grups_binarios_ = salida_final_definitiva_hungahunga_pepinillo_IP_.split(".")
        resultado_decimal_ = ""

        salida_decimal1 = 0
        salida_decimal2 = 0
        salida_decimal3 = 0
        salida_decimal4 = 0

        zzzzxds = 0

        for i in grups_binarios_:
            print("-"*10, i)
            zzzzxds += 1
            if i and zzzzxds == 1:
                if i[0] == "1": salida_decimal1 += 128; print(128)
                if i[1] == "1": salida_decimal1 += 64; print(64)
                if i[2] == "1": salida_decimal1 += 32; print(32)
                if i[3] == "1": salida_decimal1 += 16; print(16)
                if i[4] == "1": salida_decimal1 += 8; print(8)
                if i[5] == "1": salida_decimal1 += 4; print(4)
                if i[6] == "1": salida_decimal1 += 2; print(2)
                if i[7] == "1": salida_decimal1 += 1; print(1)
            if i and zzzzxds == 2:
                if i[0] == "1": salida_decimal2 += 128; print(128)
                if i[1] == "1": salida_decimal2 += 64; print(64)
                if i[2] == "1": salida_decimal2 += 32; print(32)
                if i[3] == "1": salida_decimal2 += 16; print(16)
                if i[4] == "1": salida_decimal2 += 8; print(8)
                if i[5] == "1": salida_decimal2 += 4; print(4)
                if i[6] == "1": salida_decimal2 += 2; print(2)
                if i[7] == "1": salida_decimal2 += 1; print(1)
            if i and zzzzxds == 3:
                if i[0] == "1": salida_decimal3 += 128; print(128)
                if i[1] == "1": salida_decimal3 += 64; print(64)
                if i[2] == "1": salida_decimal3 += 32; print(32)
                if i[3] == "1": salida_decimal3 += 16; print(16)
                if i[4] == "1": salida_decimal3 += 8; print(8)
                if i[5] == "1": salida_decimal3 += 4; print(4)
                if i[6] == "1": salida_decimal3 += 2; print(2)
                if i[7] == "1": salida_decimal3 += 1; print(1)
            if i and zzzzxds == 4:
                if i[0] == "1": salida_decimal4 += 128; print(128)
                if i[1] == "1": salida_decimal4 += 64; print(64)
                if i[2] == "1": salida_decimal4 += 32; print(32)
                if i[3] == "1": salida_decimal4 += 16; print(16)
                if i[4] == "1": salida_decimal4 += 8; print(8)
                if i[5] == "1": salida_decimal4 += 4; print(4)
                if i[6] == "1": salida_decimal4 += 2; print(2)
                salida_decimal4 += 1 # Por alguna razno no suma el bit final
            
        print("\n" + "="*60)

        def subnet_to_cidr(subnet):
            subnet_int = struct.unpack("!I", socket.inet_aton(subnet))[0]
            return bin(subnet_int).count('1')
        
        if ip == None and mascara == None:
            DIREC_DIF_FINAL = str(salida_decimal1) + "." + str(salida_decimal2) + "." + str(salida_decimal3) + "." + str(salida_decimal4) + "/" + str(subnet_to_cidr(get_network_data(INTERFAZ_DADA_)[1]))
        else:
            DIREC_DIF_FINAL = str(salida_decimal1) + "." + str(salida_decimal2) + "." + str(salida_decimal3) + "." + str(salida_decimal4) + "/" + str(subnet_to_cidr(mascara))
        return DIREC_DIF_FINAL
        
        # hecho en 2h y 15 minutos
    except:
        if INTERFAZ_DADA_ != None: (f"[CALCULAR_DIRECCION_DIF__] No se pudo detectar la dirección de difusión.\n\n")
        
        return f"{__TR__('NO_PUDO_DETECTAR')}"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ocultar terminal de nmap

def ocultar_consola_en_scan():
    if sys.platform == "win32":
        original_popen = subprocess.Popen

        def nuevo_popen(*args, **kwargs):
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
            return original_popen(*args, **kwargs)

        subprocess.Popen = nuevo_popen

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Detectar dispositovos (nmap)

def NMAP_detectar_dispositivos_(MAC_FALSIFICADA="", PUERTO_FALSIFICADO="", OTRAS_FALSIFICADAS="", DESTINO=""):

    if MAC_FALSIFICADA != None and MAC_FALSIFICADA != "":
        MAC_FALSIFICADA = f" --spoof-mac {MAC_FALSIFICADA}"
    if PUERTO_FALSIFICADO != None and PUERTO_FALSIFICADO != "":
        PUERTO_FALSIFICADO = f" -g {PUERTO_FALSIFICADO}"
    if OTRAS_FALSIFICADAS != None and OTRAS_FALSIFICADAS != "":
        OTRAS_FALSIFICADAS = f" {OTRAS_FALSIFICADAS}"

    try:
        ocultar_consola_en_scan()
        NMAP_ = nmap.PortScanner()
    except:
        ERR_REG_(f"[NMAP_detectar_dispositivos_] Nmap no está instalado.\n\n")
        return [f"{__TR__('NMAP_NO_INSTALADO')}", "NMAP_ERR_INSTALADO"]
    

    if DESTINO == "":
        try:
            DIREC_ = CALCULAR_DIRECCION_RED__(obt_json_(5))
            if str(DIREC_) == f"{__TR__('NO_PUDO_DETECTAR')}":
                return [f"{__TR__('DIREC_RED_MAL')}", "DIREC_RED_ERROR"]
        except:
            ERR_REG_(f"[NMAP_detectar_dispositivos_] La dirección de red no se puede calcular.\n\n")
            return [f"{__TR__('DIREC_RED_MAL')}", "DIREC_RED_ERROR"]
    else:
        DIREC_ = DESTINO
    
    print(DIREC_)
    
    try:
        NMAP_.scan(hosts=DIREC_, arguments=f"-n -sP -PE -PA21,23,80,3389{MAC_FALSIFICADA}{PUERTO_FALSIFICADO}{OTRAS_FALSIFICADAS}")
    except:
        ERR_REG_(f"[NMAP_detectar_dispositivos_] Un argumento es incorrecto.\n\n")
        return [f"{__TR__('ARG_MAL')}", "ARG_MAL"]
    
    LISTA_ = [(x, NMAP_[x]['status']['state']) for x in NMAP_.all_hosts()]
    RESULTADO_ = ""
    CANTIDAD, actual = len(LISTA_), 0
    print(len(LISTA_))
    
    for host, state in LISTA_:
        actual += 1
        
        #HOST
        RESULTADO_ += f"<span style='color: {obt_json_(7)};'>{host}</span>{f'  (Este dispositivo)' if get_network_data(obt_json_(5))[0] == host else ''}"
        
        # MAC
        try: mac = f"<br>  •  MAC: <span style='color: {obt_json_(7)};'>{NMAP_[host]['addresses']['mac']}</span>"
        except: mac = ""
        RESULTADO_ += f"""{mac}{f'<br>  •  MAC: <span style="color: {obt_json_(7)};">{get_network_data(obt_json_(5),1)[0].replace("-",":")}</span>' if mac == '' else ''}"""

        # HOSTNAME
        try: hostname = f"<br>  •  Hostname: <span style='color: {obt_json_(7)};'>{NMAP_[host]['hostnames']['name']}</span>  (<span style='color: {obt_json_(7)};'>{NMAP_[host]['hostnames']['type']}</span>)"
        except: hostname = ""
        RESULTADO_ += hostname

        # RAZÓN
        razon = f"<br>  •  {__TR__('RAZON')}<span style='color: {obt_json_(7)};'>{NMAP_[host]['status']['reason']}</span>"
        RESULTADO_ += razon
        
        if CANTIDAD != actual:
            RESULTADO_ += "<br><br>"
            print("=="*70)

    return [RESULTADO_, "BIEN", f"Hosts: {NMAP_.scanstats()['uphosts']} [up] / {NMAP_.scanstats()['totalhosts']} [total]", NMAP_.scanstats()['elapsed']]

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Detectar dispositovos (nmap)

def NMAP_detectar_puertos_(HOST, RANGO, e, ES_UDP=False, RUIDO="3", MAC_FALSIFICADA="", PUERTO_FALSIFICADO="", OTRAS_FALSIFICADAS=""):
    
    if MAC_FALSIFICADA != None and MAC_FALSIFICADA != "":
        MAC_FALSIFICADA = f" --spoof-mac {MAC_FALSIFICADA}"
    if PUERTO_FALSIFICADO != None and PUERTO_FALSIFICADO != "":
        PUERTO_FALSIFICADO = f" -g {PUERTO_FALSIFICADO}"
    if OTRAS_FALSIFICADAS != None and OTRAS_FALSIFICADAS != "":
        OTRAS_FALSIFICADAS = f" {OTRAS_FALSIFICADAS}"
    try:
        ocultar_consola_en_scan()

        NMAP_ = nmap.PortScanner()
    except:
        ERR_REG_(f"[NMAP_detectar_puertos_] Nmap no está instalado.\n\n")

        return [f"{__TR__('NMAP_NO_INSTALADO')}", "NMAP_ERR_INSTALADO"]

    try:
        if ES_UDP == False:
            NMAP_.scan(hosts=HOST, ports=RANGO, arguments=f"-sT -sV -T {RUIDO}{MAC_FALSIFICADA}{PUERTO_FALSIFICADO}{OTRAS_FALSIFICADAS}")
        else:
            NMAP_.scan(hosts=HOST, ports=RANGO, arguments=f"-sU -sV -T {RUIDO}{MAC_FALSIFICADA}{PUERTO_FALSIFICADO}{OTRAS_FALSIFICADAS}")
    except:
        ERR_REG_(f"[NMAP_detectar_puertos_] Un argumento de evasión de firewall e IDS es equivocado.\n\n")

        return [f"{__TR__('ARG_MAL')}", "ARG_MAL"]

    RESULTADO_ = ""

    hosts_detectados = NMAP_.all_hosts()

    if not hosts_detectados:
        return [f"{__TR__('NO_PODER_ESCANEAR_HOST')}", "ERR_HOST"]

    host_real = hosts_detectados[0]

    for proto in NMAP_[host_real].all_protocols():
        ports = NMAP_[host_real][proto].keys()
        for port in sorted(ports):
            nombre = NMAP_[host_real][proto][port]['name']
            razon = NMAP_[host_real][proto][port]['reason']

            producto = NMAP_[host_real][proto][port].get('product', '')
            version = NMAP_[host_real][proto][port].get('version', '')
            software = ((f"<li> Software: <span style='color: {obt_json_(7)};'>" + str(producto) + "</span>") if producto != "" else "") + (f" </span>(<span style='color: {obt_json_(7)};'>" + str(version) + "</span>)" if version != "" else "") + "</li>"

            extrainfo = NMAP_[host_real][proto][port].get('extrainfo', '')
            res_extrainfo = (f"<li> Extra info: <span style='color: {obt_json_(7)};'>{extrainfo}</span> </li>") if extrainfo != "" else ""


            cpe = NMAP_[host_real][proto][port].get('cpe', '')
            res_cpe = (f"<li> CPE: <span style='color: {obt_json_(7)};'>{cpe}</span> </li>") if extrainfo != "" else ""


            if NMAP_[host_real][proto][port]['state'] == 'open':
                if e == "raw":
                    RESULTADO_ += f"<span style='color: {obt_json_(7)};'>{port}</span>: " + str(NMAP_[host_real][proto][port]) + "<br><br>"
                else:
                    RESULTADO_ += f"""<span style='color: {obt_json_(7)};'>{port}</span>
                    <ul>
                        <li>{__TR__('NOMBRE_')} <b style='color: {obt_json_(7)};'>{nombre}</b></li>
                        <li>{__TR__('PROTOCOLO_')} <span style='color: {obt_json_(7)};'>{proto}</span> </li>
                        <li>{__TR__('RESPUESTA_')} <span style='color: {obt_json_(7)};'>{razon}</span> </li>
                        {software}
                        {res_extrainfo}
                        {res_cpe}
                    </ul>"""

    return [RESULTADO_ or f"{__TR__('NO_ENCONTRADO_PUERTOS')}<br>", "BIEN", NMAP_.scanstats()['elapsed']]

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Detección de ARP spoofing

def SCAPY_ARP_Spoofing_():
    if obt_json_(5) == None or obt_json_(5) == "": return [f"{__TR__('DIREC_RED_MAL')}", "DIREC_RED_ERROR"]
    class ARPDetector(QThread):
        new_log = Signal(str)

        def __init__(self):
            super().__init__()
            self.running = True
        
        def stop(self):
            self.running = False

        def run(self):
            self.new_log.emit(f"{__TR__('DETECTANDO_ARP_SPOOF')}<br><br>")
            interfaz = obt_json_(5)
            mac = str(get_network_data(interfaz, 1)[0]).replace('-', ':').lower()
            ip = get_network_data(interfaz)[0]
            arp_log = {}

            def process_packet(packet):
                if ARP in packet and packet[ARP].op == 2:
                    src_mac = packet[ARP].hwsrc.lower()
                    src_ip = packet[ARP].psrc

                    if src_mac == mac and src_ip != ip:
                        arp_log[src_ip] = arp_log.get(src_ip, 0) + 1
                        res = (f"<br>[{__TR__('RESPUESTA_ARP')}]\t({src_ip}) {__TR__('DICE_TENER_MAC')} ({src_mac})  |  "
                               f"{__TR__('ESTE_EQUIPO')} ({ip}) {__TR__('SI_TIENE_MAC')} ({mac}) {__TR__('EN_INTERFAZ')} ({interfaz}).<br><br>{arp_log}")
                        self.new_log.emit(res)

            sniff(prn=process_packet, filter="arp", store=0, stop_filter=lambda x: not self.running)

    class Ventana(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("AILI-SS")
            self.setGeometry(100, 100, 600, 400)

            self.layout = QVBoxLayout()
            self.log_output = QTextEdit()
            self.log_output.setReadOnly(True)
            self.log_output.setStyleSheet(f"color: {obt_json_('01')};")

            self.layout.addWidget(self.log_output)
            self.setLayout(self.layout)

            self.detector = ARPDetector()
            self.detector.new_log.connect(self.actualizar_log)
            self.detector.start()

        def actualizar_log(self, texto):
            self.log_output.append(texto)

    global ventana
    ventana = Ventana()
    ventana.setStyleSheet(estilos_())
    ventana.show()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Conseguir hash

algoritmos = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "sha3_256", "sha3_512", "blake2b", "blake2s"]

def hash_de_texto_(texto, empezado_en):
    archivo_salida = f"<span style='color: {obt_json_(6)};'>{__TR__('ALGORITMOS')}</span>"

    for algoritmo in algoritmos:
        hash_algoritmo = hashlib.new(algoritmo)
        hash_algoritmo.update(texto.encode("utf-8"))
        archivo_salida += f"<br> <br><span style='color: {obt_json_(7)};'>{algoritmo.upper()}</span> <br>{hash_algoritmo.hexdigest()}"
    
    archivo_salida += f"<br><br><span style='color: {obt_json_(6)};'>{__TR__('TIEMPO')}</span>: {datetime.now() - empezado_en}"
    texto_formateado = html.escape(str(texto)).replace('\n', '<br>')
    archivo_salida += f"""<br><br><span style='color: {obt_json_(6)};'>{__TR__('TEXTO')}</span>: <br><br>"{texto_formateado}" """
    archivo_salida += f"<br><br><span style='color: {obt_json_(6)};'>AILI-SS</span> (aili-ss.pages.dev)"
    return archivo_salida

#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def hash_de_archivo_(ruta, empezado_en):
    archivo_salida = f"<span style='color: {obt_json_(6)};'>{__TR__('ALGORITMOS')}</span>"

    with open(ruta, "rb") as f:
        for algoritmo in algoritmos:
            hash_algoritmo = hashlib.new(algoritmo)
            f.seek(0)
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algoritmo.update(chunk)
            archivo_salida += f"<br> <br><span style='color: {obt_json_(7)};'>{algoritmo.upper()}</span> <br>{hash_algoritmo.hexdigest()}"

    archivo_salida += f"<br><br><span style='color: {obt_json_(6)};'>{__TR__('TIEMPO')}</span>: {datetime.now() - empezado_en}"
    archivo_salida += f"""<br><br><span style='color: {obt_json_(6)};'>{__TR__('RUTA')}</span>: <br><br>''{html.escape(ruta)}'' """
    archivo_salida += f"<br><br><span style='color: {obt_json_(6)};'>AILI-SS</span> (aili-ss.pages.dev)"
    return archivo_salida

#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~

def Hashear_(tipo, valor):
    class Ventana(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("AILI-SS")
            self.setGeometry(100, 100, 600, 400)

            self.layout = QVBoxLayout()
            self.log_output = QTextEdit()
            self.log_output.setStyleSheet(f"color: {obt_json_('01')};")
            self.log_output.setReadOnly(True)
            if tipo == 1:
                self.log_output.setHtml(hash_de_texto_(valor, datetime.now()))
            else:
                if os.path.isfile(valor):
                    res = hash_de_archivo_(valor, datetime.now())
                else:
                    res = f"<span style='color: {obt_json_(6)};'>{__TR__('ALGORITMOS')}</span>"
                
                self.log_output.setHtml(res)

            self.layout.addWidget(self.log_output)
            self.setLayout(self.layout)

        def actualizar_log(self, texto):
            self.log_output.append(texto)

    global ventana
    ventana = Ventana()
    ventana.setStyleSheet(estilos_())
    ventana.show()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Coger información de un equipo

def NMAP_detectar_parametros_(HOST, RUIDO="3", MAC_FALSIFICADA="", PUERTO_FALSIFICADO="", OTRAS_FALSIFICADAS=""):

    if MAC_FALSIFICADA != None and MAC_FALSIFICADA != "":
        MAC_FALSIFICADA = f" --spoof-mac {MAC_FALSIFICADA}"
    if PUERTO_FALSIFICADO != None and PUERTO_FALSIFICADO != "":
        PUERTO_FALSIFICADO = f" -g {PUERTO_FALSIFICADO}"
    if OTRAS_FALSIFICADAS != None and OTRAS_FALSIFICADAS != "":
        OTRAS_FALSIFICADAS = f" {OTRAS_FALSIFICADAS}"
    try:
        ocultar_consola_en_scan()

        NMAP_ = nmap.PortScanner()
    except:
        ERR_REG_(f"[NMAP_detectar_parametros_] Nmap no está instalado.\n\n")

        return [f"{__TR__('NMAP_NO_INSTALADO')}", "NMAP_ERR_INSTALADO"]

    
    try:
        NMAP_.scan(hosts=HOST, arguments=f"-O -T{RUIDO}{MAC_FALSIFICADA}{PUERTO_FALSIFICADO}{OTRAS_FALSIFICADAS}")
    except:
        ERR_REG_(f"[NMAP_detectar_parametros_] Un argumento de evasión de firewall e IDS es equivocado.\n\n")

        return [f"{__TR__('ARG_MAL')}", "ARG_MAL"]

    SO, SO_PORCENTAJE = {__TR__('NO_PUDO_DETECTAR')}, ""
    try:
        if 'osmatch' in NMAP_[HOST]:
            for os in NMAP_[HOST]['osmatch']:
                SO = os['name']
                SO_PORCENTAJE = os['accuracy'] + "%"
    except:
        pass
    
    UPTIME, LAST_BOOT = "", ""
    try:
        if 'uptime' in NMAP_[HOST]:
            sec = int(NMAP_[HOST]['uptime']['seconds'])
            min = sec // 60
            hr = round(min // 60, 2)
            UPTIME = f"( {sec} s ) - ( {min} min ) - ( {hr} h )"
            LAST_BOOT = NMAP_[HOST]['uptime'].get('lastboot', "")
    except:
        pass

    HOSTNAME, ESTADO = "None", "None"
    try:
        HOSTNAME = NMAP_[HOST].hostname()
        ESTADO = NMAP_[HOST]['status']['state']
    except:
        pass

    return [HOSTNAME, SO, SO_PORCENTAJE, NMAP_.scanstats()["elapsed"], ESTADO, UPTIME, LAST_BOOT]

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# NMAP detectar vulnerabilidades

def NMAP_detectar_scripts_(HOST, SCRIPT, RUIDO, MAC_FALSIFICADA="", PUERTO_FALSIFICADO="", OTRAS_FALSIFICADAS=""):
    
    if MAC_FALSIFICADA != None and MAC_FALSIFICADA != "":
        MAC_FALSIFICADA = f" --spoof-mac {MAC_FALSIFICADA}"
    if PUERTO_FALSIFICADO != None and PUERTO_FALSIFICADO != "":
        PUERTO_FALSIFICADO = f" -g {PUERTO_FALSIFICADO}"
    if OTRAS_FALSIFICADAS != None and OTRAS_FALSIFICADAS != "":
        OTRAS_FALSIFICADAS = f" {OTRAS_FALSIFICADAS}"
    try:
        ocultar_consola_en_scan()
        
        NMAP_ = nmap.PortScanner()
    except:
        ERR_REG_(f"[NMAP_detectar_scripts_] Nmap no está instalado.\n\n")

        return [f"{__TR__('NMAP_NO_INSTALADO')}", "NMAP_ERR_INSTALADO"]

    try:
        with open(os.path.join(RUTA_RECURSOS, "NMAP.json"), "r") as f: VALORES = json.load(f)
        argumentos = VALORES.get(SCRIPT, "-p- -sV")
        NMAP_.scan(hosts=HOST, arguments=f"{argumentos} --script={SCRIPT} -T {RUIDO}{MAC_FALSIFICADA}{PUERTO_FALSIFICADO}{OTRAS_FALSIFICADAS}")
    except:
        ERR_REG_(f"[NMAP_detectar_scripts_] Un parámetro es equivocado.\n\n")

        return [f"{__TR__('RANGO_O_HOST_INVALIDO')}", "ERR_PARAM"]

    resultado = ""
    ####
    try:
        for proto in NMAP_[HOST].all_protocols():
            for port in sorted(NMAP_[HOST][proto].keys()):
                port_data = NMAP_[HOST][proto][port]

                if 'script' in port_data:
                    resultado += f"<br><br>{__TR__('PUERTO')} <span style='color: {obt_json_(7)};'>{port}</span>:"

                    if len(port_data['script'].items()) == 1 and str(SCRIPT).startswith("http"):
                        resultado = None # SOLO HAY UN CAMPO Y SE REPITE EN CADA ESCANEO DE HTTP (http-server-header)
                    else:
                        for script_name, output in port_data['script'].items():

                            if SCRIPT == "http-headers":
                                output = str(output).replace("Server", "<br>Server")
                                output = str(output).replace("Accept-Ranges", "<br>Accept-Ranges")
                                output = str(output).replace("Vary", "<br>Vary")
                                output = str(output).replace("Connection", "<br>Connection")
                                output = str(output).replace("Content-Type", "<br>Content-Type")
                            
                            if SCRIPT == "http-comments-displayer":
                                output = str(output).replace("Path", "<br><br> > Path")
                                output = str(output).replace("Line number", "<br>Line number")
                                output = str(output).replace("Comment", "<br>Comment")

                            if SCRIPT == "http-useragent-tester":
                                output = str(output).replace("Agents", "<br>Agents")
                            
                            if SCRIPT == "ssh2-enum-algos":
                                output = str(output).replace("kex_algorithms", "<br><br><b>kex_algorithms</b>")
                                output = str(output).replace("server_host_key_algorithms", "<br><br><b>server_host_key_algorithms</b>")
                                output = str(output).replace("encryption_algorithms", "<br><br><b>encryption_algorithms</b>")
                                output = str(output).replace("mac_algorithms", "<br><br><b>mac_algorithms</b>")
                                output = str(output).replace("compression_algorithms", "<br><br><b>compression_algorithms</b>")
                            #####
                            # FINAL
                            resultado += f"<br><br>  >>  <b><span style='color:{obt_json_(6)};'>{script_name}</span></b>: {output}"
    except:
        pass
    ####
    try:
        if 'hostscript' in NMAP_[HOST]:
            for script in NMAP_[HOST]['hostscript']:
                resultado += f"<br><br><span style='color: {obt_json_(7)};'>{script['id']}</span>  <br><br>  >>  {script['output']}"
    except:
        pass
    ####
    if not resultado or resultado == "":
        resultado = f"<br><br><span style='color:red;'> >> </span>{__TR__('NO_ENCONTRADO_RESULTADOS_SCRIPT')}"
    ####
    return [resultado, "BIEN", NMAP_.scanstats()["elapsed"]]

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Monitorizar el tráfico de la red

def Monitorizar_Paquetes_(FILTRO_DADO, tipo=None, TIEMPO_ENTRE_PAQUETES=1):
    global tipo2
    tipo2 = tipo

    if obt_json_(5) == None or obt_json_(5) == "": return [f"{__TR__('DIREC_RED_MAL')}", "DIREC_RED_ERROR"]
    class MonitoreoRED(QThread):
        new_log = Signal(str)

        def __init__(self):
            super().__init__()
            self.running = True
        
        def stop(self):
            self.running = False

        def run(self):
            #################################
            def escuchar_paquete_(filtro_red):
                try:
                    sniff(prn=imprimir_paquete_, iface=obt_json_(5), filter=filtro_red, store=0)
                except:
                    ERR_REG_(f"[escuchar_paquete_] Filtro configurado inválido.\n\n")
                    self.new_log.emit(f"{__TR__('FILTRO_O_NPCAP')}")
            
            #################################
            def imprimir_paquete_(packet):
                
                buffer = io.StringIO()
                sys_stdout_original = sys.stdout
                sys.stdout = buffer

                if tipo2 == False or tipo2 == None:

                    try:
                        packet.show()
                        output = buffer.getvalue()
                        self.new_log.emit('-'*60)
                        self.new_log.emit(output)
                    finally:
                        sys.stdout = sys_stdout_original
                
                if tipo2 == 1:
                    if IP in packet:
                        origen = packet[IP].src
                        destino = packet[IP].dst
                        tipo = "Otro"
                        sport = "-"
                        dport = "-"
                        smac = "-"
                        dmac = "-"

                        if Ether in packet:
                            smac = packet[Ether].src
                            dmac = packet[Ether].dst
                        if TCP in packet:
                            sport = packet[TCP].sport
                            dport = packet[TCP].dport
                            tipo = "TCP"
                        elif UDP in packet:
                            sport = packet[UDP].sport
                            dport = packet[UDP].dport
                            tipo = "UDP"
                        elif ICMP in packet: tipo = "ICMP"
                        elif DNS in packet: tipo = "DNS"

                        self.new_log.emit('-'*60)
                        self.new_log.emit(f"<span style='color: {obt_json_(6)};'>### {tipo} ### <br>src</span>: {origen}<span style='color: {obt_json_(7)};'>:{sport}</span> <br> <span style='color: {obt_json_(6)};'>smac</span>: {smac}<br><br><span style='color: {obt_json_(6)};'>dst</span>: {destino}<span style='color: {obt_json_(7)};'>:{dport}</span> <br> <span style='color: {obt_json_(6)};'>dmac</span>: {dmac}")
                    else:
                        pass
                try:
                    time.sleep(int(TIEMPO_ENTRE_PAQUETES))
                except:
                    pass
            
            #################################
            filtro_red = FILTRO_DADO
            global tiempo_global

            self.new_log.emit(f"{__TR__('ANALIZAR_PAQUETES_INICIO')}")

            try:
                escuchar_paquete_(filtro_red)
            except KeyboardInterrupt:
                return self.new_log.emit(f"<br>{__TR__('MONITOREO_DETENIDO')}")
            return
            #################################

    class Ventana(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("AILI-SS")
            self.setGeometry(100, 100, 600, 400)

            self.layout = QVBoxLayout()
            self.log_output = QTextEdit()
            self.log_output.setReadOnly(True)
            self.log_output.setStyleSheet(f"color: {obt_json_('01')};")

            self.layout.addWidget(self.log_output)
            self.setLayout(self.layout)

            self.detector = MonitoreoRED()
            self.detector.new_log.connect(self.actualizar_log)

            self.detector.start()

        def actualizar_log(self, texto):
            self.log_output.append(texto)

    global ventana
    ventana = Ventana()
    ventana.setStyleSheet(estilos_())
    ventana.show()

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Generar un gráfico con pings

def PING_generar_gráfico(objetivo, cantidad, RESULTADO):
    try:
        x, y = RESULTADO
        plt.figure(figsize=(8, 4))
        plt.scatter(x, y)
        plt.title(f"Ping {cantidad} {__TR__('VECES')} -> {objetivo}")
        plt.xlabel(f"{__TR__('NUM_PING')}")
        plt.ylabel(f"{__TR__('TIEMPO_RESPUESTA')}")
        plt.grid()
        plt.show()
    except:
        pass

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Detectar dispositivos bluetooth

def dispositivos_bluetooth_():
    # BLE
    async def run():
        try:
            devices = await BleakScanner.discover()
        except: return f"{__TR__('SE_NECESITA_BLUETOOTH')}"
        res, index = "", 0
        for d in devices:
            index += 1
            # HOSTNAME
            hostname = ""
            if d.name not in [None, ""]:
                hostname = f"  •  Hostname: <span style='color: {obt_json_(7)};'>{d.name}</span>"
            
            # FINAL
            res += f"({index}.)  •  MAC: <span style='color: {obt_json_(7)};'>{d.address}</span>{hostname} <br><br>"
        
        return res

    return(asyncio.run(run()))

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Devolver versión Nmap

def version_nmap():
    try:
        return f" {nmap.__version__}"
    except:
        return ""

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Escanear redes Wi-Fi

def devolver_redes_wifi_():
    def interfaz_(name=obt_json_(5)):
        wifi = pywifi.PyWiFi()
        for iface in wifi.interfaces():
            if name in iface.name():
                return iface
        return wifi.interfaces()[0]

    def interpretar_akm(akm_list):
        tipos = {
            const.AKM_TYPE_NONE: "Open",
            const.AKM_TYPE_WPA: "WPA",
            const.AKM_TYPE_WPAPSK: "WPA-PSK",
            const.AKM_TYPE_WPA2: "WPA2",
            const.AKM_TYPE_WPA2PSK: "WPA2-PSK",
            const.AKM_TYPE_UNKNOWN: "Desconocido",
        }
        return [tipos.get(akm, f"AKM-{akm}") for akm in akm_list]

    def interpretar_cipher(cipher):
        tipos = {
            0: "Sin cifrado",          # CIPHER_TYPE_NONE
            1: "WEP",                  # CIPHER_TYPE_WEP
            2: "TKIP",                 # CIPHER_TYPE_TKIP
            3: "CCMP (AES)",           # CIPHER_TYPE_CCMP
        }
        return tipos.get(cipher, f"Cifrado desconocido ({cipher})")

    def interpretar_auth(auth_list):
        tipos = {
            const.AUTH_ALG_OPEN: "Abierto",
            const.AUTH_ALG_SHARED: "Compartido",
        }
        return [tipos.get(a, f"Auth-{a}") for a in auth_list]

    def escanear_():
        try:
            iface = interfaz_(obt_json_(5))
            iface.scan()
            res0 = ""
            
            for network in iface.scan_results():
                res0 += f"<br>SSID: <span style='color: {obt_json_(7)};'>{network.ssid}</span>"
                res0 += f"<br>BSSID: <span style='color: {obt_json_(7)};'>{network.bssid}</span>"
                res0 += f"<br>Señal: <span style='color: {obt_json_(7)};'>{network.signal} dBm</span>"
                res0 += f"<br>Frecuencia: <span style='color: {obt_json_(7)};'>{network.freq} MHz</span>"
                res0 += f"<br>Requiere clave: <span style='color: {obt_json_(7)};'>{network.key}</span>"
                res0 += f"<br>Auth: <span style='color: {obt_json_(7)};'>{interpretar_auth(network.auth)[0]}</span>"
                res0 += f"<br>AKM: <span style='color: {obt_json_(7)};'>{interpretar_akm(network.akm)[0]}</span>"
                res0 += f"<br>Cifrado: <span style='color: {obt_json_(7)};'>{interpretar_cipher(network.cipher)}</span>"
                res0 += "<br>"
            
            return [res0, len(iface.scan_results())]

        except Exception as e:
            return [f"Error: {e}", 0]
    
    return escanear_()
    
####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Enviar DHCP Discovery

def enviar_dhcp_discovery():
    mac = RandMAC()

    try:
        # Construye el paquete DHCP Discover
        ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=get_network_data(obt_json_(5), 1)[0], type=0x0800)
        ip = IP(src="0.0.0.0", dst="255.255.255.255")
        udp = UDP(sport=68, dport=67)
        bootp = BOOTP(chaddr=mac, xid=0x10000000, flags=0x8000)
        dhcp = DHCP(options=[("message-type", "discover"), "end"])

        packet = ether / ip / udp / bootp / dhcp

        sendp(packet, iface=obt_json_(5), verbose=1)
        return True
    except Exception as e:
        if obt_json_(5) == None or obt_json_(5) == "":
            return f"{__TR__('COMPROBAR_INTERFAZ_EN_CONFIG')}"
        
        return f"{__TR__('NPCAP_NO_INSTALADO')}"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Guardar tema personalizado

def gua_tema_personalizado_JSON_(opc0, opc01, opc1, opc2, opc3, opc4, opc6, opc7):
    cambios = {
        "APP_BASE": opc0,
        "APP_LETRA_BASE": opc01,
        "BACKG_BASE": opc1,
        "LETRA_BASE": opc2,
        "BOTON1_BASE": opc3,
        "BOTON2_BASE": opc4,
        "COLOR_RESALTE_TITULO": opc6,
        "COLOR_IMPORT_LICENCIA": opc7,
    }

    RUTA_DIR_USUARIO = conseguir_RUTA_DIR_USUARIO_()
    ruta_config = os.path.join(RUTA_DIR_USUARIO, "ConfigTemaPers.json")

    with open(ruta_config, "w") as json_final:
        json.dump(cambios, json_final)

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Abrir licencia

def abrir_licencia_():
    try: subprocess.run(["notepad.exe", os.path.join(RUTA_RECURSOS, "LICENSE.txt")])
    except:
        try: subprocess.run(["gedit", os.path.join(RUTA_RECURSOS, "LICENSE.txt")])
        except Exception as e:
            try:
                subprocess.run(["nano", os.path.join(RUTA_RECURSOS, "LICENSE.txt")])
            except:
                ERR_REG_(f"[abrir_licencia_] No se encuentra el archivo de la licencia.\n\n")

                return "error"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# 

def cifrado_AES_(tipo=1, texto=None, clave=None):
    if tipo == 1: # CIFRAR
        llave = Fernet.generate_key()
        try:
            f = Fernet(llave)
            texto_cifrado = f.encrypt(texto.encode())
        except Exception as e:
            return ["Error", str(e)]
        return [texto_cifrado, llave]
    else: # DESCIFRAR
        try:
            f = Fernet(clave)
            texto_descifrado = f.decrypt(texto).decode()
        except Exception as e:
            if str(e) == "" or str(e) is None:
                return f"Error: {__TR__('INVALIDO')}"
            return "Error: " + str(e)
        return texto_descifrado

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Mirar dependencias instaladas

def mirar_dependencias_instaladas_(tipo):
    if tipo == 1:
        try:
            PRUEBA = shutil.which("nmap")

            version = subprocess.run(["nmap", "--version"], capture_output=True, text=True, check=True)
            match = re.search(r'Nmap version ([\d\.]+)', version.stdout)
            if match: version = match.group(1)
            else: version = "None"

            RES = [True, f"{__TR__('ENCONTRADO')}", str(version)]
        except:
            RES = [False, f"{__TR__('NO_ENCONTRADO')}", None]
        
        return RES

    else:
        try:
            PRUEBA = sniff(count=1)
            RES = [True, f"{__TR__('ENCONTRADO')}"]
        except:
            RES = [False, f"{__TR__('NO_ENCONTRADO')}"]
        
        return RES

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Mirar que tipo de IP es

def tipo_ip_(IP):
    try:
        IP_res = ipaddress.ip_address(str(IP))
    except:
        return "N/A"

    if IP_res.is_link_local: return f"Link-local"
    if IP_res.is_private: return f"{__TR__('PRIVADA')}"
    if IP_res.is_global: return f"{__TR__('PUBLICA')}"
    if IP_res.is_loopback: return f"Loopback"
    if IP_res.is_multicast: return f"Multicast"
    if IP_res.is_reserved: return f"{__TR__('RESERVADA')}"
    if IP_res.is_unspecified: return f"N/A"
    

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Devolver el resultado del reporte de hardware y software

def ReporteEquipo():
    texto_poner_ = f"<span style='color: {obt_json_(6)};'>{__TR__('HARDWARE_DE')}</span> '<span style='color: {obt_json_(7)};'>{socket.gethostname()}</span>'<br>"
    
    if True:
        #################################
        ######## CALCULAR TAMAÑO ########
        #################################

        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f} {unit}{suffix}"
                bytes /= factor

        ##################################
        ######## CALCULAR VALORES ########
        ##################################

        res1 = psutil.virtual_memory()
        res1x = f"""<li>{__TR__('USO')}: <span style='color: {obt_json_(7)};'>{get_size(res1.used)} / {get_size(res1.total)}</span></li>
        <li>{__TR__('PORCENTAJE')}: <span style='color: {obt_json_(7)};'>{res1.percent}%</span></li>
        <li>{__TR__('DISPONIBLE')}: <span style='color: {obt_json_(7)};'>{get_size(res1.available)}</span></li>
        <li>{__TR__('LIBRE')}: <span style='color: {obt_json_(7)};'>{get_size(res1.free)}</span></li>
        """

        ########

        res2_particiones = psutil.disk_partitions()
        res2_particiones_2 = ""

        for i in res2_particiones:
            try:
                partition_usage = psutil.disk_usage(i.mountpoint)
            except PermissionError:
                partition_usage = ""
            
            res2_particiones_2 += f"""<br style='font-size: 8px;'><br style='font-size: 8px;'>
            <span style='color: {obt_json_(7)};'>{i.device}</span>
            <br>{__TR__('PUNTO_MONTAJE')}: <span style='color: {obt_json_(7)};'>{i.mountpoint}</span>
            <br>{__TR__('SISTEMA_ARCHIVOS')}: <span style='color: {obt_json_(7)};'>{i.fstype}</span>
            <br>{__TR__('OPCIONES_MONTAJE')}: <span style='color: {obt_json_(7)};'>{i.opts}</span>
            <br>{__TR__('USO')}: <span style='color: {obt_json_(7)};'>{get_size(partition_usage.used)} / {get_size(partition_usage.total)}</span> (<span style='color: {obt_json_(7)};'>{partition_usage.percent}%</span>)</br>
            <br>{__TR__('LIBRE')}: <span style='color: {obt_json_(7)};'>{get_size(partition_usage.free)}</span></br>
            """
        
        res2_io_read = get_size(psutil.disk_io_counters().read_bytes)
        res2_io_write = get_size(psutil.disk_io_counters().write_bytes)

        ########

        res3_nucleos_totales = psutil.cpu_count(logical=True)
        res3_nucleos_fisicos = psutil.cpu_count(logical=False)

        freq = psutil.cpu_freq()
        res3_max_freq = f"{freq.max:.2f} Mhz ({'' if f'{freq.max:.2f}' != f'{freq.current:.2f}' else str(__TR__('RES_CPU_1'))})"
        res3_min_freq = f"{freq.min:.2f} Mhz" if f"{freq.min:.2f}" != "0.00" else f"{__TR__('NO_DISPONIBLE')}"
        res3_actual_freq = f"{freq.current:.2f} Mhz ({'' if f'{freq.max:.2f}' != f'{freq.current:.2f}' else str(__TR__('RES_CPU_1'))})"

        res3_uso_total = f"{psutil.cpu_percent()}%"
        res3_uso_nucleos = ""
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            res3_uso_nucleos += f"<br>Core {i}: <span style='color: {obt_json_(7)};'>{percentage}%</span>"

        ########

        res4 = psutil.sensors_battery()
        segs_left = res4

        if res4.secsleft == psutil.POWER_TIME_UNLIMITED:
            segs_left = "POWER_TIME_UNLIMITED"
        elif res4.secsleft == psutil.POWER_TIME_UNKNOWN:
            segs_left = "POWER_TIME_UNKNOWN"
        else:
            minutos, segundos = divmod(res4.secsleft, 60)
            horas, minutos = divmod(minutos, 60)
            segs_left = f"{horas}h {minutos}min"

        try:
            res4x = f"""<li>{__TR__('PORCENTAJE')}: <span style='color: {obt_json_(7)};'>{res4.percent}%</span></li>
            <li>{__TR__('SEG_LEFT')}: <span style='color: {obt_json_(7)};'>{segs_left}</span></li>
            <li>{__TR__('ENCHUFADO')}: <span style='color: {obt_json_(7)};'>{res4.power_plugged}</span></li>
            """
        except:
            res4x = "N/A"

        ########

        try:
            e1 = platform.linux_distribution()
            e2 = platform.dist()
        except:
            e1, e2 = "N/A", "N/A"

        res5 = [platform.system(), platform.release(), platform.version(), platform.machine(), platform.platform(), platform.uname(), platform.mac_ver(), e1, e2, os.name, platform.architecture(), os.getlogin(), psutil.boot_time()]

        ########
        
        try:
            proceso = psutil.Process(os.getpid())
            f1 = proceso.name()
            f2 = proceso.exe()
            f3 = proceso.cmdline()
            f4 = proceso.create_time()
        except:
            f1, f2, f3 = "N/A", "N/A", "N/A"

        res6 = [os.getpid(), os.getppid(), f1, f2, f3]
        ########
        
        try:
            proceso = psutil.Process(os.getpid())
            uso_memoria_bytes = proceso.memory_info().rss

            res7 = f"{round(uso_memoria_bytes / (1024 * 1024), 2)} MiB"
        except:
            res7 = "N/A"

        #############################
        ######## PONER TEXTO ########
        #############################

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>{__TR__('MEMORIA')}</span>:</p>
<ul>
{res1x}
</ul>"""
        
        ############

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>{__TR__('DISCO_DURO')}</span>:</p>
<ul>
<li>{__TR__('PARTICIONES')}: {res2_particiones_2}</li>
<br style='font-size: 8px;'>
<li>IO Read: <span style='color: {obt_json_(7)};'>{res2_io_read}</span></li>
<li>IO Write: <span style='color: {obt_json_(7)};'>{res2_io_write}</span></li>
</ul>"""
        
        ############

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>CPU</span>:</p>
<ul>
<li>{__TR__('USO_TOTAL')}: <span style='color: {obt_json_(7)};'>{res3_uso_total}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('USO_POR_NUCLEOS')}: {res3_uso_nucleos}</li>
<br style='font-size: 8px;'>
<li>{__TR__('NUCLEOS_TOTALES')}: <span style='color: {obt_json_(7)};'>{res3_nucleos_totales}</span></li>
<li>{__TR__('NUCLEOS_FISICOS')}: <span style='color: {obt_json_(7)};'>{res3_nucleos_fisicos}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('FRECUENCIA_MAX')}: <span style='color: {obt_json_(7)};'>{res3_max_freq}</span></li>
<li>{__TR__('FRECUENCIA_MIN')}: <span style='color: {obt_json_(7)};'>{res3_min_freq}</span></li>
<li>{__TR__('FRECUENCIA_ACT')}: <span style='color: {obt_json_(7)};'>{res3_actual_freq}</span></li>
</ul>"""
        
        ############

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>{__TR__('BATERIA')}</span>:</p>
<ul>
{res4x}
</ul>"""
        ############

        texto_poner_ += f"<br>{'_'*50}<br>"

        texto_poner_ += f"<br><span style='color: {obt_json_(6)};'>{__TR__('SOFTWARE_DE')}</span> '<span style='color: {obt_json_(7)};'>{socket.gethostname()}</span>'<br>"
        
        ############

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>{__TR__('SO_MAYUS')}</span>:</p>
<ul>
<li>{__TR__('SISTEMA')}: <span style='color: {obt_json_(7)};'>{res5[0]}</span></li>
<li>Release: <span style='color: {obt_json_(7)};'>{res5[1]}</span></li>
<li>{__TR__('VERSION')}: <span style='color: {obt_json_(7)};'>{res5[2]}</span></li>
<li>{__TR__('TIPO')}: <span style='color: {obt_json_(7)};'>{res5[9]}</span></li>
<br style='font-size: 8px;'>
<li>Linux: <span style='color: {obt_json_(7)};'>{res5[7]}</span></li>
<li>Dist: <span style='color: {obt_json_(7)};'>{res5[8]}</span></li>
<br style='font-size: 8px;'>
<li>MacOS {__TR__('VERSION')}: <span style='color: {obt_json_(7)};'>{res5[6]}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('MACHINE')}: <span style='color: {obt_json_(7)};'>{res5[3]}</span></li>
<li>{__TR__('ARQUITECTURA')}: <span style='color: {obt_json_(7)};'>{res5[10]}</span></li>
<li>{__TR__('PLATFORM')}: <span style='color: {obt_json_(7)};'>{res5[4]}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('USUARIO_ACTUAL')}: <span style='color: {obt_json_(7)};'>{res5[11]}</span></li>

</ul>"""
        ############

        texto_poner_ += f"""<p><span style='color: {obt_json_(6)};'>AILI-SS App</span>:</p>
<ul>
<li>PID: <span style='color: {obt_json_(7)};'>{res6[0]}</span></li>
<li>PPID: <span style='color: {obt_json_(7)};'>{res6[1]}</span></li>
<li>{__TR__('NOMBRE_2')}: <span style='color: {obt_json_(7)};'>{res6[2]}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('RUTA')}: <span style='color: {obt_json_(7)};'>{res6[3]}</span></li>
<li>cmdline: <span style='color: {obt_json_(7)};'>{res6[4]}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('USO_RAM')}: <span style='color: {obt_json_(7)};'>{res7}</span></li>
<br style='font-size: 8px;'>
<li>{__TR__('VERSION')}: <span style='color: {obt_json_(7)};'>{obt_aili_json_(0)}</span></li>
</ul>"""
        
    ############
    ############
    ############

    return texto_poner_

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Ver el estado de un servidor

def estado_servidor_(SERVIDOR, SOLO_RES=False):
    if SOLO_RES:
        if os.name == "nt":
            return f"{__TR__('NO_DISPONILBE_WIN')}"
        else:
            ESTADO = subprocess.run(["systemctl", "is-active", SERVIDOR], capture_output=True, text=True)
            return ESTADO.stdout.strip()
    
    ###############
    # PARA EL LABEL
    if os.name == "nt":
        return f"{__TR__('ESTADO')} <span style='color: orange'>{__TR__('NO_DISPONILBE_WIN')}</span><br>{__TR__('ULTIMO_RES')} N/A"

    # LINUX
    ESTADO = subprocess.run(["systemctl", "is-active", SERVIDOR], capture_output=True, text=True)
    estado_txt = ESTADO.stdout.strip()
    color = "green" if estado_txt == "active" else "red"

    return f"{__TR__('ESTADO')} <span style='color: {color}'>{estado_txt}</span><br>{__TR__('ULTIMO_RES')} <span style='color: {color}'>{ESTADO.stderr}</span>"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Encender/reiniciar/parar un servidor

def manejar_1_servidor_(SERVIDOR, ACCION, LABEL):
    if os.name == "nt":
        return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: orange'>{__TR__('NO_DISPONILBE_WIN')}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>{ACCION} - {__TR__('NO_DISPONILBE_WIN')}</span>")

    # LINUX
    RESULTADO = subprocess.run(["service", SERVIDOR, ACCION], capture_output=True, text=True)

    ESTADO = estado_servidor_(SERVIDOR)
    color = "green" if ESTADO == "active" else "red"

    if RESULTADO.returncode != 0:
        return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>{ACCION} - {RESULTADO.stderr}</span>")
    else:
        return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: green'>{ACCION} - OK</span>")

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Abrir los registros de un servidor

def abrir_registros_servidor_(SERVIDOR, LABEL):
    if os.name == "nt":
        return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: orange'>{__TR__('NO_DISPONILBE_WIN')}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>{__TR__('REGISTROS')} - {__TR__('NO_DISPONILBE_WIN')}</span>")

    # LINUX
    ESTADO = estado_servidor_(SERVIDOR)
    color = "green" if ESTADO == "active" else "red"

    try: subprocess.run(["gedit", "/var/log/syslog"])
    except:
        try: subprocess.run(["nano", "/var/log/syslog"])
        except Exception as e:
            ERR_REG_(f"[abrir_registros_servidor_] No se encuentra el archivo /var/log/syslog o no se encuentra un editor.\n\n")

            return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>{__TR__('REGISTROS')} - {__TR__('NO_HAY_EDITORES')}</span>")

    return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: green'>{__TR__('REGISTROS')} - OK</span>")

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Configurar un servidor

def configurar_servidor_(SERVIDOR, LABEL):
    if os.name == "nt":
        return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: orange'>{__TR__('NO_DISPONILBE_WIN')}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>Config - {__TR__('NO_DISPONILBE_WIN')}</span>")

    # LINUX

    # Elegir archivo
    ARCHIVOS = []
    if SERVIDOR == "isc-dhcp-server":
        ARCHIVOS = ["/etc/dhcp/dhcpd.conf", "/etc/default/isc-dhcp-server"]
    if SERVIDOR == "bind9":
        ARCHIVO = ["/etc/bind/named.conf", "/etc/bind/named.conf.local", "/etc/bind/named.conf.default-zones", "/etc/bind/named.conf.options"]
    if SERVIDOR == "apache2":
        ARCHIVO = ["/etc/apache2/apache2.conf", "/etc/apache2/ports.conf"]
    if SERVIDOR == "vsftpd":
        ARCHIVO = ["/etc/vsftpd.conf"]
    if SERVIDOR == "postfix":
        ARCHIVO = ["/etc/postfix/main.cf", "/etc/postfix/master.cf"]


    ESTADO = estado_servidor_(SERVIDOR)
    color = "green" if ESTADO == "active" else "red"

    for i in ARCHIVOS:
        try: subprocess.run(["gedit", i])
        except:
            try: subprocess.run(["nano", i])
            except Exception as e:
                ERR_REG_(f"[abrir_registros_servidor_] No se encuentra el archivo {i} o no se encuentra un editor.\n\n")

                return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: red'>Config - {__TR__('NO_HAY_EDITORES')}</span>")

    return LABEL.setText(f"{__TR__('ESTADO')} <span style='color: {color}'>{ESTADO}</span><br>{__TR__('ULTIMO_RES')} <span style='color: green'>Config - OK</span>")

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Instalar un servidor

def instalar_servidor_(SERVIDOR):
    if os.name == "nt":
        return "win"

    if SERVIDOR == "isc-dhcp-server": COMANDOS = ["sudo apt-get update", "sudo apt-get install isc-dhcp-server", "sudo ufw allow 67"]  
    if SERVIDOR == "bind9":           COMANDOS = ["sudo apt-get update", "sudo apt-get install bind9", "sudo ufw allow 53"]  
    if SERVIDOR == "apache2":         COMANDOS = ["sudo apt-get update", "sudo apt-get install apache2 apache2-utils", "sudo ufw allow 80"]  
    if SERVIDOR == "vsftpd":          COMANDOS = ["sudo apt-get update", "sudo apt-get install vsftpd", "sudo ufw allow 21"]  
    if SERVIDOR == "postfix":         COMANDOS = ["sudo apt-get update", "sudo apt-get install postfix", "sudo ufw allow 25"]

    for i in COMANDOS:
        try:
            resultado = subprocess.run(i, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            return f"{e}"
    
    return "Ok"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# Desinstalar un servidor

def desinstalar_servidor_(SERVIDOR):
    if os.name == "nt":
        return "win"

    if SERVIDOR == "isc-dhcp-server": COMANDOS = ["sudo apt uninstall isc-dhcp-server", "sudo ufw deny 67"]  
    if SERVIDOR == "bind9":           COMANDOS = ["sudo apt uninstall bind9", "sudo ufw deny 53"]  
    if SERVIDOR == "apache2":         COMANDOS = ["sudo apt uninstall apache2 apache2-utils", "sudo ufw deny 80"]  
    if SERVIDOR == "vsftpd":          COMANDOS = ["sudo apt uninstall vsftpd", "sudo ufw deny 21"]  
    if SERVIDOR == "postfix":         COMANDOS = ["sudo apt uninstall postfix", "sudo ufw deny 25"]

    for i in COMANDOS:
        try:
            resultado = subprocess.run(i, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            return f"{e}"
    
    return "Ok"

####~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~~~~~~~#############
#~~~#################~~~~~~~~~~~~~~~~~~~###################~~~~~~~~~~~
# 