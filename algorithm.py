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
                self.children.append(createTree(self.depth - 1,-self.player))

tree = createTree(4,1)

linesList = []

def DiffiMax(node,depth,player,drawThresh,winThresh,yourNum,candidFactor):
    if depth == 0:
        pass
    
    if len(node.children) == 1: # If node only has one child
        MiniMax()
    elif player == -yourNum: # Only looks for traps for chosen color and uses MiniMax for your moves
        childVals = []
        for i in range(len(node.children)):
            childVals.append((i,node.children[i].value)) # Makes list of children values
        
        if player == -1: # Sorts and calculates according to player
            sortList = sorted(childVals, reverse=True, key=lambda a:a[1]) 
            if (len(node.children)*(sortList[0][1] - sortList[1][1])/candidFactor >= winThresh) & (sortList[1][1] >= winThresh) & (node.children.check != 1) & (node.children.capture != 1):
                MiniMax(node.children[sortList[1][0]])
            else:
                MiniMax()
        else:
            sortList = sorted(childVals, key=lambda a:a[1])
            if (len(node.children)*(sortList[0][1] - sortList[1][1])/candidFactor <= winThresh) & (sortList[1][1] <= winThresh) & (node.children.check != 1) & (node.children.capture != 1):
                MiniMax(node.children[sortList[1][0]])
            else:
                MiniMax()
    else:
        MiniMax()
