import FreeCAD as App
from FreeCAD import Vector
import Part # type: ignore
import pytest  

from drawing import makeRectangle, makeCenterRectangle, makeCircle

#Vector=App.Vector

@pytest.fixture 
def freecad_document(request):
   doc_name = "boo"
   doc = App.newDocument(doc_name)
   yield doc
   App.closeDocument(doc_name)

def vector_to_tuple(vector):
    return (vector.x, vector.y, vector.z)

def line_to_tuple(line):
  start_point = vector_to_tuple(line.StartPoint)
  end_point = vector_to_tuple(line.EndPoint)
  return tuple(sorted([start_point, end_point]))

def two_polylines_equal(expected, actual):
   expected_tuples = {line_to_tuple(line) for line in expected}
   actual_tuples = {line_to_tuple(line) for line in actual}
   assert expected_tuples == actual_tuples
   

def test_rectangle(freecad_document):
    expected_rectangle_points = [
       Vector(0,0,0),
       Vector(100,0,0),
       Vector(100,50,0),
       Vector(0,50,0)
    ]

    expected_rectangle = [
      Part.LineSegment(expected_rectangle_points[i], expected_rectangle_points[(i+1)%4])
      for i in range(len(expected_rectangle_points))
    ]

    sketch = freecad_document.addObject('Sketcher::SketchObject', 'Sketch')
    makeRectangle(sketch, (0,0), (100, 50))
    two_polylines_equal(expected_rectangle, sketch.Geometry)

def test_center_rectangle(freecad_document):
    center = Vector(50, 25, 0)
    lengths = (100, 50)
    
    # Define the expected points for a rectangle centered at (50, 25)
    expected_rectangle_points = [
        Vector(0, 0, 0),
        Vector(100, 0, 0),
        Vector(100, 50, 0),
        Vector(0, 50, 0)
    ]

    # Define the expected rectangle as line segments
    expected_rectangle = [
        Part.LineSegment(expected_rectangle_points[i], expected_rectangle_points[(i+1) % 4])
        for i in range(len(expected_rectangle_points))
    ]

    sketch = freecad_document.addObject('Sketcher::SketchObject', 'Sketch')
    makeCenterRectangle(sketch, center, lengths)

    # Use the same comparison function
    two_polylines_equal(expected_rectangle, sketch.Geometry)
    

def test_circle(freecad_document):
   """
   Test that makeCircle creates a circle with the correct center and radius.
   """
   # Test parameters
   center = Vector(30, 40, 0)
   radius = 25

   # Create a new sketch
   sketch = freecad_document.addObject('Sketcher::SketchObject', 'Sketch')

   # Create the circle using makeCircle
   makeCircle(sketch, center, radius)

   # Get the created geometry
   created_circle = sketch.Geometry[0]  # First (and only) geometry element

   # Verify the circle properties
   assert isinstance(created_circle, Part.Circle), "Geometry is not a circle"

   # Check center point coordinates
   assert abs(created_circle.Center.x - center[0]) < 1e-7, "Circle center X coordinate is incorrect"
   assert abs(created_circle.Center.y - center[1]) < 1e-7, "Circle center Y coordinate is incorrect"
   assert abs(created_circle.Center.z) < 1e-7, "Circle center Z coordinate should be 0"

   # Check radius
   assert abs(created_circle.Radius - radius) < 1e-7, "Circle radius is incorrect"

   # Check normal vector (should be pointing in Z direction)
   assert abs(created_circle.Axis.x) < 1e-7, "Circle axis X component should be 0"
   assert abs(created_circle.Axis.y) < 1e-7, "Circle axis Y component should be 0"
   assert abs(created_circle.Axis.z - 1) < 1e-7, "Circle axis Z component should be 1"

   # Verify constraints
   # There should be 3 constraints: radius and X/Y position
   assert len(sketch.Constraints) == 3, "Incorrect number of constraints"

   # Check that constraints are of the expected types
   constraint_types = [c.Type for c in sketch.Constraints]
   assert "Radius" in constraint_types, "Missing radius constraint"
   #assert constraint_types.count("Distance") == 2, "Missing position constraints"