#Ejercicio 1 Datos personales
print("--- Ejercicio 1 ---")
nombre = "Sofia"
edad =21
ciudad = "Guadalajara"
print(nombre, edad, ciudad)

nombre = "Airam"
edad =19
ciudad = "Guadalajara"
print(nombre, edad, ciudad)

#Ejercicio 2 Actualizar contador
print("\n--- Ejercicio 2 ---")
print("Contador: 0")
contador = 0
contador = contador + 1
print("Contador:", contador)
contador = contador + 1
print("Contador:", contador)
contador = contador + 1
print("Contador:", contador)

#Ejercicio 3 Constante de conversión
print("\n--- Ejercicio 3 ---")
PULGADAS_A_CM = 2.54
centimetros = 13
resultado = centimetros * PULGADAS_A_CM
print(resultado)

PULGADAS_A_CM = 2.54
centimetros = 84
resultado = centimetros * PULGADAS_A_CM
print(resultado)

#Ejercicio 4 Area de un triángulo
print("\n--- Ejercicio 4 ---")
base = 8
altura = 6
area = (base * altura) / 2
print("El área del triángulo es:", area)

# Extra: Perímetro
perimetro = 2 * base + 2 * altura
print("El perímetro es:", perimetro)

base = 38
altura = 54
area = (base * altura) / 2
print("El área del triángulo es:", area)

# Extra: Perímetro
perimetro = 2 * base + 2 * altura
print("El perímetro es:", perimetro)

# Ejercicio 5 Total con IVA
print("\n--- Ejercicio 5 ---")
precio = 500
IVA = 0.16
total = precio + (precio * IVA)
print("Precio: 500 -> Total a pagar:", total)

precio = 165
IVA = 0.16
total = precio + (precio * IVA)
print("Precio: 165 -> Total a pagar:", total)

#Ejercicio 6 Intercambio de valores
print("\n--- Ejercicio 6 ---")
a = 5
b = 10
print("Valores iniciales:")
print("a =", a)
print("b =", b)
a, b = b, a
print("Valores intercambiados:")
print("a =", a)
print("b =", b)
print("\n- Segunda entrada ")
a = 20
b = 5
print("Valores iniciales:")
print("a =", a)
print("b =", b)
a, b = b, a
print("Valores intercambiados:")
print("a =", a)
print("b =", b)

#Ejercicio 7 Identificar tipos con type()
print("\n--- Ejercicio 7 ---")
variable1 = 10
variable2 = 3.14
variable3 = "Trece"
variable4 = True
print("El tipo de variable1 es:", type(variable1))
print("El tipo de variable2 es:", type(variable2))
print("El tipo de variable3 es:", type(variable3))
print("El tipo de variable4 es:", type(variable4))
print("\n- Segunda entrada ")
variable1 = 80
variable2 = 45.7
variable3 = "Veintidos"
variable4 = False
print("El tipo de variable1 es:", type(variable1))
print("El tipo de variable2 es:", type(variable2))
print("El tipo de variable3 es:", type(variable3))
print("El tipo de variable4 es:", type(variable4))

#Ejercicio 8 Convertir tipos
print("\n--- Ejercicio 8 ---")
texto_numero = "25"
numero_convertido = int(texto_numero)
entero_original = 100
texto_convertido = str(entero_original)
print("Texto a int:", numero_convertido, "| Tipo:", type(numero_convertido))
print("Int a texto:", texto_convertido, "| Tipo:", type(texto_convertido))

texto_numero = "289"
numero_convertido = int(texto_numero)
entero_original = 300
texto_convertido = str(entero_original)
print("Texto a int:", numero_convertido, "| Tipo:", type(numero_convertido))
print("Int a texto:", texto_convertido, "| Tipo:", type(texto_convertido))

#Ejercicio 9 Booleanos y comparaciones
print("\n--- Ejercicio 9 ---")
a = 5
b = 10
c = a < b
print("¿",a, "es menor que", b,"?", c)
print("¿",a, "es mayor que", b,"?", a > b)

a = 13
b = 20
c = a < b
print("¿",a, "es menor que", b,"?", c)
print("¿",a, "es mayor que", b,"?", a > b)