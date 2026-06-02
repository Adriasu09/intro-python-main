"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
# Escribe tu código aquí
letra = input("Ingresa una letra: ").lower()
vocales = ["a", "e", "i", "o", "u"]

if letra in vocales:
    print("Has ingresado una vocal")
else:
    print("Has ingresado una consonante")

"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
# Escribe tu código aquí
nota = int(input("Ingresa una nota: "))
calificacion = ["A", "B", "C", "D", "F"]

if nota == 9 or nota == 10:
    print(f"Su calificación es {calificacion[0]}")
elif nota == 7 or nota == 8:
    print(f"Su calificación es {calificacion[1]}")
elif nota == 5 or nota == 6:
    print(f"Su calificación es {calificacion[2]}")
elif nota == 4:
    print(f"Su calificación es {calificacion[3]}")
else:
    print(f"Su calificación es {calificacion[4]}")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
# Escribe tu código aquí
numero = int(input("Ingrese un número: "))
stop_bucle = 0
while stop_bucle < numero:
    print(numero, end=" ")
    numero -= 1

print()
"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí
cadena_texto = input("Ingresa una cadena de texto: ")
for caracter in cadena_texto:
    print(caracter, end=" ")

print()
"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí
numero_table = 5
print(f"tabla de multiplicar del {numero_table}")
for i in range(1, 11):
    result = i * numero_table
    print(f"{numero_table} * {i} = {result}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí
lista_usuario = []
for i in range(5):
    palabra = input("Ingresa una palabra: ")
    lista_usuario.append(palabra)

lista_mayuscula = []
for palabra in lista_usuario:
    lista_mayuscula.append(palabra.upper())

print(lista_mayuscula)


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí
mascota = input("Ingresa una mascota: ").lower()
if mascota == "perro":
    print("Tengo un perro")
elif mascota == "gato":
    print("Tengo un gato")
elif mascota == "pájaro":
    print("Tengo un pájaro")
else:
    print("No tengo una mascota convencional")

