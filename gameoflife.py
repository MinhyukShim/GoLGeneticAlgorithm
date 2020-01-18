import random
import math
import board
import copy

class GameOfLife:
    
    def __init__(self,boardWidth, boardHeight):
        self.boardSize = boardWidth*boardHeight
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight




    def addMember(self,cellProbability):
        newBoard = board.Board(self.boardWidth,self.boardHeight,cellProbability)
        newBoard.randomBoard()
        return newBoard

    def sortFirst(self,val):
	    return val[0]

    def createBasePopulation(self, populationSize):
        boards = []
        for i in range(0,populationSize):
            probability = random.random() 
            boards.append(self.addMember(probability))
        return boards



    def scorePopulation(self,populationSize,boards,numberOfCellIterations):
        scoresBoard = []
        for i in range(0,populationSize):
            originalBoard = copy.copy(boards[i])
            for j in range(0,numberOfCellIterations):
                if(not boards[i].tickBoard()):
                    break
                   
            score = boards[i].boardScore
            originalBoard.updateScore(score)
            scoresBoard.append([score,originalBoard])
            
        scoresBoard.sort(key = self.sortFirst, reverse = True)
        return scoresBoard


    def chooseBoard(self,populationSize):
        return int(random.triangular(0,int(populationSize),0))

    def crossOver(self, boardA, boardB):
        newBoard = board.Board(self.boardWidth,self.boardHeight,0)
        offspring = []
        totalScore= boardA.boardScore + boardB.boardScore

        for i in range(0,self.boardHeight):
            line = []
            for j in range(0,self.boardWidth):
                mate = random.randint(0,totalScore)
                if(mate < boardA.boardScore):
                    line.append(boardA.board[i][j])
                else: 
                    line.append(boardB.board[i][j])
            offspring.append(line)
        newBoard.addBoard(offspring)
        return newBoard

    def mutate(self, givenBoard, mutationProbability):
        newBoard = board.Board(self.boardWidth,self.boardHeight,0)
        tempBoard = []
        for i in range(0,self.boardHeight):
            line = []
            for j in range(0,self.boardWidth):
                if(random.random() <mutationProbability):
                    if(givenBoard.board[i][j] == 1):
                        line.append(0)
                    else:
                        line.append(1)
                else:
                    line.append(givenBoard.board[i][j])
            tempBoard.append(line)
        newBoard.addBoard(tempBoard)    
        return newBoard

    def resetAllScores(self,population,populationSize):
        for i in range(0,populationSize):
            population[i].resetScore()
        return population
    def geneticAlgorithm(self):
        
        numberOfGenerations = 100
        generationIncrement = 1
        populationSize = 50
        numberOfCellIterations = 500
        iterationIncrement = 10
        numberOfCouples = 25
        numberToKeep = 3

        mutationProbability = 0.02
        generationalBestBoard =board.Board(self.boardWidth,self.boardHeight,0)
        generationalBestScore =0
        population = self.createBasePopulation(populationSize)
        population = self.resetAllScores(population,populationSize)
        for i in range(0,numberOfGenerations):

                
            newPopulation = []

            popScores = []

            popScores = self.scorePopulation(populationSize,population,numberOfCellIterations)
            best = popScores[0]
            median = popScores[int(populationSize/2) -1]
            worst = popScores[populationSize-1]

            if(i%generationIncrement == 0):
                print("")
                print("Generation: " + str(i))
                print("Best for current generation: " + str(best[0]))
                print("Median for current generation: " + str(median[0]))
                print("Worst for current generation: " + str(worst[0]))
                best[1].printBoard()

            if(generationalBestScore < best[0]):
                print("New best board:")
                generationalBestBoard = best[1]
                generationalBestScore = best[0]

                #print("Score: " + str(best[0]))

            #breed offspring 
            for j in range(0,numberOfCouples):
                offspring = self.crossOver(popScores[self.chooseBoard(populationSize)][1],popScores[self.chooseBoard(populationSize)][1])
                newPopulation.append(offspring)


            #mutate
            for j in range(numberToKeep,numberOfCouples):
                newPopulation[j] = self.mutate(newPopulation[j], mutationProbability)

            #keep best board
            for j in range(0,numberToKeep):
                newPopulation.append(popScores[j][1])
            #add new boards
            while len(newPopulation) < populationSize:
                newPopulation.append(self.addMember(random.random()))

            newPopulation = self.resetAllScores(newPopulation,populationSize)
            population = newPopulation

            