import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
Colck = pygame.time.Clock()
test_font = pygame.font.Font('GameMake/GM_20/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('GameMake/GM_20/graphics/Sky.png').convert()
ground_surface = pygame.image.load('GameMake/GM_20/graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black')

snail_surf = pygame.image.load('GameMake/GM_20/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('GameMake/GM_20/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("MOUSE DOWN")
        if event.type == pygame.MOUSEBUTTONUP:
            print("MOUSE UP")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (350, 50))
    snail_rect.x -= 3
    # if snail_x_pos < 0:
    #     snail_x_pos = 600
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    Colck.tick(60)