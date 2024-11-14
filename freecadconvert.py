import sys
import os
inputFile = os.path.abspath(sys.argv[1])
outputFile = os.path.abspath(sys.argv[2])
sys.path.append("/usr/lib/freecad/lib")

import FreeCAD as App
import FreeCADGui
FreeCADGui.showMainWindow()

import Import  # type: ignore
import ImportGui # type: ignore
import Draft # type: ignore
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
ImportGui.insert(inputFile,"Unnamed")
__objs__=[]
for part in App.ActiveDocument.Objects:
    __objs__.append(part)
FreeCADGui.export(__objs__,outputFile)
del __objs__
App.closeDocument("Unnamed")