import pygame
import random

# constantes tamanho da tela
W_WIDTH = 800
W_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Aqui você pode carregar sua imagem da Anya
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 182, 193)) 
        self.rect = self.image.get_rect(center=(W_WIDTH//2, W_HEIGHT - 60))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < W_WIDTH:
            self.rect.x += self.speed

class Item(pygame.sprite.Sprite):
    def __init__(self, color, is_star=True):
        super().__init__()
        self.is_star = is_star
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(x=random.randint(0, W_WIDTH-30), y=-50)
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > W_HEIGHT:
            self.kill()