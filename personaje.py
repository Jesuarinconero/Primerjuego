import pygame


import constantes


class Personaje():
    #Cuando creamos un personaje le pasamos las coordenadas x y le damos un tamaño


    def __init__(self,x,y , animaciones):
        #VOlteo del persoanje varialbke
        self.flip = False
        #Animaciones lista
        self.animaciones = animaciones
        self.frame_index = 0
        #Guardar el tiempo
        self.guardareltiempo = pygame.time.get_ticks()
        #IMagen del personaje
        self.image = animaciones[self.frame_index]
        self.forma= self.image.get_rect()
        self.forma.center = (x,y)

    def actualizaranimaciones(self):
        tiempodeanimacion = 1000
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.guardareltiempo >= tiempodeanimacion:
            self.frame_index = self.frame_index + 1
            self.guardareltiempo = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0


    def dibujarpersonaje(self,interfaz):
        #Me guarda en esta variable para invertir la imagen es decir el personaje
        image_flip = pygame.transform.flip(self.image,self.flip,False)
        interfaz.blit(image_flip,self.forma)
        #Dibujamos el personaje en la interfaz
        pygame.draw.rect(interfaz,constantes.ColorPersonaje , self.forma, 1)

    #Funcion del movimiento
    def movimiento(self, delta_x,delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y +delta_y
