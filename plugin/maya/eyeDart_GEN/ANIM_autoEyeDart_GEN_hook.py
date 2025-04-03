import sys
import maya.cmds as cmds
import maya.mel as mel
import imp
import os
import ANIM_autoEyeDart_GEN_core

kPluginCmdName = "crossControllerGenCore"

# Initialize the script plug-in
def initializePlugin(mobject):
    # generate menu
    mainWindow = mel.eval('$temp1=$gMainWindow')

    if not cmds.menu('toolsMainMenu', exists=1):
        cmds.menu('toolsMainMenu',l='Wlls Tools', tearOff=1, p=mainWindow)
    cmds.menuItem('ANIM_autoEyeDart_GEN_core',l='Eye Dart Tools',p='toolsMainMenu', c=lambda*args:ANIM_autoEyeDart_GEN_core.mainUI())       
    return

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    # delete this plugin menu first
    cmds.deleteUI('ANIM_autoEyeDart_GEN_core')

    # check if the root menu has other menu or not. If not then delete it
    if cmds.menu('toolsMainMenu', q=1, ni=1) == 0:
        cmds.deleteUI('toolsMainMenu')
    return