import pytest
import FreeCAD
import Part # type: ignore
import os

class TestRectangleDrawing:
    @classmethod
    def setup_class(cls):
        # Create a new document for testing
        cls.doc = FreeCAD.newDocument("TestDoc")
    
    @classmethod
    def teardown_class(cls):
        # Close and delete the test document
        FreeCAD.closeDocument("TestDoc")
        test_file = "TestDoc.FCStd"
        if os.path.exists(test_file):
            os.remove(test_file)

    def test_create_rectangle(self):
        # Define rectangle parameters
        length = 100.0
        width = 50.0
        
        # Create rectangle vertices
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(length, 0, 0)
        v3 = FreeCAD.Vector(length, width, 0)
        v4 = FreeCAD.Vector(0, width, 0)
        
        # Create edges
        edge1 = Part.makeLine(v1, v2)
        edge2 = Part.makeLine(v2, v3)
        edge3 = Part.makeLine(v3, v4)
        edge4 = Part.makeLine(v4, v1)
        
        # Create wire from edges
        wire = Part.Wire([edge1, edge2, edge3, edge4])
        
        # Create face from wire
        face = Part.Face(wire)
        
        # Create a shape object in the document
        rectangle = self.doc.addObject("Part::Feature", "Rectangle")
        rectangle.Shape = face
        
        # Test assertions
        assert rectangle is not None
        assert rectangle.Shape is not None
        assert isinstance(rectangle.Shape, Part.Shape)
        assert len(rectangle.Shape.Edges) == 4
        assert abs(rectangle.Shape.Area - (length * width)) < 1e-7
        
        # Test dimensions
        bbox = rectangle.Shape.BoundBox
        assert abs(bbox.XLength - length) < 1e-7
        assert abs(bbox.YLength - width) < 1e-7
        
    def test_invalid_rectangle(self):
        # Test that creating a rectangle with invalid dimensions raises an exception
        with pytest.raises(Part.OCCError):
            v1 = FreeCAD.Vector(0, 0, 0)
            v2 = FreeCAD.Vector(0, 0, 0)  # Invalid: same point
            edge = Part.makeLine(v1, v2)