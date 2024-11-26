import FreeCAD as App
import FreeCADGui as Gui
import Part # type: ignore
import Sketcher  # type: ignore
from save import save_as
from slot import create_slot

doc = App.newDocument()
body = doc.addObject('PartDesign::Body', 'Body')
sketch_front = doc.addObject('Sketcher::SketchObject', 'Sketch')
#sketch_front.Label = "SketchFront"
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

doc.recompute()
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
pad_name = "Pad"
pad = doc.addObject("PartDesign::Pad", pad_name)
pad.Profile = sketch_front
pad.Length = 40
p = doc.getObject(pad_name)
p.Midplane = True # Symmetric 
doc.recompute()

body.addObject(pad)
doc.recompute()
pad.Visibility = True
body.Visibility = True
sketch_front.Visibility = True
doc.recompute()

sketch_top = doc.addObject('Sketcher::SketchObject', 'SketchTop')
sketch_top_from_doc = doc.getObject(sketch_top.Name)
sketch_top_from_doc.AttachmentSupport = (pad, ['Face1',])
sketch_top_from_doc.MapMode = 'FlatFace'

# geoList = []
# geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-13.502590, -6.571736, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 8.000000), 3.196452, 6.338045))
# geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-14.415868, 10.059232, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 8.000000), 0.054859, 3.196452))
# geoList.append(Part.LineSegment(App.Vector(-21.490555, -7.010389, 0.000000),App.Vector(-22.403833, 9.620578, 0.000000)))
# geoList.append(Part.LineSegment(App.Vector(-5.514625, -6.133082, 0.000000),App.Vector(-6.427903, 10.497886, 0.000000)))
# sketch_top_from_doc.addGeometry(geoList,False)
# del geoList

create_slot(doc, sketch_top)

doc.recompute()
save_as(doc, __file__)




