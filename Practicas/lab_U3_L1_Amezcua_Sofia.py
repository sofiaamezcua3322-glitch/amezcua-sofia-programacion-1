#Lab U3 Comparaciones múltiples
#Alumna: Sofia Amezcua Rosales
#Objetivo: Practicar cadenas de decisión simples y encadenadas (if, else, elif) con más de dos comparaciones y el comparador encadenado propio de Python (por ejemplo, 0 <= x <= 100)

#Ejecicio 1. Clasificaci]on por edad
print ("---------- Ejecicio 1 ----------")
edad = int(input ("Ingresa tu edad: "))
if edad < 13:
    print("Clasificación: Niño")
elif edad <= 17:
    print ("Clasificación: Adolescente")
else:
    print ("Clasificación Adulto")

#Ejercicio 2. Validar acceso (usuario y contraseña)
print ("---------- Ejercicio 2 ----------")
USUARIO_CORRECTO = "Kinger"
PASSWORD_CORRECTO = "xxddcc"

usuario = input("Usuario: ")
password = input ("Contraseña: ")

if usuario != USUARIO_CORRECTO:
    print("Usuario no encontrado")
elif password != PASSWORD_CORRECTO:
    print("Password incorrecta")
else:
    print ("Acceso concedido")

#Ejercicio 3. Calculadora de envío
print ("---------- Ejercicio 3 ----------")
peso = float(input("Ingresa el peso del paquete en kg: "))
if peso <= 1:
    costo = 50.0
elif peso <= 5:
    costo = 90.0
else:
    costo = 150.0

    if peso > 10:
        costo *= 0.90
print (f"El costo final de envío es: ${costo:.2f}")

#Ejercicio 4. Clasificar la temperatura
print ("---------- Ejercicio 4 ----------")
temperatura = float(input("Ingresa la temperatura en grados: "))
if temperatura < 10:
    print ("Clasificación: Frío")
elif temperatura <= 24:
    print ("Clasificación: Templado")
else:
    print ("Clasificación: Calor")

#Ejercicio 5. Clasificación con letras
print ("---------- Ejercicio 5 ----------")
calificacion = float(input("Ingresa tu calificación: "))
if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print (f"Tu calidicación es: {letra}")

#Ejercicio 6. Descuento por monto de compra
print ("---------- Ejercicio 6 ----------")
monto = float (input("Ingresa el monto de la compra: "))
if monto > 500:
    descuento_porcentaje = 20
elif monto > 200:
    descuento_porcentaje = 10
else:
    descuento_porcentaje = 0
descuento = monto * (descuento_porcentaje / 100)
monto_final = monto - descuento

print(f"Porecentaje de descuento: {descuento_porcentaje}%")
print(f"Monto final a pagar: ${monto_final:.2f}")

#Ejercicio 7. Validad un rango con comparación encadenada
print ("---------- Ejercicio 7 ----------")
numero = float(input("Ingresa un número: "))
if 1 <= numero <= 100:
    print("El numero está en el rango [1, 100].")
else:
    print("El número no está en el rango [1, 100].")

#Ejercicio 8. Clasificar el IMC
print ("---------- Ejercicio 8 ----------")
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2)

if imc < 18.5:
    categoria = "bajo peso"
elif imc <= 24.9:
    categoria = "normal"
elif imc <= 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"

print (f"Tu IMC es {imc:.2f}: {categoria}")

#Ejercicio 9. Tarifas de electricidad
print ("---------- Ejercicio 9 ----------")
consumo = float(input("Ingresa tu consumo mensual en kWh: "))
if consumo <= 150:
    costo_total = consumo * 1.20
elif consumo <= 300:
    costo_total = (150 * 1.20) + ((consumo - 150) * 1.80)
else:
    costo_total = (150 * 1.20) + (150 * 1.80) + ((consumo -300) * 2.50)
print(f"Consumo: {consumo} kWh")
print (f"Costo total: ${costo_total:.1f}")