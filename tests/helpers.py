import FreeCAD as App
from FreeCAD import Vector
import pytest


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