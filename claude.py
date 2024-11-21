import unittest
import FreeCAD
import Part # type: ignore
import math

class TestGeometryComparison(unittest.TestCase):
    def setUp(self):
        self.doc = FreeCAD.newDocument("TestDoc")
        # Define tolerance for floating point comparisons
        self.epsilon = 1e-7

    def tearDown(self):
        FreeCAD.closeDocument(self.doc.Name)

    def assert_points_equal(self, point1, point2, msg=None):
        """Compare two points (FreeCAD.Vector) for equality within epsilon."""
        self.assertAlmostEqual(point1.x, point2.x, delta=self.epsilon, 
                             msg=f"{msg}: X coordinates differ")
        self.assertAlmostEqual(point1.y, point2.y, delta=self.epsilon, 
                             msg=f"{msg}: Y coordinates differ")
        self.assertAlmostEqual(point1.z, point2.z, delta=self.epsilon, 
                             msg=f"{msg}: Z coordinates differ")

    def assert_lines_equal(self, line1, line2, msg=None):
        """Compare two lines (Part.LineSegment) for equality."""
        # Check if lines have same start and end points (in either direction)
        direct_match = (
            self.are_points_equal(line1.StartPoint, line2.StartPoint) and
            self.are_points_equal(line1.EndPoint, line2.EndPoint)
        )
        reverse_match = (
            self.are_points_equal(line1.StartPoint, line2.EndPoint) and
            self.are_points_equal(line1.EndPoint, line2.StartPoint)
        )
        
        self.assertTrue(direct_match or reverse_match, 
                       msg or "Lines are not equal")

    def are_points_equal(self, point1, point2):
        """Check if two points are equal within epsilon."""
        return (abs(point1.x - point2.x) < self.epsilon and
                abs(point1.y - point2.y) < self.epsilon and
                abs(point1.z - point2.z) < self.epsilon)

    def test_comparing_identical_rectangles(self):
        """Test comparing two identical rectangles."""
        # Create first rectangle
        rect1_points = [
            FreeCAD.Vector(0, 0, 0),
            FreeCAD.Vector(100, 0, 0),
            FreeCAD.Vector(100, 50, 0),
            FreeCAD.Vector(0, 50, 0)
        ]
        rect1_lines = [
            Part.LineSegment(rect1_points[i], rect1_points[(i+1)%4])
            for i in range(4)
        ]

        # Create second identical rectangle
        rect2_points = [
            FreeCAD.Vector(0, 0, 0),
            FreeCAD.Vector(100, 0, 0),
            FreeCAD.Vector(100, 50, 0),
            FreeCAD.Vector(0, 50, 0)
        ]
        rect2_lines = [
            Part.LineSegment(rect2_points[i], rect2_points[(i+1)%4])
            for i in range(4)
        ]

        # Compare each line
        for i in range(4):
            self.assert_lines_equal(rect1_lines[i], rect2_lines[i],
                                  f"Line {i} differs between rectangles")

    def test_comparing_translated_rectangles(self):
        """Test comparing two rectangles with same shape but different positions."""
        # Create first rectangle at origin
        rect1_points = [
            FreeCAD.Vector(0, 0, 0),
            FreeCAD.Vector(100, 0, 0),
            FreeCAD.Vector(100, 50, 0),
            FreeCAD.Vector(0, 50, 0)
        ]
        rect1_lines = [
            Part.LineSegment(rect1_points[i], rect1_points[(i+1)%4])
            for i in range(4)
        ]

        # Create second rectangle translated by (10, 10, 0)
        translation = FreeCAD.Vector(10, 10, 0)
        rect2_points = [p.add(translation) for p in rect1_points]
        rect2_lines = [
            Part.LineSegment(rect2_points[i], rect2_points[(i+1)%4])
            for i in range(4)
        ]

        # Compare dimensions and shape
        for i in range(4):
            # Compare lengths
            self.assertAlmostEqual(
                rect1_lines[i].length(),
                rect2_lines[i].length(),
                delta=self.epsilon,
                msg=f"Line {i} length differs between rectangles"
            )

            # Compare angles between consecutive lines
            v1_current = rect1_lines[i].EndPoint - rect1_lines[i].StartPoint
            v1_next = rect1_lines[(i+1)%4].EndPoint - rect1_lines[(i+1)%4].StartPoint
            v2_current = rect2_lines[i].EndPoint - rect2_lines[i].StartPoint
            v2_next = rect2_lines[(i+1)%4].EndPoint - rect2_lines[(i+1)%4].StartPoint

            angle1 = math.degrees(math.acos(
                (v1_current.x * v1_next.x + v1_current.y * v1_next.y) /
                (v1_current.Length * v1_next.Length)
            ))
            angle2 = math.degrees(math.acos(
                (v2_current.x * v2_next.x + v2_current.y * v2_next.y) /
                (v2_current.Length * v2_next.Length)
            ))
            
            self.assertAlmostEqual(
                angle1, angle2,
                delta=self.epsilon,
                msg=f"Angle at corner {i} differs between rectangles"
            )

    def test_comparing_shape_objects(self):
        """Test comparing rectangles as complete shapes."""
        # Create first rectangle as a shape
        points1 = [
            FreeCAD.Vector(0, 0, 0),
            FreeCAD.Vector(100, 0, 0),
            FreeCAD.Vector(100, 50, 0),
            FreeCAD.Vector(0, 50, 0)
        ]
        wire1 = Part.makePolygon(points1 + [points1[0]])
        face1 = Part.Face(wire1)

        # Create second rectangle as a shape
        points2 = [
            FreeCAD.Vector(0, 0, 0),
            FreeCAD.Vector(100, 0, 0),
            FreeCAD.Vector(100, 50, 0),
            FreeCAD.Vector(0, 50, 0)
        ]
        wire2 = Part.makePolygon(points2 + [points2[0]])
        face2 = Part.Face(wire2)

        # Compare areas
        self.assertAlmostEqual(face1.Area, face2.Area, delta=self.epsilon,
                             msg="Rectangle areas differ")

        # Compare perimeters
        self.assertAlmostEqual(wire1.Length, wire2.Length, delta=self.epsilon,
                             msg="Rectangle perimeters differ")

        # Compare bounding boxes
        bbox1 = face1.BoundBox
        bbox2 = face2.BoundBox
        self.assertAlmostEqual(bbox1.DiagonalLength, bbox2.DiagonalLength,
                             delta=self.epsilon,
                             msg="Rectangle diagonal lengths differ")

if __name__ == '__main__':
    unittest.main()

#-------------------

from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float

@dataclass
class Context:
    sketch: Sketcher.SketchObject
    pen_state: str
    position: Position
    polyline: List[Part.LineSegment]
    polyline_points: List[Tuple[float, float]]
    geometries: List[Part.LineSegment]
    constraints: List

def pendown(sketch: Sketcher.SketchObject, point: Tuple[float, float]) -> None:
    context = Context(sketch=sketch, pen_state='up', position=Position(0, 0), polyline=[], polyline_points=[], geometries=[], constraints=[])
    context.position.x = point[0]
    context.position.y = point[1]
    ...


import unittest
import FreeCAD
import Part
import Sketcher
import math

class TestSketchComparison(unittest.TestCase):
    def setUp(self):
        self.doc = FreeCAD.newDocument("TestDoc")
        
        # Create first sketch
        self.body1 = self.doc.addObject('PartDesign::Body', 'Body1')
        self.sketch1 = self.doc.addObject('Sketcher::SketchObject', 'Sketch1')
        self.body1.addObject(self.sketch1)
        
        # Create second sketch
        self.body2 = self.doc.addObject('PartDesign::Body', 'Body2')
        self.sketch2 = self.doc.addObject('Sketcher::SketchObject', 'Sketch2')
        self.body2.addObject(self.sketch2)
        
    def create_rectangle1(self):
        """Creates rectangle using four lines and constraints"""
        # Create a 10x20 rectangle with lines and constraints
        self.sketch1.addGeometry(Part.LineSegment(FreeCAD.Vector(0,0,0),
                                                FreeCAD.Vector(10,0,0)))
        self.sketch1.addGeometry(Part.LineSegment(FreeCAD.Vector(10,0,0),
                                                FreeCAD.Vector(10,20,0)))
        self.sketch1.addGeometry(Part.LineSegment(FreeCAD.Vector(10,20,0),
                                                FreeCAD.Vector(0,20,0)))
        self.sketch1.addGeometry(Part.LineSegment(FreeCAD.Vector(0,20,0),
                                                FreeCAD.Vector(0,0,0)))
        
        # Add constraints (perpendicular corners)
        self.sketch1.addConstraint(Sketcher.Constraint('Perpendicular',0,1))
        self.sketch1.addConstraint(Sketcher.Constraint('Perpendicular',1,2))
        self.sketch1.addConstraint(Sketcher.Constraint('Perpendicular',2,3))
        self.sketch1.addConstraint(Sketcher.Constraint('Perpendicular',3,0))
        
    def create_rectangle2(self):
        """Creates same rectangle using different approach (rectangle tool simulation)"""
        # Create same 10x20 rectangle but with different construction method
        self.sketch2.addGeometry(Part.Rectangle(FreeCAD.Vector(0,0,0),
                                              FreeCAD.Vector(10,20,0)))
    
    def are_sketches_equal(self, sketch1, sketch2, tolerance=1e-7):
        """
        Compare two sketches to check if they produce the same geometry
        Returns: bool, string (True/False, explanation message)
        """
        try:
            # Get shapes from sketches
            shape1 = sketch1.Shape
            shape2 = sketch2.Shape
            
            if shape1.isNull() or shape2.isNull():
                return False, "One or both shapes are null"
            
            # Compare basic properties
            if len(shape1.Edges) != len(shape2.Edges):
                return False, f"Different number of edges: {len(shape1.Edges)} vs {len(shape2.Edges)}"
            
            # Compare areas
            area1 = shape1.Area
            area2 = shape2.Area
            if abs(area1 - area2) > tolerance:
                return False, f"Different areas: {area1} vs {area2}"
            
            # Compare bounding boxes
            bbox1 = shape1.BoundBox
            bbox2 = shape2.BoundBox
            if (abs(bbox1.XLength - bbox2.XLength) > tolerance or
                abs(bbox1.YLength - bbox2.YLength) > tolerance):
                return False, "Different bounding box dimensions"
            
            # Compare vertices (allowing for different vertex order)
            verts1 = sorted([(v.X, v.Y) for v in shape1.Vertexes])
            verts2 = sorted([(v.X, v.Y) for v in shape2.Vertexes])
            
            for v1, v2 in zip(verts1, verts2):
                if (abs(v1[0] - v2[0]) > tolerance or
                    abs(v1[1] - v2[1]) > tolerance):
                    return False, f"Vertex mismatch: {v1} vs {v2}"
            
            return True, "Sketches are geometrically equivalent"
            
        except Exception as e:
            return False, f"Comparison failed: {str(e)}"
    
    def test_rectangle_equality(self):
        # Create rectangles using different methods
        self.create_rectangle1()
        self.create_rectangle2()
        
        # Recompute both sketches
        self.doc.recompute()
        
        # Compare the sketches
        are_equal, message = self.are_sketches_equal(self.sketch1, self.sketch2)
        
        # Assert they are equal
        self.assertTrue(are_equal, f"Rectangles should be equal. {message}")
        
        # Test with slightly different rectangle (negative test)
        sketch3 = self.doc.addObject('Sketcher::SketchObject', 'Sketch3')
        sketch3.addGeometry(Part.Rectangle(FreeCAD.Vector(0,0,0),
                                         FreeCAD.Vector(10,20.1,0)))
        self.doc.recompute()
        
        are_equal, message = self.are_sketches_equal(self.sketch1, sketch3)
        self.assertFalse(are_equal, "Rectangles with different dimensions should not be equal")
        
    def tearDown(self):
        FreeCAD.closeDocument("TestDoc")

if __name__ == '__main__':
    unittest.main()