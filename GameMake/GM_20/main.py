from matplotlib.pyplot import text
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
Colck = pygame.time.Clock()
test_font = pygame.font.Font('GameMake/GM_20/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('GameMake/GM_20/graphics/Sky.png')
ground_surface = pygame.image.load('GameMake/GM_20/graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (350, 50))

    pygame.display.update()
    Colck.tick(60)