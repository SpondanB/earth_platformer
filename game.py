import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Earthlands")
        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [100,260]
        self.img_mov = [False, False, False, False]

        self.colision_area = pygame.Rect(50, 50, 300, 100)
    
    def run(self):
        while True:
            self.screen.fill((14, 215, 255))

            self.img_pos[1] += (self.img_mov[1] - self.img_mov[0]) * 5
            self.img_pos[0] += (self.img_mov[3] - self.img_mov[2]) * 5

            img_rect = pygame.Rect(*self.img_pos, *self.img.get_size())

            if img_rect.colliderect(self.colision_area):
                pygame.draw.rect(self.screen,(0,0,255), self.colision_area)
            else:
                pygame.draw.rect(self.screen,(255,0,0), self.colision_area)

            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.img_mov[0] = True
                    if event.key == pygame.K_DOWN:
                        self.img_mov[1] = True
                    if event.key == pygame.K_LEFT:
                        self.img_mov[2] = True
                    if event.key == pygame.K_RIGHT:
                        self.img_mov[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.img_mov[0] = False
                    if event.key == pygame.K_DOWN:
                        self.img_mov[1] = False
                    if event.key == pygame.K_LEFT:
                        self.img_mov[2] = False
                    if event.key == pygame.K_RIGHT:
                        self.img_mov[3] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()