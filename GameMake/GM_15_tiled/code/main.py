import pygame, sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
tmx_data = load_pygame('GameMake/GM_15_tiled/data/tmx/basic.tmx')

# # get layers
# print(tmx_data.layers)  # get all layers
# for layer in tmx_data.visible_layers:   # get visible layers
#     print(layer)


# print(tmx_data.layernames)  # get all layer names as dict

# print(tmx_data.get_layer_by_name('Floor'))  # get on layer by name

# for obj in tmx_data.objectgroups:   # get object layers
#     print(obj)

# get tiles
layer = tmx_data.get_layer_by_name('Floor')
print(layer.tiles())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    pygame.display.update()