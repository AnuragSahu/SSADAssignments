# file name variables.py

class Vars():
    def __init__(self):
         self._height = 42
         self._widthOfPatch = 30
         self._heightOfGround = 3
         self._padFromAbove = 3
         self._multPatches =4 

    def getMultPatches(self):
        return self._multPatches

    def getHeight(self):
        return self._height

    def setHeight(self,var):
        self._setHeight=var

    def getWidthOfPatch(self):
        return self._widthOfPatch 

    def setWidthOfPatch(self,var):
        self._widthOfPatch=var

    def getHeightOfGround(self):
        return self._heightOfGround

    def getPadFromAbove(self):
        return self._padFromAbove


