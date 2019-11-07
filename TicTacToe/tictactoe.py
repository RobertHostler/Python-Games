import random
import time


class Grid:
    def __init__(self):
        self.matrix = [
            ["", "", ""],
            ["", "", ""], 
            ["", "", ""]
        ]

    def __str__(self):
        string = "\n"
        for row in self.matrix:
            for column in row:
                if column == "":
                    string += "_ "
                else:
                    string += column + " "
            string += "\n"
        return string

    def update(self, x, y, xo):
        if xo == "X":
            self.matrix[y - 1][x - 1] = "X"
            print(self)
        elif xo == "O":
            self.matrix[y - 1][x - 1] = "O"
            print(self)

    def possibleMoves(self):
        # this function is only meant to be used by the CPU
        availableMoves = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == "":
                    availableMoves.append((j + 1, i + 1))
        return availableMoves

    @staticmethod
    def rowWin(mat):
        highPriorityMoves = []
        mediumPriorityMoves = []

        for i in range(len(mat)):
            row = mat[i]
            cpucount = 0
            playercount = 0
            emptycount = 0

            for char in row:
                if char == "X":
                    playercount += 1
                elif char == "O":
                    cpucount += 1
                elif char == "":
                    emptycount += 1
            if cpucount == 2 and emptycount == 1:
                # high priority move
                for j in range(len(row)):
                    if row[j] == "":
                        highPriorityMoves.append((j + 1, i + 1))
            elif playercount == 2 and emptycount == 1:
                # medium priority move
                for j in range(len(row)):
                    if row[j] == "":
                        mediumPriorityMoves.append((j + 1, i + 1))

        return (highPriorityMoves, mediumPriorityMoves)

    @staticmethod
    def columnWin(mat):
        highPriorityMoves = []
        mediumPriorityMoves = []

        for j in range(len(mat)):
            column = []
            for i in range(len(mat[0])):
                column.append(mat[i][j])

            cpucount = 0
            playercount = 0
            emptycount = 0

            for char in column:
                if char == "X":
                    playercount += 1
                elif char == "O":
                    cpucount += 1
                elif char == "":
                    emptycount += 1
            
            if cpucount == 2 and emptycount == 1:
                for i in range(len(column)):
                    if column[i] == "":
                        highPriorityMoves.append((j + 1, i + 1))
            elif playercount == 2 and emptycount == 1:
                for i in range(len(column)):
                    if column[i] == "":
                        mediumPriorityMoves.append((j + 1, i + 1))

        return (highPriorityMoves, mediumPriorityMoves)

    @staticmethod
    def downDiagonalWin(mat):
        downDiagonal = [mat[0][0], mat[1][1], mat[2][2]]
        highPriorityMoves = []
        mediumPriorityMoves = []

        cpucount = 0
        playercount = 0
        emptycount = 0
        for char in downDiagonal:
            if char == "X":
                playercount += 1
            elif char == "O":
                cpucount += 1
            else:
                emptycount += 1
        if cpucount == 2 and emptycount == 1:
            # high priority move
            for i in range(len(downDiagonal)):
                if downDiagonal[i] == "":
                    highPriorityMoves.append((i + 1, i + 1))
        elif playercount == 2 and emptycount == 1:
            # medium priority move
            for i in range(len(downDiagonal)):
                if downDiagonal[i] == "":
                    mediumPriorityMoves.append((i + 1, i + 1))
        
        return (highPriorityMoves, mediumPriorityMoves)

    @staticmethod
    def upDiagonalWin(mat):
        upDiagonal = [mat[2][0], mat[1][1], mat[0][2]]
        highPriorityMoves = []
        mediumPriorityMoves = []

        cpucount = 0
        playercount = 0
        emptycount = 0
        for char in upDiagonal:
            if char == "X":
                playercount += 1
            elif char == "O":
                cpucount += 1
            else:
                emptycount += 1
        if cpucount == 2 and emptycount == 1:
            # high priority move
            for i in range(len(upDiagonal)):
                if upDiagonal[i] == "":
                    highPriorityMoves.append((i + 1, 3 - i ))
        elif playercount == 2 and emptycount == 1:
            # medium priority move
            for i in range(len(upDiagonal)):
                if upDiagonal[i] == "":
                    mediumPriorityMoves.append((i + 1, 3 - i ))

        return (highPriorityMoves, mediumPriorityMoves)


class Player:
    def __init__(self, name="CPU"):
        self.name = name
        print(self.name + " has been initialized\n")

    @staticmethod
    def easyCPUmove(grid):
        # randomly select an available move

        availableMoves = grid.possibleMoves()
        CPUmove = random.choice(availableMoves)
        print(availableMoves)
        print("CPU's [EASY] move is ", CPUmove)
        return CPUmove

    @staticmethod
    def mediumCPUmove(grid):
        # employ a little more reasoning in the tic tac toe algorithm but still a little chance
        availableMoves = grid.possibleMoves()
        highPriorityMoves = []
        mediumPriorityMoves = []

        rowWins = Grid.rowWin(grid.matrix)
        highPriorityMoves.extend(rowWins[0])
        mediumPriorityMoves.extend(rowWins[1])

        columnWins = Grid.columnWin(grid.matrix)
        highPriorityMoves.extend(columnWins[0])
        mediumPriorityMoves.extend(columnWins[1])

        downDiagonalWins = Grid.downDiagonalWin(grid.matrix)
        highPriorityMoves.extend(downDiagonalWins[0])
        mediumPriorityMoves.extend(downDiagonalWins[1])

        upDiagonalWins = Grid.upDiagonalWin(grid.matrix)
        highPriorityMoves.extend(upDiagonalWins[0])
        mediumPriorityMoves.extend(upDiagonalWins[1])

        if highPriorityMoves != []:
            CPUmove = random.choice(highPriorityMoves)
        elif mediumPriorityMoves != []:
            CPUmove = random.choice(mediumPriorityMoves)
        else:
            CPUmove = random.choice(availableMoves)

        print("High priority moves: ", highPriorityMoves)
        print("Medium priority moves: ", mediumPriorityMoves)
        print("All available moves: ", availableMoves)
        print("CPU's [MEDIUM] move is ", CPUmove)
        return CPUmove

    @staticmethod
    def hardCPUmove(grid):
        print("CPU's [HARD] move is: ", (1, 1))
        return (1, 1)


class Game:
    def __init__(self, P1, P2):
        self.CPUlevel = 0

        if (P1.name == "CPU" and P2.name != "CPU") or (P1.name != "CPU" and P2.name == "CPU"):
            self.CPUlevel = int(input("Enter the CPU difficulty level, from 1 to 3: "))
        elif P1.name == "CPU" and P2.name == "CPU":
            print("There can only be one CPU player.")
            exit()

        self.P1 = P1
        self.P2 = P2
        self.grid = Grid()
        self.moveNumber = 1

    def play(self):
        while self.moveNumber < 10:
            if self.moveNumber % 2 == 0:
                currentPlayer = self.P2
                print("move {}: {}'s move (You are O)".format(
                    self.moveNumber, self.P2.name
                ))
                xo = "O"
            else:
                currentPlayer = self.P1
                print("move {}: {}'s move (You are X)".format(
                    self.moveNumber, self.P1.name
                ))
                xo = "X"

            if currentPlayer.name == "CPU":
                time.sleep(3)
                if self.CPUlevel == 1:
                    coordinates = Player.easyCPUmove(self.grid)
                elif self.CPUlevel == 2:
                    coordinates = Player.mediumCPUmove(self.grid)
                else:
                    coordinates = Player.hardCPUmove(self.grid)
            else:
                Rawx = input("X coordinate: ")
                Rawy = input("Y coordinate: ")
                coordinates = self.sanitizeinput(Rawx, Rawy)

            if coordinates != (0, 0):
                self.moveNumber += 1
                self.grid.update(coordinates[0], coordinates[1], xo)
                self.checkVictory()
            else:
                print("Try that move again.")

        print("Draw!")

    def sanitizeinput(self, rawinputX, rawinputY):
        x, y = 0, 0
        inputX = rawinputX.strip()
        inputY = rawinputY.strip()

        if inputX == "1" or inputX == "2" or inputX == "3":
            x = int(inputX)
        else:
            print("Can you even count? That is not a valid X-coordinate in this game.")
            return (0, 0)

        if inputY == "1" or inputY == "2" or inputY == "3":
            y = int(inputY)
        else:
            print("Can you even count? That is not a valid Y-coordinate in this game.")
            return (0, 0)

        if self.grid.matrix[y - 1][x - 1] != "":
            print("\nAre you retarded? You cannot change a previous move, you cheater.")
            return (0, 0)
        else:
            return (x, y)

    def checkVictory(self):
        winningCharacter = ""

        for i in range(len(self.grid.matrix)):
            if self.grid.matrix[i][0] == self.grid.matrix[i][1] == self.grid.matrix[i][2] != "":
                print("Row - based victory!")
                winningCharacter = self.grid.matrix[i][0]

        for j in range(len(self.grid.matrix[0])):
            if self.grid.matrix[0][j] == self.grid.matrix[1][j] == self.grid.matrix[2][j] != "":
                print("Column - based victory!")
                winningCharacter = self.grid.matrix[0][j]

        if self.grid.matrix[0][0] == self.grid.matrix[1][1] == self.grid.matrix[2][2] != "":
            print("Descending diagonal based victory!")
            winningCharacter = self.grid.matrix[0][0]
        elif self.grid.matrix[2][0] == self.grid.matrix[1][1] == self.grid.matrix[0][2] != "":
            print("Ascending - diagonal based victory!")
            winningCharacter = self.grid.matrix[2][0]

        if winningCharacter == "X":
            print(self.P1.name + " is the winner!")
            print(self.grid)
            exit()
        elif winningCharacter == "O":
            print(self.P2.name + " is the winner!")
            print(self.grid)
            exit()


def main():
    name1 = input("Enter a name for player 1: ")
    P1 = Player(name1)

    # we can always assume that the cpu will be player 2.

    singlePlayer = input("Do you want to play against the CPU? [y/n]")
    if singlePlayer == "y":
        P2 = Player()
    elif singlePlayer == "n":
        name2 = input("Enter a name for player 2: ")
        P2 = Player(name2)
    else:
        print("Your choice is unclear.")
        exit()

    game = Game(P1, P2)
    game.play()
    

if __name__ == "__main__":
    main()