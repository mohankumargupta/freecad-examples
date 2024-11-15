import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import makeCenterRectangle

def create():
    doc = App.newDocument()
    body = doc.addObject('PartDesign::Body', 'Body')
    sketch = doc.addObject('Sketcher::SketchObject', 'Sketch')
    yz_plane = doc.getObject('XY_Plane')
    sketch.AttachmentSupport = [(yz_plane, '')]
    sketch.MapMode = 'FlatFace'

    makeCenterRectangle(sketch, (50,45), (100,50))

    doc.recompute()
    save_as(doc, __file__)
    return doc

if __name__ == "__main__":
    create()



