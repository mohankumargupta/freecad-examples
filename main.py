import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import os

doc = App.newDocument()
box = Part.makeBox(80, 40, 20)
myPart = doc.addObject("Part::Feature", "myBox")
myPart.Shape = box
doc.recompute()

filename = "box.FCStd"
if os.path.exists(filename):
    os.remove(filename)

doc.saveAs("box.FCStd")



