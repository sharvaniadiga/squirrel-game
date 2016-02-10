'''
Created on Jan 29, 2016

@author: sharvani
'''

import constants

class Square(object):
    
    def __init__(self):
        self.yeildOfNuts = 0;
        self.occupiedBy = constants.UNOCCUPIED
    
    def getYeildOfNuts(self):
        return self.yeildOfNuts
    
    def setYeildOfNuts(self, value):
        self.yeildOfNuts = value
        
    def getOccupiedBy(self):
        return self.occupiedBy
    
    def setOccupiedBy(self, player):
        self.occupiedBy = player
        
#===============================================================================
# square1 = square()
# square2 = square()
# square1.setYeildOfNuts(3)
# square2.setYeildOfNuts(10)
# print square1.getYeildOfNuts()
# print square1.yeildOfNuts
# print square2.getYeildOfNuts()
# print square2.yeildOfNuts
# print square1.getYeildOfNuts()
# print square1.yeildOfNuts
#===============================================================================
    #===========================================================================
    # @property
    # def yeildOfNuts(self):
    #     return self.yeildOfNuts
    # 
    # @property
    # def occupiedBy(self):
    #     return self.occupiedBy
    # 
    # @yeildOfNuts.setter
    # def yeildOfNuts(self, value):
    #     self.yeildOfNuts = value
    #     
    # @occupiedBy.setter
    # def occupiedBy(self, player):
    #     self.occupiedBy = player
    #===========================================================================
    #===========================================================================
    # @classmethod    
    # def getYeildOfNuts(self):
    #     return self.yeildOfNuts
    # 
    # @classmethod
    # def setYeildOfNuts(self, yeildOfNuts1):
    #     self.yeildOfNuts = yeildOfNuts1
    # 
    # @classmethod
    # def getOccupiedBy(self):
    #     return self.occupiedBy
    # 
    # @classmethod
    # def setOccupiedBy(self, player):
    #     self.occupiedBy = player
    #===========================================================================