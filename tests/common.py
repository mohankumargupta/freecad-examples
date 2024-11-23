from FreeCAD import Vector
import FreeCAD as App
import Part # type: ignore
import Sketcher # type: ignore
from collections import Counter

def are_sketches_geometrically_equal(sketch1, sketch2, tolerance=1e-7):
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
        
        # # Compare areas
        # area1 = shape1.Area
        # area2 = shape2.Area
        # if abs(area1 - area2) > tolerance:
        #     return False, f"Different areas: {area1} vs {area2}"
        
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

def are_sketches_equal(sketch1, sketch2):
    return are_sketches_geometrically_equal(sketch1, sketch2) and compare_constraints(sketch1, sketch2)

def create_rectangle(sketch, bottom_left_corner, width, height):
        x,y = bottom_left_corner
        sketch.addGeometry(Part.LineSegment(Vector(x,y,0),
                                                Vector(x+width,y,0)))
        sketch.addGeometry(Part.LineSegment(Vector(x+width, y, 0),
                                                Vector(x+width, y+height, 0)))
        sketch.addGeometry(Part.LineSegment(Vector(x+width, y+height, 0),
                                                Vector(x, y+height, 0)))
        sketch.addGeometry(Part.LineSegment(Vector(x, y+height, 0),
                                                Vector(x,y,0)))
    
def create_rectangle_80x40_fully_constrained(sketch):
    geoList = []
    geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(80.000000, 0.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(80.000000, 0.000000, 0.000000),App.Vector(80.000000, 40.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(80.000000, 40.000000, 0.000000),App.Vector(0.000000, 40.000000, 0.000000)))
    geoList.append(Part.LineSegment(App.Vector(0.000000, 40.000000, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
    sketch.addGeometry(geoList,False)
    del geoList
    
    constraintList = []
    constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
    constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
    constraintList.append(Sketcher.Constraint('Horizontal', 0))
    constraintList.append(Sketcher.Constraint('Horizontal', 2))
    constraintList.append(Sketcher.Constraint('Vertical', 1))
    constraintList.append(Sketcher.Constraint('Vertical', 3))
    sketch.addConstraint(constraintList)
    del constraintList
    
    sketch.addConstraint(Sketcher.Constraint('DistanceX',- 1,1,0,1,80.000000)) 
    sketch.addConstraint(Sketcher.Constraint('DistanceY',-1,1,0,1,40.000000)) 
    sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

def get_constraint_signature(constraint):
    """
    Creates a comparable signature for a constraint, ignoring internal indexes
    
    Args:
        constraint: A FreeCAD sketch constraint
        
    Returns:
        tuple: (constraint_type, relevant_values) that can be used for comparison
    """
    # Get base type
    c_type = constraint.Type
    
    # Handle different constraint types
    if c_type == 'Distance':
        return (c_type, round(constraint.Value, 7))
    elif c_type == 'DistanceX' or c_type == 'DistanceY':
        return (c_type, round(constraint.Value, 7))
    elif c_type == 'Angle':
        return (c_type, round(constraint.Value, 7))
    elif c_type in ['Horizontal', 'Vertical']:
        return (c_type,)
    elif c_type == 'Parallel':
        return (c_type,)
    elif c_type == 'Perpendicular':
        return (c_type,)
    elif c_type == 'Equal':
        return (c_type,)
    elif c_type == 'Coincident':
        return (c_type,)
    elif c_type == 'Radius':
        return (c_type, round(constraint.Value, 7))
    else:
        return (c_type, getattr(constraint, 'Value', None))

def compare_constraints(sketch1, sketch2):
    """
    Compare constraints between two sketches
    
    Args:
        sketch1: First FreeCAD sketch
        sketch2: Second FreeCAD sketch
        
    Returns:
        tuple: (bool, str) - (True if constraints are equivalent, explanation message)
    """
    try:
        constraints1 = sketch1.Constraints
        constraints2 = sketch2.Constraints
        
        # Get signatures for all constraints
        sigs1 = [get_constraint_signature(c) for c in constraints1]
        sigs2 = [get_constraint_signature(c) for c in constraints2]
        
        # Count occurrences of each constraint signature
        count1 = Counter(sigs1)
        count2 = Counter(sigs2)
        
        if count1 != count2:
            # Find differences
            missing_in_2 = count1 - count2
            extra_in_2 = count2 - count1
            
            msg = []
            if missing_in_2:
                msg.append(f"Constraints in sketch1 but not in sketch2: {dict(missing_in_2)}")
            if extra_in_2:
                msg.append(f"Constraints in sketch2 but not in sketch1: {dict(extra_in_2)}")
                
            return False, "\n".join(msg)
            
        return True, "Constraints are equivalent"
        
    except Exception as e:
        return False, f"Comparison failed: {str(e)}"

