#file  -> name obstackle.py

import os,time,sys
from arts import *
from variables import *



class pipe():

    def __init__(self):
        self._arts = Arts()
        self._vars = Vars()
        boardObj = Board()
        self._scnGen = SceneGenerator()
        self._arts = Arts()
        self._baseHeight = self._vars.getHeightOfGround()
        self._abvGnd = 0
        self._e1 = Enemy()
        self._e2 = BossEnemy()
        self._scn = Scenes()
        self._height , self._width =  self._scn.getInitDim()
        self._place = 0
    
    def setPlace(self,var):
        self._place = var


