import os
import time

# Activar colores ANSI en Windows
os.system("")

# COLORES
ROJO = "\033[31m"
RESET = "\033[0m"

enter1 = input("Primero que todo, Necesitas nmap instalado para usar nuestro systema de escaneos avanzados, Presiona enter para quitar advertencia")
os.system("cls")

print(f"""
{ROJO}EEEEEE{RESET}  Unirse al Cyber team hack?: Mandanos mensaje a tiktok @perkito00
{ROJO}E{RESET}       Escaners: 5 Nmap + Ping
{ROJO}EEEEEE{RESET}  SCANER-v0.3 VERSION ACTUALIZADA! agregamos colores. y mas cosas 
{ROJO}E{RESET}       Creator: Luis
{ROJO}EEEEEE{RESET}  Compatibylity: Windows/Linux 
""")

print(f"""
---------------------------------------------------------------------------------------------------------------------
{ROJO}1.{RESET} Escaneo super rapido Ruidoso y Peligroso, Usar en propias redes.                    Escaneo T5 *
{ROJO}2.{RESET} Escaneo rapido el mejor que puedes usar.                                           Escaneo T4 *
{ROJO}3.{RESET} Escaneo Anti bloqueos de Firewalls, escanea servicios.                              Multi T5 SV *
{ROJO}4.{RESET} Escaneo de Sistema operativo + puertos + servicios.                                Multi T4 *
{ROJO}5.{RESET} Ping para ver si existe tal IP.                                                     Ping *
{ROJO}6.{RESET} Visualizador de TODAS las carpetas (Windows).                                      DIR *
{ROJO}7.{RESET} Escaneo de vulnerabilidades.                                                        NMAP *
{ROJO}0.{RESET} Exit.
{ROJO}99.{RESET} Info sobre creacion del ESCANERS SYSTEM
---------------------------------------------------------------------------------------------------------------------
""")

while True:
    opcion = input(f"{ROJO}Ingresa una opcion valida > {RESET}")

    if opcion == "1":
        ip = input("Ingresa ip a escaneo Rapido: ")
        print("Escaneando... Porfavor espera")
        os.system(f"nmap -T5 {ip}")

    elif opcion == "2":
        ip2 = input("Ingresa Ip valida a escaneo Rapido T4: ")
        for i in range(200):
            print("Escaneando puertos abiertos...")
            time.sleep(0.01)
            
        os.system(f"nmap -T4 {ip2}")

    elif opcion == "3":
        ip3 = input("Ingresa ip a Multi Escaneo: ")
        os.system(f"nmap -T5 -sV -Pn {ip3}")

    elif opcion == "4":
        ip4 = input("Ingresa ip Valida a Escaneo multiple: ")
        os.system(f"nmap -T4 -O -sV {ip4}")

    elif opcion == "5":
        ip5 = input("Ingresa ip a Ping: ")
        os.system(f"ping {ip5}")
    
    elif opcion == "6":
        print("Aviso, no estas hackeando nada, solo viendo carpetas.")
        time.sleep(3)
        os.system("dir /s")
        time.sleep(4)
        os.system("cls")
    
    elif opcion == "7":
        ip7 = input("Ingresa ip a escanear vulnerabilidades: ")
        os.system(f"nmap -T4 --script=vuln {ip7}")

    elif opcion == "99":
        print("""
Info: Este systema fue creado por un niño de 10 años llamado Luis.
Todo hecho en Python, con fines educativos y legales.
Siempre hacking ético.
""")
    
    elif opcion == "0":
        print("Chau, Gracias por usar mi systema")
        time.sleep(1)
        break

    else:
        print("Opcion incorrecta, lee bien las opciones.")
