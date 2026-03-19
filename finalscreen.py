import pygame
import random

# --- Tamanho da tela e FPS ---
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 600
FPS = 60

def victory(screen):
    from menu import menu
    try:
        victorybackground = pygame.image.load("assets/paz mundial.jpg").convert()
        victorybackground = pygame.transform.scale(victorybackground, (SCREEN_WIDTH, SCREEN_HEIGHT))
        font_obj = pygame.font.Font("assets/fonts/spy-agency.ttf", 32) # Diminuí um pouco o tamanho
    except FileNotFoundError as e:
        print(f"Erro {e}")
        return

    text_victory = font_obj.render("Você venceu!", True, (97,10,16))
    text_victory2 = font_obj.render("Anya agora é uma discípula imperial!", True, (141,169,155))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "menu"

        screen.blit(victorybackground, (0, 0))
        screen.blit(text_victory, (80, 200))
        screen.blit(text_victory2, (80, 260)) 
        
        pygame.display.flip()


def defeat(screen):
    from menu import menu
    try:
        defeatbackground = pygame.image.load("assets/anya crying.jpg").convert()
        defeatbackground = pygame.transform.scale(defeatbackground, (SCREEN_WIDTH, SCREEN_HEIGHT))
        font_obj = pygame.font.Font("assets/fonts/spy-agency.ttf", 32)
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return

    text_defeat = font_obj.render("Você perdeu!", True, (97,10,16))
    text_defeat2 = font_obj.render("Anya recebeu 8 raios e foi expulsa!", True, (141,169,155))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "menu"
    
        screen.blit(defeatbackground, (0, 0))
        screen.blit(text_defeat, (80, 200))
        screen.blit(text_defeat2, (80, 260))
        
        pygame.display.flip()
