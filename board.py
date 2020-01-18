import random
import copy
class Board:


    def __init__(self,boardWidth, boardHeight,probability):
        self.boardSize = boardWidth*boardHeight
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.cellProbability = probability
        self.board = []
        self.boardScore = 0
        for i in range(0,boardHeight):
            line = []
            for j in range(0,boardWidth):
                line.append(0)
            self.board.append(line)

    def printBoard(self):
        for i in range(0,self.boardHeight):
            print(self.board[i])


    def tickBoard(self):
        newBoard = []
        currentScore = copy.copy(self.boardScore)
        y = self.boardHeight
        x = self.boardWidth
        for i in range(0,self.boardHeight):
            line = []
            for j in range(0,self.boardWidth):
                currentCell = self.board[i][j]
                adjacentCells = 0
                adjacentCells += self.board[(i-1)%y][(j-1) % x]
                adjacentCells += self.board[(i-1)%y][(j) % x]
                adjacentCells += self.board[(i-1)%y][(j+1) % x]
                adjacentCells += self.board[i%y][(j-1) % x]
               
                adjacentCells += self.board[i%y][(j+1) % x]
                adjacentCells += self.board[(i+1)%y][(j-1) % x]
                adjacentCells += self.board[(i+1)%y][(j) % x]
                adjacentCells += self.board[(i+1)%y][(j+1) % x]
                if (currentCell == 1 and adjacentCells<2):
                    line.append(0)
                elif(currentCell == 1 and  (adjacentCells== 2 or adjacentCells == 3)):
                    line.append(1)
                    self.boardScore +=1
                elif(currentCell == 1 and adjacentCells > 3):
                    line.append(0)
                elif(currentCell == 0 and adjacentCells == 3):
                    line.append(1)
                    self.boardScore +=1
                else:
                    line.append(0)
            newBoard.append(line)
        self.board = newBoard       
        if (currentScore == self.boardScore):
            return False
        else:
            return True


    def addBoard(self,board):
        self.board = board
        for i in range(0,self.boardHeight):
            for j in range(0,self.boardScore):
                if(self.board[i][j] == 1):
                    self.boardScore += 1
    
    def resetScore(self):
        self.boardScore = 0
        for i in range(0,self.boardHeight):
            for j in range(0,self.boardScore):
                if(self.board[i][j] == 1):
                    self.boardScore += 1        

    def updateScore(self,score):
        self.boardScore = score

    def randomBoard(self):
        self.board = []
        for i in range(0,self.boardHeight):
            line = []
            for j in range(0,self.boardWidth):
                if (random.random() < self.cellProbability):
                    line.append(1)
                    self.boardScore +=1
                else:
                    line.append(0)
            self.board.append(line)