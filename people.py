# This is the File Where all the Living Creature of the Game are Present.
# It has a Person class which is Inherited by both Player (Our ownhero Mario)
# And the Villinas.
from abc import ABC, abstractmethod
from arts import *


class Person(ABC):
    # This is the parent class for every living creatures
    # Following People Inherit this code
    # 1. Mario (Basic Hero) *
    # 2. Luigi (Upgraded Mario) *
    # 3. Toad 
    # 4. Princess Peach *
    # 5. Goomba *
    # 6. Koopa also red *
    # 7. Para Koopa also red
    # 8. piranha plant * 
    # 9. Hammer bro
    # 10. Lakitu
    # 11. Spiny
    # 12. Buzzy beetle
    # 13. Bullet bill
    # 14. Blooper
    # 15. Cheep cheep
    # 16. Bowser *
    # All the Character aren't able to be completed
    # I expect to complete star '*' marked characters to be complete

    def __init__(self):
        super().__init__()

    @abstractmethod    
    def move(self):
        # Lets to charcter to move
        pass
    
#    @abstractmethod    
#    def attack(self):
        # Lets the character to attack if it can
#        pass

    @abstractmethod    
    def die(self):
        # How the character dies
        pass

class Hero(Person):

    def __init__(self):
        self._lives = 3
        self._score = 0
        self._head = [' ','o','o',' ']
        self._body = ['[','|','|','}']
        self._legs = [' ','}','{',' ']

        print(self._head)
        print(self._body)
        print(self._legs)

    def move(self):
        print ("Moving...")

 #   def attack(self):
 #       print("Attacking")

    def die(self):
        self._lives-=1


class Enemy(Person):
    def __init__(self):
        self._lives = 1
        self._heightAbvGnd = 0;
        self._place = 0;
        self._arts  = Arts()
        self._flg = 1
    
    def setFlag (self):
        return True

    def getFlag(self):
        if(self._flg==1):
            self._flg=0
            return True
        return False
    
    def isAlive(self):
        return self._lives

    def die(self):
        self._lives=0

    def setAlive(self):
        self._lives=1

    def getEnemyHeight(self):
        return self._heightAbvGnd;

    def setEnemyHeight(self, ht):
        self._heightAbvGnd = ht

    def getEnemyPlace(self):
        return self._place

    def setEnemyPlace(self, pls):
        self._place = pls

    def getEnemyDim(self):
        return self._arts.getEnemyDim

    def move(self,d):
        if(d=="left"):
            self._place =self._place-2 
            
        else:  self._place = self._place +2

#    def attack(self):

    def die(self):
        self._lives-=1

    
class BossEnemy(Person):
    def __init__(self):
        self._lives = 3
        self._heightAbvGnd = 0;
        self._place = 0;
        self._arts  = Arts()
        self._flg = 1
        self._bulletPos = 0
        self._bulletHgh = 3

    def moveBullet(self):
        self._bulletPos-=1

    def getBulletPos(self):
        return self._bulletPos,self._bulletHgh

    def setBulletHgh(self,hgh):
        self._bulletHgh = hgh

    def setFlag (self):
        return True

    def getFlag(self):
        if(self._flg==1):
            self._flg=0
            return True
        return False
    
    def isAlive(self):
        return self._lives

    def die(self):
        self._lives=0

    def setAlive(self):
        self._lives=1

    def getEnemyHeight(self):
        return self._heightAbvGnd;

    def setEnemyHeight(self, ht):
        self._heightAbvGnd = ht

    def getEnemyPlace(self):
        return self._place

    def setEnemyPlace(self, pls):
        self._place = pls

    def getEnemyDim(self):
        return self._arts.getEnemyDim

    def move(self,d):
        if(d=="left"):
            self._place =self._place-2 
            
        else:  self._place = self._place +2

#    def attack(self):

    def die(self):
        self._lives-=1


class Bullet():

    def __init__(self):
        self._hgh = 5
        self._place = 0
        self._pst = 0

    def fire(self,hgh,place):
        self._pst =1
        self._hgh = hgh
        self._place = place

    def moveBlt(self):
        self._place -=1
        if(self._place<0):
            self._pst =0
    
    def getBulletCor(self):
        return self._hgh, self._place

    def bltpst(self):
        return self._pst



#mario = Hero()
#mario.move()
#mario.attack()
#mario.die()

