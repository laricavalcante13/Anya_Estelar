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

def time_score(screen, score, raios_tomados, limite_raios, segundos_decorridos, tempo_limite):
    font = pygame.font.Font(None, 36)  # Fonte padrão tamanho 36

    # Score das estrelas
    score_surface = font.render(f"Estrelas: {score}", True, (255, 215, 0))
    screen.blit(score_surface, (10, 50))  

    # Score dos raios
    raios_surface = font.render(f"Raios: {raios_tomados}/{limite_raios}", True, (163, 171, 174))
    screen.blit(raios_surface, (10, 90))  

    # Tempo restante
    tempo_restante = max(0, (tempo_limite - segundos_decorridos) // 1000)  
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    tempo_surface = font.render(f"Tempo: {minutos:02d}:{segundos:02d}", True, (138, 76, 87))
    screen.blit(tempo_surface, (10, 10)) 

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
            anya.shocked()
            bolts.update() 
            print(f"Raios: {raios_tomados}/8")
            if raios_tomados >= limite_raios:
                print("Game Over! Anya levou 8 raios e foi expulsa do Colégio Éden.")
                running = False

        # 5. Desenho
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        time_score(screen, score, raios_tomados, limite_raios, segundos_decorridos, TEMPO_LIMITE)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
