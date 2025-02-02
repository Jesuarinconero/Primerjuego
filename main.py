from operator import truediv

import pygame
import constantes
from constantes import escala_del_personaje
from personaje import Personaje
from weapon import Armas

#Inicializamos pygame
pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO , constantes.ALTO))
#Nombre de ventana
pygame.display.set_caption("El juegito jiji")
def escalarimagen(image, escala):
    w = image.get_width()
    h = image.get_height()
    nuevaimagen = pygame.transform.scale(image, (w * escala, h * escala))
    return nuevaimagen
#Importamos las imagenes del personaje
animaciones = []
for i in range(5):
    imagenepersonaje = pygame.image.load(f"asset/imagen/personajes/jugador/jugador{i}.png")
    imagenepersonaje = escalarimagen(imagenepersonaje, constantes.escala_del_personaje)  # Corrected function call

    animaciones.append(imagenepersonaje)

#Armas
imagen_pistola = pygame.image.load(f"asset/imagen/armas/img.png")
imagen_pistola  = escalarimagen(imagen_pistola, constantes.escala_del_arma)
imagenbalas = pygame.image.load("asset/imagen/armas/balas.png")

#Crear un jugador de la clase jugaro
jugador = Personaje(50,50, animaciones)
#Creamos un arma de la clase arma
arco = Armas (imagen_pistola)




#Definir las variables del movimiento del jugador para saber si se mueve
mover_arriba  = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False
# Controlar el frame rate es decir el tiempo en el que se mueve el jugador
reloj = pygame.time.Clock()
run = True
#Mientra la ventana este corriendo vamos a recorrer los eventos
while run:

    #movimiento 60 fps
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.Colordefondo)
    #Dibujamos el personaje en la interfaz
    jugador.dibujarpersonaje(ventana)

    #Calcular el moviemiento del jugador
    delta_x = 0
    delta_y = 0


    if mover_derecha == True:
        delta_x = constantes.velocidad_personaje
    if mover_izquierda == True:
        delta_x = -constantes.velocidad_personaje
    if mover_arriba == True:
        delta_y = -constantes.velocidad_personaje
    if mover_abajo == True:
        delta_y = constantes.velocidad_personaje
    #Movimiento del jugador o mover jugador
    jugador.movimiento(delta_x,delta_y)
    jugador.actualizaranimaciones()

    #Actualizar arma
    arco.actualizarimagenarma(jugador)
    #Dibujamos el marma
    arco.dibujar(ventana)
    #entrega la lista de todo los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #Evento de reconocumiento de tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               mover_izquierda=True
            if event.key == pygame.K_s:
                 mover_abajo=True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
    #Actualiza la pantalla
    pygame.display.update()
pygame.quit()
