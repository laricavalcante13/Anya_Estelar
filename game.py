import pygame
import random
from entities import Player, Item

# --- Configurações Iniciais ---
start_ticks = pygame.time.get_ticks() # Tempo inicial
TEMPO_LIMITE = 60000 # 60 segundos
# --- Tamanho da tela e FPS ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Anya Estelar: Missão Paz Mundial")
    background = pygame.image.load("assets/background.jpg").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    raios_tomados = 0 
    limite_raios = 8
    score = 0
    start_ticks = pygame.time.get_ticks()

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

        # 2. Lógica de Tempo e Vitória
        segundos_decorridos = (pygame.time.get_ticks() - start_ticks)
        if segundos_decorridos >= TEMPO_LIMITE:
            print("Missão concluída! Anya se tornou uma discípula imperial!")
            running = False

        # 3. Spawning e Updates
        if random.random() < 0.02: 
            s = Item(is_star=True)
            stars.add(s)
            all_sprites.add(s)
        
        if random.random() < 0.03:
            b = Item(is_star=False)
            bolts.add(b)
            all_sprites.add(b)

        all_sprites.update()

        # 4. Colisões
        if pygame.sprite.spritecollide(anya, stars, True):
            score += 1
            print(f"Estrelas: {score}")

        colisao_raio = pygame.sprite.spritecollide(anya, bolts, True)
        if colisao_raio:
            raios_tomados += 1
            update() 
            print(f"Raios: {raios_tomados}/8")
            if raios_tomados >= limite_raios:
                print("Game Over! Anya levou 8 raios e foi expulsa do Colégio Éden.")
                running = False

        # 5. Desenho
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
