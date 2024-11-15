import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from document import save_as
from drawing import makeVerticalLine

doc = App.newDocument()
body = doc.addObject('PartDesign::Body', 'Body')
sketch_front = doc.addObject('Sketcher::SketchObject', 'Sketch')
#sketch_front.Label = "SketchFront"
yz_plane = doc.getObject('YZ_Plane')
sketch_front.AttachmentSupport = [(yz_plane, '')]
sketch_front.MapMode = 'FlatFace'

makeVerticalLine(sketch_front, (0,20), 100)

doc.recompute()
save_as(doc, __file__)




