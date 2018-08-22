# scenes.py

import random  
import numpy as np
import sys
from arts import *
import os
import time
from variables import *

class Scenes():

    # All the Different components are here to set the components like Trees and all to set into 20 * 22 matrix called patch
    def __init__(self):
        self._vars = Vars()
        self._width = self._vars.getWidthOfPatch();
        self._height = self._vars.getHeight();
        self._space = np.full((self._height,self._width),' ')
        self._asc = Arts()
        self._gndHeight = self._vars.getHeightOfGround()
        self._siftPipe = 6
        self._siftWall = 6
        self._wallHeight = 5


    def getInitDim(self):
        return self._space.shape

    def setGnd(self):
        self._space[-self._gndHeight:,:] = self._asc.getGnd()
        return self._space

#    def draw(self):
#        np.savetxt(sys.stdout.buffer, self._space, fmt='%s', delimiter='')
#        a=self._space
#        print ('\n'.join(''.join(str(cell) for cell in row) for row in a))

    def setCloud(self,a):
        l,b=self._asc.getCloudDim()
        pdb = random.randint(0,self._width-b)
        pdh = random.randint(0,self._height-l-self._gndHeight)
        a[pdh:pdh+l,pdb:pdb+b] = self._asc.getCloud()
        return a


    def setPipe(self,a):
        l,b = self._asc.getPipeDim()
        a[-(self._gndHeight+l):-(self._gndHeight),self._siftPipe:self._siftPipe+b] = self._asc.getPipe()
        return a


    def setMario(self):
        l,b = self._asc.getMarioDim()
        self._space[-(self._gndHeight+l):-(self._gndHeight),:b] = self._asc.getMario()

    def setSuperMario(self):
        l,b = self._asc.getSuperMarioDim()
        self._space[-(self._gndHeight+l):-(self._gndHeight),:b] = self._asc.getSuperMario()

    def setWall(self,a):
        l,b = self._asc.getWallDim()
        a[-(self._gndHeight+self._wallHeight+l):-(self._gndHeight+self._wallHeight),(self._siftWall):(self._siftWall+b)] = self._asc.getWall()
        return a

    def setSurWall(self,a):
        l,b = self._asc.getWallDim()
        a[-(self._gndHeight+self._wallHeight+l):-(self._gndHeight+self._wallHeight),(self._siftWall):(self._siftWall+b)] = self._asc.getSurWall()
        return a
        
    def setEnemy(self):
        l,b = self._asc.getEnemyDim()
        self._space[-(self._gndHeight+l):-(self._gndHeight),-b:] = self._asc.getEnemy()
    
    def setHoleGnd(self,a):
        a[-self._gndHeight:,:] = self._asc.getHoleGnd()
        return a

    def setTree(self,a): 
        l,b = self._asc.getTreeDim()
        a[-(self._gndHeight+l):-(self._gndHeight),self._siftPipe*2:self._siftPipe*2+b] = self._asc.getTree()
        return a


    def setSmallCld(self,a): 
        l,b=self._asc.getSmallCloudDim()
        a[:l,:b] = self._asc.getSmallCloud()
        return a


class SceneGenerator:

    # Has the components to render all the above generated scenecs into one scene (World scene of 22 * 80) and display screen of 22 * 40 
    def __init__(self):
        self._scn = Scenes()
        self._vars = Vars()
        self._height , self._width =  self._scn.getInitDim()
        self._showWidth = self._width * self._vars.getMultPatches()
        self._Canvas = np.full((self._height,self._showWidth),' ')
        self._World = np.full((self._height,self._showWidth*2),' ')
        self._Gnd = self._scn.setGnd()
        self._Cld = self._scn.setCloud(np.copy(self._Gnd))
        self._Tree = self._scn.setTree(np.copy(self._Gnd))
        self._TreeCld = self._scn.setTree(np.copy(self._Cld))
        self._SmallCldTree = self._scn.setSmallCld(np.copy(self._Tree))
        self._SmallCld = self._scn.setSmallCld(np.copy(self._Gnd))
        self._trans = 0
        self._stt=0

        self._gndHeight=3

        self._HolGnd = self._scn.setHoleGnd(np.copy(self._Cld))
        self._Hol = self._scn.setHoleGnd(np.copy(self._Gnd))
        self._Pipe = self._scn.setPipe(np.copy(self._Gnd))
        self._PipeCld = self._scn.setCloud(np.copy(self._Cld))
        self.startWorldScene()

        self._arts = Arts()

    def firstScene(self):
        # HardCoded Initial Scene
        self._blank = self._Canvas
        self._blank[:,:self._width]=self._scn.setSmallCld(np.copy(self._scn.setGnd()))
        self._blank[:,self._width:self._width*2] = self._scn.setTree(np.copy(self._scn.setGnd()))
        self._blank[:,self._width*2:self._width*3] = self._scn.setCloud(np.copy(self._scn.setGnd()))
        self._blank[:,self._width*3:self._width*4] = self._scn.setSurWall(np.copy(self._scn.setGnd()))
        return self._blank
    
    def givePatch(self):
        x = random.randint(1,10)
        return {
            1: self._SmallCld,
            2: self._Cld,
            3: self._Tree,
            4: self._Gnd,
            5: self._SmallCldTree,
            6: self._SmallCld,
            7: self._SmallCldTree,
            8: self._Cld,
            9: self._SmallCld,
            10: self._Cld }[x]

    
    def randScenes(self): 
        self._blank = np.copy(self._Canvas) 
        for i in range(4):
            self._blank[:,self._width*i:self._width*(i+1)] = self.givePatch()
        return self._blank 

    def startWorldScene(self):
        self._World[:,:self._showWidth] = self.firstScene()
        self._World[:,self._showWidth:self._showWidth*2] = self.randScenes()
        return self._World
    
    def randScenes(self): 
        self._blank = np.copy(self._Canvas) 
        for i in range(4):
            self._blank[:,self._width*i:self._width*(i+1)] = self.givePatch()
        return self._blank 

    def startWorldScene(self):
        self._World[:,:self._showWidth] = self.firstScene()
        self._World[:,self._showWidth:self._showWidth*2] = self.randScenes()
        return self._World

    def moveForwardWorldScene(self):
        if(self._stt==20):
            self._World[:,:self._showWidth+self._width*3] = self._World[:,self._width:]
            self._World[:,self._showWidth+self._width*3:] = self.givePatch()
            self._stt=0
        speed = 2   #Comment it out later to see the effect of speed
        self._stt+=2    
#        self._World[:,:self._showWidth] = self._World[:,self._stt:self._showWidth+self._stt]
#        self._World[:,:self._showWidth]  =np.copy(self._World[:,self._stt:self._showWidth+self._stt])
        return self._World[:,self._stt:self._showWidth+self._stt]

    def moveBackWorldScene(self):
        if(self._stt==0):
            return self.retWorld()
        speed = 2
        self._stt-=2
        return self._World[:,self._stt:self._showWidth+self._stt]

    def retWorld(self):
        return self._World[:,self._stt:self._stt+self._showWidth]

    def putMario(self,tmp,hgh,place):
        l,b = self._arts.getMarioDim()
        tmp[-(self._gndHeight+hgh+l):-(self._gndHeight+hgh),self._width+place:b+place+self._width] = self._arts.getMario()
        return tmp

    def putEnemy(self,tmp,hgh,place):
        l,b = self._arts.getEnemyDim()
        tmp[-(self._gndHeight+hgh+l):-(self._gndHeight+hgh),place:b+place] = self._arts.getEnemy()
        return tmp

    def putBossEnemy(self,tmp,hgh,place):
        l,b = self._arts.getBossEnemyDim()
        tmp[-(self._gndHeight+hgh+l):-(self._gndHeight+hgh),place:b+place] = self._arts.getBossEnemy()
        return tmp

    def putBult(self,tmp,hgh,place):
        l,b = self._arts.getBulletDim()
        tmp[-(self._gndHeight+hgh+l):-(self._gndHeight+hgh),place:place+b] = self._arts.getBullet()
        return tmp

    def putPipe(self):
        l,b = self._arts.getPipeDim()
        self._World[-(self._gndHeight+l):-(self._gndHeight),self._showWidth:self._showWidth+b] = self._arts.getPipe()


#sc1 = Scenes()
#sc1.setCloud()
#sc1.setPipe()
#sc1. setMario()
#sc1.setSuperMario()
#sc1.setWall()
#sc1.setSurWall()
#sc1.setEnemy()
#sc1.setGnd()
#sc1.setHoleGnd()
#a=0
#while(True):
#    sc1.draw()
#    time.sleep(0.1)
#    os.system('cls' if os.name=='nt' else 'clear')
#    print(a)
#    a+=1
#import time
#acd = SceneGenerator()
#while(True):
#    a=acd.moveWorldScene()  ## DO change here between first and randome scenes
#    print ('\n'.join(''.join(str(cell) for cell in row) for row in a))
#    time.sleep(0.1)
