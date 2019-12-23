### Work in progress

import random

class createTree:
    def __init__(self,depth,player=1):
        self.depth = depth
        self.player = player
        self.value = None
        self.capture = random.randint(1,5) # the value 1 represents a capture
        self.check = random.randint(1,5) # the value 1 represents a check
        self.children = []
        self.childVals()
        
    def childVals(self):
        if self.depth > 0:
            self.branchCount = random.randint(1,10)
            print(self.depth,self.branchCount)
            for i in range(0,self.branchCount):
                self.children.append(createTree(self.depth-1,player=-self.player))
        elif self.depth == 0:
            self.value = random.gauss(.1,1)

linesList = []

# drawThresh is always positive
# winThresh is always positive
# yourNum is the color of "player": 1 for white, -1 for black

# TODO First check if Minimax leads to player beating opponent
# TODO If optimal line has player lose, can still choose traps to increase practical chances

def DiffiMax(node,drawThresh,winThresh,yourNum,linesList):
    # TODO Look for last DiffiMax trap continuation in lineList and delete it. Run MiniMax there instead.
    # TODO If there are no DiffiMax traps in lineList, then player is lost because only MiniMax has been used
    print(1,node.depth)
    if node.depth != 1: # Cycles through all nodes
        for child in node.children:
            node.value, linesList = DiffiMax(child,drawThresh,winThresh,yourNum,linesList)
            print(node.value)
        return node.value, linesList
    print(2,node.depth)
    node.children.sort(reverse=True,key=lambda a:a.value) # Sorts children for future selections
    print(3)
    if node.player == -yourNum: # If it is your opponent's choice
        if len(node.children) == 1: # If node only has one child. Checked because next condition requires two children.
            linesList = [(node.children[0],node.children[0].value)]+linesList
            return node.children[0].value,linesList
        elif node.player == -1: # Opponent has black pieces
            # Checks for difficult positions for opponent while accounting for forcing moves:
            if (node.children[-1].value - node.children[-2].value <= -winThresh) & (node.children[-2].value >= winThresh)\
                                                                                & (node.children[-1].value >= -drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[-1].capture != 1)\
                                                                                & (node.children[-2].capture != 1):     
                linesList = [(node.children[-2],node.children[-2].value,node.children[-1].value)]+linesList
                return node.children[-2].value, linesList
            else:
                linesList = [(node.children[-1],node.children[-1].value)]+linesList
                return node.children[-1].value, linesList
        elif node.player == 1: # Opponent has white pieces
            if (node.children[0].value - node.children[1].value >= winThresh) & (node.children[1].value <= -winThresh)\
                                                                                & (node.children[0].value <= drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[0].capture != 1)\
                                                                                & (node.children[1].capture != 1):  
                linesList = [(node.children[1],node.children[1].value,node.children[0].value)]+linesList
                return node.children[1].value, linesList 
            else:
                linesList = [(node.children[0],node.children[0].value)]+linesList
                return node.children[0].value, linesList
    elif node.player == yourNum: # If it is your choice
        if node.player == 1: # You have the white pieces
            linesList = [(node.children[0],node.children[0].value)]+linesList
            return node.children[0].value, linesList
        
        elif node.player == -1: # You have the black pieces
            linesList = [(node.children[-1],node.children[-1].value)]+linesList
            return node.children[-1].value, linesList

tree = createTree(4)
# If depth == even, then algorithm begins with opponent choice (because choice starts with depth 1)

finalEval, linesList = DiffiMax(tree,1,2.5,1,linesList)

print(finalEval)
