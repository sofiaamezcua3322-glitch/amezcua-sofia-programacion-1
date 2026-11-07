#While
print ("-- While --")
while True:
    print ("Se ejecuta al menos una vez")
    user_input = input("¿Continuar? (y/n): ")
    if user_input.lower()!= 'y': #upper()
        break

#Contadores y acumuladores
print ("-- Contador --")
contador = 0
for _ in range(5):
    contador = contador + 1
    print(contador)

#Acumulador
print ("-- Acumulador --")
print (" --- 1 ---")
precios = [50, 120, 30]
total = 0
for precio in precios:
    total = total + precio
    print (total)

print ("--- 2 ---")
precios = [30, 10, 9, 50, 29, 10]
total = 0
for precio in precios:
    print (precio)

#Matriz
print ("-- Matriz --")
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print (matriz [0][0]) 

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print (matriz [0][1]) # fila 0, columna 1

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print (matriz [0][2]) # fila 0, columna 2

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print (matriz [1][2]) # fila 1, columna 2

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print (matriz [1][1]) # fila 1, columna 1

#Matirz extras
martiz = [
    [15, 8],
    [20, 30]
]

martiz = [
    ["S", "O", "R", "P"],
    ["R", "E", "S"]
]


#inserción - Append() y insert()
print ("--- Inserción ---")
frutas = ["manzana", "pera"]
frutas.append("uva")           # agrega al final
frutas.insert(1, "kiwi")       # agrega en la posición 1
print (frutas)

#frutas.append("cereza")
#frutas.append(input("ingresa fruta: "))
#Nota: append() agerga hasta el final de la lista, insert() agrega en la posición que quieras obviamente poniendo el numero xd

#Eliminación - Remove() y Pop() y DEL
print ("--- Eliminación ---")
frutas.remove("pera")         #  elimina por valor
frutas.pop(0)                 #  elemina por índice
del          frutas[0]        #  elimina por índice
print (frutas)

#In e Index()
print ("--- In e Index ---")
frutas = ["manzana", "pera", "uva"]
print ("pera" in frutas)      # True
print (frutas.index("uva"))   # 2