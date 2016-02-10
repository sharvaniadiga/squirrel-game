'''
Created on Jan 29, 2016

@author: sharvani
'''

import sys

import Square
import constants
import SquarePosition
import TreeNode
import PlayerAlgorithm

if __name__ == '__main__':
    pass

#field = [[ Square.Square() for i in range(constants.NUMBER_OF_SQUARES)] for j in range(constants.NUMBER_OF_SQUARES)]

traversalLogString = constants.NULL_STRING

#functions definition
def initializeFieldValues(lines, algorithmToBeUsed):
    if (algorithmToBeUsed != constants.BATTLE_SIMULATION): 
        boardValueStartIndex = constants.INPUT_FILE_BOARD_VALUE_START
        boardCurrentStateStartIndex = constants.INPUT_FILE_CURRENT_STATE_START
    else:
        boardValueStartIndex = constants.BATTLE_SIMULATION_BOARD_VALUE_START_INDEX
        boardCurrentStateStartIndex = constants.BATTLE_SIMULATION_BOARD_STATE_START_INDEX
    field = [[ Square.Square() for i in range(constants.NUMBER_OF_SQUARES)] for j in range(constants.NUMBER_OF_SQUARES)]
    for i in range(boardValueStartIndex, boardValueStartIndex + constants.NUMBER_OF_SQUARES):
        line = lines[i].split()
        for j in range(0, len(line)):
            field[i - boardValueStartIndex][j].setYeildOfNuts(int(line[j]))
    for i in range(boardCurrentStateStartIndex, boardCurrentStateStartIndex + constants.NUMBER_OF_SQUARES):
        for j in range(0, len(lines[i])):
            field[i - boardCurrentStateStartIndex][j].setOccupiedBy(lines[i][j])
    return field

def evaluationFunction(currentField, player):
    currentBoardSumPlayerX = 0
    currentBoardSumPlayerO = 0
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if (currentField[i][j].getOccupiedBy() == constants.PLAYER_X):
                currentBoardSumPlayerX += currentField[i][j].getYeildOfNuts()
            elif (currentField[i][j].getOccupiedBy() == constants.PLAYER_O):
                currentBoardSumPlayerO += currentField[i][j].getYeildOfNuts()
    evalFunctionValue = 0
    if(player == constants.PLAYER_X):
        evalFunctionValue = currentBoardSumPlayerX - currentBoardSumPlayerO
    else:
        evalFunctionValue = currentBoardSumPlayerO - currentBoardSumPlayerX
    return evalFunctionValue

def copyField(currentField):
    fieldClone = [[ Square.Square() for i in range(constants.NUMBER_OF_SQUARES)] for j in range(constants.NUMBER_OF_SQUARES)]
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            fieldClone[i][j].setOccupiedBy(currentField[i][j].getOccupiedBy())
            fieldClone[i][j].setYeildOfNuts(currentField[i][j].getYeildOfNuts())
    return fieldClone

def getOpponentPlayer(currentPlayer):
    opponentPlayer = constants.NULL_STRING
    if(currentPlayer == constants.PLAYER_X):
        opponentPlayer = constants.PLAYER_O
    elif (currentPlayer == constants.PLAYER_O):
        opponentPlayer = constants.PLAYER_X
    return opponentPlayer
    
def acquireOrResetNeighboringSquaresAfterRaid(currentField, i, j, player, action):
    otherPlayer = getOpponentPlayer(player)
    neighboringSquares = getAcquiredNeighboringSquares(currentField, i, j, otherPlayer)
    for k in range(0, len(neighboringSquares)):
        square = neighboringSquares[k]
        if( action == constants.ACQUIRE):
            currentField[square.getPositionX()][square.getPositionY()].setOccupiedBy(player)
        elif( action == constants.RESET):
            currentField[square.getPositionX()][square.getPositionY()].setOccupiedBy(otherPlayer)
        
def isRaid(currentField, i, j, player):
    if (((i - 1) >= 0) and (currentField[i - 1][j].getOccupiedBy() == player)):
        return True
    elif ( ((j - 1) >= 0) and (currentField[i][j - 1].getOccupiedBy() == player)):
        return True
    elif ( ((j + 1) < constants.NUMBER_OF_SQUARES ) and (currentField[i][j + 1].getOccupiedBy() == player)):
        return True
    elif ( ((i + 1) < constants.NUMBER_OF_SQUARES) and (currentField[i + 1][j].getOccupiedBy() == player)):
        return True
    else : 
        return False

def getAcquiredNeighboringSquares(currentField, i, j, opponentPlayer):
    opponentNeighboringSquares = []
    if (((i - 1) >= 0) and (currentField[i - 1][j].getOccupiedBy() == opponentPlayer)):
        opponentSquarePosition = SquarePosition.SquarePosition()
        opponentSquarePosition.setPosition(i - 1,j)
        opponentNeighboringSquares.append(opponentSquarePosition)
    if ( ((j - 1) >= 0) and (currentField[i][j - 1].getOccupiedBy() == opponentPlayer)):
        opponentSquarePosition = SquarePosition.SquarePosition()
        opponentSquarePosition.setPosition(i,j - 1)
        opponentNeighboringSquares.append(opponentSquarePosition)
    if ( ((j + 1) < constants.NUMBER_OF_SQUARES ) and (currentField[i][j + 1].getOccupiedBy() == opponentPlayer)):
        opponentSquarePosition = SquarePosition.SquarePosition()
        opponentSquarePosition.setPosition(i,j + 1)
        opponentNeighboringSquares.append(opponentSquarePosition)
    if ( ((i + 1) < constants.NUMBER_OF_SQUARES) and (currentField[i + 1][j].getOccupiedBy() == opponentPlayer)):
        opponentSquarePosition = SquarePosition.SquarePosition()
        opponentSquarePosition.setPosition(i + 1,j)
        opponentNeighboringSquares.append(opponentSquarePosition)
    return opponentNeighboringSquares

def getMax(x, y):
    if(x > y):
        return x
    else:
        return y
    
def getMin(x, y):
    if(x < y):
        return x
    else:
        return y
  
def fillNextMove(field, currentPlayer, nextSquarePosition):
    opponentPlayer = getOpponentPlayer(currentPlayer)
    if(isRaid(field, nextSquarePosition.getPositionX(), nextSquarePosition.getPositionY(), currentPlayer)):
        opponentNeighboringSquares = getAcquiredNeighboringSquares(field, nextSquarePosition.getPositionX(), nextSquarePosition.getPositionY(), opponentPlayer)
        for i in range(0, len(opponentNeighboringSquares)):
            square = opponentNeighboringSquares[i]
            field[square.getPositionX()][square.getPositionY()].setOccupiedBy(currentPlayer)
    field[nextSquarePosition.getPositionX()][nextSquarePosition.getPositionY()].setOccupiedBy(currentPlayer)
    return field

def printStringOntoFile(fileName, str1):
    outputFile = open(fileName, 'w')
    outputFile.write(str1)
    outputFile.close()
  
def getFinalFieldString(currentField):
    str1 = constants.NULL_STRING
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            str1 += currentField[i][j].getOccupiedBy()
        str1 += "\n"
    return str1
    
def greedyBestFirstSearch(field, currentPlayer):
    #compute current board sum of nuts in player X's and player O's territories
    nextSquarePosition = SquarePosition.SquarePosition()
    nextSquarePosition.setPosition(constants.INFINITY, constants.INFINITY)
    #maxNutValueAfterConsideredMove = currentPlayerBoardSum
    maxNutValueAfterConsideredMove = 0
    maxValueSet = False
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if (field[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                fieldClone = copyField(field)
                if(isRaid(field, i, j, currentPlayer)):
                    acquireOrResetNeighboringSquaresAfterRaid(fieldClone, i, j, currentPlayer, constants.ACQUIRE)
                fieldClone[i][j].setOccupiedBy(currentPlayer)
                currentMoveTotalYeildOfNuts = evaluationFunction(fieldClone, currentPlayer)
                if(maxValueSet == False):
                    nextSquarePosition.setPosition(i, j)
                    maxNutValueAfterConsideredMove = currentMoveTotalYeildOfNuts
                    maxValueSet = True
                if (currentMoveTotalYeildOfNuts > maxNutValueAfterConsideredMove):
                    nextSquarePosition.setPosition(i, j)
                    maxNutValueAfterConsideredMove = currentMoveTotalYeildOfNuts
    return nextSquarePosition

#minimax implementation function definitions
def getStringOfIntArg(intValue):
    strValue = constants.NULL_STRING
    if(intValue == constants.INFINITY):
        strValue = constants.INFINITY_STRING
    elif (intValue == (-constants.INFINITY)):
        strValue = "-" + constants.INFINITY_STRING
    else:
        strValue = str(intValue)
    return strValue

def traversalLogStringEntry(treeNode, depth, alpha, beta):
    global traversalLogString
    str1 = constants.NULL_STRING
    position = constants.NULL_STRING
    if (depth == constants.INITIAL_DEPTH):
        position = constants.ROOT
    else:
        position = constants.TRAVERSAL_LOG_ALPHABET_MAP[treeNode.getPosition().getPositionY()] + str(treeNode.getPosition().getPositionX() + 1)
    value = getStringOfIntArg(treeNode.getValue())
    if((alpha == constants.NULL_STRING) and (alpha == constants.NULL_STRING)):
        str1 +=  "\n" + position +"," + str(depth) + "," + value
    else:
        str1 +=  "\n" + position +"," + str(depth) + "," + value + "," + str(getStringOfIntArg(alpha)) + "," + str(getStringOfIntArg(beta))
    global count
    traversalLogString += str1
    return 

def minValue(currentField, depth, cuttingOffDepth, treeNode, currentPlayer):
    if(depth == cuttingOffDepth):
        treeNode.setValue(evaluationFunction(currentField, currentPlayer))
        traversalLogStringEntry(treeNode, depth, constants.NULL_STRING, constants.NULL_STRING)
        return treeNode
    v = treeNode
    traversalLogStringEntry(v, depth, constants.NULL_STRING, constants.NULL_STRING)
    opponentPlayer = getOpponentPlayer(currentPlayer)
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if( currentField[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                currentTreeNode = TreeNode.TreeNode()
                currentTreeNode.setPosition(i, j)
                copyOfCurrentField = copyField(currentField)
                
                if(isRaid(currentField, i, j, opponentPlayer)):
                    acquireOrResetNeighboringSquaresAfterRaid(currentField, i, j, opponentPlayer, constants.ACQUIRE)
                currentField[i][j].setOccupiedBy(opponentPlayer)
                currentTreeNode.setValue(constants.INFINITY)
                intermediateNode = maxValue(currentField, depth + 1, cuttingOffDepth, currentTreeNode, currentPlayer)
                if(v.getValue() >  intermediateNode.getValue()):
                    v.setValue(intermediateNode.getValue())
                    if( depth == 0 ):
                        v.setPosition(intermediateNode.getPosition().getPositionX(), intermediateNode.getPosition().getPositionY())
                traversalLogStringEntry(v, depth, constants.NULL_STRING, constants.NULL_STRING)
                currentField = copyOfCurrentField
    return v
    
def maxValue(currentField, depth, cuttingOffDepth, treeNode, currentPlayer):
    if(depth == cuttingOffDepth):
        treeNode.setValue(evaluationFunction(currentField, currentPlayer))
        traversalLogStringEntry(treeNode, depth, constants.NULL_STRING, constants.NULL_STRING)
        return treeNode
    v = treeNode
    traversalLogStringEntry(v, depth, constants.NULL_STRING, constants.NULL_STRING)
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if( currentField[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                currentTreeNode = TreeNode.TreeNode()
                currentTreeNode.setPosition(i, j)
                copyOfCurrentField = copyField(currentField)
                if(isRaid(currentField, i, j, currentPlayer)):
                    acquireOrResetNeighboringSquaresAfterRaid(currentField, i, j, currentPlayer, constants.ACQUIRE)
                currentField[i][j].setOccupiedBy(currentPlayer)
                currentTreeNode.setValue(constants.INFINITY)
                intermediateNode = minValue(currentField, depth + 1, cuttingOffDepth, currentTreeNode, currentPlayer)
                if(v.getValue() < intermediateNode.getValue()):
                    v.setValue(intermediateNode.getValue())
                    if( depth == 0 ):
                        v.setPosition(intermediateNode.getPosition().getPositionX(), intermediateNode.getPosition().getPositionY())
                traversalLogStringEntry(v, depth, constants.NULL_STRING, constants.NULL_STRING)
                currentField = copyOfCurrentField
    return v

def minimaxDecision(currentField, cuttingOffDepth, currentPlayer):
    depth = constants.INITIAL_DEPTH
    treeNode = TreeNode.TreeNode()
    treeNode.setPosition(constants.INFINITY, constants.INFINITY)
    treeNode.setValue(-constants.INFINITY)
    finalPosition = maxValue(currentField, depth, cuttingOffDepth, treeNode, currentPlayer)
    return finalPosition.getPosition()

#alpha-beta pruning implementation function definitions
def minValueAB(currentField, currentPlayer, depth, cuttingOffDepth, treeNode, alpha, beta):
    if(depth == cuttingOffDepth):
        treeNode.setValue(evaluationFunction(currentField, currentPlayer))
        traversalLogStringEntry(treeNode, depth, alpha, beta)
        return treeNode
    v = treeNode
    traversalLogStringEntry(v, depth, alpha, beta)
    opponentPlayer = getOpponentPlayer(currentPlayer)
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if( currentField[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                currentTreeNode = TreeNode.TreeNode()
                currentTreeNode.setPosition(i, j)
                copyOfCurrentField = copyField(currentField)
                
                if(isRaid(currentField, i, j, opponentPlayer)):
                    acquireOrResetNeighboringSquaresAfterRaid(currentField, i, j, opponentPlayer, constants.ACQUIRE)
                currentField[i][j].setOccupiedBy(opponentPlayer)
                currentTreeNode.setValue(constants.INFINITY)
                intermediateNode = maxValueAB(currentField, currentPlayer, depth + 1, cuttingOffDepth, currentTreeNode, alpha, beta)
                if(v.getValue() >  intermediateNode.getValue()):
                    v.setValue(intermediateNode.getValue())
                    if( depth == 0 ):
                        v.setPosition(intermediateNode.getPosition().getPositionX(), intermediateNode.getPosition().getPositionY())
                if(v.getValue() <= alpha):
                    traversalLogStringEntry(v, depth, alpha, beta)
                    return v
                beta = getMin(beta, v.getValue())
                traversalLogStringEntry(v, depth, alpha, beta)
                currentField = copyOfCurrentField
    return v
    
def maxValueAB(currentField, currentPlayer, depth, cuttingOffDepth, treeNode, alpha, beta):
    if(depth == cuttingOffDepth):
        treeNode.setValue(evaluationFunction(currentField, currentPlayer))
        traversalLogStringEntry(treeNode, depth, alpha, beta)
        return treeNode
    v = treeNode
    traversalLogStringEntry(v, depth, alpha, beta)
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if( currentField[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                currentTreeNode = TreeNode.TreeNode()
                currentTreeNode.setPosition(i, j)
                copyOfCurrentField = copyField(currentField)
                if(isRaid(currentField, i, j, currentPlayer)):
                    acquireOrResetNeighboringSquaresAfterRaid(currentField, i, j, currentPlayer, constants.ACQUIRE)
                currentField[i][j].setOccupiedBy(currentPlayer)
                currentTreeNode.setValue(constants.INFINITY)
                intermediateNode = minValueAB(currentField, currentPlayer, depth + 1, cuttingOffDepth, currentTreeNode, alpha, beta)
                if(v.getValue() < intermediateNode.getValue()):
                    v.setValue(intermediateNode.getValue())
                    if( depth == 0 ):
                        v.setPosition(intermediateNode.getPosition().getPositionX(), intermediateNode.getPosition().getPositionY())
                if(v.getValue() >= beta):
                    traversalLogStringEntry(v, depth, alpha, beta)
                    return v
                alpha = getMax(alpha, v.getValue())
                traversalLogStringEntry(v, depth, alpha, beta)
                currentField = copyOfCurrentField
    return v

def alphaBetaSearch(currentField, currentPlayer, cuttingOffDepth):
    depth = constants.INITIAL_DEPTH
    treeNode = TreeNode.TreeNode()
    treeNode.setPosition(constants.INFINITY, constants.INFINITY)
    treeNode.setValue(-constants.INFINITY)
    alpha = -constants.INFINITY
    beta = constants.INFINITY
    finalPosition = maxValueAB(currentField, currentPlayer, depth, cuttingOffDepth, treeNode, alpha, beta)
    return finalPosition.getPosition()

#battle simulation
def freeNodeExists(field):
    for i in range(0, constants.NUMBER_OF_SQUARES):
        for j in range(0, constants.NUMBER_OF_SQUARES):
            if (field[i][j].getOccupiedBy() == constants.UNOCCUPIED):
                return True
    return False

def switchPlayer(currentPlayer, player1, player2):
    if(currentPlayer.getPlayer() == player1.getPlayer()):
        return player2
    elif(currentPlayer.getPlayer() == player2.getPlayer()):
        return player1

def invokeAlgorithm(field, battleSimulationCurrentPlayer):
    if(battleSimulationCurrentPlayer.getAlgorithm() == constants.GREEDY_BEST_FIRST_SEARCH):
        nextPosition = greedyBestFirstSearch(field, battleSimulationCurrentPlayer.getPlayer())
    elif(battleSimulationCurrentPlayer.getAlgorithm() == constants.MINIMAX):
        nextPosition = minimaxDecision(field, battleSimulationCurrentPlayer.getCutOffDepth(), battleSimulationCurrentPlayer.getPlayer())
    elif(battleSimulationCurrentPlayer.getAlgorithm() == constants.ALPHA_BETA_PRUNING):
        nextPosition = alphaBetaSearch(field, battleSimulationCurrentPlayer.getPlayer(), battleSimulationCurrentPlayer.getCutOffDepth())
    return nextPosition

#main
with open(sys.argv[2]) as f:
    lines = f.read().splitlines()
    f.close()
algorithmSelection = lines[constants.ALGORITHM_SELECTION]

if (algorithmSelection != constants.BATTLE_SIMULATION) : 
    currentPlayer = lines[constants.PLAYER_SELECTION]
    cuttingOffDepth = lines[constants.CUTTING_OFF_DEPTH]  
    field = initializeFieldValues(lines, algorithmSelection)
    if(algorithmSelection == constants.GREEDY_BEST_FIRST_SEARCH):
        fieldClone = copyField(field)
        nextSquarePosition = greedyBestFirstSearch(fieldClone, currentPlayer)
        fillNextMove(field, currentPlayer, nextSquarePosition)
        printStringOntoFile(constants.NEXT_STATE_FILE_NAME, getFinalFieldString(field))
    elif( algorithmSelection == constants.MINIMAX):
        traversalLogString = constants.MINIMAX_TRAVERSAL_LOG_FIRST_LINE
        fieldClone = copyField(field)
        finalPosition = minimaxDecision(fieldClone, int(cuttingOffDepth), currentPlayer)
        field = fillNextMove(field, currentPlayer, finalPosition)
        printStringOntoFile(constants.NEXT_STATE_FILE_NAME, getFinalFieldString(field))
        printStringOntoFile(constants.TRAVERSAL_LOG_FILE_NAME, traversalLogString)
    elif( algorithmSelection == constants.ALPHA_BETA_PRUNING):
        traversalLogString = constants.ALPHA_BETA_PRUNING_TRAVERSAL_LOG_FIRST_LINE
        fieldClone = copyField(field)
        finalPosition = alphaBetaSearch(fieldClone, currentPlayer, int(cuttingOffDepth))
        field = fillNextMove(field, currentPlayer, finalPosition)
        printStringOntoFile(constants.NEXT_STATE_FILE_NAME, getFinalFieldString(field))
        printStringOntoFile(constants.TRAVERSAL_LOG_FILE_NAME, traversalLogString)
else:
    player1 = PlayerAlgorithm.PlayerAlgorithm(lines[constants.BATTLE_SIMULATION_PLAYER1], lines[constants.BATTLE_SIMULATION_PLAYER1_ALGORITHM], int(lines[constants.BATTLE_SIMULATION_PLAYER1_CUTOFF_DEPTH]))
    player2 = PlayerAlgorithm.PlayerAlgorithm(lines[constants.BATTLE_SIMULATION_PLAYER2], lines[constants.BATTLE_SIMULATION_PLAYER2_ALGORITHM], int(lines[constants.BATTLE_SIMULATION_PLAYER2_CUTOFF_DEPTH]))
    field = initializeFieldValues(lines, algorithmSelection)
    battleSimulationCurrentPlayer = player1
    traceString = constants.NULL_STRING
    while(freeNodeExists(field)):
        fieldClone = copyField(field)
        nextPosition = invokeAlgorithm(fieldClone, battleSimulationCurrentPlayer)
        field = fillNextMove(field, battleSimulationCurrentPlayer.getPlayer(), nextPosition)
        traceString += getFinalFieldString(field)
        battleSimulationCurrentPlayer = switchPlayer(battleSimulationCurrentPlayer, player1, player2)
    printStringOntoFile(constants.TRACE_STATE_FILE_NAME, traceString)