# file name => controls.py

import numpy as np
import sys
from board import *
from arts import *
from scenes import *
from people import *
from board import *
import random 
from arts import *

class ControlCenter():

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
        self._em = 0
        self._wl = 0
        self._pp = 0
        self._marioPlace =0
        self._b1 = Bullet()
        self._bsjp = 20
        self._bsjpdef = self._bsjp
        self._pipePlace = ((self._width*4)-10)
        self._stepsTakenback = 0

    def controls(self,way,jp,life,score):
         #### Controls w -> jump  d -> forward   a -> backWards  
         #### For nothing it return the same thing again

        self._abvGnd = (5-abs(jp))*2
        if(random.randint(0,100)<1):
            self._scnGen.putPipe()
        if(way=='d'):
            movedScene = self._scnGen.moveForwardWorldScene()
            self._pipePlace-=3 
            
        elif(way=='a'):
            movedScene = self._scnGen.moveBackWorldScene()
            self._pipePlace+=1
            
        elif(way =='w'):
            movedScene = self._scnGen.retWorld()
            if(jp==5):
                jp-=1


        else: 
            movedScene = self._scnGen.retWorld()

        marioPlaced = np.copy(movedScene)

        marioPlaced = self._scnGen.putMario(marioPlaced,self._abvGnd,0)
        life = self.distMarioEnemy(jp,life)
#        if(self._pipePlace>0):
#            marioPlaced = self.putPipe(marioPlaced,self._pipePlace-self._width)
        if(self._em==0 and random.randint(0,20)<2):
           self._em = 1
           self._e1.setAlive()
           self._e1.setEnemyPlace(self._width*4-10);
        if(self._em==1):
            marioPlaced,score = self.plceEnemy(marioPlaced,score)
        return marioPlaced,jp,life,score

    def plceEnemy(self,enemyLess,score):
        if(self._e1.isAlive()==0):
            return enemyLess
        self._e1.setEnemyHeight(0)
        l,b = self._arts.getEnemyDim()
        if(self._e1.getFlag()):
            dist =self._width*self._vars.getMultPatches()-b-2
            self._e1.setEnemyPlace(dist)
        self._e1.setEnemyPlace(self._e1.getEnemyPlace()-2)
        if(self._e1.getEnemyPlace()==0):
            score+=10
            self._e1.die()

        if(self._e1.getEnemyPlace()>self._width):
            dist = self._e1.getEnemyPlace()-2
        else:
            dist = self._e1.getEnemyPlace()+3

        self._e1.setEnemyPlace(dist)
        enemyPlaced = self._scnGen.putEnemy(enemyLess,self._e1.getEnemyHeight(),dist)
        return enemyPlaced,score

    def distMarioEnemy(self,jp,life):
        dist = self._e1.getEnemyPlace()
        if(jp==5 and dist==self._width):
            life-=1
        if((jp==-4 or jp==-5) and (dist>=self._width-3 and dist<=self._width+3)):
            self._e1.die()
            self._em=0
        return life


    def placeBossEnemy(self, way, jp, life, gameWin):
        self._marioAbvGnd = (5-abs(jp))*2
        self._bossAbvGnd = (self._bsjpdef-abs(self._bsjp));
        self._bsjp-=2;
        if(self._bsjp<-self._bsjpdef):
            self._bsjp=self._bsjpdef
        scene = np.copy(self._scnGen.retWorld())
        if(way=='d'):
            self._marioPlace +=2 
#            if(self._marioPlace>= self._width*3):
#               gameWin =1 
#               return scene,jp,life,gameWin
            if(self._marioPlace+5>self._width*3):
               return scene,jp,life,1

        elif(way=='a'):
            self._marioPlace -= 2

        elif(way=='w'):
            if(jp==5):
                jp-=1

        marioPlaced = self._scnGen.putMario(scene,self._marioAbvGnd,self._marioPlace)
        marioPlaced = self._scnGen.putBossEnemy(marioPlaced ,self._bossAbvGnd,self._width*3)
        if(self._b1.bltpst()==0 and random.randint(0,10)<7 and self._bossAbvGnd < 10):
            self._b1.fire(self._bossAbvGnd,self._width*3)
        if(self._b1.bltpst()==1):
            l,b = self._b1.getBulletCor()
            self._b1.moveBlt()
            marioPlaced = self._scnGen.putBult(marioPlaced,l,b) 
            if(self._marioAbvGnd+3>=l and self._marioAbvGnd<=l and self._marioPlace+3<=b and self._marioPlace>=b):
                life-=1
        
        return marioPlaced,jp,life,gameWin




#boardObj = Board()

#cont = ControlCenter()
#finMatrix = cont.controls('w')
#boardObj.draw(finMatrix,1,1,1)
