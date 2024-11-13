import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import createDocumentAndBody, createSketch, save_as
from const import Constraints, Plane
from utils import Pen

doc, body = createDocumentAndBody()
sketch = createSketch(doc, "sketch", Plane.YZ)
body.addObject(sketch)

# Use body and sketch here
pen = Pen(doc, sketch)
pen.pendown((0,20))
pen.right(55)
pen.down(20)
pen.left(10)
pen.up(10)
pen.left(45)
pen.up(10)

sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,1,-2))
sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
sketch.addConstraint(Sketcher.Constraint('Distance', 0,1,0,2,55))
sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 0, 1, 20))

doc.recompute()


save_as(doc, __file__)

