### Work in progress

import random
import math

class createTree:
    def __init__(self,depth,player):
        self.depth = depth
        self.player = player
        self.value = random.gauss(.1,1)
        self.capture = random.randint(1,5) # the value 1 represents a capture
        self.check = random.randint(1,5) # the value 1 represents a check
        self.children = []
        self.childVals()
        self.children.sort(reverse=True,key=lambda a:a.value) # Sorts children for future selections

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

# TODO Need to check that optimal line for opponent is not losing for player
# TODO Have MiniMax that alternates by returning to DiffiMax

def DiffiMax(node,drawThresh,winThresh,yourNum):
    if (node.value >= drawThresh) & (node.player == yourNum) & (node.player == -1): 
        pass
    elif (node.value <= -drawThresh) & (node.player == yourNum) & (node.player == 1):
        pass
        # TODO If previous choice was DiffiMax, delete that choice and choose Minimax at that point
        
    if depth == 0: # If node has no children
        lineList.append(node)
        return node
    elif node.player == yourNum: # Only looks for traps for opponent and uses MiniMax for player's moves
        if len(node.children) == 1: # If node only has one child
            lineList.append(node)
            MiniMax(node.children[0],drawThresh,winThresh,yourNum)
        elif node.player == -1: # For player with black pieces, opponent with white
            # Checks for difficult positions for opponent while accounting for forcing moves:
            if (node.children[0].value - node.children[1].value >= winThresh) & (node.children[1].value <= -winThresh)\
                                                                                    & (node.check != 1)\
                                                                                    & (node.capture != 1)\
                                                                                    & (node.children[0].capture != 1)\
                                                                                    & (node.children[1].capture != 1):  
                MiniMax(node.children[1],drawThresh,winThresh,yourNum)
            else:
                MiniMax(node.children[0],drawThresh,winThresh,yourNum)
        else: # For player with white pieces, opponent with black 
            if (node.children[-1].value - node.children[-2].value <= -winThresh) & (node.children[-2].value >= winThresh)\
                                                                                    & (node.check != 1)\
                                                                                    & (node.capture != 1)\
                                                                                    & (node.children[-1].capture != 1)\
                                                                                    & (node.children[-2].capture != 1):     
                MiniMax(node.children[-2],drawThresh,winThresh,yourNum)
            else:
                MiniMax(node.children[-1],drawThresh,winThresh,yourNum)   
    else: # When opponent's move
        if len(node.children) == 1: # If node only has one child
            lineList.append(node)
            DiffiMax(node.children[0],drawThresh,winThresh,yourNum)
        elif node.player == -1:
            DiffiMax(node.children[-1],drawThresh,winThresh,yourNum)
        else:
            DiffiMax(node.children[0],drawThresh,winThresh,yourNum)
            
#TODO
def MiniMax(node,drawThresh,winThresh,yourNum):
    pass
            
