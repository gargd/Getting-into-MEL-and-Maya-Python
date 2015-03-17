import maya.cmds as mc

listBox=mc.ls(sl=True)
selSize=len(listBox)
for i in range(0,selSize,1):
        rescaler=(i+1)*0.5
        mc.scale(rescaler,rescaler,rescaler,listBox[i],r=True)
