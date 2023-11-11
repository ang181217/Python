import re

def validar_ip(ip):
    patron_ip = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    if patron_ip.match(ip):
        octetos = ip.split('.')
        if all(0 <= int(octeto) <= 255 for octeto in octetos):
            return True
    return False

ip_ingresada = input("Ingresa una dirección IP: ")

if validar_ip(ip_ingresada):
    print(f"{ip_ingresada} es una dirección IP válida.")
else:
    print(f"{ip_ingresada} no es una dirección IP válida.")
