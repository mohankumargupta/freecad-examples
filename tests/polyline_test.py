import FreeCAD as App
from FreeCAD import Vector
import Part # type: ignore
import pytest  

from common import are_sketches_equal, create_rectangle
from drawing import penup, pendown, left, right, up, down

def test_rectangle(sketches):
    sketch_expected, sketch_actual = sketches

    bottom_left_corner = (5,5)
    width = 40
    height = 20
    
    top_right_corner = (5+width, 5+ height)

    create_rectangle(sketch_expected, bottom_left_corner, width, height)
    
    pendown(sketch_actual, bottom_left_corner)
    right(width)
    up(height)
    left(-width)
    down(-height)

    assert are_sketches_equal(sketch_expected, sketch_actual)



