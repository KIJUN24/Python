import pygame

class UI:
    def __init__(self, surface):

        # setup
        self.display_surface = surface  # UI를 실행시키기 위해서는 surface변수 필요(main file에서는 screen으로 변수를 준 뒤 실행)

        # health
        self.health_bar = pygame.image.load('C:\\Users\\lkjun\\OneDrive\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_9\\graphics\\ui\\health_bar.png').convert_alpha()
        self.health_bar_topleft = (54, 39)  # 왼쪽 위 꼭짓점 위치
        self.bar_max_width = 152            # health bar max width
        self.bar_height = 4                 # health bar height

        # coins
        self.coin = pygame.image.load('C:\\Users\\lkjun\\OneDrive\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_9\\graphics\\ui\\coin.png').convert_alpha()
        self.coin_rect = self.coin.get_rect(topleft = (50,61))  
        self.font = pygame.font.Font("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_9\\graphics\\ui\\ARCADEPI.TTF", 30)

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20,10)) # 왼쪽 위 꼭짓점 기준(20, 10)에 health_bar를 그림.
        # health_bar 계산
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))    # 사각형 설정(꼭짓점, (bar의 넓이, 높이))
        pygame.draw.rect(self.display_surface, "#dc4949", health_bar_rect)  # display_surface에 "#dc4949"색으로 health_bar_rect를 그림

    def show_coins(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)    # display_surface에 coin을 coin_rect위치에 그림
        coin_amount_surf = self.font.render(str(amount), False, '#33323d')  # amount를 '#33323d'색으로 폰트 설정
        coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4, self.coin_rect.centery))  # blit하기 위해 rect로 위치 설정
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)   # display_surface에 coin_amount_surf를 coin_amount_rect위치에 그림.