import pygame
import random

# --- Tamanho da tela e FPS ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Função para exibir a tela de vitória
def victory(screen):
    pygame.mixer.music.load("assets/sounds/waku-waku.mp3")
    pygame.mixer.music.play(0)
    try:
        victorybackground = pygame.image.load("assets/paz-mundial.jpeg").convert()
        font_victory = pygame.font.Font("assets/fonts/spy-agency.ttf", 52) 
        font_victory2 = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24) 
        font_return = pygame.font.Font("assets/fonts/Orbitron-ExtraBold.ttf", 30)

    except FileNotFoundError as e:
        print(f"Erro {e}")
        return

    # Textos da tela de vitória
    text_victory = font_victory.render("Você venceu!", True, (250,179,173))
    text_victory2 = font_victory2.render("Anya se tornou uma discípula imperial do Colégio Éden!", True, (255,255,255))
    text_return = font_return.render("Pressione ENTER para jogar novamente", True, (255,255,255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         
                pygame.mixer.music.stop()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return "menu"

        # Renderização da tela de vitória
        screen.blit(victorybackground, (0, 0))
        screen.blit(text_victory, (150, 160))
        screen.blit(text_victory2, (50, 240)) 
        screen.blit(text_return, (80, 350))

        pygame.display.flip()

# Função para exibir a tela de derrota
def defeat(screen):
    pygame.mixer.music.load("assets/sounds/sorry.mp3")
    pygame.mixer.music.play(0)
    try:
        defeatbackground = pygame.image.load("assets/defeated.png").convert()
        font_defeat = pygame.font.Font("assets/fonts/spy-agency.ttf", 52)
        font_defeat2 = pygame.font.Font("assets/fonts/Orbitron-Medium.ttf", 24)
        font_return = pygame.font.Font("assets/fonts/Orbitron-ExtraBold.ttf", 30)

    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return
    
    # Textos da tela de derrota
    text_defeat = font_defeat.render("Você perdeu!", True, (44,40,39))
    text_defeat2 = font_defeat2.render("Anya recebeu 8 raios e foi expulsa do Colégio Éden!", True, (255,255,255))
    text_return = font_return.render("Pressione ENTER para jogar novamente", True, (255,255,255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return "menu"
    
        # Renderização da tela de derrota
        screen.blit(defeatbackground, (0, 0))
        screen.blit(text_defeat, (160, 160))
        screen.blit(text_defeat2, (75, 240))
        screen.blit(text_return, (80, 350))

        pygame.display.flip()
