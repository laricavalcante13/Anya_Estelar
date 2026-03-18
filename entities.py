import pygame
import random

#-----Tamanho da tela-----
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_normal = pygame.image.load("assets/anya/anya-happy2.png").convert_alpha()
        self.image_shock = pygame.image.load("assets/anya/anya-shocked.png").convert_alpha()
        self.image = self.image_normal
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 60))
        self.speed = 7
        self.timer_shock = 0 

    def shocked(self):
        self.image = self.image_shock
        self.timer_shock = pygame.time.get_ticks()

    def update(self):
        # Lógica de movimento.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        # Volta ao normal após 500ms do raio.
        if self.image == self.image_shock and pygame.time.get_ticks() - self.timer_shock > 500:
            self.image = self.image_normal

class Item(pygame.sprite.Sprite):
    def __init__(self, is_star=True):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.blit(pygame.image.load("assets/star.png") if is_star else pygame.image.load("assets/bolt.png"))
        self.rect = self.image.get_rect(x=random.randint(0, SCREEN_WIDTH-30), y=-50)
        self.speed = random.randint(3, 6)
        self.is_star = is_star

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill() # Remove o grupo quando sair da tela.
