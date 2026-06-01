"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
# Escribe tu código aquí

mensaje = "Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí

mensaje = "Hello world!"
print(mensaje)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí

full_name = "Adriana"
age = 35
height = 1.82
children = False
hobbies = ["patinar", "juegos de mesa", "programar" ]
students = ("Luisa", "Lexy", "Dhana", "Adriana")
user = {
    "name": "Adriana",
    "age": 35,
    "height": 1.82,
    "las_name": "Suárez"
}
animals = {"perro", "gato", "loro", "gato"}

print(full_name)
print(type(full_name))
print(age)
print(type(age))
print(height)
print(type(height))
print(children)
print(type(children))
print(hobbies)
print(type(hobbies))
print(students)
print(type(students))
print(user)
print(type(user))
print(animals)
print(type(animals))

