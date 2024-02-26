from random import randint, choice
from termcolor import colored


def generateplanes(n):
    mat = [["_" for _ in range(10)] for _ in range(10)]
    planesrows = []
    planescolumns = []
    planeheadrows = []
    planeheadcolumns = []
    while n > 0:
        ok = 0
        row = randint(0, 9)
        col = randint(0, 9)
        direction = choice(["up", "down", "left", "right"])
        if n == 3:
            planecolor = "yellow"
        if n == 2:
            planecolor = "blue"
        if n == 1:
            planecolor = "red"
        if direction == "up":
            if row >= 3 and col >= 2 and col <= 7:
                for i in range(len(planesrows)):
                    if ((row == planesrows[i] and col == planescolumns[i]) or (
                            row - 1 == planesrows[i] and col == planescolumns[i])
                            or (row - 2 == planesrows[i] and col == planescolumns[i]) or (
                                    row - 3 == planesrows[i] and col == planescolumns[i])
                            or (row - 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col - 2 == planescolumns[i])
                            or (row - 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col + 2 == planescolumns[i])
                            or (row - 3 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row - 3 == planesrows[i] and col + 1 == planescolumns[i])):
                        ok = 1
                if ok == 0:
                    planeheadrows.append(row)
                    planeheadcolumns.append(col)
                    planesrows.append(row)
                    planescolumns.append(col)
                    mat[row][col] = "H"
                    # 2
                    planesrows.append(row - 1)
                    planescolumns.append(col)
                    mat[row - 1][col] = "X"
                    # 3
                    planesrows.append(row - 2)
                    planescolumns.append(col)
                    mat[row - 2][col] = "X"
                    # 4
                    planesrows.append(row - 3)
                    planescolumns.append(col)
                    mat[row - 3][col] = "X"
                    # 5
                    planesrows.append(row - 1)
                    planescolumns.append(col - 1)
                    mat[row - 1][col - 1] = "X"
                    # 6
                    planesrows.append(row - 1)
                    planescolumns.append(col - 2)
                    mat[row - 1][col - 2] = "X"
                    # 7
                    planesrows.append(row - 1)
                    planescolumns.append(col + 1)
                    mat[row - 1][col + 1] = "X"
                    # 8
                    planesrows.append(row - 1)
                    planescolumns.append(col + 2)
                    mat[row - 1][col + 2] = "X"
                    # 9
                    planesrows.append(row - 3)
                    planescolumns.append(col - 1)
                    mat[row - 3][col - 1] = "X"
                    # 10
                    planesrows.append(row - 3)
                    planescolumns.append(col + 1)
                    mat[row - 3][col + 1] = "X"
                    n = n - 1

        elif direction == "down":
            if row <= 5 and col >= 2 and col <= 7:
                for i in range(len(planesrows)):
                    if ((row == planesrows[i] and col == planescolumns[i]) or (
                            row + 1 == planesrows[i] and col == planescolumns[i])
                            or (row + 2 == planesrows[i] and col == planescolumns[i]) or (
                                    row + 3 == planesrows[i] and col == planescolumns[i])
                            or (row + 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row + 1 == planesrows[i] and col - 2 == planescolumns[i])
                            or (row + 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                    row + 1 == planesrows[i] and col + 2 == planescolumns[i])
                            or (row + 3 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row + 3 == planesrows[i] and col + 1 == planescolumns[i])):
                        ok = 1
                if ok == 0:
                    planeheadrows.append(row)
                    planeheadcolumns.append(col)
                    planesrows.append(row)
                    planescolumns.append(col)
                    mat[row][col] = "H"
                    # 2
                    planesrows.append(row + 1)
                    planescolumns.append(col)
                    mat[row + 1][col] = "X"
                    # 3
                    planesrows.append(row + 2)
                    planescolumns.append(col)
                    mat[row + 2][col] = "X"
                    # 4
                    planesrows.append(row + 3)
                    planescolumns.append(col)
                    mat[row + 3][col] = "X"
                    # 5
                    planesrows.append(row + 1)
                    planescolumns.append(col - 1)
                    mat[row + 1][col - 1] = "X"
                    # 6
                    planesrows.append(row + 1)
                    planescolumns.append(col - 2)
                    mat[row + 1][col - 2] = "X"
                    # 7
                    planesrows.append(row + 1)
                    planescolumns.append(col + 1)
                    mat[row + 1][col + 1] = "X"
                    # 8
                    planesrows.append(row + 1)
                    planescolumns.append(col + 2)
                    mat[row + 1][col + 2] = "X"
                    # 9
                    planesrows.append(row + 3)
                    planescolumns.append(col - 1)
                    mat[row + 3][col - 1] = "X"
                    # 10
                    planesrows.append(row + 3)
                    planescolumns.append(col + 1)
                    mat[row + 3][col + 1] = "X"
                    n = n - 1

        elif direction == "left":
            if col >= 3 and row >= 2 and row <= 7:
                for i in range(len(planesrows)):
                    if ((row == planesrows[i] and col == planescolumns[i]) or (
                            row == planesrows[i] and col - 1 == planescolumns[i])
                            or (row == planesrows[i] and col - 2 == planescolumns[i]) or (
                                    row == planesrows[i] and col - 3 == planescolumns[i])
                            or (row + 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col - 1 == planescolumns[i])
                            or (row + 2 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                    row - 2 == planesrows[i] and col - 1 == planescolumns[i])
                            or (row + 1 == planesrows[i] and col - 3 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col - 3 == planescolumns[i])):
                        ok = 1
                if ok == 0:
                    planeheadrows.append(row)
                    planeheadcolumns.append(col)
                    planesrows.append(row)
                    planescolumns.append(col)
                    mat[row][col] = "H"
                    # 2
                    planesrows.append(row)
                    planescolumns.append(col - 1)
                    mat[row][col - 1] = "X"
                    # 3
                    planesrows.append(row)
                    planescolumns.append(col - 2)
                    mat[row][col - 2] = "X"
                    # 4
                    planesrows.append(row)
                    planescolumns.append(col - 3)
                    mat[row][col - 3] = "X"
                    # 5
                    planesrows.append(row + 1)
                    planescolumns.append(col - 1)
                    mat[row + 1][col - 1] = "X"
                    # 6
                    planesrows.append(row - 1)
                    planescolumns.append(col - 1)
                    mat[row - 1][col - 1] = "X"
                    # 7
                    planesrows.append(row + 2)
                    planescolumns.append(col - 1)
                    mat[row + 2][col - 1] = "X"
                    # 8
                    planesrows.append(row - 2)
                    planescolumns.append(col - 1)
                    mat[row - 2][col - 1] = "X"
                    # 9
                    planesrows.append(row + 1)
                    planescolumns.append(col - 3)
                    mat[row + 1][col - 3] = "X"
                    # 10
                    planesrows.append(row - 1)
                    planescolumns.append(col - 3)
                    mat[row - 1][col - 3] = "X"
                    n = n - 1

        elif direction == "right":
            if col <= 6 and row >= 2 and row <= 7:
                for i in range(len(planesrows)):
                    if ((row == planesrows[i] and col == planescolumns[i]) or (
                            row == planesrows[i] and col + 1 == planescolumns[i])
                            or (row == planesrows[i] and col + 2 == planescolumns[i]) or (
                                    row == planesrows[i] and col + 3 == planescolumns[i])
                            or (row + 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col + 1 == planescolumns[i])
                            or (row + 2 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                    row - 2 == planesrows[i] and col + 1 == planescolumns[i])
                            or (row + 1 == planesrows[i] and col + 3 == planescolumns[i]) or (
                                    row - 1 == planesrows[i] and col + 3 == planescolumns[i])):
                        ok = 1
                if ok == 0:
                    planeheadrows.append(row)
                    planeheadcolumns.append(col)
                    planesrows.append(row)
                    planescolumns.append(col)
                    mat[row][col] = "H"
                    # 2
                    planesrows.append(row)
                    planescolumns.append(col + 1)
                    mat[row][col + 1] = "X"
                    # 3
                    planesrows.append(row)
                    planescolumns.append(col + 2)
                    mat[row][col + 2] = "X"
                    # 4
                    planesrows.append(row)
                    planescolumns.append(col + 3)
                    mat[row][col + 3] = "X"
                    # 5
                    planesrows.append(row + 1)
                    planescolumns.append(col + 1)
                    mat[row + 1][col + 1] = "X"
                    # 6
                    planesrows.append(row - 1)
                    planescolumns.append(col + 1)
                    mat[row - 1][col + 1] = "X"
                    # 7
                    planesrows.append(row + 2)
                    planescolumns.append(col + 1)
                    mat[row + 2][col + 1] = "X"
                    # 8
                    planesrows.append(row - 2)
                    planescolumns.append(col + 1)
                    mat[row - 2][col + 1] = "X"
                    # 9
                    planesrows.append(row + 1)
                    planescolumns.append(col + 3)
                    mat[row + 1][col + 3] = "X"
                    # 10
                    planesrows.append(row - 1)
                    planescolumns.append(col + 3)
                    mat[row - 1][col + 3] = "X"
                    n = n - 1
    return mat, planesrows, planescolumns, planeheadrows, planeheadcolumns


def chooseplanes(n, inp, directions):
    mat = [[" " for _ in range(10)] for _ in range(10)]
    planesrows = []
    planescolumns = []
    planeheadrows = []
    planeheadcolumns = []
    while n > 0:
        ok = 0
        try:
            row, col = process_player_input(inp[n - 1])
            direction = directions[n - 1]
            if direction not in ["up", "down", "left", "right"]:
                raise KeyError("Invalid Direction")
            if n == 3:
                planecolor = "yellow"
            if n == 2:
                planecolor = "blue"
            if n == 1:
                planecolor = "red"
            if direction == "up":
                if row >= 3 and col >= 2 and col <= 7:
                    for i in range(len(planesrows)):
                        if ((row == planesrows[i] and col == planescolumns[i]) or (
                                row - 1 == planesrows[i] and col == planescolumns[i])
                                or (row - 2 == planesrows[i] and col == planescolumns[i]) or (
                                        row - 3 == planesrows[i] and col == planescolumns[i])
                                or (row - 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col - 2 == planescolumns[i])
                                or (row - 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col + 2 == planescolumns[i])
                                or (row - 3 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row - 3 == planesrows[i] and col + 1 == planescolumns[i])):
                            ok = 1
                    if ok == 0:
                        planeheadrows.append(row)
                        planeheadcolumns.append(col)
                        planesrows.append(row)
                        planescolumns.append(col)
                        mat[row][col] = "H"
                        # 2
                        planesrows.append(row - 1)
                        planescolumns.append(col)
                        mat[row - 1][col] = "X"
                        # 3
                        planesrows.append(row - 2)
                        planescolumns.append(col)
                        mat[row - 2][col] = "X"
                        # 4
                        planesrows.append(row - 3)
                        planescolumns.append(col)
                        mat[row - 3][col] = "X"
                        # 5
                        planesrows.append(row - 1)
                        planescolumns.append(col - 1)
                        mat[row - 1][col - 1] = "X"
                        # 6
                        planesrows.append(row - 1)
                        planescolumns.append(col - 2)
                        mat[row - 1][col - 2] = "X"
                        # 7
                        planesrows.append(row - 1)
                        planescolumns.append(col + 1)
                        mat[row - 1][col + 1] = "X"
                        # 8
                        planesrows.append(row - 1)
                        planescolumns.append(col + 2)
                        mat[row - 1][col + 2] = "X"
                        # 9
                        planesrows.append(row - 3)
                        planescolumns.append(col - 1)
                        mat[row - 3][col - 1] = "X"
                        # 10
                        planesrows.append(row - 3)
                        planescolumns.append(col + 1)
                        mat[row - 3][col + 1] = "X"
                        n = n - 1

            elif direction == "down":
                if row <= 5 and col >= 2 and col <= 7:
                    for i in range(len(planesrows)):
                        if ((row == planesrows[i] and col == planescolumns[i]) or (
                                row + 1 == planesrows[i] and col == planescolumns[i])
                                or (row + 2 == planesrows[i] and col == planescolumns[i]) or (
                                        row + 3 == planesrows[i] and col == planescolumns[i])
                                or (row + 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row + 1 == planesrows[i] and col - 2 == planescolumns[i])
                                or (row + 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                        row + 1 == planesrows[i] and col + 2 == planescolumns[i])
                                or (row + 3 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row + 3 == planesrows[i] and col + 1 == planescolumns[i])):
                            ok = 1
                    if ok == 0:
                        planeheadrows.append(row)
                        planeheadcolumns.append(col)
                        planesrows.append(row)
                        planescolumns.append(col)
                        mat[row][col] = "H"
                        # 2
                        planesrows.append(row + 1)
                        planescolumns.append(col)
                        mat[row + 1][col] = "X"
                        # 3
                        planesrows.append(row + 2)
                        planescolumns.append(col)
                        mat[row + 2][col] = "X"
                        # 4
                        planesrows.append(row + 3)
                        planescolumns.append(col)
                        mat[row + 3][col] = "X"
                        # 5
                        planesrows.append(row + 1)
                        planescolumns.append(col - 1)
                        mat[row + 1][col - 1] = "X"
                        # 6
                        planesrows.append(row + 1)
                        planescolumns.append(col - 2)
                        mat[row + 1][col - 2] = "X"
                        # 7
                        planesrows.append(row + 1)
                        planescolumns.append(col + 1)
                        mat[row + 1][col + 1] = "X"
                        # 8
                        planesrows.append(row + 1)
                        planescolumns.append(col + 2)
                        mat[row + 1][col + 2] = "X"
                        # 9
                        planesrows.append(row + 3)
                        planescolumns.append(col - 1)
                        mat[row + 3][col - 1] = "X"
                        # 10
                        planesrows.append(row + 3)
                        planescolumns.append(col + 1)
                        mat[row + 3][col + 1] = "X"
                        n = n - 1

            elif direction == "left":
                if col >= 3 and row >= 2 and row <= 7:
                    for i in range(len(planesrows)):
                        if ((row == planesrows[i] and col == planescolumns[i]) or (
                                row == planesrows[i] and col - 1 == planescolumns[i])
                                or (row == planesrows[i] and col - 2 == planescolumns[i]) or (
                                        row == planesrows[i] and col - 3 == planescolumns[i])
                                or (row + 1 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col - 1 == planescolumns[i])
                                or (row + 2 == planesrows[i] and col - 1 == planescolumns[i]) or (
                                        row - 2 == planesrows[i] and col - 1 == planescolumns[i])
                                or (row + 1 == planesrows[i] and col - 3 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col - 3 == planescolumns[i])):
                            ok = 1
                    if ok == 0:
                        planeheadrows.append(row)
                        planeheadcolumns.append(col)
                        planesrows.append(row)
                        planescolumns.append(col)
                        mat[row][col] = "H"
                        # 2
                        planesrows.append(row)
                        planescolumns.append(col - 1)
                        mat[row][col - 1] = "X"
                        # 3
                        planesrows.append(row)
                        planescolumns.append(col - 2)
                        mat[row][col - 2] = "X"
                        # 4
                        planesrows.append(row)
                        planescolumns.append(col - 3)
                        mat[row][col - 3] = "X"
                        # 5
                        planesrows.append(row + 1)
                        planescolumns.append(col - 1)
                        mat[row + 1][col - 1] = "X"
                        # 6
                        planesrows.append(row - 1)
                        planescolumns.append(col - 1)
                        mat[row - 1][col - 1] = "X"
                        # 7
                        planesrows.append(row + 2)
                        planescolumns.append(col - 1)
                        mat[row + 2][col - 1] = "X"
                        # 8
                        planesrows.append(row - 2)
                        planescolumns.append(col - 1)
                        mat[row - 2][col - 1] = "X"
                        # 9
                        planesrows.append(row + 1)
                        planescolumns.append(col - 3)
                        mat[row + 1][col - 3] = "X"
                        # 10
                        planesrows.append(row - 1)
                        planescolumns.append(col - 3)
                        mat[row - 1][col - 3] = "X"
                        n = n - 1

            elif direction == "right":
                if col <= 6 and row >= 2 and row <= 7:
                    for i in range(len(planesrows)):
                        if ((row == planesrows[i] and col == planescolumns[i]) or (
                                row == planesrows[i] and col + 1 == planescolumns[i])
                                or (row == planesrows[i] and col + 2 == planescolumns[i]) or (
                                        row == planesrows[i] and col + 3 == planescolumns[i])
                                or (row + 1 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col + 1 == planescolumns[i])
                                or (row + 2 == planesrows[i] and col + 1 == planescolumns[i]) or (
                                        row - 2 == planesrows[i] and col + 1 == planescolumns[i])
                                or (row + 1 == planesrows[i] and col + 3 == planescolumns[i]) or (
                                        row - 1 == planesrows[i] and col + 3 == planescolumns[i])):
                            ok = 1
                    if ok == 0:
                        planeheadrows.append(row)
                        planeheadcolumns.append(col)
                        planesrows.append(row)
                        planescolumns.append(col)
                        mat[row][col] = "H"
                        # 2
                        planesrows.append(row)
                        planescolumns.append(col + 1)
                        mat[row][col + 1] = "X"
                        # 3
                        planesrows.append(row)
                        planescolumns.append(col + 2)
                        mat[row][col + 2] = "X"
                        # 4
                        planesrows.append(row)
                        planescolumns.append(col + 3)
                        mat[row][col + 3] = "X"
                        # 5
                        planesrows.append(row + 1)
                        planescolumns.append(col + 1)
                        mat[row + 1][col + 1] = "X"
                        # 6
                        planesrows.append(row - 1)
                        planescolumns.append(col + 1)
                        mat[row - 1][col + 1] = "X"
                        # 7
                        planesrows.append(row + 2)
                        planescolumns.append(col + 1)
                        mat[row + 2][col + 1] = "X"
                        # 8
                        planesrows.append(row - 2)
                        planescolumns.append(col + 1)
                        mat[row - 2][col + 1] = "X"
                        # 9
                        planesrows.append(row + 1)
                        planescolumns.append(col + 3)
                        mat[row + 1][col + 3] = "X"
                        # 10
                        planesrows.append(row - 1)
                        planescolumns.append(col + 3)
                        mat[row - 1][col + 3] = "X"
                        n = n - 1
        except KeyError as ke:
            print(ke)
    return mat, planesrows, planescolumns, planeheadrows, planeheadcolumns


def process_player_input(inp):
    v = []
    for i in inp:
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
    if v[0] == 'A':
        col = 0
    if v[0] == 'B':
        col = 1
    if v[0] == 'C':
        col = 2
    if v[0] == 'D':
        col = 3
    if v[0] == 'E':
        col = 4
    if v[0] == 'F':
        col = 5
    if v[0] == 'G':
        col = 6
    if v[0] == 'H':
        col = 7
    if v[0] == 'I':
        col = 8
    if v[0] == 'J':
        col = 9
    if len(v) == 2:
        row = int(v[1]) - 1
    else:
        row = 9
    return row, col
