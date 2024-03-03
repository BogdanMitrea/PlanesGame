import pygame

from board.Board import Board, GameWonException, GameLostException
from random import randint, choice

from pygame.locals import *
from ui.uidesign import Button


class Console:
    def __init__(self, playerboard: Board, aiboard: Board):
        self.__clicked_cells = [[False] * 10 for _ in range(10)]
        self.__drawn_cells = [[0] * 10 for _ in range(10)]
        self.__drawn_ai_cells = [[0] * 10 for _ in range(10)]
        self.__playerboard = playerboard
        self.__aiboard = aiboard
        self.__possibleguesses = list(range(99))

    def process_player_guess(self, guess):
        v = []
        for i in guess:
            v.append(i)
        if len(v) != 2 and len(v) != 3:
            raise KeyError("Input a letter followed by a number")
        if len(v) == 3 and (v[1] != '1' or v[2] != '0'):
            raise KeyError("Input a letter followed by a number")
        if v[0].islower():
            v[0] = v[0].upper()
        if not v[0].isalpha():
            raise KeyError("Input a letter followed by a number")
        if ascii(v[0]) > ascii('J'):
            raise KeyError("Invalid letter and number combination")
        if int(v[1]) < 1 or int(v[1]) > 10:
            raise KeyError("Invalid letter and number combination")
        col = ord(v[0]) - ord('A')
        if len(v) == 2:
            row = int(v[1]) - 1
        else:
            row = 9
        return row, col

    def player_guess(self, guess):
        ok = 0
        res = 0
        while ok == 0:
            try:
                row, col = self.process_player_guess(guess)
                res = self.__aiboard.playerguess(row, col)
                ok = 1
            except KeyError as ke:
                print(ke)
        return res

    def ai_guess(self):
        """
        the function will get the last guess details and if it was air will guess randomly and if it was a hit it will
        guess somewhere in the distance of 1 square and if that is not possible it will guess randomly again
        :return:
        """
        lg, lr, lc = self.__playerboard.getlastguess()
        if str(lg) == "air":
            cguess = choice(self.__possibleguesses)
            row = cguess // 10
            col = cguess % 10
            self.__possibleguesses.remove(cguess)
            res = self.__playerboard.aiguess(row, col)
            return res, row, col
        else:
            ok = 1
            counter = 0
            sideguesses = []
            while ok == 1:
                ok = 0
                row = int(lr) + randint(-1, 1)
                col = int(lc) + randint(-1, 1)
                if row == -1 or row == 10 or col == -1 or col == 10:
                    ok = 1
                cguess = row * 10 + col
                if cguess not in sideguesses:
                    sideguesses.append(cguess)
                    counter += 1
                if cguess not in self.__possibleguesses:
                    ok = 1
                if counter > 8:
                    break
            ok = 0
            if counter > 8:
                self.__playerboard.setlastguessair()
                cguess = choice(self.__possibleguesses)
                row = cguess // 10
                col = cguess % 10
                self.__possibleguesses.remove(cguess)
                ok = 1
            if ok == 0:
                self.__possibleguesses.remove(cguess)
            res = self.__playerboard.aiguess(row, col)
            return res, row, col

    def create_label(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def draw_table(self, screen, margin):
        CELL_SIZE = 30
        TABLE_WIDTH = 10 * CELL_SIZE
        TABLE_HEIGHT = 10 * CELL_SIZE
        for col in range(1, 11):
            label = chr(ord('A') + col - 1)
            font = pygame.font.SysFont(None, 24)
            text = font.render(label, True, (255, 255, 255))
            screen.blit(text, (col * CELL_SIZE + 0.5 * CELL_SIZE - 6 + margin, 5))

        # Draw row labels (1 to 10)
        for row in range(1, 11):
            label = str(row)
            font = pygame.font.SysFont(None, 24)
            text = font.render(label, True, (255, 255, 255))
            screen.blit(text, (5 + margin, row * CELL_SIZE + 0.5 * CELL_SIZE - 12))

        uifont = pygame.font.SysFont(None, 20)
        # Draw grid
        for row in range(1, 11):
            for col in range(1, 11):
                if margin > 0:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     (col * CELL_SIZE + margin, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                    if self.__drawn_ai_cells[row - 1][col - 1] != 0:
                        if self.__drawn_ai_cells[row - 1][col - 1] == 3:
                            x_text = uifont.render("H", True, (255, 69, 0))
                        elif self.__drawn_ai_cells[row - 1][col - 1] == 2:
                            x_text = uifont.render("x", True, (255, 69, 0))
                        else:
                            x_text = uifont.render("a", True, (0, 0, 0))
                        screen.blit(x_text, (int(row) * 30 + 12 + margin, int(col) * 30 + 8))
                else:
                    if self.__clicked_cells[row - 1][col - 1]:
                        pygame.draw.rect(screen, (0, 255, 0),
                                         (col * CELL_SIZE + margin, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                    else:
                        pygame.draw.rect(screen, (0, 0, 0),
                                         (col * CELL_SIZE + margin, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                    if self.__drawn_cells[row - 1][col - 1] != 0:
                        if self.__drawn_cells[row - 1][col - 1] == 3:
                            x_text = uifont.render("H", True, (255, 69, 0))
                        elif self.__drawn_cells[row - 1][col - 1] == 2:
                            x_text = uifont.render("x", True, (255, 69, 0))
                        else:
                            x_text = uifont.render("a", True, (0, 0, 139))
                        screen.blit(x_text, (int(row) * 30 + 12 + margin, int(col) * 30 + 8))

    def get_cell_from_mouse(self, pos, margin):
        CELL_SIZE = 30
        x, y = pos[0]-margin,pos[1]-margin
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if col <= 10 and row <= 10:
            return row, col
        return None

    def menu(self):
        playerguess = ""
        pygame.init()
        running = True
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image = pygame.image.load("PlaneBKG3.jpg")
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        wintext = None
        wintext_rect = None
        done = False
        attackbutton = Button(350, 175, 70, 30, (255, 0, 0), "ATTACK")
        pygame.display.set_caption("Planes Game")
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if attackbutton.is_clicked(event.pos):
                            if playerguess != "":
                                try:
                                    if len(playerguess) > 2:
                                        col = 9
                                    else:
                                        col = int(playerguess[1]) - 1
                                    row = ord(playerguess[0]) - ord('A')
                                    if row >= 0 and col >= 0:
                                        res = self.player_guess(playerguess)
                                        self.__drawn_cells[row][col] = res
                                        self.draw_table(screen, 450)
                                        pygame.display.flip()
                                except GameWonException:
                                    font = pygame.font.Font(None, 36)  # None means default font
                                    wintext, wintext_rect = self.create_label("Congratulations you won!", font,
                                                                              (255, 69, 0))
                                    wintext_rect.center = (180, 350)
                                    screen.fill((100, 100, 100))
                                    screen.blit(background_image, (0, 0))
                                    self.__drawn_cells[row][col] = 3
                                    self.draw_table(screen, 0)
                                    self.draw_table(screen, 450)
                                    screen.blit(wintext, wintext_rect)
                                    pygame.display.flip()
                                    done = True
                                    row = -1
                                if row >= 0 and col >= 0:
                                    try:
                                        res, row, col = self.ai_guess()
                                        self.__drawn_ai_cells[row][col] = res
                                    except GameLostException:
                                        font = pygame.font.Font(None, 36)  # None means default font
                                        losetext, losetext_rect = self.create_label("Computer wins!", font,
                                                                                    (255, 69, 0))
                                        losetext_rect.center = (180 + 450, 350)
                                        screen.fill((100, 100, 100))
                                        screen.blit(background_image, (0, 0))
                                        copyheadcoordinates = self.__playerboard.getcopycoordinates()
                                        for i in range(3):
                                            if self.__drawn_ai_cells[copyheadcoordinates[i][0]][
                                                copyheadcoordinates[i][1]] != 3:
                                                self.__drawn_ai_cells[copyheadcoordinates[i][0]][
                                                    copyheadcoordinates[i][1]] = 3
                                        self.draw_table(screen, 0)
                                        self.draw_table(screen, 450)
                                        screen.blit(losetext, losetext_rect)
                                        pygame.display.flip()
                                        done = True
                        cell = self.get_cell_from_mouse(pygame.mouse.get_pos(), 0)
                        if cell:
                            self.__clicked_cells = [[False] * 10 for _ in range(10)]
                            self.__clicked_cells[cell[0] - 1][cell[1] - 1] = True
                            playerguess = "" + chr(ord('A') - 1 + cell[1]) + str(cell[0])
            if not done:
                screen.fill((100, 100, 100))
                screen.blit(background_image, (0, 0))
                attackbutton.draw(screen)
                self.draw_table(screen, 0)
                self.draw_table(screen, 450)
                pygame.display.flip()
        pygame.quit()
