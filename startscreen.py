from board.Board import Board, Sketchboard
from ui.ui import Console
from ui.uidesign import Button,draw_table,get_cell_from_mouse

import pygame
from pygame.locals import *
from generateplanes import chooseplanes

def start():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Planes Game")
    button1 = Button(50, 50, 200, 100, (128, 128, 128), "Generate planes automaticallly")
    button2 = Button(550, 50, 200, 100, (128, 128, 128), "Choose positions for planes")
    button3 = Button(350, 540, 100, 50, (0, 128, 0), "START")
    up = Button(550, 300, 100, 25, (128, 128, 128), "UP")
    down = Button(550, 350, 100, 25, (128, 128, 128), "DOWN")
    left = Button(550, 400, 100, 25, (128, 128, 128), "LEFT")
    right = Button(550, 450, 100, 25, (128, 128, 128), "RIGHT")
    background_image = pygame.image.load("PlaneIMG.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    headrows = headcols = rows = cols = None
    playerboard = aiboard = None
    userchoice = 3
    directions = False
    clicked_cells = [[False] * 10 for _ in range(10)]
    inputheadcells = []
    inputdirections = []
    chosenplanes = 0
    b3 = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.is_clicked(event.pos):
                    userchoice = 1
                    b3 = True
                    sketchboard = Sketchboard()
                    playerboard = Board(int(userchoice), sketchboard)
                    headrows, headcols = playerboard.getheadsrowsandcols()
                    rows, cols = playerboard.getplanerowsandcols()
                    aiboard = Board(1, sketchboard)
                elif button2.is_clicked(event.pos):
                    userchoice = 2
                    headrows = headcols = rows = cols = None
                    b3 = True
                if button3.is_clicked(event.pos) and b3:
                    running = False
                    pygame.quit()
                    console = Console(playerboard, aiboard)
                    console.menu()

                if directions == True and up.is_clicked(event.pos) and userchoice == 2:
                    directions = False
                    chosenplanes += 1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("up")
                if directions == True and down.is_clicked(event.pos) and userchoice == 2:
                    directions = False
                    chosenplanes += 1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("down")
                if directions == True and left.is_clicked(event.pos) and userchoice == 2:
                    directions = False
                    chosenplanes += 1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("left")
                if directions == True and right.is_clicked(event.pos) and userchoice == 2:
                    directions = False
                    chosenplanes += 1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("right")
                if running:
                    cell = get_cell_from_mouse(pygame.mouse.get_pos(), 250, 250)
                if cell and userchoice == 2:
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    clicked_cells[cell[0] - 1][cell[1] - 1] = True
                    headcell = "" + chr(ord('A') - 1 + cell[1]) + str(cell[0])
                    directions = True
        if running:
            screen.fill((255, 255, 255))
            screen.blit(background_image, (0, 0))
            button1.draw(screen)
            button2.draw(screen)
            if chosenplanes == 3:
                sketchboard = Sketchboard()
                playerboard = Board(int(userchoice), sketchboard, inputheadcells, inputdirections)
                headrows, headcols = playerboard.getheadsrowsandcols()
                rows, cols = playerboard.getplanerowsandcols()
                aiboard = Board(1, sketchboard)
            if directions:
                up.draw(screen)
                down.draw(screen)
                left.draw(screen)
                right.draw(screen)
            if b3:
                button3.draw(screen)
                draw_table(screen, 250, 250, headrows, headcols, rows, cols, clicked_cells)
            pygame.display.flip()