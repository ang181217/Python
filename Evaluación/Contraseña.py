import random
import string

def generar_contrasena(longitud, num_minusculas, num_mayusculas, num_numeros):
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    caracteres = ''.join([random.choice(minusculas) for _ in range(num_minusculas)])
    caracteres += ''.join([random.choice(mayusculas) for _ in range(num_mayusculas)])
    caracteres += ''.join([random.choice(numeros) for _ in range(num_numeros)])
    caracteres += ''.join([random.choice(string.punctuation) for _ in range(longitud - len(caracteres))])
    contrasena = ''.join(random.sample(caracteres, longitud))
    return contrasena

if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    num_minusculas = int(input("Ingresa el número de letras minúsculas: "))
    num_mayusculas = int(input("Ingresa el número de letras mayúsculas: "))
    num_numeros = int(input("Ingresa el número de dígitos: "))

    generar_contrasena = generar_contrasena(longitud, num_minusculas, num_mayusculas, num_numeros)
    
    print(f"Tu contraseña generada es: {generar_contrasena}")
