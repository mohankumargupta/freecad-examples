import FreeCAD as App
#import FreeCADGui as Gui
import Part # type: ignore

doc = App.newDocument()
box = Part.makeBox(80, 40, 20)
myPart = doc.addObject("Part::Feature", "myBox")
myPart.Shape = box

doc.recompute()
doc.saveAs("box.FCStd")



