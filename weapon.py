import pygame
import constantes
import math
import time  # Usaremos time para medir el tiempo
import random



class Armas:
    def __init__(self, image, imagenbala):
        self.imagenoriginal = image  # Imagen original sin modificar
        self.angulo = 0
        self.imagenactual = self.imagenoriginal  # Imagen que se usará para dibujar
        self.imagenbala = imagenbala

        self.forma = self.imagenactual.get_rect()
        self.disparada = False  # Control para evitar disparos automáticos
        self.last_shot_time = 0  # Tiempo del último disparo
        self.cooldown = 0.5  # Tiempo de cooldown en segundos

    def actualizarimagenarma(self, jugador):
        """Actualiza la posición del arma y dispara si el jugador hace clic"""
        balas = None
        self.forma.center = jugador.forma.center

        if jugador.flip:
            self.forma.x -= jugador.forma.width / 2
            self.rotararma(True)
        else:
            self.forma.x += jugador.forma.width / 2
            self.rotararma(False)

        # Apuntar con el mouse
        mouse_position = pygame.mouse.get_pos()
        diferencia_x = mouse_position[0] - self.forma.centerx
        diferencia_y = -(mouse_position[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferencia_y, diferencia_x))

        # Obtener el tiempo actual
        current_time = time.time()

        # Disparar solo si el cooldown ha terminado y el jugador hace clic
        if pygame.mouse.get_pressed()[0] and current_time - self.last_shot_time >= self.cooldown:
            balas = Bullet(self.imagenbala, self.forma.centerx, self.forma.centery, self.angulo)
            self.last_shot_time = current_time  # Actualizar el tiempo del último disparo

        return balas  # Devuelve la bala disparada

    def dibujar(self, interfaz):
        """Dibuja el arma en la pantalla"""
        imagen_rotada = pygame.transform.rotate(self.imagenoriginal, self.angulo)
        nueva_forma = imagen_rotada.get_rect(center=self.forma.center)
        interfaz.blit(imagen_rotada, nueva_forma)

    def rotararma(self, voltear):
        """Rota y refleja el arma según la dirección del personaje"""
        if voltear:
            self.imagenactual = pygame.transform.flip(self.imagenoriginal, True, False)
        else:
            self.imagenactual = self.imagenoriginal


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagenoriginal = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagenoriginal, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 10  # Velocidad de la bala

    def actualizar(self , lista_enemigos):
        """Mueve la bala en la dirección en la que fue disparada"""
        # Movimiento de la bala basado en el ángulo
        self.rect.x += math.cos(math.radians(self.angulo)) * self.velocidad
        self.rect.y -= math.sin(math.radians(self.angulo)) * self.velocidad
        #Verificar si hay colision
        for enemigo in lista_enemigos:
            if enemigo.forma.colliderect(self.rect):
                daño= 15 + random.randint(-7,7)
                enemigo.energia - daño
                self.kill()
                break

    def dibujar(self, interfaz):
        """Dibuja la bala en la pantalla"""
        interfaz.blit(self.image, self.rect.topleft)
