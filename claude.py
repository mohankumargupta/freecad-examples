import unittest
import FreeCAD
import Part
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