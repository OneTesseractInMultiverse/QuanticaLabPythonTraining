# --------------------------------------------------
# Declaracion de variables
# --------------------------------------------------

# nombre de la variable | valor de la variable
# Python es un leguaje con tipos dinámicos. Eso quiere decir que 
# el intérprete de Python se encarga de inferir cual es el tipo 
# de dato da cada una de las variables basado en su representación

# Declaración de una variable cuyo valor es un número entero

primer_entero = 101

# Veamos el qué tipo de datos detectó Python
print(type(primer_entero))

# Lo malo de esto, es que se pueden redefinir variables y Python
# no va a tirar ningún error. Por ejemplo:

primer_entero = "Esto es una cade de caracteres"

# Veamos ahora después de redefinir esta variable, qué tipo de dato
# detecta Python
print(type(primer_entero))

# Python no nos da error, sin embargo, esto es una mala práctica de 
# programación.

entero_a = 1290
flotante_a = 123.1233

resultado = entero_a + flotante_a
print(type(resultado))

# -------------------------------------------------------
# ESTRUCTURAS DE CONTROL
# -------------------------------------------------------

# -------------------------------------------------------
# EJEMPLO DE UN IF de IFs en Python ---------------------

hoy_esta_lloviendo = False
hoy_pagan_salario = False
hoy_estoy_aprendiendo_python = True
pronto_voy_a_tener_hambre = True

if hoy_esta_lloviendo and hoy_pagan_salario:
    # Para definir que un bloque de código se encuentra dentro de otro,
    # el bloque contenido se debe escribir 4 espacios hacia andentro con
    # respecto al bloque que lo contiene
    print("Hoy no es un buen día")
elif hoy_pagan_salario and (not hoy_estoy_aprendiendo_python) or pronto_voy_a_tener_hambre:
    print("Hoy es un dia normal")
else:
    print("Esto pasa si ninguna de las condiciones anteriores se cumple")

# ---------------------------------------------------------
# EJEMPLO DE UN WHILE -------------------------------------

# Este ciclo solicita al usuario un número entero. Si el número
# digitado no es un entero válido, le muestra un error y le
# solicita nuevamente un número entero. Le sigue solicitando
# un número hasta que el usuario digite un número válido

valor_valido = False
while not valor_valido:
    try:
        valor_digitado = int(input("Digite un número entero: "))
        valor_valido = True
        print("Uste digitó {} y este es un número entero válido".format(valor_digitado))
    except Exception as e:
        print("El valor digitado no es un número entero válido")


# ---------------------------------------------------------
# EJEMPLO DE UN FOR  --------------------------------------

# For con un rango. Para esto, vamos a hacer un código que imprima
# todos los números divisibles por 3 entre 0 y 100

multiplos_de_tres = []

for numero in range(0, 100):
    if numero % 3 == 0:
        multiplos_de_tres.append(numero)

print(multiplos_de_tres)

tamano = int(input("digite el tamaño de la matriz: "))

# Imprimiendo una matriz de caracteres
for fila in range(0, tamano):
    lista_fila = ""
    for columna in range(0, tamano):
        lista_fila += "[*]"
    print(lista_fila)


print("\n\n ------------------------------------------------------------------ \n \n")

# Imprimiendo una matriz de caracteres pero con una de las diagonales
for fila in range(0, tamano):
    lista_fila = ""
    for columna in range(0, tamano):
        if fila == columna:
            lista_fila += "[A]"
        else:
            lista_fila += "[*]"
    print(lista_fila)



# Tarea cree código que genere las matrices con los siguientes patrones:
# (debe funcionar para matrices de cualquier tamano)

"""
 (1) - 
 
    [A][*][*][*][A]
    [*][A][*][A][*]
    [*][*][A][*][*]
    [*][A][*][A][*]
    [A][*][*][*][A]
    
 (2) - 
 
    [0][0][0][0][0]
    [*][0][0][0][*]
    [*][*][0][*][*]
    [*][0][0][0][*]
    [O][O][O][O][O]
    
(2) - 
 
    [0][*][*][*][*]
    [0][0][*][*][*]
    [0][0][0][*][*]
    [0][0][0][0][*]
    [O][O][O][O][O]
 
"""











