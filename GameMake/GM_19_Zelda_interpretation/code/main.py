import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        
        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('GameMake/GM_12_Zelda/audio/main.ogg')
        main_sound.set_volume(0.6)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()        # m키를 누르면 level파일에 있는 toggle_menu()함수가 실행
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            self.screen.fill(WATER_COLOR)
            self.level.run()                            # level파일의 run()함수를 실행
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()      # Game안에 run()함수를 실행