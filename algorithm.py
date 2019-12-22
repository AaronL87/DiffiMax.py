### Work in progress

import random
import math

class createTree:
    def __init__(self,player,depth):
        self.depth = depth
        self.player = player
        self.value = None
        self.capture = random.randint(1,5) # the value 1 represents a capture
        self.check = random.randint(1,5) # the value 1 represents a check
        self.children = []
        self.childVals(depth)
        
    def childVals(self,depth):
        if self.depth > 0:
            branchCount = random.randint(1,10)
            for i in range(1,branchCount):
                self.children.append(createTree(-self.player,self.depth-1))
        elif self.depth == 0:
            self.value = random.gauss(.1,1)
            self.children.sort(reverse=True,key=lambda a:a.value) # Sorts children for future selections

tree = createTree(1,4)
# If depth == even, then algorithm begins with opponent choice (because choice starts with depth 1)

linesList = []

# drawThresh is always positive
# winThresh is always positive
# yourNum is the color of "player": 1 for white, -1 for black

# TODO First check if Minimax leads to player beating opponent
# TODO If optimal line has player lose, can still choose traps to increase practical chances
# TODO Have MiniMax that alternates by returning to DiffiMax

def DiffiMax(node,drawThresh,winThresh,yourNum):
    '''
    if (node.value >= drawThresh) & (node.player == yourNum) & (node.player == -1): 
        # TODO Look for last DiffiMax trap continuation in lineList and delete it. Run MiniMax there instead.
        # TODO If there are no DiffiMax traps in lineList, then player is lost because only MiniMax has been used
        pass
    elif (node.value <= -drawThresh) & (node.player == yourNum) & (node.player == 1):
        pass
    '''

    if (node.depth != 1) & (node.player == -yourNum) & (node.value == None):
        largestVal = None
        for child in node.children:
            childObj = DiffiMax(child,drawThresh,winThresh,yourNum)
            if largestVal == None:
                largestVal = childObj
            elif childObj.value > largestVal.value:
                largestVal = childObj
        return largestVal
        
    elif (node.depth != 1) & (node.player == yourNum) & (node.value == None):
        pass

    if (node.depth == 1) & (node.player == -yourNum): # If your opponent is the first to choose
        if len(node.children) == 1: # If node only has one child
            linesList.append((node.children[0],node.children[0].value))
            return node.children[0]
        elif node.player == -1: # Player has white pieces
            if (node.children[-1].value - node.children[-2].value <= -winThresh) & (node.children[-2].value >= winThresh)\
                                                                                & (node.children[-1].value >= -drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[-1].capture != 1)\
                                                                                & (node.children[-2].capture != 1):     
                linesList.append((node.children[-2],node.children[-2].value,node.children[-1].value - node.children[-2].value))
                return node.children[-2]
            else:
                linesList.append((node.children[-1],node.children[-1].value))
                return node.children[-1]
        elif node.player == 1: # For player with black pieces, opponent with white
            # Checks for difficult positions for opponent while accounting for forcing moves:
            if (node.children[0].value - node.children[1].value >= winThresh) & (node.children[1].value <= -winThresh)\
                                                                                & (node.children[0].value <= drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[0].capture != 1)\
                                                                                & (node.children[1].capture != 1):  
                linesList.append((node.children[1],node.children[1].value,node.children[0].value - node.children[0].value))
                return node.children[1]
            else:
                linesList.append((node.children[0],node.children[0].value))
                return node.children[0]

    elif (node.depth == 1) & (node.player == yourNum): #If you are the first to choose 
        if node.player == 1:
            linesList.append((node.children[0],node.children[0].value))
            return node.children[0]
        elif node.player == -1:
            linesList.append((node.children[-1],node.children[-1].value))
            return node.children[-1]
