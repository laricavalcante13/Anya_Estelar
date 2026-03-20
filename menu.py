import pygame
import sys
from game import main
from database import init_db, get_high_score

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
# Tela e Fundo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Missão Anya Estelar")
# Música do jogo
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/kura-kura2.mp3")
pygame.mixer.music.set_volume(0.5)

def menu():  
    clock = pygame.time.Clock()
    init_db()
    recorde = get_high_score()
    pygame.mixer.music.play(-1)

    try:
        background = pygame.image.load("assets/menu3.jpg").convert()
        font_title = pygame.font.Font("assets/fonts/spy-agency.ttf", 42)
        font_start = pygame.font.Font("assets/fonts/Orbitron-ExtraBold.ttf", 40)
        font_instr = pygame.font.Font("assets/fonts/spy-agency.ttf", 18)
        font_goal = pygame.font.Font("assets/fonts/Orbitron-Bold.ttf", 18)
        font_high_score = pygame.font.Font("assets/fonts/Orbitron-ExtraBold.ttf", 24)
    except FileNotFoundError as e:
        print(f"Erro {e}")
        return

    # Textos Parte 1 (Título)
    title = font_title.render("Missão Anya Estelar", True, (250,179,173))
    start_text = font_start.render("Pressione ENTER para continuar", True, (255,255,255))
    high_score_text = font_high_score.render(f"HIGH SCORE: {get_high_score()}", True, (255,255,255))

    # Textos Parte 2 (Instruções)
    instr_title = font_title.render("Instruções:", True, (250,179,173))
    instructions_text = font_instr.render("Use as setas esquerda e direita para mover", True, (141,169,155))
    goal_text = font_goal.render("Colete as estrelas e evite os raios para não ser expulsa do Colégio Éden!", True, (141,169,155))
    play_text = font_start.render("ENTER para Iniciar Missão", True, (255,255,255))

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
                        return True         # Inicia o jogo
                
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
            screen.blit(high_score_text, (270, 500))
        
        elif fase_menu == 2:
            screen.blit(instr_title, (250, 100))
            screen.blit(instructions_text, (105, 250))
            screen.blit(goal_text, (30, 300))
            screen.blit(play_text, (80, 450))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    while True:
        # 1. Abre o menu. Ele fica preso aqui até você dar ENTER na tela 2.
        jogar = menu() 
        pygame.mixer.music.stop()

        
        if jogar:
            main() 
        else:
            break