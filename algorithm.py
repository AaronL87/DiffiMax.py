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
            
def DiffiMax(node,drawThresh,winThresh,yourNum):
    # TODO Look for last DiffiMax trap continuation in lineList and delete it. Run MiniMax there instead.
    # TODO If there are no DiffiMax traps in lineList, then player is lost because only MiniMax has been used
    print(1,node.depth)
    if node.depth != 1: # Cycles through all nodes
        for child in node.children:
            child.value = DiffiMax(child,drawThresh,winThresh,yourNum)
            print(child.value)
            
        node.value = DiffiSort(node,drawThresh,winThresh,yourNum)
        return node.value
    
    DiffiSort(node,drawThresh,winThresh,yourNum)
    
    
def DiffiSort(node,drawThresh,winThresh,yourNum):
    print(2,node.depth)
    node.children.sort(reverse=True,key=lambda a:a.value) # Sorts children for future selections
    print(3)
    if node.player == -yourNum: # If it is your opponent's choice
        if len(node.children) == 1: # If node only has one child. Checked because next condition requires two children.
            return node.children[0].value
        elif node.player == -1: # Opponent has black pieces
            # Checks for difficult positions for opponent while accounting for forcing moves:
            if (node.children[-1].value - node.children[-2].value <= -winThresh) & (node.children[-2].value >= winThresh)\
                                                                                & (node.children[-1].value >= -drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[-1].capture != 1)\
                                                                                & (node.children[-2].capture != 1):     
                return node.children[-2].value
            else:
                return node.children[-1].value
        elif node.player == 1: # Opponent has white pieces
            if (node.children[0].value - node.children[1].value >= winThresh) & (node.children[1].value <= -winThresh)\
                                                                                & (node.children[0].value <= drawThresh)\
                                                                                & (node.check != 1) & (node.capture != 1)\
                                                                                & (node.children[0].capture != 1)\
                                                                                & (node.children[1].capture != 1):  
                return node.children[1].value
            else:
                return node.children[0].value
    elif node.player == yourNum: # If it is your choice
        if node.player == 1: # You have the white pieces
            return node.children[0].value
        
        elif node.player == -1: # You have the black pieces
            return node.children[-1].value

tree = createTree(4)
# If depth == even, then algorithm begins with opponent choice (because choice starts with depth 1)

DiffiMax(tree,1,2.5,1)
