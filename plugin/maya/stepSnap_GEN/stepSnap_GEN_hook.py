import sys
import maya.cmds as cmds
import maya.mel as mel
import imp
import os
import stepSnap_GEN_core

kPluginCmdName = "stepSnapGenCore"

# Initialize the script plug-in
def initializePlugin(mobject):
    # generate menu
    mainWindow = mel.eval('$temp1=$gMainWindow')

    if not cmds.menu('toolsMainMenu', exists=1):
        cmds.menu('toolsMainMenu',l='TOOLS', tearOff=1, p=mainWindow)
    cmds.menuItem('ss_GEN_core',l='Step Snap [GEN]',p='toolsMainMenu', c=lambda*args:stepSnap_GEN_core.mainUI())       
    return

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    # delete this plugin menu first
    cmds.deleteUI('ss_GEN_core')

    # check if the root menu has other menu or not. If not then delete it
    if cmds.menu('toolsMainMenu', q=1, ni=1) == 0:
        cmds.deleteUI('toolsMainMenu')
    return