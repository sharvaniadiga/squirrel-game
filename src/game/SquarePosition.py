'''
Created on Feb 3, 2016

@author: sharvani
'''

class SquarePosition(object):
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def getPositionX(self):
        return self.x
    
    def getPositionY(self):
        return self.y
    
#===============================================================================
# #test
# opponentNeighboringSquares = []
# opponentSquarePosition = SquarePosition()
# opponentSquarePosition.setPosition(0,1)
# opponentNeighboringSquares.append(opponentSquarePosition)
# opponentSquarePosition = SquarePosition()
# opponentSquarePosition.setPosition(0,1)
# opponentNeighboringSquares.append(opponentSquarePosition)
# print len(opponentNeighboringSquares)
# for i in range(0,2):
#     print "%s %s" % (opponentNeighboringSquares[i].getPositionX(), opponentNeighboringSquares[i].getPositionY())
#===============================================================================
