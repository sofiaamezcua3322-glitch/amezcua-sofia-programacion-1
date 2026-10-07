#Ejercicio 1 ¿Es par o impar?
print("--- Ejercicio 1 ---")
numero = 14
es_par = numero % 2 == 0
if es_par:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

numero = 7
es_par = numero % 2 == 0
if es_par:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")

#Ejercicio 2 Concatenar vs sumar
print("\n--- Ejercicio 2 ---")
numero1 = "10"
numero2 = "20"
print("Concatenación:", numero1 + numero2)
print("Suma:", int(numero1) + int(numero2))

numero1 = "32"
numero2 = "85"
print("Concatenación:", numero1 + numero2)
print("Suma:", int(numero1) + int(numero2))

# Explicación: 
# Cuando usamos el operador '+' con datos tipo str (texto), Python "concatena" Es decir, une los caracteres ("10" y "20" forman "1020"). Cuando los convertimos a int (entero), Python entiende que son valores numéricos y realiza la suma (10 + 20 = 30).

#Ejercicio 3 Mini reporte de un perfil
print("\n--- Ejercicio 3 ---")
nombre = "Bonnie"
edad = 20
estatura = 1.71
es_estudiante = True
print("Nombre:", nombre, "| Tipo:", type(nombre))
print("Edad:", edad, "| Tipo:", type(edad))
print("Estatura:", estatura, "| Tipo:", type(estatura))
print("¿Es estudiante?:", es_estudiante, "| Tipo:", type(es_estudiante))
# Extra: Quinta variable combinando datos
mensaje_perfil = nombre + " ¿es estudiante? " + str(es_estudiante) + " y tiene " + str(edad) + " años."
print("Mensaje combinado:", mensaje_perfil)
print("\n- Segunda entrada ")
nombre = "Bon"
edad = 20
estatura = 1.72
es_estudiante = False
print("Nombre:", nombre, "| Tipo:", type(nombre))
print("Edad:", edad, "| Tipo:", type(edad))
print("Estatura:", estatura, "| Tipo:", type(estatura))
print("¿Es estudiante?:", es_estudiante, "| Tipo:", type(es_estudiante))
# Extra: Quinta variable combinando datos
mensaje_perfil = nombre + " ¿es estudiante? " + str(es_estudiante) + " y tiene " + str(edad) + " años."
print("Mensaje combinado:", mensaje_perfil)

#Ejercicio 4 Operadores aritmeticos basicos
print("\n--- Ejercicio 4 ---")
a = 36
b = 6
print("a =", a)
print("b =", b)
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

#Ejercicio 5 División entera y módulo
print("\n--- Ejercicio 5 ---")
a = 36
b = 6
print("a =", a)
print("b =", b)
print("División entera:", a // b)
print("Módulo o residuo:", a % b)
# Usando variables para una división no exacta
print("\n- División no exacta")
x = 17
y = 5
print("x =", x)
print("y =", y)
print("División entera:", x // y)
print("Módulo o residuo:", x % y)
# Explicación:
# El operador '/' realiza una división normal y devuelve un número decimal (float), por ejemplo 17 / 5 = 3.4. El operador '//' realiza una división entera, eliminando los decimales (devuelve 3).

#Ejercicio 6 Operadores relacionales
print("\n--- Ejercicio 6 ---")
numero1 = 10
numero2 = 25
mayor = numero1 > numero2
menor = numero1 < numero2
igual = numero1 == numero2
diferente = numero1 != numero2
print("¿", numero1, "es mayor que", numero2, "?", mayor)
print("¿", numero1, "es menor que", numero2, "?", menor)
print("¿", numero1, "es igual que", numero2, "?", igual)
print("¿", numero1, "es diferente de", numero2, "?", diferente)

# Prueba 2: Números iguales
print("\n- Segunda entrada ")
numero1 = 8
numero2 = 8
mayor_que = numero1 > numero2
menor_que = numero1 < numero2
igual_a = numero1 == numero2
diferente_de = numero1 != numero2
print ("¿", numero1, "es mayor que", numero2, "?", mayor_que)
print ("¿", numero1, "es menor que", numero2, "?", menor_que)
print ("¿", numero1, "es igual que", numero2, "?", igual_a)
print ("¿", numero1, "es diferente de", numero2, "?", diferente_de)

#Ejercicio 7 Operadores lógicos
print("\n--- Ejercicio 7 ---")
expresion1 = (10 > 5)
expresion2 = (3 == 4)   

resultado_and = expresion1 and expresion2
resultado_or = expresion1 or expresion2
resultado_not = not expresion1

print("Expresión 1 (10 > 5):", expresion1)
print("Expresión 2 (3 == 4):", expresion2)
print("Combinación con AND:", resultado_and)
print("Combinación con OR:", resultado_or)
print("Combinación con NOT (invirtiendo exp1):", resultado_not)


#Ejercicio 8 Promedio y aprobación
print("\n--- Ejercicio 8 ---")
# Prueba 1: Aprobado
calif1, calif2, calif3 = 8, 7, 9
promedio = (calif1 + calif2 + calif3) / 3
aprobado = promedio >= 6
print(f"Calificaciones: {calif1}, {calif2}, {calif3} | Promedio: {promedio} | Aprobado: {aprobado}")

# Prueba 2: Reprobado
calif1, calif2, calif3 = 5, 4, 6
promedio = (calif1 + calif2 + calif3) / 3
aprobado = promedio >= 6
print(f"Calificaciones: {calif1}, {calif2}, {calif3} | Promedio: {promedio} | Aprobado: {aprobado}")

#Ejercicio 9 Validación de elegibilidad
print("\n--- Ejercicio 9 ---")
# Caso 1: Elegible (Mayor de 17 y mexicana)
edad = 20
nacionalidad = "mexicana"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
es_elegible_or = (edad > 17) or (nacionalidad == "mexicana") # Extra
print(f"Caso 1 (Edad: {edad}, Nac: {nacionalidad}) -> Elegible (AND): {es_elegible} | Elegible (OR): {es_elegible_or}")

# Caso 2: No elegible por edad (Menor de 18 pero mexicana)
edad = 16
nacionalidad = "mexicana"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
es_elegible_or = (edad > 17) or (nacionalidad == "mexicana") # Extra
print(f"Caso 2 (Edad: {edad}, Nac: {nacionalidad}) -> Elegible (AND): {es_elegible} | Elegible (OR): {es_elegible_or}")

# Caso 3: No elegible por nacionalidad (Mayor de 17 pero otra nacionalidad)
edad = 25
nacionalidad = "canadiense"
es_elegible = (edad > 17) and (nacionalidad == "mexicana")
es_elegible_or = (edad > 17) or (nacionalidad == "mexicana") # Extra
print(f"Caso 3 (Edad: {edad}, Nac: {nacionalidad}) -> Elegible (AND): {es_elegible} | Elegible (OR): {es_elegible_or}")

# Explicación del Extra:
# Con 'and', AMBAS condiciones tienen que ser verdaderas para que el resultado sea True (tiene que ser mayor de edad Y mexicano a la vez).
# Con 'or', basta con que UNA sola de las condiciones se cumpla para dar True. Por ejemplo, en el Caso 3, es_elegible (and) dio False porque no es mexicano, pero es_elegible_or dio True simplemente porque sí tiene más de 17 años.