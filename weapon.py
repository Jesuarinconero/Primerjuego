import pygame
import constantes
import personaje
import math


class Armas:
    def __init__(self, image):
        self.imagenoriginal = image  # Imagen original sin modificar
        self.angulo = 0
        self.imagenactual = self.imagenoriginal  # Imagen que se usará para dibujar
        self.forma = self.imagenactual.get_rect()

    def actualizarimagenarma(self, jugador):
        self.forma.center = jugador.forma.center

        if jugador.flip:
            self.forma.x -= jugador.forma.width / 2
            self.rotararma(True)  # Rotar cuando el personaje esté volteado
        else:
            self.forma.x += jugador.forma.width / 2
            self.rotararma(False)
            # MOver pistola con mouse
        mouse_position = pygame.mouse.get_pos()
        diferenica_x = mouse_position[0] - self.forma.centerx
        diferenica_y = -(mouse_position[1] - self.forma.centery)
        #Calculamos el mouse
        self.angulo = math.degrees(math.atan2(diferenica_y,diferenica_x))


    def dibujar(self, interfaz):
        self.imagenactual = pygame.transform.rotate(self.imagenactual,self.angulo)
        interfaz.blit(self.imagenactual, self.forma)
        pygame.draw.rect(interfaz, constantes.colorarma, self.forma, 1)

    def rotararma(self, voltear):
        """ Rota y refleja el arma según la dirección del personaje. """
        if voltear:
            imagen_flip = pygame.transform.flip(self.imagenoriginal, True, False)
        else:
            imagen_flip = self.imagenoriginal  # No voltear si no es necesario

        # Rotar el arma
        self.imagenactual = pygame.transform.rotate(imagen_flip, self.angulo)

        # Actualizar la forma después de rotar
        self.forma = self.imagenactual.get_rect(center=self.forma.center)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        
