import pygame
import random

# --- Configurações Iniciais ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores (Substitua por imagens depois)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (200, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("anya.png").convert_alpha()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 182, 193)) # Rosa Anya
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 60))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Anya Estelar: Missão Paz Mundial")
    clock = pygame.time.Clock()

    # Grupos de Sprites
    all_sprites = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    bolts = pygame.sprite.Group()

    anya = Player()
    all_sprites.add(anya)

    score = 0
    running = True

    while running:
        # 1. Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Lógica de Spawning (Surgimento)
        if random.random() < 0.02: # Chance de cair estrela
            s = Item(GOLD, True)
            stars.add(s)
            all_sprites.add(s)
        
        if random.random() < 0.03: # Chance de cair raio (mais frequente)
            b = Item(RED, False)
            bolts.add(b)
            all_sprites.add(b)

        # 3. Update
        all_sprites.update()

        # Colisões
        if pygame.sprite.spritecollide(anya, stars, True):
            score += 1
            print(f"Estrelas: {score}")
            if score >= 8:
                print("Missão Cumprida, Anya Estelar! Você salvou a paz mundial!")
                running = False
        # Dentro do loop de colisões no game.py
        if pygame.sprite.spritecollide(anya, bolts, True):
            vidas_tonitrus -= 1
            anya.chocada() 

        if pygame.sprite.spritecollide(anya, bolts, True):
            print("Você ganhou 8 raios! Está expulsa do colégio Éden e adeus a paz mundial.")
            running = False

        # 4. Desenho
        screen.fill(WHITE)
        all_sprites.draw(screen)
        
        # Exibir placar  (implementar fonte aqui!!!)

        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
