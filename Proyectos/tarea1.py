velocidad_y = 0
altura_del_suelo = -67
x = -163
y = altura_del_suelo
disfraz = "Pomni 2 run"
fondo = "circo"
visible = False
def recibir_aparecer():
    global velocidad_y, altura_del_suelo, x, y, fondo, disfraz, visible

    fondo = "circo"
    visible = True
    disfraz = "Pomni 2 run"
    velocidad_y = 0
    altura_del_suelo = -67

    x = -163
    y = altura_del_suelo

    while not tecla_espacio_presionada ():
        esperar_tick()

    while True:
        if tecla_espacio_presionada() and y == altura_del_suelo:
            velocidad_y = 20
            disfraz = "Pomni run 1"

        if (y + velocidad_y) < altura_del_suelo:
            y = altura_del_suelo
            disfraz = "Pomni run 2"

        else:
            y += velocidad_y
            velocidad_y -= 1

        actualizar_pantalla()

def tecla_espacio_presionada():
    pass

def esperar_tick():
    pass

def actualizar_pantalla():
    pass