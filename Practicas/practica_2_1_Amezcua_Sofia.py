#Ejercicio 1 Datos personales
nombre = "Sofia"
edad =21
ciudad = "Guadalajara"
print(nombre, edad, ciudad)

#Ejercicio 2 Actualizar contador
contador = 0
operacion1 = 1
operacion2 = 2
resultado = 0
resultado += operacion1+operacion2
print(resultado)

#Ejercicio 3 Constante de conversión
PULGADAS_A_CM = 2.54
centimetros = input("Ingrese la cantidad de pulgadas a convertir: ")
resultado = float(centimetros) * PULGADAS_A_CM
print(resultado)

#Ejercicio 4 Area de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)

# Ejercicio 5 Total con IVA
precio = float(input("Ingrese el precio del producto: "))
IVA = 0.16
total = precio + (precio * IVA)
print(total)

#Ejercicio 6 Intercambio de valores
a = 5
b = 10
print("Valores iniciales:")
print("a =", a)
print("b =", b)
a, b = b, a
print("Valores intercambiados:")
print("a =", a)
print("b =", b)

#Ejercicio 7 Identificar tipos con type()
variable1 = 10
variable2 = 3.14
variable3 = "Trece"
variable4 = bool(True)
print("El tipo de variable1 es:", type(variable1))
print("El tipo de variable2 es:", type(variable2))
print("El tipo de variable3 es:", type(variable3))
print("El tipo de variable4 es:", type(variable4))

#Ejercicio 8 Convertir tipos
numero_entero = int(input("Ingrese un número entero: "))
numero_flotante = float(numero_entero)
print("El número entero es:", numero_entero)
print("El número flotante es:", numero_flotante)

#Ejercicio 9 Booleanos y comparaciones
a = 5
b = 10
c = a < b
print("¿",a, "es menor que", b,"?", c)
print("¿",a, "es mayor que", b,"?", a > b)
