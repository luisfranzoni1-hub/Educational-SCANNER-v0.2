import os
import time

enter1 = input("Primero que todo, Necesitas nmap instalado para usar nuestro systema de escaneos avanzados, Presiona enter para quitar advertencia")
os.system(f"cls")

print("""
EEEEEE  Unirse al Cyber team hack?: Mandanos mensaje a tiktok @perkito00 Solo debes decir "Quiero unirme a cyber team hack" y programamos Juntos, tambien enseñamos a programar python
E       Escaners: 5 Nmap + Ping
EEEEEE  SCANER-v0.2
E       Creator: Luis
EEEEEE  Compatibylity: Windows/Linux 
""")
print("""
---------------------------------------------------------------------------------------------------------------------
1. Escaneo super rapido Ruidoso y Peligroso, Usar en propias redes.                           Escaneo de puertos T5 *
2. Escaneo rapido el mejor que puedes usar para nuestros escaneos de puertos.                 Escaneo de puertos T4 *
3. Escaneo Anti bloqueos de Firewalls, Super rapido, Y escanea servicios.                     Multi-Escaneo T5 SV PN*         NO! No me ago responsable por los escaneos que ases.
4. Escaneo De Systema operativo y puertos Rapido, Y escanea servicios activos de los puertos. Multi escaneo T4 O SV *         Recuerda que El hacking etico y la legalidad lo es todo.
5. Ping para ver si existe tal ip,                                                            Ping, Existencia de IP*
6. Visualizador de TODAS las carpetas de tu pc, Usa dir, solo en windows.                                           *
0. Exit.                                                                                                            *
99. Info sobre creacion de ESCANERS SYSTEM                                                                          *
----------------------------------------------------------------------------------------------------------------------
      """)

while True:
    opcion = input("Ingresa una opcion valida, Primero lee bien, Gracias!> ")

    if opcion == "1":
        ip = input("Ingresa ip a escaneo Rapido: ")
        print("Escaneando... Porfavor espera")
        os.system(f"nmap -T5 {ip}")

    elif opcion == "2":
        ip2 = input("Ingresa Ip valida a escaneo Rapido T4: ")
        os.system(f"nmap -T4 {ip2}")

    elif opcion == "3":
        ip3 = input("Ingresa ip a Multi Escaneo: ")
        os.system(f"nmap -T5 -sV -Pn {ip3}")

    elif opcion == "4":
        ip4 = input("Ingresa ip Valida a Escaneo multiple, De los buenos: ")
        os.system(f"nmap -T4 -O -sV {ip4}")

    elif opcion == "5":
        ip5 = input("Ingresa ip a Ping para ver si existe tal ip, Se recomienda usar este antes de escanear: ")
        os.system(f"ping {ip5}")
    
    elif opcion == "6":
        print("Aviso, No estas hackeando nada, estas visualizando TODAS las carpetas de tu pc windows, gracias por usar la opcion 6 ")
        time.sleep(3)
        os.system(f"dir/s")
        print("Son demasiados archivos, debemos limpiar tu pantalla :)")
        time.sleep(4)
        print("Gracias por esperar :D")
        os.system(f"cls")
    
    elif opcion == "99":
        print("""
Info: Este systema fue creado por un niño de 10 años que se llamaba Luis, Quiso aser su propio systema de escaneo legal con su conocimiento de python
Y esperemos que todo salga bien, todo echo por una niño, Lanzare actualizaciones de mas escaneos, como vulnerabilidades, Escaneos sql, y mucho mas
Tomate un cafe ponete a programar o a aser cyberseguridad siempre la legalidad, Gracias por leer Esta info :)
              """)
    
    elif opcion == "0":
        print("Chau, Gracias por usar mi humilde systema echo con la lengua de programacion python")
        time.sleep(1)
        break

    else:
        print("Opcion incorrecta, Lee todas las opciones, son los numeros Gracias!")
