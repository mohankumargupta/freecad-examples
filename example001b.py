import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
#from save import save_as
from document import createDocument, save_as
from const import Constraints

doc, body, sketch_front = createDocument()

sketch_front.Label = "SketchFront"
yz_plane = doc.getObject('YZ_Plane')
sketch_front.AttachmentSupport = [(yz_plane, '')]
sketch_front.MapMode = 'FlatFace'



line1 = sketch_front.addGeometry(Part.LineSegment(App.Vector(0,20,0), App.Vector(55,20,0)), False)
#line1 = sketch.Geometry[0]  
line2 = sketch_front.addGeometry(Part.LineSegment(App.Vector(55,20,0), App.Vector(55,0,0)), False)
#line3 = sketch_front.addGeometry(Part.LineSegment(App.Vector(55,0,0), App.Vector(45,0,0)), False)
#line4 = sketch_front.addGeometry(Part.LineSegment(App.Vector(45,0,0), App.Vector(45,10,0)), False)
#line5 = sketch_front.addGeometry(Part.LineSegment(App.Vector(45,10,0), App.Vector(0,10,0)), False)
#line6 = sketch_front.addGeometry(Part.LineSegment(App.Vector(0,10,0), App.Vector(0,20,0)), False)

line1_index = 0
sketch_front.addConstraint(Sketcher.Constraint("Vertical", Constraints.X_AXIS, Constraints.LINE_START, line1_index, Constraints.LINE_START))
sketch_front.addConstraint(Sketcher.Constraint("Horizontal", line1_index))
sketch_front.addConstraint(Sketcher.Constraint("Distance", line1_index, Constraints.LINE_START, line1_index, Constraints.LINE_END, 55))

line2_index = 1
sketch_front.addConstraint(Sketcher.Constraint("Horizontal", Constraints.X_AXIS, Constraints.LINE_START, line2_index, Constraints.LINE_END))
sketch_front.addConstraint(Sketcher.Constraint("Vertical", line2_index))
sketch_front.addConstraint(Sketcher.Constraint("Coincident", line1_index, Constraints.LINE_END, line2_index, Constraints.LINE_START))
sketch_front.addConstraint(Sketcher.Constraint("Distance", line2_index, Constraints.LINE_START, line2_index, Constraints.LINE_END, 20))


# Pad
#pad = doc.addObject("PartDesign::Pad", "Pad")
#pad.Profile = sketch_front
#pad.Length = 40
#doc.recompute()

#body.addObject(pad)

#body.Tip = sketch_front
doc.recompute()
save_as(doc, __file__)

