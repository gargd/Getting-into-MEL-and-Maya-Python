import maya.cmds as mc

dwin=mc.window(title="Renamer",wh=(400,256))
mc.columnLayout()
mc.text("Select the object to be renamed:")
mc.separator(h=50,style='none')
mc.text("Enter the new name")
mc.textField('newname')
mc.button(label="Rename selected",command="renameSel()")

mc.showWindow(dwin)

def renameSel():
    selList=mc.ls(selection=True)
    newname=mc.textField('newname',query=True,text=True)
    mc.rename(selList,newname)
