import pygame
import random

# --- Tamanho da tela  ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe do jogador.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_normal = pygame.image.load("assets/anya-happy2.png").convert_alpha()
        self.image_shock = pygame.image.load("assets/anya-shocked.png").convert_alpha()
        self.image = self.image_normal
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 60))
        self.speed = 7
        self.timer_shock = 0 

    def shocked(self):
        # Troca a imagem em caso de colisão e inicia o timer.
        self.image = self.image_shock
        self.timer_shock = pygame.time.get_ticks()

    def update(self):
        # Lógica de movimento.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        # Imagem do jogador volta ao normal após colisão.
        if self.image == self.image_shock and pygame.time.get_ticks() - self.timer_shock > 500:
            self.image = self.image_normal

# Classe dos itens (estrelas e raios).
class Item(pygame.sprite.Sprite):
    def __init__(self, segundos, is_star=True):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        if is_star:
            self.image = pygame.image.load("assets/star.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/bolt.png").convert_alpha()
        self.rect = self.image.get_rect(x=random.randint(0, SCREEN_WIDTH-50), y=-50)
        bonus = segundos * 0.1 
        self.speed = random.randint(3, 6) + bonus
        self.is_star = is_star

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill() # Remove o grupo quando sair da tela.
