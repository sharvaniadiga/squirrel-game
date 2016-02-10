'''
Created on Feb 5, 2016

@author: sharvani
'''
import SquarePosition

class TreeNode(object):
    def setPosition(self, x, y):
        self.position = SquarePosition.SquarePosition()
        self.position.setPosition(x, y)
        
    def getPosition(self):
        return self.position
    
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value