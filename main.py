import pygame, sys, time, random
from pygame.locals import *
from m import *

pygame.init()
window = pygame.display.set_mode((450, 600))
pygame.display.set_caption("2048")

# Настройка цвета и шрифта
BLACK = (112, 128, 144)
YELLOW = (240, 230, 140)
ORANGE = (255, 69, 0)
CYAN = (135, 206, 250)
GREEN = (51, 255, 51)
myfont = pygame.font.SysFont(None, 80)


def buildText(board, i, j):
    if board[j][i] == "0":
        text = myfont.render(" ", True, CYAN)
    else:
        text = myfont.render(board[j][i], True, CYAN)
    textRect = text.get_rect()
    textRect.centerx = i * 100 + 75
    textRect.centery = j * 100 + 180
    return text, textRect


def showText(board):
    """Отображение цифр на экране"""
    for i in range(4):
        for j in range(4):
            window.blit(buildText(board, i, j)[0], buildText(board, i, j)[1])


def quitWindow(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()


def gameOver():
    label = myfont.render("Вы проиграли!", True, ORANGE)
    labelRect = label.get_rect()
    labelRect.centerx = window.get_rect().centerx
    labelRect.centery = window.get_rect().centery
    window.blit(label, labelRect)
    event = pygame.event.wait()
    quitWindow(event)


def win():
    window.fill(BlACK)
    label = myfont.render("Вы победили!", True, GREEN)
    labelRect = label.get_rect()
    labelRect.centerx = window.get_rect().centerx
    labelRect.centery = window.get_rect().centery
    window.blit(label, labelRect)
    event = pygame.event.wait()
    quitWindow(event)


def gameLoop():
    # Инициализируйте игровое поле с 16 блоками для хранения номера
    board = init_board()
    blocks = []
    for i in range(4):
        for j in range(4):
            blocks.append([pygame.Rect((i * 100) + 30, (j * 100) + 135, 90, 90), BLACK])
    while True:
        for event in pygame.event.get():

            quitWindow(event)
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    board = main(board, "u")
                if event.key == K_DOWN:
                    board = main(board, "d")
                if event.key == K_LEFT:
                    board = main(board, "l")
                if event.key == K_RIGHT:
                    board = main(board, "r")
        window.fill(BLACK)
        header = myfont.render("Игра 2048", True, CYAN)
        window.blit(header, (30, 50))
        pygame.draw.rect(window, YELLOW, pygame.Rect(20, 125, 410, 410))

        for block in blocks:
            pygame.draw.rect(window, block[1], block[0])
        showText(board)
        if checkLose(board):
            gameOver()
        elif checkWin(board):
            win()
        pygame.display.update()
        time.sleep(0.50)
gameLoop()