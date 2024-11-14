import FreeCAD as App
from FreeCAD import Vector
import Part # type: ignore
import pytest  

from drawing import makeRectangle, makeCenterRectangle

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
    

