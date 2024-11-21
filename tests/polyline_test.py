import FreeCAD as App
from FreeCAD import Vector
import Part # type: ignore
import pytest  

from common import are_sketches_equal, create_rectangle
from drawing import penup, pendown, left, right, up, down

def test_rectangle(document_and_sketches):
    doc, sketch_expected, sketch_actual = document_and_sketches

    bottom_left_corner = (5,5)
    width = 40
    height = 20
    
    top_right_corner = (5+width, 5+ height)

    create_rectangle(sketch_expected, bottom_left_corner, width, height)
    doc.recompute()
    
    pendown(sketch_actual, bottom_left_corner)
    right(width)
    up(height)
    left(width)
    down(height)
    penup()

    doc.recompute()

    result, message =  are_sketches_equal(sketch_expected, sketch_actual)

    assert result, message


