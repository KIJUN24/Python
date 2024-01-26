# image : https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=2531s


from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '\\' + image
            # full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list






#     for information in walk(path):
#         print(information)

# import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\run')
