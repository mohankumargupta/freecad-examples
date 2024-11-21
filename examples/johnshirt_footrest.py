import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import penup, pendown, up, left, right, diagonalSouthWest



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

    pendown(sketch, (0, height))
    up(height)
    right(width)
    diagonalSouthWest(20)
    penup()

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



