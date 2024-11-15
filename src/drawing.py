import FreeCAD as App
from FreeCAD import Base # type: ignore
import Part # type: ignore
from Part import LineSegment # type: ignore
import Sketcher # type: ignore

import math

#LineSegment = Part.LineSegment
Vector2D = Base.Vector2d

def _polyline_functions():
    context = {
        'pen_state': 'up',
        'position': {'x': 0, 'y': 0},
        'polyline_points': [],
        'geometries': [],
        'constraints': []
    }

    def createLinesFromPoints():
        polyline_count = len(context['polyline_points'])
        lines = [
            Part.LineSegment(context['polyline_points'][i], context['polyline_points'][(i+1)%polyline_count])
            for i in range(polyline_count)
        ]
        context['geometries'] += lines
        context['polyline_points'] = []


    def createGeometriesFromLines():
        pass


    def pendown(x,y):
        context['position']['x'] = x
        context['position']['y'] = y
        context['polyline_points'].append(
            LineSegment(Vector2D(x,y))
        )

    def penup():
        pass

    def move():
        pass

    def up(distance):
        pass

    def down(distance):
        pass

    def left(distance):
        pass

    def right(distance):
        pass    

    return {
        'penup': penup,
        'pendown': pendown,
        'up': up,
        'down': down,
        'left': left,
        'right': right
    }

_turtle = _polyline_functions()
penup = _turtle['penup']
pendown = _turtle['pendown']
up = _turtle['up']
down = _turtle['down']
left = _turtle['left']
right = _turtle['right']

def makeRectangle(sketch, corner, lengths):
    hmin, hmax = corner[0], corner[0] + lengths[0]
    vmin, vmax = corner[1], corner[1] + lengths[1]

    i = int(sketch.GeometryCount)
    sketch.addGeometry(
        Part.LineSegment(App.Vector(hmin, vmax), App.Vector(hmax, vmax, 0))
    )
    sketch.addGeometry(
        Part.LineSegment(App.Vector(hmax, vmax, 0), App.Vector(hmax, vmin, 0))
    )
    sketch.addGeometry(
        Part.LineSegment(App.Vector(hmax, vmin, 0), App.Vector(hmin, vmin, 0))
    )
    sketch.addGeometry(
        Part.LineSegment(App.Vector(hmin, vmin, 0), App.Vector(hmin, vmax, 0))
    )

    # add the rectangular constraints
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 0, 2, i + 1, 1))
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 1, 2, i + 2, 1))
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 2, 2, i + 3, 1))
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 3, 2, i + 0, 1))

    sketch.addConstraint(Sketcher.Constraint("Horizontal", i + 0))
    sketch.addConstraint(Sketcher.Constraint("Horizontal", i + 2))
    sketch.addConstraint(Sketcher.Constraint("Vertical", i + 1))
    sketch.addConstraint(Sketcher.Constraint("Vertical", i + 3))

    sketch.addConstraint(Sketcher.Constraint("Distance", 0,1,0,2,lengths[0]))
    sketch.addConstraint(Sketcher.Constraint("Distance", 1,1,1,2,lengths[1]))

    if hmin == 0:
        sketch.addConstraint(Sketcher.Constraint("PointOnObject", 2,2, -2))

    else:
        sketch.addConstraint(Sketcher.Constraint("DistanceX", 2, 2, hmin))

    if vmin == 0:
        sketch.addConstraint(Sketcher.Constraint("PointOnObject", 2,2, -1))
        
    else:    
        sketch.addConstraint(Sketcher.Constraint("DistanceY", 2, 2, vmin))

    

def makeCenterRectangle(sketch, center, lengths):
    """
    Creates a rectangle centered at a given point.
    
    Parameters:
    sketch: The FreeCAD sketch object
    center: Tuple (x, y) representing the center point
    lengths: Tuple (width, height) representing rectangle dimensions
    """
    # Calculate corner point from center and dimensions
    corner_x = center[0] - lengths[0]/2
    corner_y = center[1] - lengths[1]/2
    corner = (corner_x, corner_y)
    
    # Use existing makeRectangle function with calculated corner
    makeRectangle(sketch, corner, lengths)
    
    # The index of the last geometry before our rectangle
    i = int(sketch.GeometryCount) - 4
    
    # Add constraints to ensure center point
    # Constrain horizontal center
    #sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 0, 1, center[0]))
    #sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 2, 1, center[0]))
    
    # Constrain vertical center
    #sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 1, 1, center[1]))
    #sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 3, 1, center[1]))

def makeCircle(sketch, center, radius):
    i = int(sketch.GeometryCount)
    sketch.addGeometry(Part.Circle(App.Vector(*center), App.Vector(0, 0, 1), radius), False)
    sketch.addConstraint(Sketcher.Constraint("Radius", i, radius))
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 3, center[0]))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 3, center[1]))

def makeArcThreePoint(sketch, start_point, mid_point, end_point):
    """
    Creates an arc that passes through three points.
    
    Parameters:
    sketch: The FreeCAD sketch object
    start_point: Tuple (x, y) or Vector representing the start point of the arc
    mid_point: Tuple (x, y) or Vector representing a point the arc passes through
    end_point: Tuple (x, y) or Vector representing the end point of the arc
    """
    # Convert tuples to Vectors if necessary
    start = App.Vector(*start_point) if not isinstance(start_point, App.Vector) else start_point
    mid = App.Vector(*mid_point) if not isinstance(mid_point, App.Vector) else mid_point
    end = App.Vector(*end_point) if not isinstance(end_point, App.Vector) else end_point
    
    # Ensure Z coordinates are 0
    start.z = mid.z = end.z = 0
    
    # Get the current geometry count
    i = int(sketch.GeometryCount)
    
    # Create an arc through three points
    arc = Part.ArcOfCircle(start, mid, end)
    sketch.addGeometry(arc, False)
    
    # Add constraints to fix the three points
    # Start point
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 1, start.x))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 1, start.y))
    
    # End point
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 2, end.x))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 2, end.y))
    
    # Mid point (point on arc)
    sketch.addConstraint(Sketcher.Constraint("PointOnObject", i, 3, i))  # Point lies on arc
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 3, mid.x))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 3, mid.y))

    return i  # Return the index of the created geometry

def makeHorizontalLine(sketch, start_point, length):
    """
    Creates a horizontal line starting from a point with given length.
    
    Parameters:
    sketch: The FreeCAD sketch object
    start_point: Tuple (x, y) or Vector representing the start point of the line
    length: Float representing the length of the line
    
    Returns:
    int: Index of the created geometry
    """
    # Convert tuple to Vector if necessary
    start = App.Vector(*start_point) if not isinstance(start_point, App.Vector) else start_point
    
    # Ensure Z coordinate is 0
    start.z = 0
    
    # Calculate end point (horizontal line so only X changes)
    end = App.Vector(start.x + length, start.y, 0)
    
    # Get current geometry count
    i = int(sketch.GeometryCount)
    
    # Create the line
    line = Part.LineSegment(start, end)
    sketch.addGeometry(line, False)
    
    # Add horizontal constraint
    sketch.addConstraint(Sketcher.Constraint("Horizontal", i))
    
    # Fix start point
    #sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 1, start.x))
    #sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 1, start.y))
    
    # Set length
    #sketch.addConstraint(Sketcher.Constraint("Distance", i, length))
    
    return i  # Return the index of the created geometry

def makeVerticalLine(sketch, start_point, length):
    """
    Creates a vertical line starting from a point with given length.
    
    Parameters:
    sketch: The FreeCAD sketch object
    start_point: Tuple (x, y) or Vector representing the start point of the line
    length: Float representing the length of the line
    
    Returns:
    int: Index of the created geometry
    """
    # Convert tuple to Vector if necessary
    start = App.Vector(*start_point) if not isinstance(start_point, App.Vector) else start_point
    
    # Ensure Z coordinate is 0
    start.z = 0
    
    # Calculate end point (vertical line so only Y changes)
    end = App.Vector(start.x, start.y + length, 0)
    
    # Get current geometry count
    i = int(sketch.GeometryCount)
    
    # Create the line
    line = Part.LineSegment(start, end)
    sketch.addGeometry(line, False)
    
    # Add vertical constraint
    sketch.addConstraint(Sketcher.Constraint("Vertical", i))
    
    # Fix start point
    #sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 1, start.x))
    #sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 1, start.y))
    
    # Set length
    #sketch.addConstraint(Sketcher.Constraint("Distance", i, length))
    
    return i  # Return the index of the created geometry

def makeHorizontalSlot(sketch, start_point, length, width):
    """
    Creates a horizontal slot (two half circles connected by lines) starting from a point.
    
    Parameters:
    sketch: The FreeCAD sketch object
    start_point: Tuple (x, y) or Vector representing the start point of the slot
    length: Float representing the total length of the slot
    width: Float representing the width of the slot (diameter of end circles)
    
    Returns:
    tuple: Indices of the created geometries (left_arc, top_line, right_arc, bottom_line)
    """
    # Convert tuple to Vector if necessary
    start = App.Vector(*start_point) if not isinstance(start_point, App.Vector) else start_point
    start.z = 0
    
    radius = width / 2
    # Calculate key points
    center_left = App.Vector(start.x + radius, start.y, 0)
    center_right = App.Vector(start.x + length - radius, start.y, 0)
    
    # Get starting index
    i = int(sketch.GeometryCount)
    
    # Create left arc (180 degrees, from bottom to top)
    start_left = App.Vector(start.x, start.y, 0)
    mid_left = App.Vector(start.x + radius, start.y + radius, 0)
    end_left = App.Vector(start.x + 2 * radius, start.y, 0)
    arc_left = Part.ArcOfCircle(start_left, mid_left, end_left)
    sketch.addGeometry(arc_left, False)
    
    # Create top horizontal line
    line_top = Part.LineSegment(end_left, App.Vector(start.x + length, start.y, 0))
    sketch.addGeometry(line_top, False)
    
    # Create right arc (180 degrees, from top to bottom)
    start_right = App.Vector(start.x + length, start.y, 0)
    mid_right = App.Vector(start.x + length - radius, start.y - radius, 0)
    end_right = App.Vector(start.x + length - 2 * radius, start.y, 0)
    arc_right = Part.ArcOfCircle(start_right, mid_right, end_right)
    sketch.addGeometry(arc_right, False)
    
    # Create bottom horizontal line
    line_bottom = Part.LineSegment(end_right, start_left)
    sketch.addGeometry(line_bottom, False)
    
    # Add constraints
    # Connect all segments
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 0, 2, i + 1, 1))  # Left arc to top line
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 1, 2, i + 2, 1))  # Top line to right arc
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 2, 2, i + 3, 1))  # Right arc to bottom line
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 3, 2, i + 0, 1))  # Bottom line to left arc
    
    # Make lines horizontal
    sketch.addConstraint(Sketcher.Constraint("Horizontal", i + 1))  # Top line
    sketch.addConstraint(Sketcher.Constraint("Horizontal", i + 3))  # Bottom line
    
    # Equal radius for both arcs
    sketch.addConstraint(Sketcher.Constraint("Equal", i + 0, i + 2))
    
    # Fix start point position
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 0, 1, start.x))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 0, 1, start.y))
    
    # Set dimensions
    sketch.addConstraint(Sketcher.Constraint("Radius", i + 0, radius))  # Width through radius
    sketch.addConstraint(Sketcher.Constraint("Distance", i + 1, length))  # Total length
    
    return (i, i + 1, i + 2, i + 3)  # Return indices of all created geometries

def makeVerticalSlot(sketch, start_point, length, width):
    """
    Creates a vertical slot (two half circles connected by lines) starting from a point.
    
    Parameters:
    sketch: The FreeCAD sketch object
    start_point: Tuple (x, y) or Vector representing the start point of the slot
    length: Float representing the total length of the slot
    width: Float representing the width of the slot (diameter of end circles)
    
    Returns:
    tuple: Indices of the created geometries (bottom_arc, right_line, top_arc, left_line)
    """
    # Convert tuple to Vector if necessary
    start = App.Vector(*start_point) if not isinstance(start_point, App.Vector) else start_point
    start.z = 0
    
    radius = width / 2
    # Calculate key points
    center_bottom = App.Vector(start.x, start.y + radius, 0)
    center_top = App.Vector(start.x, start.y + length - radius, 0)
    
    # Get starting index
    i = int(sketch.GeometryCount)
    
    # Create bottom arc (180 degrees, from left to right)
    start_bottom = App.Vector(start.x, start.y, 0)
    mid_bottom = App.Vector(start.x + radius, start.y + radius, 0)
    end_bottom = App.Vector(start.x, start.y + 2 * radius, 0)
    arc_bottom = Part.ArcOfCircle(start_bottom, mid_bottom, end_bottom)
    sketch.addGeometry(arc_bottom, False)
    
    # Create right vertical line
    line_right = Part.LineSegment(end_bottom, App.Vector(start.x, start.y + length, 0))
    sketch.addGeometry(line_right, False)
    
    # Create top arc (180 degrees, from right to left)
    start_top = App.Vector(start.x, start.y + length, 0)
    mid_top = App.Vector(start.x - radius, start.y + length - radius, 0)
    end_top = App.Vector(start.x, start.y + length - 2 * radius, 0)
    arc_top = Part.ArcOfCircle(start_top, mid_top, end_top)
    sketch.addGeometry(arc_top, False)
    
    # Create left vertical line
    line_left = Part.LineSegment(end_top, start_bottom)
    sketch.addGeometry(line_left, False)
    
    # Add constraints
    # Connect all segments
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 0, 2, i + 1, 1))  # Bottom arc to right line
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 1, 2, i + 2, 1))  # Right line to top arc
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 2, 2, i + 3, 1))  # Top arc to left line
    sketch.addConstraint(Sketcher.Constraint("Coincident", i + 3, 2, i + 0, 1))  # Left line to bottom arc
    
    # Make lines vertical
    sketch.addConstraint(Sketcher.Constraint("Vertical", i + 1))  # Right line
    sketch.addConstraint(Sketcher.Constraint("Vertical", i + 3))  # Left line
    
    # Equal radius for both arcs
    sketch.addConstraint(Sketcher.Constraint("Equal", i + 0, i + 2))
    
    # Fix start point position
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 0, 1, start.x))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 0, 1, start.y))
    
    # Set dimensions
    sketch.addConstraint(Sketcher.Constraint("Radius", i + 0, radius))  # Width through radius
    sketch.addConstraint(Sketcher.Constraint("Distance", i + 1, length))  # Total length
    
    return (i, i + 1, i + 2, i + 3)  # Return indices of all created geometries

def makeCenterArc(sketch, center_point, radius, start_angle, end_angle):
    """
    Creates an arc defined by center point, radius, and start/end angles.
    
    Parameters:
    sketch: The FreeCAD sketch object
    center_point: Tuple (x, y) or Vector representing the center point of the arc
    radius: Float representing the radius of the arc
    start_angle: Float representing the starting angle in degrees (0 = positive X axis)
    end_angle: Float representing the ending angle in degrees
    
    Returns:
    int: Index of the created geometry
    """
    # Convert tuple to Vector if necessary
    center = App.Vector(*center_point) if not isinstance(center_point, App.Vector) else center_point
    center.z = 0
    
    # Convert angles to radians
    start_rad = math.radians(start_angle)
    end_rad = math.radians(end_angle)
    
    # Calculate start, end and middle points
    start = App.Vector(
        center.x + radius * math.cos(start_rad),
        center.y + radius * math.sin(start_rad),
        0
    )
    end = App.Vector(
        center.x + radius * math.cos(end_rad),
        center.y + radius * math.sin(end_rad),
        0
    )
    
    # Calculate a point in the middle of the arc
    mid_angle = (start_rad + end_rad) / 2
    mid = App.Vector(
        center.x + radius * math.cos(mid_angle),
        center.y + radius * math.sin(mid_angle),
        0
    )
    
    # Get current geometry count
    i = int(sketch.GeometryCount)
    
    # Create the arc through three points
    arc = Part.ArcOfCircle(start, mid, end)
    sketch.addGeometry(arc, False)
    
    # Fix the center point
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 3, center.x))  # Center X position
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 3, center.y))  # Center Y position
    
    # Fix the radius
    sketch.addConstraint(Sketcher.Constraint("Radius", i, radius))
    
    # Fix the start and end points
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 1, start.x))  # Start X position
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 1, start.y))  # Start Y position
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i, 2, end.x))    # End X position
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i, 2, end.y))    # End Y position
    
    return i  # Return the index of the created geometry    