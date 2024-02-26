from board.Board import Board, Sketchboard
from ui.ui import Console
from ui.uidesign import Button

import pygame
from pygame.locals import *
from generateplanes import chooseplanes


def get_cell_from_mouse(pos, x,y):
    CELL_SIZE = 25
    x1, y1 = pos[0] - x, pos[1] - y
    col = x1 // CELL_SIZE
    row = y1 // CELL_SIZE
    if 0<col <= 10 and 0<row <= 10:
        return row, col
    return None

def draw_table(screen, x, y, headrows, headcols, rows, cols, clicked_cell):
    CELL_SIZE = 25
    TABLE_WIDTH = 10 * CELL_SIZE
    TABLE_HEIGHT = 10 * CELL_SIZE
    for col in range(1, 11):
        label = chr(ord('A') + col - 1)
        font = pygame.font.SysFont(None, 24)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (col * CELL_SIZE + 0.5 * CELL_SIZE - 6 + x, 5 + y))

    # Draw row labels (1 to 10)
    for row in range(1, 11):
        label = str(row)
        font = pygame.font.SysFont(None, 24)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (5 + x, row * CELL_SIZE + 0.5 * CELL_SIZE - 12 + y))

    for row in range(10):
        for col in range(10):
            if clicked_cell[row][col]:
                pygame.draw.rect(screen, (0, 255, 0),
                                 ((col+1) * CELL_SIZE + x, (row+1) * CELL_SIZE + y, CELL_SIZE, CELL_SIZE), 1)
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 ((col+1) * CELL_SIZE + x, (row+1) * CELL_SIZE + y, CELL_SIZE, CELL_SIZE), 1)

    uifont = pygame.font.SysFont(None, 16)
    if headrows!=None:
        for i in range(len(headrows)):
            x_text = uifont.render("H", True, (255, 255, 255))
            screen.blit(x_text, (int(headrows[i] + 1) * 25 + 10 + x, int(headcols[i] + 1) * 25 + 8 + y))
        for i in range(len(rows)):
            if not (rows[i] == headrows[0] and cols[i] == headcols[0]) and not (
                    rows[i] == headrows[1] and cols[i] == headcols[1]) and not (
                    rows[i] == headrows[2] and cols[i] == headcols[2]):
                x_text = uifont.render("x", True, (255, 255, 255))
                screen.blit(x_text, (int(rows[i] + 1) * 25 + 10 + x, int(cols[i] + 1) * 25 + 8 + y))


if __name__ == '__main__':
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Planes Game")
    button1 = Button(50, 50, 200, 100, (128, 128, 128), "Generate planes automaticallly")
    button2 = Button(550, 50, 200, 100, (128, 128, 128), "Choose positions for planes")
    button3 = Button(350, 540, 100, 50, (0, 128, 0), "START")
    up=Button(550, 300, 100, 25, (128, 128, 128), "UP")
    down=Button(550, 350, 100, 25, (128, 128, 128), "DOWN")
    left=Button(550, 400, 100, 25, (128, 128, 128), "LEFT")
    right=Button(550, 450, 100, 25, (128, 128, 128), "RIGHT")
    background_image = pygame.image.load("PlaneIMG.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    headrows = headcols = rows = cols = None
    playerboard = aiboard = None
    userchoice = 3
    directions=False
    clicked_cells=[[False] * 10 for _ in range(10)]
    inputheadcells=[]
    inputdirections=[]
    chosenplanes=0
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
                    headrows=headcols=rows=cols=None
                    b3 = True
                if button3.is_clicked(event.pos) and b3:
                    running = False
                    pygame.quit()
                    console = Console(playerboard, aiboard)
                    console.menu()

                if directions==True and up.is_clicked(event.pos) and userchoice ==2:
                    directions = False
                    chosenplanes+=1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("up")
                if directions==True and down.is_clicked(event.pos) and userchoice ==2:
                    directions = False
                    chosenplanes+=1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("down")
                if directions==True and left.is_clicked(event.pos) and userchoice ==2:
                    directions = False
                    chosenplanes+=1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("left")
                if directions==True and right.is_clicked(event.pos) and userchoice ==2:
                    directions=False
                    chosenplanes+=1
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    inputheadcells.append(headcell)
                    inputdirections.append("right")
                if running:
                    cell = get_cell_from_mouse(pygame.mouse.get_pos(), 250,250)
                if cell and userchoice ==2:
                    clicked_cells = [[False] * 10 for _ in range(10)]
                    clicked_cells[cell[0] - 1][cell[1] - 1] = True
                    headcell = "" + chr(ord('A') - 1 + cell[1]) + str(cell[0])
                    print("Clicked cell:", chr(ord('A') - 1 + cell[1]) + str(cell[0]))
                    directions=True
        if running:
            screen.fill((255, 255, 255))
            screen.blit(background_image, (0, 0))
            button1.draw(screen)
            button2.draw(screen)
            if chosenplanes==3:
                sketchboard = Sketchboard()
                playerboard = Board(int(userchoice), sketchboard,inputheadcells,inputdirections)
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
