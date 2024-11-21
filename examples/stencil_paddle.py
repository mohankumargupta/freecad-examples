import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import makeArcTwoPoints, penup, pendown, down, right, up, left, arcLeft

def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    yz_plane = doc.getObject('XY_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    pendown(sketch, (5,5))
    down(25)
    right(10)
    up(25)
    arcLeft(10, 30)
    penup()

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



