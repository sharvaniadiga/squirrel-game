'''
Created on Feb 8, 2016

@author: sharvani
'''
class PlayerAlgorithm(object):
    def __init__(self, player, algorithm, cutOffDepth):
        self.player = player
        self.algorithm = algorithm
        self.cutOffDepth = cutOffDepth
        
    def getPlayer(self):
        return self.player
    
    def getAlgorithm(self):
        return self.algorithm
    
    def getCutOffDepth(self):
        return self.cutOffDepth