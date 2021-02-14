import pygame
import sys
import tkinter as tk
from tkinter import messagebox
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption('X \ O ')
raw = 3
rectgrid = [pygame.draw.rect(win, (0, 0, 0), (i*(600//3), j*(600//3), 200, 200))
            for i in range(raw) for j in range(raw)]
winlisty = [{(x, y)for y in range(3)}for x in range(3)]
winlistx = [{(x, y)for x in range(3)}for y in range(3)]
winlistdiag = [{(x, x)for x in range(3)}, {(x, 2-x) for x in range(3)}]


def grid(win, raw):
    sep = 600//3
    for i in range(raw):
        pygame.draw.line(win, (255, 255, 255), (i*sep, 0), (i*sep, 600), 7)
        pygame.draw.line(win, (255, 255, 255), (0, i * sep), (600, i * sep), 7)


isX = False
isO = True
X_move = set({})
O_move = set({})
X_win = False
O_win = False
drow = False


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


while 1:

    if not X_win and not O_win and not drow:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            for rect in rectgrid:
                if event.type == pygame.MOUSEBUTTONUP and rect.collidepoint(pygame.mouse.get_pos()):
                    if isO:
                        pygame.draw.circle(
                            win, (0, 0, 255), (rect[0]+100, rect[1]+100), 50, 7)
                        isX = True
                        isO = False
                        O_move.add((rect[0]//200, rect[1]//200))
                    elif isX:
                        pygame.draw.line(
                            win, (255, 0, 0), (rect[0]+50, rect[1]+50), (rect[0]+150, rect[1]+150), 7)
                        pygame.draw.line(
                            win, (255, 0, 0), (rect[0]+150, rect[1]+50), (rect[0]+50, rect[1]+150), 7)
                        isX = False
                        isO = True
                        X_move.add((rect[0] // 200, rect[1] // 200))
                    rectgrid.remove(rect)
    else:
        rectgrid = [pygame.draw.rect(win, (0, 0, 0), (i * (600 // 3), j * (600 // 3), 200, 200)) for i in range(raw) for
                    j in range(raw)]
        isX = False
        isO = True
        X_move = set({})
        O_move = set({})
        X_win = False
        O_win = False
        drow = False

    for s in winlistx:
        if s & O_move == s and len(O_move) >= 3:
            O_win = True
        elif s & X_move == s and len(X_move) >= 3:
            X_win = True
    for s in winlisty:
        if s & O_move == s and len(O_move) >= 3:
            O_win = True
        elif s & X_move == s and len(X_move) >= 3:
            X_win = True
    for s in winlistdiag:
        if s & O_move == s and len(O_move) >= 3:
            O_win = True
        elif s & X_move == s and len(X_move) >= 3:
            X_win = True
    if rectgrid == []:
        drow = True

    grid(win, raw)
    pygame.display.update()
    if O_win:
        message_box('O Wins!', 'Play again...')

    elif X_win:
        message_box('X Wins!', 'Play again...')

    elif drow:
        message_box("It's a Drow!", 'Play again...')

    #win.fill((0, 0, 0))

    #print (O_move,X_move)
