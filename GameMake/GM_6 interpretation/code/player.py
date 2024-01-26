# image : https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=2531s

import pygame
from support import import_folder       # spport라는 파일에서 import_folder 함수를 사용하겠다.

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, create_jump_particles):        # Player class를 사용하려면 pos, surface, create_jump_particels 정보가 있어야 한다.
        super().__init__()                                          # pygame.sprite.Sprite의 정보를 사용하기 위해 필요
        self.import_character_assets()                              # import_character_assets()함수 선언
        self.frame_index = 0                                        # frame_index 변수를 사용하기 전 0으로 초기화
        self.animation_speed = 0.15                                 # animation_speed를 0.15로 설정
        self.image = self.animations['idle'][self.frame_index]      # self.animations : import_character_assets()에서 선언한 변수[str][dir]
        self.rect = self.image.get_rect(topleft = pos)              # 이미지의 사각형 영역 반환, 이미지의 topleft를 기준으로 pos잡음.
        # get_rect : 이미지의 크기를 가진 직사각형 객체를 가져온다.

        # dust particles
        self.import_dust_run_particles()                            # import_dust_run_particles()함수 선언
        self.dust_frame_index = 0                                   # dust_frame_index 번수를 사용하기 전 0으로 초기화
        self.dust_animation_speed = 0.15                            # dust_animation_speed를 0.15로 설정
        self.display_surface = surface                              # display_surface을 Player에서 필요한 정보인 surface로 설정
        self.create_jump_particles = create_jump_particles          # create_jump_particles을 Player에서 필요한 정보인 create_jump_particles로 설정

        # player movement
        self.direction = pygame.math.Vector2(0,0)                   # Vector2 : 물체를 이동시키는데 도움이 되는 class
        self.speed = 8                                              # speed라는 변수를 8로 지정
        self.gravity = 0.8                                          # gravity라는 변수를 0.8로 지정
        self.jump_speed = -16                                       # jump_speed라는 변수를 -16으로 지정 (밑으로 내려갈수록 더 높은 수이기 때문에 점프를 하면 y값이 줄어든다.)

        # player status
        self.status = 'idle'                                        # status를 'idle'로 지정
        self.facing_right = True                                    # 게임 시작 시 캐릭터가 오른쪽을 보게 끔 하기 위해 True로 설정
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_character_assets(self):
        character_path = 'C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\'
        # character_path = '../graphics/character/'
        # character까지의 주소를 가져옴
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}  # animations에 사진 폴더와 같은 이름의 dir를 만들어줌.

        for animation in self.animations.keys():                    # import_character_assets에서 선언한 animations에 있는 정보들을 animation으로 저장.
            full_path = character_path + animation                  # character 주소 + animation 정보 ('idle', 'run', 'jump', 'fall')
            self.animations[animation] = import_folder(full_path)   # animations[animation]에 위 주소의 사진을 불러옴.

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\dust_particles\\run')
        # dust_particles 안에 있는 run의 사진 파일을 불러옴.

    def animate(self):
        animation = self.animations[self.status]    # animation에 self.status('idle')의 사진을 불러옴.
                                                    # 가만히 있을 때는 idle 사진이 animation되게 함.

        # loop over frame index
        self.frame_index += self.animation_speed    # frame_index에 animation_speed를 더해줌
        if self.frame_index >= len(animation):      # frame_index가 animation으로 지정된 사진의 수보다 크거나 작으면
            self.frame_index = 0                    # frame_index는 0으로 돌아간다.

        image = animation[int(self.frame_index)]    # image는 animation(dir)로 설정 -> dir안에 frame_index를 int형 변환후 넣어줌.
        if self.facing_right:       # facing_right가 True 일 때 (캐릭터가 오른쪽을 볼 때)
            self.image = image
        else:                       # 캐릭터가 왼쪽을 볼 때
            flipped_image = pygame.transform.flip(image, True, False)   # image를 x축 기준으로 뒤집음.
            self.image = flipped_image

        #  set the rect
        if self.on_ground and self.on_right:                                        # on_ground와 on_right가 True일 때
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)    # 이미지의 사각형 영역 반환, 이미지의 bottomright를 rect.bottomright로 설정
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        # get_rect : 이미지의 크기를 가진 직사각형 객체를 가져온다.

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:     # status가 run이라면
            self.dust_frame_index += self.dust_animation_speed  # dust_frame_index에 dust_animation_speed만큼 계속 증가시킴.
            if self.dust_frame_index >= len(self.dust_run_particles):   # dust_frame_index가 dust_run_particles의 사진 수 보다 크거나 같다면
                self.dust_frame_index = 0       # dust_frame_index를 다시 0으로 설정

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]     # dust_particle : dust_run_particles(dir)에 dust_frame_index를 int형으로 변환 후 dir에 넣음.

            if self.facing_right:           # facing_right가 True일 때 
                # 자연스러움을 위해 사진을 옮김.
                pos = self.rect.bottomleft - pygame.math.Vector2(6,10)      # pos는 rect의 bottomleft에서 왼쪽으로 6픽셀, 위로 10픽셀 이동한 정보.
                self.display_surface.blit(dust_particle, pos)       # surface에 dust_particle이라는 사진을 위치(대상)에 복사해 넣는다.
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6,10)     # pos는 rect의 bottomright에서 왼쪽으로 6픽셀, 위로 10픽셀 이동한 정보.
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)   # x축 기준으로 사진 뒤집기.
                self.display_surface.blit(flipped_dust_particle, pos)   # surface에 flipped_dust_particle이라는 사진을 위치(대상)에 복사해 넣는다.

    def get_input(self):
        keys = pygame.key.get_pressed()         # key가 눌러진 것을 인식

        if keys[pygame.K_RIGHT]:                # right key를 눌렀을 때
            self.direction.x = 1                # direction의 x값이 1 증가 (Vector2의 x값 증가)
            self.facing_right = True            # 캐릭터가 오른쪽을 보게 함.
        elif keys[pygame.K_LEFT]:               # left key를 눌렀을 때
            self.direction.x = -1               # direction의 x값이 1 감소 (Vector2의 x값 감소)
            self.facing_right = False           # 캐릭터가 오른쪽을 못 보게 함.
        else:                                   # right, left key 다 안 눌렀을 때
            self.direction.x = 0                # direction의 x값 변화 없음 (Vector2의 x값 변화 없음)

        if keys[pygame.K_SPACE] and self.on_ground:         # space key를 눌렀을 때
            self.jump()                                     # jump 함수를 실행
            self.create_jump_particles(self.rect.midbottom) # jump시 점프 이미지의 반환된 사각형의 중심을 midbottom으로 잡아줌.

    def get_status(self):
        if self.direction.y < 0:            # direction.y (Vector y값)이 0보다 작아지면 -> 점프를 한다면
            self.status = 'jump'                # status를 jump로 설정
        elif self.direction.y > 1:          # direction.y (Vector y값)이 1보다 커지면 -> 점프를 하고 내려오는 중이라면
            self.status = 'fall'                # status를 fall로 설정
        else:                               # 둘 다 아닐 때
            if self.direction.x != 0:           # direction.x (Vector x값)이 0이 아니라면 -> 움직이는 중이라면
                self.status = 'run'                 # status를 run으로 설정
            else:                               # x값의 변동이 없다면 -> 움직이지 않는다면
                self.status = 'idle'                # status를 idle로 설정

    def apply_gravity(self):
        self.direction.y += self.gravity        # direction의 y값이 gravity만큼 증가한다.
        self.rect.y += self.direction.y         # 반환된 사각형의 y값에 위에서 증가하는 direction.y값을 증가시켜줌.


    def jump(self):
        self.direction.y = self.jump_speed      # direction의 y값은 jump_speed이 된다. (Vector의 y값이 jump실행시 순간적으로 -16이 됨.)
        # 캐릭터가 점프함.

    def update(self):                           # 위에 만든 함수들 update(실행)
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()