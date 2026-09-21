import time

Vidas = 0
visible = False

def recibir_aparecer():
    global Vidas, visible

    Vidas = 3
    visible = True

    while True:
        if tocando ("gloink cuadrado"):
            Vidas -= 1
            time.sleep (1)

        if tocando ("gloink cuadrado"):
            Vidas -= 1
            time.sleep (1)

        if tocando ("gloink estrella"):
            Vidas -= 1
            time.sleep (1)

        if tocando ("gloink luna"):
            Vidas -= 1
            time.sleep (1)

        if tocando ("gloink pino"):
            Vidas -= 1
            time.sleep (1)

        if tocando ("gloink triangulo"):
            Vidas -= 1
            time.sleep (1)

        if Vidas == 0:
            enviar_mensaje ("Pomni gloinks")
            visible = False
            detener_todo()
            break

        esperar_tick()

def tocando():
    return False

def enviar_mensaje():
    pass

def detener_todo():
    pass

def esperar_tick():
    pass