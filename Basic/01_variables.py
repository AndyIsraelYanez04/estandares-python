# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

mi_variable_en_str = "My String variable"
print(mi_variable_en_str)

mi_variable_int = 5
print(mi_variable_int)

mi_variable_int_a_str = str(mi_variable_int) #tranformando un entero a string
print(mi_variable_int_a_str)
print(type(mi_variable_int_a_str))

mi_variable_bool = False
print(mi_variable_bool)

# Concatenación de variables en un print
print(mi_variable_en_str, mi_variable_int_a_str, mi_variable_bool)
print("Este es el valor de:", mi_variable_bool)

# Algunas funciones del sistema
print(len(mi_variable_en_str))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Andy", "de la Cruz", 'Isra', 22
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
# name = input('¿Cuál es tu nombre? ')
# age = input('¿Cuántos años tienes? ')
# print(name)
# print(age)

# Cambiamos su tipo
name = 35
age = "Andy"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
