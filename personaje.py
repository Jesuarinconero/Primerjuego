import pygame

import constantes

class Personaje():
    #Cuando creamos un personaje le pasamos las coordenadas x y le damos un tamaño
    def __init__(self,x,y):

        self.forma= pygame.Rect(0,0,constantes.Alto_personaje,constantes.Ancho_personaje)
        self.forma.center = (x,y)



    def dibujarpersonaje(self,interfaz):
        #Dibujamos el personaje en la interfaz
        pygame.draw.rect(interfaz,constantes.ColorPersonaje , self.forma)

    #Funcion del movimiento
    def movimiento(self, delta_x,delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y +delta_y