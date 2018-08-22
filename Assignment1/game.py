####### file name => game.py

import os, time
from board import *
from arts import *
from charScan import *
from alarmexception import *
from controls import *
from subprocess import call

charScanner = CharScan()

def chkInpt(timeout =1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL,timeout)
    t0 = time.time()
    try:
        chrInt = charScanner()
        signal.alarm(0)
        t1 = time.time()
        while(t1-t0 <1/20):
            t1 = time.time()
        return chrInt
    except AlarmException:
        print (end='')
    signal.signal(signal.SIGALRM,signal.SIG_IGN)
    return ''

def alarmHandler(signum,frame):
    raise AlarmException

def main():
        var = Vars()
        call(["xdg-open","/home/anurag/HW/Assignment_1/sound.mp3"])
##        os.startfile("/home/anurag/HW/Assignment_1/sound.mp3")
        boardObj = Board()
        cont = ControlCenter()
        score=0
        tim =0
        art = Arts()
        jp = 5
        life=3
        gameWin = 0
        way=''
        while(life>0 and gameWin==0):
            if(tim<600):  #Time before mario faces enemy
                finMatrix, jp, life,score = cont.controls(way,jp,life,score)  # Generating scenes
                if(jp!=5):
                    jp-=1
                    if(jp==-5):
                        jp=5
            
            else:
                finMatrix, jp, life, gameWin = cont.placeBossEnemy( way, jp, life, gameWin)
                if(gameWin==1):
                    break;
                if(jp!=5):
                    jp-=1
                    if(jp==-5):
                        jp=5



            score+=1
            tim+=1
            boardObj.draw(finMatrix,score,life,int(tim/16)) # Printing the Matrix in to Termial
            way = chkInpt()
            os.system('cls' if os.name=='nt' else 'clear')   # Clearing the terminal after every 0.1 sec

        if(gameWin==1):
            boardObj.winner()
 
        boardObj.gameOver()
if __name__== '__main__':
	main()
