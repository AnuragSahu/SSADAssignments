### File name => board.py 

import numpy as np
import sys
from arts import *
from scenes import *
from variables import *
from time import sleep
import os
class Board():
    """Manage the Background Of Game """
    def __init__(self):
        self._spacing = 5      # For Score Board
        self._padding = 10      # For Score Board
        self._scnGen = SceneGenerator()
        self._arts = Arts()
        self._vars = Vars()

    def draw(self,finMatrix,score,life,time):
        self._scoreBoard = self._padding*' '+"Mario Score: "+str(score)+self._spacing*' '+"Life: "+str(life)+self._spacing*' '+"Time: "+str(time)
        print(self._scoreBoard)
        print ('\n'.join(''.join(str(cell) for cell in row) for row in finMatrix))
#        np.savetxt(sys.stdout.buffer, finMatrix, fmt='%0c')
    
    def gameOver(self):
        length = self._vars.getHeight()
        breath = self._vars.getWidthOfPatch()*self._vars.getMultPatches()
        l,b = self._arts.getGameOverDim()
#        pad = int (breath - b / 2)
        pad=10
        dim = 0
        while(dim<length-l-5):
            bckgnd=np.full((length,breath),'.')
            bckgnd[dim:dim+l, pad:pad+b] = self._arts.getGameOver()
            print ('\n'.join(''.join(str(cell) for cell in row) for row in bckgnd))
            sleep(1/15)
            os.system('cls' if os.name=='nt' else 'clear')   # Clearing the terminal after every 0.1 sec
            if(dim ==length-l-6):
                dim=0
            dim+=1
    

    def winner(self):
        length = self._vars.getHeight()
        breath = self._vars.getWidthOfPatch()*self._vars.getMultPatches()
        l,b = self._arts.getWinnerDim()
#        pad = int (breath - b / 2)
        pad=10
        dim = 0
        while(dim<length-l-5):
            bckgnd=np.full((length,breath),'.')
            bckgnd[dim:dim+l, pad:pad+b] = self._arts.getWinner()
            print ('\n'.join(''.join(str(cell) for cell in row) for row in bckgnd))
            sleep(1/15)
            os.system('cls' if os.name=='nt' else 'clear')   # Clearing the terminal after every 0.1 sec
            if(dim ==length-l-6):
                dim=0
            dim+=1
    


#brd = Board()
#while(True):
#    os.system('cls' if os.name=='nt' else 'clear')
#    brd.draw()
