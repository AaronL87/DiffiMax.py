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
    # TODO Look for last DiffiMax trap continuation in lineList and delete it. Run MiniMax there instead.
    # TODO If there are no DiffiMax traps in lineList, then player is lost because only MiniMax has been used

    if node.depth != 1: # Cycles through all nodes
        for child in node.children:
            node.value = DiffiMax(child,drawThresh,winThresh,yourNum)

    if node.player == -yourNum: # If it is your opponent's choice
        if len(node.children) == 1: # If node only has one child. Checked because next condition requires two children.
            linesList = [(node.children[0],node.children[0].value)]+linesList
            return node.children[0].value
        
        elif node.player == -1: # Opponent has black pieces
            # Checks for difficult positions for opponent while accounting for forcing moves:
            if (node.children[-1].value - node.children[-2].value <= -winThresh) & (node.children[-2].value >= winThresh)\
                                                                                & (node.children[-1].value >= -drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[-1].capture != 1)\
                                                                                & (node.children[-2].capture != 1):     
                linesList = [(node.children[-2],node.children[-2].value,node.children[-1].value]+linesList
                return node.children[-2].value

            else:
                linesList = [(node.children[-1],node.children[-1].value)]+linesList
                return node.children[-1].value
        
        elif node.player == 1: # Opponent has white pieces
            if (node.children[0].value - node.children[1].value >= winThresh) & (node.children[1].value <= -winThresh)\
                                                                                & (node.children[0].value <= drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[0].capture != 1)\
                                                                                & (node.children[1].capture != 1):  
                linesList = [(node.children[1],node.children[1].value,node.children[0].value]+linesList
                return node.children[1].value
            
            else:
                linesList = [(node.children[0],node.children[0].value)]+linesList
                return node.children[0].value

    elif node.player == yourNum: # If it is your choice
        if node.player == 1: # You have the white pieces
            linesList = [(node.children[0],node.children[0].value)]+linesList
            return node.children[0].value
        
        elif node.player == -1: # You have the black pieces
            linesList = [(node.children[-1],node.children[-1].value)]+linesList
            return node.children[-1].value
            
  DiffiMax(tree,1,2.5,1)
  print(linesList)
