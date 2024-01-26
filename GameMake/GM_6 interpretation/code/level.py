import pygame                                   # pygame을 위한 import.
from tiles import Tile                          # tiles 파일에서 Tile class를 가져옴.
from settings import tile_size, screen_width    # settings 파일에서 tile_size와 screen_width변수를 가져옴.
from player import Player                       # player 파일에서 Player class를 가져옴.
from particles import ParticleEffect            # particels 파일에서 ParticleEffect class를 가져옴.

class Level:
    def __init__(self, level_data, surface):                # class를 정의할 때 첫번째로 만드는 함수이다.
                                                            # 이 함수를 사용하려면 level_data와 surface를 넣어줘야 한다.
        # level setup
        self.display_surface = surface                      
        self.setup_level(level_data)                        # setup_level 함수 실행
        self.world_shift = 0                                # 변수를 사용하기 전 0으로 초기화
        self.current_x = 0                                  # 변수를 사용하기 전 0으로 초기화

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()      # dust_sprite라는 단일 스프라이트를 보유
        self.player_on_ground = False

#########################################################################################################

    def create_jump_particles(self, pos):                   # 함수를 사용하려면 pos의 정보가 있어야 함.
        if self.player.sprite.facing_right:                 # player파일의 sprite에서 facing_right가 True일 때
            pos -= pygame.math.Vector2(10, 5)               # pos는 Vector2(10, 5)만큼 빼준다.
        else:
            pos += pygame.math.Vector2(10, -5)              # pos는 Vector2(10, 5)만큼 더한다.
        jump_particle_sprite = ParticleEffect(pos, 'jump')  # jump_particle_sprite에 particles 파일의 class를 사용 (조건에 필요한 정보를 넣어줌(pos, 'jump'))
        self.dust_sprite.add(jump_particle_sprite)          # dust_sprite에 jump_particle_sprite를 추가시킴

    def get_player_on_ground(self):                         
        if self.player.sprite.on_ground:                    # player파일의 sprite에서 on_ground가 True일 때
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            # player_on_ground가 True가 아니고 player 파일의 on_ground가 True이며 dust_sprite가 그룹에 포함하지 않는다면
            # GroupSingle.sprite() : 이 그룹에 포함된 Sprite에 엑세스 하는 특수 속성
            # 그룹이 비어 있으면 None이 될 수 있음. Sprite를 GroupSingle 컨테이너에 추가하도록 속성을 할당할 수도 있음.
            if self.player.sprite.facing_right:         # player파일에 facing_right가 True일 때
                offset = pygame.math.Vector2(10, 15)    # offset은 Vector2(10, 15)이다.
            else:
                offset = pygame.math.Vector2(-10, 15)
                # Vector2 : 사진을 이동시키는 역할로 사용.
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            # 위치를 player파일의 rect.midbottom에서 offset만큼 빼줌.
            self.dust_sprite.add(fall_dust_particle)    # dust_sprite에 fall_dust_particle를 더함.

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()          # 객체(sprite)가 여러개인 경우 Group으로 사용
        self.player = pygame.sprite.GroupSingle()   # 단일 sprite만 존재.

        for row_index, row in enumerate(layout):    # enumerate : 인덱스와 원소로 이루어진 튜플을 만들어줌. (layout을 튜플 형태로 만듦.)
            # print(row_index)
            # print(row)
            for col_index, cell in enumerate(row):  # (row를 튜플 형태로 만듦.)
                # print(f'{row_index}, {col_index} : {cell}')
                x = col_index * tile_size           # x 계산
                y = row_index * tile_size           # y 계산

                if cell == 'X':                     # cell이 'X'라면
                    tile = Tile((x,y), tile_size)   # Tile이라는 class사용.
                    self.tiles.add(tile)            # tiles에 tile을 더함.
                
                if cell == 'P':                     # cell이 'P'라면
                    player_sprite = Player((x,y), self.display_surface, self.create_jump_particles) # Player class 사용
                    self.player.add(player_sprite)  # self.player에 player_sprite는 더한다.

                # cell이 x인 곳에는 Tile을 사용하고 cell이 p인 곳에는 Player을 사용한다.


    def scroll_x(self):
        player = self.player.sprite                                 # player를 set_level에서 선언한 player의 sprite로 설정.
        player_x = player.rect.centerx                              # playe의 사각형에 centerx값을 player_x에 저장한다.
        direction_x = player.direction.x                            # player의 direction.x값을 direction_x에 저장한다.

        if player_x < screen_width * 1/4 and direction_x < 0:       #  player_x가 screen_width * 1/4값보다 작고 direction_x값이 0보다 작으면
            self.world_shift = 8        # world_shift를 8로 설정한다.
            player.speed = 0            # player파일의 speed를 0로 설정한다.
        elif player_x > screen_width * 3/4 and direction_x > 0:     # player_x가 screen_width * 3/4값보다 크고 direction_x값이 0보다 크면
            self.world_shift = -8       # world_shift를 -8로 설정한다.
            player.speed = 0            # player파일의 speed를 0로 설정한다.
        else:
            self.world_shift = 0        # world_shift를 0로 설정한다.
            player.speed = 8            # player파일의 speed를 0로 설정한다.

        # 캐릭터가 왼쪽이나 오른쪽으로 가다가 범위를 지나갈 때 캐릭터의 이동 스피드를 0으로 놓고 화면이 움직이는 스피드를 올려준다.
        # 캐릭터가 왼쪽으나 오른쪽으로 이동을 해도 범위 값을 지나가지 않는다면 화면의 스피드는 0으로 넣고 캐릭터의 이동 스피드를 올려준다.

    def horizontal_movement_collision(self):    # 가로 움직임 충돌
        player = self.player.sprite             # 위에서 선언한 self.player sprite
        player.rect.x += player.direction.x * player.speed      
        # player.rect.x는 바로 위에서 선언한 player의 사각형 x값이고 
        # += 기준 오른쪽인 더하는 대상은 player파일에서 선언한 direction x값과 speed값이다.

        for sprite in self.tiles.sprites():     # tiles가 포함된 그룹의 스프라이트 목록을 반환 -> tile가 포함된 그룹의 스프라이트들을 sprite로 설정
            if sprite.rect.colliderect(player.rect):        # sprite의 rect가 player의 rect와 겹치는지 확인(테스트). 사각형의 일부가 겹치면 True를 반환.
                if player.direction.x < 0:      # player의 direction에 x값이 0보다 작으면
                    player.rect.left = sprite.rect.right    # player의 사각형 left은 for문의 sprite의 사각형 right과 같다. (player의 left 값에 sprite 사각형의 right의 값이 된다.)
                    player.on_left = True       # player의 on_left는 True로 설정된다.
                    self.current_x = player.rect.left       # current_x에 player 사각형의 left값을 저장한다.
                elif player.direction.x > 0:    # player의 direction에 x값이 0보다 크면
                    player.rect.right = sprite.rect.left    # player의 사각형 right은 for문의 sprite의 사각형 left과 같다. (player의 right 값에 sprite 사각형의 left의 값이 된다.)
                    player.on_right = True      # player의 on_right는 True로 설정된다.
                    self.current_x = player.rect.right      # current_x에 player 사각형의 right값을 저장한다.

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            # player의 on_left가 True이고(and) (player의 사격형 left값이 current_x값보다 작거나(or) player의 direction에 x값이 0이상) 이 조건이라면
            player.on_left = False  # player의 on_left는 False로 설정.

        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            # player의 on_right가 True이고(and) (player의 사격형 right값이 current_x값보다 크거나(or) player의 direction에 x값이 0이하) 이 조건이라면
            player.on_right = False # player의 on_right는 False로 설정.

    def vertical_movement_collision(self):      # 세로 움직임 충돌 -> 가로와 x,y만 다르고 대체적으로 비슷
        player = self.player.sprite             # 위에서 선언한 self.player sprite
        player.apply_gravity()                  # player파일에서 선언한 apply_gravity를 사용

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def run(self):  # 아래에 있는 함수들을 업데이트 시키고 surface에 넣어서 보여줌.

        # dust particles
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()
        self.player.draw(self.display_surface)