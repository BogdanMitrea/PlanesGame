from generateplanes import generateplanes, chooseplanes
from termcolor import colored
import pygame


class GameWonException(Exception):
    pass


class GameLostException(Exception):
    pass


class Sketchboard:
    def __init__(self):
        self.__sketchboard = [[" " for _ in range(10)] for _ in range(10)]

    def setsymbol(self, row, col, symbol):
        """

        :param row: the row where a new symbol should be placed
        :param col: the column where a new symbol should be placed
        :param symbol: an x
        :return: puts x where the player has guessed
        """
        self.__sketchboard[row][col] = symbol

    def getsymbol(self, row, col):
        """

        :param row:
        :param col:
        :return: returns the symbol of a square or None if there is not any
        """
        if self.__sketchboard[row][col] == " ":
            return None
        return self.__sketchboard[row][col]

    def __str__(self):
        """

        :return:prints a sketchboard which is an empty board completed by the guesses of the user with the role of
        helping the user better visualize where ai planes might be
        """
        result = ""
        gb = self.__sketchboard
        result += '   | A | B | C | D | E | F | G | H | I | J\n'
        result += '---+---+---+---+---+---+---+---+---+---+---\n'
        for row in range(9):
            result += " " + str(row + 1) + " | " + gb[row][0] + " | " + gb[row][1] + " | " + gb[row][2] + " | " + \
                      gb[row][
                          3] + " | " + gb[row][4] + \
                      " | " + gb[row][5] + " | " + gb[row][6] + " | " + gb[row][7] + " | " + gb[row][8] + " | " + \
                      gb[row][9] + "\n"
            result += '---+---+---+---+---+---+---+---+---+---\n'
        result += "10" + " | " + gb[9][0] + " | " + gb[9][1] + " | " + gb[9][2] + " | " + gb[9][3] + " | " + gb[9][
            4] + " | " + gb[9][
                      5] + \
                  " | " + gb[9][6] + " | " + gb[9][7] + " | " + gb[9][8] + " | " + gb[9][9] + "\n"
        return result


class Board:
    def __init__(self, userchoice, sketchboard: Sketchboard, coordinates=None, directions=None):
        if userchoice == 1:
            self.__board, self.__planesrows, self.__planescolumns, self.__planeheadrows, self.__planeheadcolumns = generateplanes(
                3)
        if userchoice == 2:
            self.__board, self.__planesrows, self.__planescolumns, self.__planeheadrows, self.__planeheadcolumns = chooseplanes(
                3, coordinates, directions)
        self.__copyheadcoordinates = []
        for i in range(3):
            self.__copyheadcoordinates.append((self.__planeheadrows[i], self.__planeheadcolumns[i]))
        self.__nrofplanes = 3
        self.__sketchboard = sketchboard
        self.__lastguess = "air"
        self.__lastguessrow = 0
        self.__lastguesscol = 0

    def playerguess(self, row, col):
        """
        The function  checks if a plane was hit by matching the given coordinates with the ones saved for planerows and
        planecolumns and if it hits the head of a plane the entire plane gets deleted so that the next guesses will not
         print that a new plane was hit
        :param row: a digit from 0 to 9
        :param col: a digit from 0 to 9

        It will print a message depending if a plane was hit or not or if the game is over
        """
        for i in range(len(self.__planeheadrows) - 1, -1, -1):
            if row == self.__planeheadrows[i] and col == self.__planeheadcolumns[i]:
                self.__nrofplanes -= 1
                pos = 0
                for j in range(len(self.__planesrows)):
                    if self.__planeheadrows[i] == self.__planesrows[j] and self.__planeheadcolumns[i] == \
                            self.__planescolumns[j]:
                        pos = j
                # for k in range(pos+1,pos+10):
                # self.__sketchboard.setsymbol(self.__planesrows[k], self.__planescolumns[k], colored("x", "yellow"))
                del self.__planesrows[pos:pos + 10]
                del self.__planescolumns[pos:pos + 10]

                del self.__planeheadrows[i]
                del self.__planeheadcolumns[i]
                if self.__sketchboard.getsymbol(row, col) is None:
                    self.__sketchboard.setsymbol(row, col, colored("x", "red"))
                # print("Head hit! You destroyed an enemy plane! ", self.__nrofplanes, " remaining")
                if self.__nrofplanes == 0:
                    raise GameWonException()
                return 3

        for i in range(len(self.__planesrows)):
            if row == self.__planesrows[i] and col == self.__planescolumns[i]:
                if self.__sketchboard.getsymbol(row, col) is None:
                    self.__sketchboard.setsymbol(row, col, colored("x", "yellow"))
                #print("You have hit the enemy plane! Not a head hit though.")
                self.__lastguess = "hit"
                self.__lastguessrow = row
                self.__lastguesscol = col
                return 2

        self.__lastguess = "air"
        self.__lastguessrow = row
        self.__lastguesscol = col
        if self.__sketchboard.getsymbol(row, col) is None:
            self.__sketchboard.setsymbol(row, col, colored("x", "blue"))
        #print("Nothing but air.\n")
        return 1

    def aiguess(self, row, col):
        """
        The function takes the generated numbers representing the row and the column and prints them and checks if a
        plane was hit by matching the coordinates with the ones saved for planerows and planecolumns and if it hits the
        head of a plane the entire plane gets deleted so that the next guesses will not print that a new plane was hit
        :param row: a digit from 0 to 9
        :param col: a digit from 0 to 9
        It will print a message depending if a plane was hit or not or if the game is over
        """
        rownumber, letter = interpretnumbers(row, col)
        # print("The computer played ", str(letter) + str(rownumber))

        for i in range(len(self.__planeheadrows) - 1, -1, -1):
            if row == self.__planeheadrows[i] and col == self.__planeheadcolumns[i]:
                self.__nrofplanes -= 1
                pos = 0
                for j in range(len(self.__planesrows)):
                    if self.__planeheadrows[i] == self.__planesrows[j] and self.__planeheadcolumns[i] == \
                            self.__planescolumns[j]:
                        pos = j
                del self.__planesrows[pos:pos + 10]
                del self.__planescolumns[pos:pos + 10]

                del self.__planeheadrows[i]
                del self.__planeheadcolumns[i]
                # print("Head hit! Your plane was destroyed, you have ", self.__nrofplanes, " remaining\n")
                self.__lastguess = "air"
                if self.__nrofplanes == 0:
                    raise GameLostException()
                return 3
        for i in range(len(self.__planesrows)):
            if row == self.__planesrows[i] and col == self.__planescolumns[i]:
                #print("Your plane was hit!\n")
                self.__lastguess = "hit"
                self.__lastguessrow = row
                self.__lastguesscol = col
                return 2
        #print("Nothing but air.\n")
        return 1

    def getplanerowsandcols(self):
        """

        :return: all the coordiantes where planes are, used for testing
        """
        return self.__planesrows, self.__planescolumns

    def getheadsrowsandcols(self):
        """

        :return: all the coordiantes where planes are, used for testing
        """
        return self.__planeheadrows, self.__planeheadcolumns

    def getcopycoordinates(self):
        return self.__copyheadcoordinates

    def setlastguessair(self):
        """

        :return: sets the last guess to air so that a new random move can be played
        """
        self.__lastguess = "air"

    def getlastguess(self):
        """

        :return: returns the type of the last guess either air or hit and the row and the column of the last guess
        """
        return self.__lastguess, self.__lastguessrow, self.__lastguesscol

    def getsketchboard(self):
        """

        :return:prints the sketchboard which is board that shows every player guess
        """
        print(self.__sketchboard)

    def __str__(self):
        """

        :return: the board printed in the form of a table
        """
        result = ""
        gb = self.__board
        result += '     | A | B | C | D | E | F | G | H | I | J\n'
        result += '---+---+---+---+--+---+--+---+--+--+--\n'
        for row in range(9):
            result += str(row + 1) + "   | " + gb[row][0] + " | " + gb[row][1] + " | " + gb[row][2] + " | " + \
                      gb[row][
                          3] + " | " + gb[row][4] + \
                      " | " + gb[row][5] + " | " + gb[row][6] + " | " + gb[row][7] + " | " + gb[row][8] + " | " + \
                      gb[row][9] + "\n"
            result += '---+---+---+---+--+---+--+---+--+--+--\n'
        result += "10" + " | " + gb[9][0] + " | " + gb[9][1] + " | " + gb[9][2] + " | " + gb[9][3] + " | " + gb[9][
            4] + " | " + gb[9][
                      5] + \
                  " | " + gb[9][6] + " | " + gb[9][7] + " | " + gb[9][8] + " | " + gb[9][9] + "\n"
        return result


def interpretnumbers(a, b):
    """
    :param a,b: two numbers from 0 to 9
    :return: the corresponding combination of letter and number of the digits a and b
    """
    col = 0
    row = a + 1
    col = chr(b + ord('A'))
    return row, col
