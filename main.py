import gameoflife

boardHeight = 25
boardWidth =25
originalProbability = 0.5

game = gameoflife.GameOfLife(boardWidth,boardHeight)

board = game.geneticAlgorithm()