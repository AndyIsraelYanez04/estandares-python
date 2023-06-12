"""ejercicio pequeño para hacer 
en Python. Tu objetivo es escribir un programa que determine si un 
número ingresado por el usuario es par o impar.

Planteamiento del ejercicio:

1. Solicitar al usuario que ingrese un número.
2. Leer y almacenar el valor ingresado en una variable.
3. Verificar si el número es divisible por 2.
4. Si el número es divisible por 2, imprimir un mensaje indicando que es par.
5. Si el número no es divisible por 2, imprimir un mensaje indicando que es impar.

Tu tarea es escribir el código para este programa y comprobar si el número ingresado 
por el usuario es par o impar. ¡Diviértete resolviendo el ejercicio!"""



# n1 = int(input("ingrese numero"))

# if n1 % 2 == 0 :
#     print( n1, "este numero es par" + str(n1 % 2) ) #me da el residuo  %
# else :
#     print (n1, "es impar")

"""¡Claro! Aquí tienes un ejercicio sencillo para practicar en Python:

Ejercicio: Calculadora de suma y resta
Escribe un programa en Python que le pida al usuario ingresar dos números enteros
 y luego le permita elegir si desea sumar o restar esos números. 
 El programa debe realizar la operación seleccionada y mostrar el resultado.

Puedes intentar resolver este ejercicio por ti mismo y luego comparar tu solución 

con la que te proporcionaré. ¡Diviértete programando!"""


# num1 = int(input("Ingrese el primer número: "))
# operador = input("Ingrese el operador")
# num2 = int(input("Ingrese el segundo número: "))

# if operador == "+":
#     resultado = num1 + num2
#     print("El resultado de la suma es:", resultado)
# elif operador == "-":
#     resultado = num1 - num2
#     print("El resultado de la resta es:", resultado)
# elif operador == "/":
#     resultado = num1 / num2
#     print("El resultado de la division es:", resultado)

# elif operador == "*":
#     resultado = num1 * num2
#     print("El resultado de la multiplicaion es:", resultado)
# else:
#     print("Solo funciona con las cuatro operaciones basicas")

"""¡Por supuesto! Aquí tienes otro ejercicio sencillo para que lo resuelvas por ti mismo en Python:

Ejercicio: Cálculo del área de un triángulo
Escribe un programa en Python que solicite al usuario ingresar la base y la altura 
de un triángulo y calcule su área. Recuerda que el área de un triángulo se calcula
 utilizando la fórmula: área = (base * altura) / 2.

Puedes intentar resolver este ejercicio por ti mismo y luego verificar tu solución. ¡Buena suerte!"""




# base = float(input("Ingrese la base del triángulo: "))
# altura = float(input("Ingrese la altura del triángulo: "))

# area = (base * altura) / 2

# print("El área del triángulo es:", area)


"""Por supuesto, aquí tienes otro ejercicio sencillo para que lo resuelvas por ti mismo en Python:

Ejercicio: Contador de vocales
Escribe un programa en Python que solicite al usuario ingresar una palabra o una frase
 y luego cuente y muestre la cantidad de vocales que contiene. Puedes asumir que el usuario 
 solo ingresará letras en minúscula y sin caracteres especiales.

Puedes intentar resolver este ejercicio por ti mismo y luego verificar tu solución. 
¡Diviértete programando!"""


# palabra = input("Ingrese una palabra o frase: ")
# vocales = "aeiou"
# contador = 0

# for letra in palabra:
#     if letra.lower() in vocales:
#         contador += 1

# print("La cantidad de vocales en la palabra o frase es:", contador)


"""¡Por supuesto! Aquí tienes otro ejercicio sencillo para que lo resuelvas por ti mismo en Python:

Ejercicio: Calculadora de promedio
Escribe un programa en Python que solicite al usuario ingresar tres números y luego calcule 
y muestre el promedio de esos números.

Puedes intentar resolver este ejercicio por ti mismo y luego verificar tu solución. 

¡Diviértete programando!"""


# n1 = int(input("ingrese primer numero "))
# n2 = int(input("ingrese segundo numero "))
# n3 = int(input("ingrese tercer numero "))

# promedio = (n1 + n2 + n3)

# print("el promedio es ", promedio/ 3)


"""2. Conversor de temperatura: Escribe un programa que solicite al usuario ingresar una temperatura 
en grados Celsius y la convierta a grados Fahrenheit. La fórmula para la conversión 
es: Fahrenheit = (Celsius * 9/5) + 32."""



# n1 = float(input("una temperatura en grados Celsius "))

# Fahrenheit = (n1 * 9 / 5) + 32

# print("este es el resultado", Fahrenheit)



"""3. Números primos: Escribe un programa que solicite al usuario ingresar un número y determine 
si es primo o no. Un número primo es aquel que solo es divisible por 1 y por sí mismo.
"""

# numero = int(input("Ingrese un número: "))

# if numero <= 1:
#     print("El número no es primo.")
# else:
#     es_primo = True
#     for i in range(2, numero):
#         if numero % i == 0:
#             es_primo = False
#             break

#     if es_primo:
#         print("El número es primo.")
#     else:
#         print("El número no es primo.")

"""4. Calculadora de factorial: Escribe un programa que solicite al usuario ingresar un número y 
calcule su factorial. El factorial de un número entero n se calcula multiplicando todos los números 
desde 1 hasta n."""


# numero = int(input("Ingrese un número: "))

# factorial = 1

# if numero < 0:
#     print("El factorial no está definido para números negativos.")
# elif numero == 0:
#     print("El factorial de 0 es 1.")
# else:
#     for i in range(1, numero + 1):
#         factorial *= i

#     print("El factorial de", numero, "es:", factorial)


"""5. Inversión de cadena: Escribe un programa que solicite al usuario ingresar una palabra o una 
frase y muestre la cadena invertida. Por ejemplo, si el usuario ingresa "Hola, mundo!", el programa 
debería mostrar "!odnum ,aloH"."""



# n1 = input("ingrese palabra")

# resultado = n1[::-1] # imprime desde el finala cada letar

# print(resultado)

"""1. Clase Persona: Crea una clase llamada Persona con atributos como nombre, edad
 y profesión. Luego, crea objetos de esta clase y muestra sus atributos.
 
"""

# class Persona:
#     def __init__(self, nombre, edad, profesion):
#         self.nombre = nombre
#         self.edad = edad
#         self.profesion = profesion

# # Crear objetos de la clase Persona
# persona1 = Persona("Juan", 30, "Ingeniero")
# persona2 = Persona("María", 25, "Abogada")

# # Mostrar los atributos de los objetos
# print("Persona 1:")
# print("Nombre:", persona1.nombre)
# print("Edad:", persona1.edad)
# print("Profesión:", persona1.profesion)
# print()

# print("Persona 2:")
# print("Nombre:", persona2.nombre)
# print("Edad:", persona2.edad)
# print("Profesión:", persona2.profesion)


"""2. Clase Coche: Crea una clase llamada Coche con atributos como marca, modelo y año. 
Implementa métodos para acelerar, frenar y mostrar información del coche.
"""

# class Coche:
#     def __init__(self, marca, modelo, año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#         self.velocidad = 0

#     def acelerar(self, incremento):
#         self.velocidad += incremento

#     def frenar(self, decremento):
#         self.velocidad -= decremento

#     def mostrar_informacion(self):
#         print("Marca:", self.marca)
#         print("Modelo:", self.modelo)
#         print("Año:", self.año)
#         print("Velocidad:", self.velocidad, "km/h")

# # Crear un objeto de la clase Coche
# coche1 = Coche("Toyota", "Corolla", 2022)

# # Mostrar información del coche antes de acelerar o frenar
# coche1.mostrar_informacion()
# print()

# # Acelerar el coche en 50 km/h
# coche1.acelerar(50)

# # Mostrar información del coche después de acelerar
# coche1.mostrar_informacion()
# print()

# # Frenar el coche en 20 km/h
# coche1.frenar(20)

# # Mostrar información del coche después de frenar
# coche1.mostrar_informacion()



"""4. Clase Libro: Crea una clase llamada Libro con atributos como título, autor y año de publicación. 
Implementa un método para mostrar la información completa del libro.
"""

class Libro:
    def __init__(self,titulo, autor ,año_publicaion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicaion = año_publicaion

    def mostrar_informacion(self):
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Año_publicacion:", self.año_publicaion)

#creacion de un objeto 
mi_libro = Libro("lo que el viento se llevo" , "Andy", "2000")

mi_libro.mostrar_informacion()
print()


    

"""5. Clase Estudiante: Crea una clase llamada Estudiante con atributos como nombre, edad y lista de
 asignaturas. Implementa métodos para agregar una asignatura, eliminar una asignatura 
 y mostrar las asignaturas del estudiante.
"""



class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def eliminar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            print("La asignatura no está en la lista de asignaturas del estudiante.")

    def mostrar_asignaturas(self):
        if self.asignaturas:
            print("Asignaturas del estudiante", self.nombre + ":")
            for asignatura in self.asignaturas:
                print(asignatura)
        else:
            print("El estudiante no tiene asignaturas.")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Juan", 20)

# Agregar asignaturas al estudiante
estudiante1.agregar_asignatura("Matemáticas")
estudiante1.agregar_asignatura("Historia")
estudiante1.agregar_asignatura("Inglés")

# Mostrar las asignaturas del estudiante
estudiante1.mostrar_asignaturas()
print()

# Eliminar una asignatura del estudiante
estudiante1.eliminar_asignatura("Historia")

# Mostrar las asignaturas actualizadas del estudiante
estudiante1.mostrar_asignaturas()

