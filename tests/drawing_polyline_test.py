import FreeCAD as App
from FreeCAD import Vector
import Part # type: ignore
import pytest  


from helpers import two_polylines_equal
from drawing import penup, pendown, up, down, left, right


def test_L_shaped_polyline(freecad_document):
   expected_polyline_points = [
      Vector(20,10,0),
      Vector(20,20,0),
      Vector(25,20,0),
      Vector(25,15,0),
      Vector(30,15,0),
      Vector(30,10,0)
   ]

   count = len(expected_polyline_points)
   expected_polyline = [   
      Part.LineSegment(expected_polyline_points[i], expected_polyline_points[(i+1)% count])
      for i in range(count)
   ]
    
   sketch = freecad_document.addObject('Sketcher::SketchObject', 'Sketch')
   pendown(sketch, 20,10)
   up(10)
   right(5)
   down(5)
   right(5)
   down(5)
   left(10)
   penup()

   two_polylines_equal(expected_polyline, sketch.Geometry)







