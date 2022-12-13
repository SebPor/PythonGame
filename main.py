import pygame
from sys import exit

def main():
    #Primero tenemos que inicializar Pygame
    pygame.init()
    #Aquí definimos la variables de configuración de nuestro ventana
    #Se ve que Python reconoce directamente las variables en mayúscula como constantes
    WIDTH = 600
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)
    speed = [1,1]

    #Creamos la ventana
    #Le tenemos que pasar un tuple con el alto y el ancho
    screen = pygame.display.set_mode(SIZE)

    #Cargamos una imagen
    ball = pygame.image.load("AlexBonck.png")
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
        
        ballrect = ballrect.move(speed)# También es valido ballrect.move(2,2)
        if ballrect.left < 0 or ballrect.right > WIDTH:
            speed[0] *= -1
        if ballrect.top < 0 or ballrect.bottom > HEIGHT:
            speed[1] *= -1 

        screen.fill("black")
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
