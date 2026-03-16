import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carregue suas duas imagens aqui
        self.image_normal = pygame.image.load("anya.png").convert_alpha()
        self.image_shock = pygame.image.load("anya_shocked.png").convert_alpha()
        self.image = self.image_normal
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 60))
        self.speed = 7
        self.timer_shock = 0 # Para voltar ao normal após um tempo

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
        # Volta ao normal após 500ms do raio
        if self.image == self.image_shock and pygame.time.get_ticks() - self.timer_shock > 500:
            self.image = self.image_normal

class Item(pygame.sprite.Sprite):
    def __init__(self, color, is_star=True):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(x=random.randint(0, SCREEN_WIDTH-30), y=-50)
        self.speed = random.randint(3, 6)
        self.is_star = is_star

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill() # Remove o grupo quando sair da tela
