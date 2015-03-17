import maya.cmds as mc
import random

dWin=mc.window(title="Disperserer",wh=(256,256))

mc.columnLayout()
mc.button(label="Disperse selected",command="disperse()")
mc.text(label="Set XYZ range values")
rangeField=mc.floatFieldGrp(numberOfFields=3)

mc.showWindow(dWin)

def disperse():
    selList=mc.ls(selection=True)
    rangeX=mc.floatFieldGrp(rangeField,query=True,value1=True)
    rangeY=mc.floatFieldGrp(rangeField,query=True,value2=True)
    rangeZ=mc.floatFieldGrp(rangeField,query=True,value3=True)
    
    for obj in selList:
        randomX=random.randint(-rangeX,rangeX)
        randomY=random.randint(-rangeY,rangeY)
        randomZ=random.randint(-rangeZ,rangeZ)
        mc.setAttr(obj+".translateX",randomX)
        mc.setAttr(obj+".translateY",randomY)
        mc.setAttr(obj+".translateZ",randomZ)
