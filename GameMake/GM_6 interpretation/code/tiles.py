import pygame

class Tile(pygame.sprite.Sprite):                           # pygame안에 sprite안에 Sprite를 사용하겠다.
    def __init__(self, pos, size):                          # class를 만들 때 첫 번째로 만들어주는 함수. 어떤 정보가 필요한지 알려주는 함수.
                                                            # 다른 곳에서 Tile함수를 사용하고 싶다면 pos, size 정보를 넣어줘야 사용가능하다.
        super().__init__()                                  # Sprite에 있는 정보들을 모두 사용할 것이다.
        self.image = pygame.Surface((size, size))           # image라는 변수에 Surface생성 ((size, size)) : 사이즈 정보 필요(튜플형식)
        self.image.fill('gray')                             # 생성한 Surface를 회색으로 채움.
        self.rect = self.image.get_rect(topleft = pos)      # Surface의 사각형 영역 반환. (기준점 좌표 : topleft = pos) -> pos정보 필요
        # get_rect : 이미지의 크기를 가진 직사각형 객체를 가져온다.

    def update(self, x_shift):                              # update를 하여면 x_shift정보가 있어야 한다.
        self.rect.x += x_shift                              # 사각형의 x값이 x_shift만큼 증가한다.
        # rect.x : 개체의 위치(x값)를 업데이트 하기위해 사용.