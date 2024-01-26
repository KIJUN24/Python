# image : https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=2531s

import pygame
from support import import_folder
from math import sin

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, create_jump_particles, change_health):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.collision_rect = pygame.Rect(self.rect.topleft, (50, self.rect.height))

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # health management
        self.change_health = change_health
        self.invincible = False
        self.invincibility_duration = 500
        self.hurt_time = 0

        # audio
        self.jump_sound = pygame.mixer.Sound('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_10___6,9_finish\\audio\\effects\\jump.wav')
        self.jump_sound.set_volume(0.3)
        self.hit_sound = pygame.mixer.Sound('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_10___6,9_finish\\audio\\effects\\hit.wav')

    def import_character_assets(self):
        character_path = 'C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\character\\'
        # character 경로를 character_path에 저장
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}  
        # '~'리스트를 만듦.

        for animation in self.animations.keys():    # Key들만 모아서 animation에 저장(idle, run, jump, fall)
            full_path = character_path + animation  # full_path는 위에서 선언한 character_path 경로와 animation을 합친 것임.
            self.animations[animation] = import_folder(full_path)   # full_path의 정보들을 가져와 animations[animation]에 저장

    def import_dust_run_particles(self):    # dust_particles 안에 run 폴더를 가져옴.
        self.dust_run_particles = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\character\\dust_particles\\run')

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:   # facing_right가 True라면
            self.image = image
            self.rect.bottomleft = self.collision_rect.bottomleft   # rect의 bottomleft를 collision_rect의 bottomleft값으로 저장
        else:   # 아니라면
            flipped_image = pygame.transform.flip(image, True, False)   # image를 x축 기준으로 반전시키고 flipped_image에 저장해라
            self.image = flipped_image  # self.image에 flipped_image정보 값 저장
            self.rect.bottomright = self.collision_rect.bottomright     # rect의 bottomright를 collision_rect의 bottomright값으로 저장

        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6,10)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6,10)
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)
                self.display_surface.blit(flipped_dust_particle, pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
            self.create_jump_particles(self.rect.midbottom)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):    # player가 점프한 후 중력작용하는 효과를 주는 함수
        self.direction.y += self.gravity    # direction.y값에 gravity값을 증가시켜줌.
        self.collision_rect.y += self.direction.y   # collision_recr.y 값에 direction.y값을 증가시켜줌.

    def jump(self):     # jump할 때 사용하는 함수
        self.direction.y = self.jump_speed  # direction.y값에 jump_speed값을 증가시켜줌.
        self.jump_sound.play()  # Sound

    def get_damage(self):
        if not self.invincible:         # invincible이 False라면
            self.hit_sound.play()       # Sound
            self.change_health(-10)     # change_health(-10) : 10만큼 줄어듦.
            self.invincible = True      # invincible이 True로 바꿔줌
            self.hurt_time = pygame.time.get_ticks()    # 약간의 delay를 줌.
    
    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()
        self.invincibility_timer()
        self.wave_value()