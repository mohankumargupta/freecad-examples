import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import makeVerticalLine, makeHorizontalLine

def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    #sketch_front.Label = "SketchFront"
    yz_plane = doc.getObject('YZ_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    l1 = makeHorizontalLine(sketch, (0, 20), 150)
    l2 = makeVerticalLine(sketch, (150,20), 100)
    l3 = makeHorizontalLine(sketch, (150, 120), -150)
    l4 = makeVerticalLine(sketch, (0,120), -100)

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



