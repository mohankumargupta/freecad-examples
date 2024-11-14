import FreeCAD as App
import Part 

from drawing import makeRectangle

Vector=App.Vector


def test_rectangle():
    expected_rectangle_points = [
       Vector(0,0,0),
       Vector(100,0,0),
       Vector(100,50,0),
       Vector(0,50,0)
    ]

    expected_rectangle_lines = [
      Part.LineSegment(expected_rectangle_points[i], expected_rectangle_points[(i+1)%4])
      for i in range(len(expected_rectangle_points))
    ]

    rectangle = makeRectangle(0,0, 100, 50)

    assert rectangle == expected_rectangle_lines

