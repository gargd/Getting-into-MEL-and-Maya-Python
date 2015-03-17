import maya.cmds as mc

pdStatus=mc.promptDialog(message="Please input number of teeth",button="OK")
if pdStatus=="OK":
    numTeeth=mc.promptDialog(query=True,text=True)
    numTeeth=int(numTeeth)

    gear=mc.polyPipe(subdivisionsAxis=numTeeth*2,h=0.5,r=1.5)

    intSA=mc.getAttr(gear[1]+".subdivisionsAxis")
    intStartFace=intSA*2
    intEndFace=intSA*3-1

    mc.select(cl=True)

    for i in range(intStartFace,intEndFace,2):  
        mc.select(gear[0]+".f[%d]"%i,add=True)
    mc.polyExtrudeFacet(ltz=0.5)
    mc.polySmooth(gear[0])
    
