from FreeCAD import Vector
import FreeCAD as App
import Part # type: ignore

def are_sketches_equal(sketch1, sketch2, tolerance=1e-7):
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

def create_rectangle(sketch, bottom_left_corner, width, height):
        x,y = bottom_left_corner
        sketch.addGeometry(Part.LineSegment(Vector(x,y,0),
                                                Vector(x+width,y,0)))
        sketch.addGeometry(Part.LineSegment(Vector(x+width, y, 0),
                                                Vector(x+width, y+height, 0)))
        sketch.addGeometry(Part.LineSegment(Vector(x+width, y+height, 0),
                                                Vector(x, y+height, 0)))
        sketch.addGeometry(Part.LineSegment(Vector(x, y+height, 0),
                                                Vector(0,0,0)))
    
