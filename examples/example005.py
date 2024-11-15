import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import makeRectangle

def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    yz_plane = doc.getObject('XY_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    makeRectangle(sketch, (0,20), (100,50))

    # sketch.addConstraint(Sketcher.Constraint("Coincident", 0,2, 1,1))
    # sketch.addConstraint(Sketcher.Constraint("Coincident", 1,2, 2,1))
    # sketch.addConstraint(Sketcher.Constraint("Coincident", 2,2, 3,1))
    # sketch.addConstraint(Sketcher.Constraint("Coincident", 3,2, 0,1))

    #sketch.addConstraint(Sketcher.Constraint("Distance", 0,1,0,2,150))
    #sketch.addConstraint(Sketcher.Constraint("Distance", 1,1,1,2,100))

    #sketch.addConstraint(Sketcher.Constraint("PointOnObject", 0,1,-2))
    #sketch.addConstraint(Sketcher.Constraint("DistanceY", 0,1,20))    

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



