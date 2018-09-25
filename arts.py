# file name ->>  arts.py

import numpy as np
from variables import *
import sys
class Arts():

    
    def __init__(self):

       self._smallCloud = np.array([[' ','.','-','(','`',' ',' ',')',' ',' '],
                                    [':','(',' ',' ',' ',' ',' ',' ',')',')'],
                                    ['`','(',' ',' ',' ',' ',')',' ',')',')'],
                                    [' ','`',' ','_','_','.',':','\'',' ',' ']
                                    ])



       self._bird = np.array([[' ',' ',' ',' ','_',' ',' ',' '],
                              [' ',' ','>','\'','o',')',' ',' '],
                              ['/','/','/','(',' \\','\\',',\\','\\']
                              ])

       self._tree = np.array([[' ',' ','/','\\',' ',' '],
                               [' ','/','/','\\','\\',' '],	
                               ['/','/','/','\\','\\','\\'],
                               ['/','/','/','\\','\\','\\'],
                               ['/','/','/','\\','\\','\\'],
                               ['/','/','/','\\','\\','\\'],
                               [' ',' ','|','|',' ',' '],   
                               [' ',' ','|','|',' ',' ']
                               ])

       self._cloud = np.array([[' ',' ',' ',' ',' ','.','-','~','~','~','-','.',' ',' ',' ',' ',' ',' ',' ',' '],
                               [' ',' ','.','-','(',' ',' ',' ',' ',' ',' ',' ',')','_',' ',' ',' ',' ',' ',' '],
                               [' ','/',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\ ','-','.',' ',' ',' '],
                               ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','\\',' ',' '],
                               [' ','\\',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','.','\'',' '],
                               [' ',' ',' ','\\','_','_','_','_','_','_','_','_','_','_','_','.','-',' ',' ',' ']
                               ])

       self._pipe = np.array([['_','_','_','_','_','_','_','_','_','_'],
                              ['|','_',' ',' ',' ',' ',' ',' ','_','|'],
                              [' ','|',' ',' ',' ',' ',' ',' ','|',' '],
                              [' ','|',' ',' ',' ',' ',' ',' ','|',' ']
                              ])

       self._mario = np.array([[' ','o',' '],
                               ['/','|','\\'],
                               ['/',' ','\\']
                               ])

       self._superMario =  np.array([[' ','O',' '],
                                     ['/','|','\\'],
                                     [' ','|',' '],
                                     ['/',' ','\\']
                                     ])

       self._enemy = np.array([[' ','_','_','_','_',' '],
                                ['|','|','O','O','|','|'],
                                ['(','_','_','_','_',')']
                                ])

       self._gameOver = np.array([list("  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______       __  "),
                                  list(" /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     |  | "),
                                  list("|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    |  | "),
                                  list("|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     |  | "),
                                  list("|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--   |    \    /    |  |____ |  |\  \----.|__| "),
                                  list(" \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|(__) "),
                                  ])

       self._winner = np.array([list("____    __    ____  __  .__   __. .__   __.  _______ .______      "),
                                list("\   \  /  \  /   / |  | |  \ |  | |  \ |  | |   ____||   _  \     "),
                                list(" \   \/    \/   /  |  | |   \|  | |   \|  | |  |__   |  |_)  |    "),
                                list("  \            /   |  | |  . `  | |  . `  | |   __|  |      /     "),
                                list("   \    /\    /    |  | |  |\   | |  |\   | |  |____ |  |\  \----."),
                                list("    \__/  \__/     |__| |__| \__| |__| \__| |_______|| _| `._____|"),
                                ])

       self._bossEnemy = np.array([list(" <(__)> | | |"),
                                   list(" | \/ | \_|_/"),
                                   list(" \^  ^/   |  "),
                                   list(" /\--/\  /|  "),
                                   list("/  \/  \/ |  ")
                                   ])

       self._bullet = np.array([list("<<<<")])

       self._vars = Vars()
       self._width = self._vars.getWidthOfPatch();
       self._height = self._vars.getHeight();

       #       self._scn = Scenes()
#       self._height,self._width = self._scn.getInitDim()
#       self._height,self._width = [22,20]
        
       self._gnd = np.full((3,self._width),'T') 

       self._holeGnd =  np.full((3,self._width),'T') 
       self._holeGnd [:,8:14] =' '

       self._wall = np.chararray((3, 6))
       self._wall[:] = 'W'

       self._surWall = np.chararray((3,6))
       self._surWall = '?'
    

    def getWinnerDim(self):
        return self._winner.shape

    def getWinner(self):
        return self._winner
    
    def getBulletDim(self):
        return self._bullet.shape

    def getBullet(self):
        return self._bullet
    
    def getBossEnemyDim(self):
        return self._bossEnemy.shape

    def getBossEnemy(self):
        return self._bossEnemy
       
    def getCloud(self):
        return self._cloud

    def getCloudDim(self):
        return self._cloud.shape
    
    def getSmallCloud(self):
        return self._smallCloud

    def getSmallCloudDim(self):
        return self._smallCloud.shape

    def getPipeDim(self):
        return self._pipe.shape

    def getPipe(self):
        return self._pipe
    
    def getMario(self):
        return self._mario

    def getMarioDim(self):
        return self._mario.shape

    def getSuperMarioDim(self):
        return self._superMario.shape

    def getSuperMario(self):
        return self._superMario
            
    def getGnd(self):
        return self._gnd

    def getWallDim(self):
        return self._wall.shape

    def getWall(self):
        return self._wall

    def getSurWallDim(self):
        return self._surWall.shape

    def getSurWall(self):
        return self._surWall

    def getEnemyDim(self):
        return self._enemy.shape

    def getEnemy(self):
        return self._enemy
    
    def getHoleGnd(self):
        return self._holeGnd

    def getTreeDim(self):
        return self._tree.shape

    def getTree(self):
        return self._tree

    def getBirdDim(self):
        return self._bird.shape

    def getBird(self):
        return self._bird

    def getGameOverDim(self):
        return self._gameOver.shape

    def getGameOver(self):
        return self._gameOver

    
#art = Arts()
#a= art.getPipe()
#np.savetxt(sys.stdout.buffer,art.getGnd(), fmt='%s', delimiter='')
#print(a.shape)
