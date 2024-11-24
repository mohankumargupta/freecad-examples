import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
#from drawing import arcLeft
from turtlesketch import penup, pendown, down, right, up, arc_left

def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    yz_plane = doc.getObject('XY_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    outer_diameter = 65
    inner_diameter = 50
    grip_height = 20
    grip_width = 25

    outer_radius = outer_diameter / 2.0
    inner_radius = inner_diameter / 2.0

    pendown(sketch, (5,5))
    down(grip_height)
    right(grip_width)
    up(grip_height)
    arc_left(grip_width, outer_radius)
    penup()

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



