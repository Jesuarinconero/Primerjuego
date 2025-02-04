import pygame
import constantes
from personaje import Personaje
from weapon import Armas
import os
# Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("El jueguito jiji")

def escalarimagen(image, escala):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * escala, h * escala))


#Funcion contar elementos
def contrar_elementos(directorio):

    return len(os.listdir(directorio))
#FUncion listar nombre de elementos
def nombre_carpetas(directorio):
    return os.listdir(directorio)
# Cargar imágenes del personaje
animaciones = []
for i in range(5):
    imagen_personaje = pygame.image.load(f"asset/imagen/personajes/jugador/jugador{i}.png")
    imagen_personaje = escalarimagen(imagen_personaje, constantes.escala_del_personaje)
    animaciones.append(imagen_personaje)
#enemigos
directorio_enemigos = f"asset/imagen/personajes/enemigos"
tipo_enemigos = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []
for enemi in tipo_enemigos:
    list_temp=[]
    ruta_temp = f"asset/imagen/personajes/enemigos/{enemi}"
    num_animaciones  = contrar_elementos(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{enemi}_{i+1}.png").convert_alpha()
        img_enemigo = escalarimagen(img_enemigo,constantes.escalaenemigos)
        list_temp.append(img_enemigo)
    animaciones_enemigos.append(list_temp)

# Cargar imágenes del arma y la bala
imagen_pistola = pygame.image.load(f"/home/jesus/PycharmProjects/Proyectopygameprimerjuego/asset/imagen/armas/img.png")
imagen_pistola = escalarimagen(imagen_pistola, constantes.escala_del_arma)


imagen_bala = pygame.image.load(f"asset/imagen/armas/balas.png")
imagen_bala = escalarimagen(imagen_bala, constantes.escala_del_arma)

# Crear jugador y arma
jugador = Personaje(50, 50, animaciones , 100)
#Crear enemigos de la clase personaje
goblin = Personaje(400,400,animaciones_enemigos[0],100)
honguito = Personaje(200,200 ,animaciones_enemigos[1],100)
goblin_2 = Personaje(100,250 , animaciones_enemigos[0],100)

lista_enemigos = []
lista_enemigos.append(goblin)
lista_enemigos.append(goblin_2)
lista_enemigos.append(honguito)


pistola = Armas(imagen_pistola, imagen_bala)


# Variables de movimiento del jugador
mover_arriba = mover_abajo = mover_derecha = mover_izquierda = False

# Reloj para controlar el frame rate
reloj = pygame.time.Clock()
run = True



# Crear grupo de balas, fuera del ciclo principal
grupos_balas = pygame.sprite.Group()

while run:
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.Colordefondo)

    # Dibujar el personaje
    jugador.dibujarpersonaje(ventana)
    for enemi in lista_enemigos:
        enemi.dibujarpersonaje(ventana)

    # Movimiento del jugador
    delta_x = (mover_derecha - mover_izquierda) * constantes.velocidad_personaje
    delta_y = (mover_abajo - mover_arriba) * constantes.velocidad_personaje
    jugador.movimiento(delta_x, delta_y)
    jugador.actualizaranimaciones()
    #actualizar enemigos
    for enemi in lista_enemigos:
        enemi.actualizaranimaciones()


    # Actualizar arma y disparar
    bala = pistola.actualizarimagenarma(jugador)

    # Si la bala es disparada, agregarla al grupo
    if bala:
        grupos_balas.add(bala)
    # Actualizar las balas y dibujarlas
    for bala in grupos_balas:
        bala.actualizar(lista_enemigos)  # Asegúrate de mover la bala
    grupos_balas.draw(ventana)  # Dibuja las balas en la ventana

    # Actualizar las balas y dibujarlas
    grupos_balas.update()  # Actualiza las balas en el grupo
    grupos_balas.draw(ventana)  # Dibuja las balas en la ventana

    pistola.dibujar(ventana)

    # Manejar eventos del teclado y ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detectar teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: mover_izquierda = True
            if event.key == pygame.K_s: mover_abajo = True
            if event.key == pygame.K_d: mover_derecha = True
            if event.key == pygame.K_w: mover_arriba = True

        # Detectar teclas liberadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: mover_izquierda = False
            if event.key == pygame.K_s: mover_abajo = False
            if event.key == pygame.K_d: mover_derecha = False
            if event.key == pygame.K_w: mover_arriba = False

    # Actualizar la pantalla
    pygame.display.update()
pygame.quit()

