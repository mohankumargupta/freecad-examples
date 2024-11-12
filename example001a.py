import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from save import save_as

doc = App.newDocument()
body = doc.addObject('PartDesign::Body', 'Body')
sketch_front = doc.addObject('Sketcher::SketchObject', 'Sketch')
sketch_front.Label = "SketchFront"
yz_plane = doc.getObject('YZ_Plane')
sketch_front.AttachmentSupport = [(yz_plane, '')]
sketch_front.MapMode = 'FlatFace'

line1 = sketch_front.addGeometry(Part.LineSegment(App.Vector(0,20,0), App.Vector(55,20,0)), False)
#line1 = sketch.Geometry[0]  
line2 = sketch_front.addGeometry(Part.LineSegment(App.Vector(55,20,0), App.Vector(55,0,0)), False)
line3 = sketch_front.addGeometry(Part.LineSegment(App.Vector(55,0,0), App.Vector(45,0,0)), False)
line4 = sketch_front.addGeometry(Part.LineSegment(App.Vector(45,0,0), App.Vector(45,10,0)), False)
line5 = sketch_front.addGeometry(Part.LineSegment(App.Vector(45,10,0), App.Vector(0,10,0)), False)
line6 = sketch_front.addGeometry(Part.LineSegment(App.Vector(0,10,0), App.Vector(0,20,0)), False)

# # Add horizontal line (top of the 7)
# line1 = sketch_front.addGeometry(Part.LineSegment(App.Vector(0,15,0), App.Vector(20,15,0)), False)

# # Add vertical line (vertical part of the 7)
# line2 = sketch_front.addGeometry(Part.LineSegment(App.Vector(20,15,0), App.Vector(20,0,0)), False)

# # Add constraints

# # Make first line horizontal
# sketch_front.addConstraint(Sketcher.Constraint('Horizontal', line1))

# # Make second line vertical
# sketch_front.addConstraint(Sketcher.Constraint('Vertical', line2))

# # Add dimensional constraints
# # Set length of horizontal line to 20 units
# sketch_front.addConstraint(Sketcher.Constraint('Distance', line1, 20))

# # Set length of vertical line to 15 units
# sketch_front.addConstraint(Sketcher.Constraint('Distance', line2, 15))


# Pad
pad = doc.addObject("PartDesign::Pad", "Pad")
pad.Profile = sketch_front
pad.Length = 40
doc.recompute()

body.addObject(pad)

#body.Tip = sketch_front
doc.recompute()
save_as(doc, __file__)




