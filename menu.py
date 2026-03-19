import pygame
import sys
from game import main

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Missão Anya Estelar")

def menu():  
    clock = pygame.time.Clock()

    try:
        background = pygame.image.load("assets/menu3.jpg").convert()
        font_title = pygame.font.Font("assets/fonts/spy-agency.ttf", 42)
        font_start = pygame.font.Font("assets/fonts/Orbitron-ExtraBold.ttf", 40)
        font_instr = pygame.font.Font("assets/fonts/spy-agency.ttf", 18)
        font_goal = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 18)
    except FileNotFoundError as e:
        print(f"Erro {e}")
        return

    # Textos Parte 1 (Título)
    title = font_title.render("Missão Anya Estelar", True, (97,10,16))
    start_text = font_start.render("Pressione ENTER para continuar", True, (141,169,155))
    
    # Textos Parte 2 (Instruções)
    instr_title = font_title.render("Instruções:", True, (250,179,173))
    instructions_text = font_instr.render("Use as setas esquerda e direita para mover", True, (255,255,255))
    goal_text = font_goal.render("Colete as estrelas e evite os raios para não ser expulsa do Colégio Éden!", True, (255,255,255))
    play_text = font_start.render("ENTER para Iniciar Missão", True, (141,169,155))

    # Variável de controle: 1 para Título, 2 para Instruções
    fase_menu = 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if fase_menu == 1:
                        fase_menu = 2  # Avança para as instruções
                    else:
                        main()         # Inicia o jogo
                
                elif event.key == pygame.K_ESCAPE:
                    if fase_menu == 2:
                        fase_menu = 1  # Volta para o título
                    else:
                        running = False

        # --- Renderização ---
        screen.blit(background, (0, 0))

        if fase_menu == 1:
            screen.blit(title, (80, 200))
            screen.blit(start_text, (25, 350))
        
        elif fase_menu == 2:
            screen.blit(instr_title, (250, 100))
            screen.blit(instructions_text, (105, 250))
            screen.blit(goal_text, (30, 300))
            screen.blit(play_text, (80, 450))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    menu()