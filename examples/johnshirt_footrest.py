import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from turtlesketch import penup, pendown, down, right, diagonalSouthWest, diagonalNorthEast ,moveTo, arc



def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    yz_plane = doc.getObject('YZ_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    length = 220
    height = 50
    width = 70

    pendown(sketch, (0, 0))
    right(width)
    l1 = diagonalSouthWest(7)
    moveTo((0,0))
    down(height)
    l2 = diagonalNorthEast(7)
    endpoint = sketch.Geometry[l1].EndPoint
    #arc(endpoint, radius=40, outside=False,  mirror_centre=False)
    
    #penup()

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



