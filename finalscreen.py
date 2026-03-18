import pygame
import random
from game import main
from menu import menu

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Missão Anya Estelar")

def victory():

    try:
        victorybackground = pygame.image.load("assets/paz mundial.jpg").convert()
        font_victory = pygame.font.Font("assets/fonts/spy-agency.ttf", 42)
    except FileNotFoundError as e:
        print(f"Erro: Certifique-se de que os arquivos estão na pasta assets! {e}")
        return


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "menu"

        screen.blit(victorybackground, (0, 0))
        screen.blit(font_victory, (80, 200))
        pygame.display.flip()


def defeat():

    try:
        defeatbackground = pygame.image.load("assets/anya crying.jpg").convert()
        font_defeat = pygame.font.Font("assets/fonts/spy-agency.ttf", 42)
    except FileNotFoundError as e:
        print(f"Erro: Certifique-se de que os arquivos estão na pasta assets! {e}")
        return

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "menu"
    
        screen.blit(defeatbackground, (0, 0))
        screen.blit(font_defeat, (80, 200))
        pygame.display.flip()

