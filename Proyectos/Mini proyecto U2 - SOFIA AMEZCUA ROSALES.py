#Alumno: Sofia Amezcua Rosales
#Descripción: Programa de consola que registra productros de una compra, valida los datos ingresados, calcula subtotales, IVA (16%) y total, y finalmente imprime un recibo formateado en consola.

# Mensaje de Bienvenida, nombre de los productos y precio
print("\n========================================")
print("¡Bienvenido a la tienda digital de Caine!")
print("========================================")
print("Catalogo de productos:")
print("1. Peluche de Caine - $258.00")
print("2. Peluche de Pomni - $258.00")
print("3. Peluche de Jax - $258.00")
print("4. Llavero de Ragatha - $143.00")
print("5. Llavero de Gangle - $143.00")
print("6. Llavero de Zooble - $143.00")
print("7. Pin de Bubble - $115.00")
print("8. Paquete de Stickers - $96.00")
print("9. Ribbit Hoodle - $572.00")
print("10. Libro de Arte - $1199.00")
print("========================================\n")

# 1. Captura y validación de la cantidad de productos
cantidad_productos = 0
cantidad_valida = False

while cantidad_valida == False:
    cantidad_productos_str = input("¿Cuántos productos diferentes desea comprar? ")
    if cantidad_productos_str.isdigit():
        if int(cantidad_productos_str) > 0:
            cantidad_productos = int(cantidad_productos_str)
            cantidad_valida = True
        else:
            print("Error: Por favor, ingresa un número entero válido mayor a 0.\n")
    else:
        print("Error: Por favor, ingresa un número entero válido mayor a 0.\n")

# Captura para juntar los datos de cada producto
nombres_carrito = []
precios_carrito = []
cantidades_carrito = []
subtotales_carrito = []

subtotal_general = 0.0

#2. Registro de datos por producto
for i in range(cantidad_productos):
    print("\n--- Registrando Producto " + str(i + 1) + " ---")

    producto_valido = False
    
    while producto_valido == False:
        id_producto = input("Ingresa el número del producto (1-10):")
        
        nombre_producto = ""
        precio_producto = 0.0
        
        if id_producto == "1":
            nombre_producto = "Peluche de Caine"
            precio_producto = 258.00
            producto_valido = True
        elif id_producto == "2":
            nombre_producto = "Peluche de Pomni"
            precio_producto = 258.00
            producto_valido = True
        elif id_producto == "3":
            nombre_producto = "Peluche de Jax"
            precio_producto = 258.00
            producto_valido = True
        elif id_producto == "4":
            nombre_producto = "Llavero de Ragatha"
            precio_producto = 143.00
            producto_valido = True
        elif id_producto == "5":
            nombre_producto = "Llavero de Gangle"
            precio_producto = 143.00
            producto_valido = True
        elif id_producto == "6":
            nombre_producto = "Llavero de Zooble"
            precio_producto = 143.00
            producto_valido = True
        elif id_producto == "7":
            nombre_producto = "Pin de Bubble"
            precio_producto = 115.00
            producto_valido = True
        elif id_producto == "8":
            nombre_producto = "Paquete de Stickers"
            precio_producto = 96.00
            producto_valido = True
        elif id_producto == "9":
            nombre_producto = "Ribbit Hoodle"
            precio_producto = 572.00
            producto_valido = True
        elif id_producto == "10":
            nombre_producto = "Libro de Arte"
            precio_producto = 1199.00
            producto_valido = True
        else:
            print("Error: Opción no válida. Por favor, ingresa un número del 1 al 10.")
            
        if producto_valido == True:
            print("Seleccionaste: " + nombre_producto + " ($" + str(precio_producto) + ")")

#Ya estoy hasta la madre maestra, esto no esta funcionandoooo
#No se como hacerle para no tener que poner de uno en uno    
    
    # Validación de la cantidad
    cantidad_valida2 = False
    while cantidad_valida2 == False:
        cantidad_str = input("¿Cuantas unidades de '" + nombre_producto + "' deseas llevar?")
        if cantidad_str.isdigit():
            if int(cantidad_str) > 0:
                cantidad_producto = int(cantidad_str)
                cantidad_valida2 = True
            else:
                print("Error: Por favor, ingresa una cantidad entera válida mayor a 0.")
        else:
            print("Error: Por favor, ingresa una cantidad entera válida mayor a 0.")

    #3. Cálculos por producto por cada producto
    subtotal_producto = precio_producto * cantidad_producto
    subtotal_general = subtotal_general + subtotal_producto

    # Guardado en listas separadas
    nombres_carrito.append(nombre_producto)
    precios_carrito.append(precio_producto)
    cantidades_carrito.append(cantidad_producto)
    subtotales_carrito.append(subtotal_producto)

#Como chuchas se ponia el iva 
# 4. Cálculos generales (IVA y total)
tasa_iva = 0.16
monto_iva = subtotal_general * tasa_iva
total_pagar = subtotal_general + monto_iva 

# 5. Impresión del recibo final
print("\n=======================================================")
print("                    TICKET DE COMPRA                   ")
print("=======================================================")

print("CANT  | PRODUCTO               | PRECIO   | SUBTOTAL")
print("-------------------------------------------------------")

for x in range(len(nombres_carrito)):
    print(str(cantidades_carrito[x]) + "     | " + nombres_carrito[x] + " | $" + str(precios_carrito[x]) + " | $" + str(subtotales_carrito[x]))

print("-------------------------------------------------------")

# Centrando de los espacios y usando round() para los decimales
print("                                   Subtotal: $" + str(round(subtotal_general, 2)))
print("                                   IVA (16%): $" + str(round(monto_iva, 2)))
print("                                   TOTAL A PAGAR: $" + str(round(total_pagar, 2)))
print("=======================================================")
print("        ¡Gracias por visitar la tienda de Caine!       ")
print("=======================================================\n")

#FUNCIONAAA SI FUNCIOONAAAA :D
#LLEVO TODO EL PERRO DIA AQUI AAAAAAAAAAAAAAAAAAAAH