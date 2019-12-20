### Work in progress

import random
import math

class createTree:
    def __init__(self,depth,player):
        self.depth = depth
        self.player = player
        self.value = random.gauss(.1,1)
        self.capture = random.randint(1,5) # 1 represents a capture
        self.check = random.randint(1,5) # 1 represents a check
        self.children = []
        self.childVals()

    def childVals(self):
        if self.depth >= 0:
            branchCount = random.randint(1,10)
            for i in range(1,branchCount):
                self.children.append(createTree(self.depth-1,-self.player))

tree = createTree(4,1)

linesList = []


# drawThresh is always positive
# winThresh is always positive
# yourNum is the color of "player": 1 for white, -1 for black

def DiffiMax(node,depth,player,drawThresh,winThresh,yourNum):
    if (abs(node.value) >= drawThresh) & (node.player == yourNum): #TODO
        
        
    if depth == 0:
            return node, node.value
    
    if len(node.children) == 1: # If node only has one child
        DiffiMax(node.children[0],depth-1,drawThresh,winThresh,yourNum)
    
    elif node.player == yourNum: # Only looks for traps for opponent and uses MiniMax for player's moves
        childVals = []
        
        for i in range(len(node.children)):
            childVals.append((i,node.children[i].value)) # Makes list of children values
        
        if node.player == -1: # Sorts and calculates according to player's color, which is white here
            sortList = sorted(childVals, reverse=True, key=lambda a:a[1]) 
            
            if (sortList[0][1] - sortList[1][1] >= winThresh) & (sortList[1][1] >= winThresh) & (node.check != 1) & (node.capture != 1)\
                & (node.children[sortList[0][0]].capture != 1) & (node.children[sortList[1][0]].capture != 1):  
                
                DiffiMax(node.children[sortList[1][0]])
            
            else:
                MiniMax()
        else: # If calculating for player with black pieces
            sortList = sorted(childVals, key=lambda a:a[1])
            
            if (sortList[0][1] - sortList[1][1] <= winThresh) & (sortList[1][1] <= winThresh) & (node.check != 1) & (node.capture != 1)\
                & (node.children[sortList[0][0]].capture != 1) & (node.children[sortList[1][0]].capture != 1):  
                
                DiffiMax(node.children[sortList[1][0]])
            
            else:
                DiffiMax()
    
    else: # When player's move
        DiffiMax()
