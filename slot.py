import FreeCAD as App
import Part  # type: ignore
import Sketcher # type: ignore

def create_slot(doc, sketch, length=40, width=10, depth=5, position=App.Vector(50, 0, 0)):
    """
    Creates a slot feature using FreeCAD Python API
    
    Parameters:
    length (float): Length of the slot in mm
    width (float): Width of the slot in mm
    depth (float): Depth of the slot in mm
    position (Vector): Position vector for the slot origin
    
    Returns:
    The created feature
    """

    # Calculate dimensions
    radius = width / 2
    
    # Add geometry to create slot profile
    # Center line
    sketch.addGeometry(Part.LineSegment(App.Vector(0, 0, 0), App.Vector(length, 0, 0)), True)
    
    # Create semicircles at ends
    # radius = width / 2
    # sketch.addGeometry(Part.ArcOfCircle(
    #     Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), radius),
    #     -1.5708, 1.5708))  # -90 to 90 degrees
    # sketch.addGeometry(Part.ArcOfCircle(
    #     Part.Circle(App.Vector(length, 0, 0), App.Vector(0, 0, 1), radius),
    #     1.5708, 4.7124))   # 90 to 270 degrees
    
    # Add semicircles at ends (outward facing)
    sketch.addGeometry(Part.ArcOfCircle(
        Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), radius),
        1.570800, 4.712393))  # Left end: -90 to 90 degrees
    # sketch.addGeometry(Part.ArcOfCircle(
    #     Part.Circle(App.Vector(length, 0, 0), App.Vector(0, 0, 1), radius),
    #     1.570800, 4.712393))   # Right end: 90 to 270 degrees
    sketch.addGeometry(Part.ArcOfCircle(
        Part.Circle(App.Vector(length, 0, 0), App.Vector(0, 0, 1), radius),
         4.712393, 7.853985))   # Right end: 90 to 270 degrees



    # Connect semicircles with lines
    sketch.addGeometry(Part.LineSegment(
        App.Vector(0, radius, 0), App.Vector(length, radius, 0)))
    sketch.addGeometry(Part.LineSegment(
        App.Vector(length, -radius, 0), App.Vector(0, -radius, 0)))
    
    # Add constraints to make the sketch fully constrained
    # sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, 1, 1))  # Line to arc
    # sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 2, 1))  # Line to arc
    # sketch.addConstraint(Sketcher.Constraint('Equal', 1, 2))  # Equal radius arcs
    # sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))  # Horizontal center line
    # sketch.addConstraint(Sketcher.Constraint('Horizontal', 3))  # Horizontal top line
    # sketch.addConstraint(Sketcher.Constraint('Horizontal', 4))  # Horizontal bottom line
    
    # Create pad
    pad = doc.addObject("PartDesign::Pad", "Slot")
    pad.Profile = sketch
    pad.Length = depth
    

    #return pad
