import FreeCAD
import Sketcher # type: ignore
import Part # type: ignore
from document import save_as
from turtlesketch import pendown, penup, up, down, left, right, removeConstraint

def create():
    # Create a new document
    doc = FreeCAD.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')

    # Create a new sketch
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    body.addObject(sketch)

    initial_pos = (0,0)
    length = 220
    width=70
    height=50

    pendown(sketch, initial_pos)
    right(width)
    up(height)
    line1 = left(width)
    line2 = down(height)
    penup()

    removeConstraint(line1, "DistanceX")
    removeConstraint(line2, "DistanceY")
    
    doc.recompute()

    save_as(doc, __file__)
    return doc