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
    sketch = doc.addObject('Sketcher::SketchObject', 'Rectangle')
    body.addObject(sketch)

    bottom_corner = (5,10)
    width=40
    height=20

    pendown(sketch, bottom_corner)
    right(width)
    up(height)
    line1 = left(width)
    line2 = down(height)
    penup()

    removeConstraint(line1, "DistanceX")
    removeConstraint(line2, "DistanceY")
    


    doc.recompute()

    # Add the geometry for a rectangle
    # Parameters: starting point (0,0), width = 100mm, height = 50mm
    # sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0,0,0), FreeCAD.Vector(100,0,0)), False)  # bottom line
    # sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(100,0,0), FreeCAD.Vector(100,50,0)), False)  # right line
    # sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(100,50,0), FreeCAD.Vector(0,50,0)), False)  # top line
    # sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0,50,0), FreeCAD.Vector(0,0,0)), False)  # left line

    # # Add constraints to make it a proper rectangle
    # # Horizontal constraints
    # sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))  # bottom line
    # sketch.addConstraint(Sketcher.Constraint('Horizontal', 2))  # top line

    # # Vertical constraints
    # sketch.addConstraint(Sketcher.Constraint('Vertical', 1))    # right line
    # sketch.addConstraint(Sketcher.Constraint('Vertical', 3))    # left line

    # Equal length constraints for opposite sides
    #sketch.addConstraint(Sketcher.Constraint('Equal', 0, 2))    # horizontal lines
    #sketch.addConstraint(Sketcher.Constraint('Equal', 1, 3))    # vertical lines

    # Add dimensional constraints
    #sketch.addConstraint(Sketcher.Constraint('Distance', 0, 100.0))  # width = 100mm
    #sketch.addConstraint(Sketcher.Constraint('Distance', 1, 50.0))   # height = 50mm

    # Recompute the sketch
    #doc.recompute()

    # pad = doc.addObject('PartDesign::Pad','Pad')
    # pad.Profile = sketch
    # pad.Length = 40
    # body.addObject(pad)
    doc.recompute()
    #pad.Visibility = True
    body.Visibility = True
    sketch.Visibility = True

    #doc.recompute()

    # Save the document (optional)

    save_as(doc, __file__)
    return doc