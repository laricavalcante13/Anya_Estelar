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
        background = pygame.image.load("assets/anya discipula imperial.jpg").convert()
        font_title = pygame.font.Font("assets/spy-agency.ttf", 42)
        font_start = pygame.font.Font("assets/Orbitron-ExtraBold.ttf", 40)
        font_instr = pygame.font.Font("assets/spy-agency.ttf", 18)
        font_goal = pygame.font.Font("assets/spy-agency.ttf", 14)
    except FileNotFoundError as e:
        print(f"Erro: Certifique-se de que os arquivos estão na pasta assets! {e}")
        return

    #  Textos tela inicial
    title = font_title.render("Missão Anya Estelar", True, (0, 0, 0))
    start_text = font_start.render("Pressione ENTER para começar", True, (211, 211, 211))
    instructions_text = font_instr.render("Use as setas esquerda e direita para mover", True, (211, 211, 211))
    goal_text = font_goal.render("Colete as estrelas e evite os raios para não ser expulsa do Colégio Éden!", True, (250, 179, 173))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main() 
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # Renderizar textos na tela do menu
        screen.blit(background, (0, 0))
        screen.blit(title, (80, 250))
        screen.blit(start_text, (25, 350))
        screen.blit(instructions_text, (105, 430))
        screen.blit(goal_text, (30, 520))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    menu()
