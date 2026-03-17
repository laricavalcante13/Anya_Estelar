import pygame
import random
from game import main

# --- Tamanho da tela e FPS ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    background = pygame.image.load("assets/menu.jpg").convert()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # inicia o jogo
                    main()  # chama a função principal do jogo
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Background
        screen.blit(background, (0, 0))

        # Textos
        font = pygame.font.Font(None, 48)
        title = font.render("Anya Estelar: Missão Paz Mundial", True, (255, 255, 255))
        start_text = font.render("Pressione ENTER para começar", True, (200, 200, 200))
        instructions_text = font.render("Use as setas para mover, evite os raios e colete as estrelas!", True, (200, 200, 200))
        screen.blit(title, (200, 150))
        screen.blit(start_text, (100, 300))
        screen.blit(instructions_text, (100, 350))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    menu()