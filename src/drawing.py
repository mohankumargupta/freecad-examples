# import FreeCAD as App
# from FreeCAD import Vector # type: ignore
# import Part # type: ignore
# from Part import LineSegment # type: ignore
# import Sketcher # type: ignore

# import math

# #LineSegment = Part.LineSegment


# def _polyline_functions():
#     context = {
#         'sketch': None,
#         'initial_position': None,
#         'pen_state': 'up',
#         'position': {'x': 0, 'y': 0},
#         'polyline': [],
#         'polyline_points': [],
#         'geometries': [],
#         'constraints': []
#     }

#     def pendown(sketch, point):
#         x,y = point
#         context['sketch'] = sketch
#         context['position']['x'] = x
#         context['position']['y'] = y
#         context["initial_position"] = point

#     def penup(pos=None):
#         count = len(context['sketch'].Geometry)
#         constraintList = []
#         for i in range(0, count - 1):
#             constraintList.append(Sketcher.Constraint("Coincident", i, 2, i+1, 1))
#         constraintList.append(Sketcher.Constraint("Coincident", count - 1, 2, 0, 1))
                
#         if pos:
#             x,y =pos
#             if pos == (0,0):
#                 constraintList.append(Sketcher.Constraint("Coincident", 0, 1, -1, 1))

#             elif x == 0:
#                 pass
#             elif y ==0:
#                 pass
#             else:
#                 constraintList.append(Sketcher.Constraint("DistanceX", 0, 1, x))
#                 constraintList.append(Sketcher.Constraint("DistanceY", 0, 1, y)) 


#         else:
#             pass

#         context['sketch'].addConstraint(constraintList)
        

#     def move(distance_x, distance_y, constraint_type):
#         x = context['position']['x']
#         y = context['position']['y']
#         geoId = context['sketch'].addGeometry(
#             LineSegment(Vector(x,y), Vector(x + distance_x,y+distance_y))
#         )

#         if constraint_type:
#             context['sketch'].addConstraint(
#                 Sketcher.Constraint(constraint_type, geoId)
#             )            
        
#         #context['polyline'].append(
#         #    LineSegment(Vector(x,y), Vector(x + distance_x,y+distance_y))
#         #)
#         context['position']['x'] = x + distance_x
#         context['position']['y'] = y + distance_y        

#     def up(distance):
#         move(0,distance, "Vertical")


#     def down(distance):
#         move(0,-distance, "Vertical")

#     def left(distance):
#         move(-distance, 0, "Horizontal")

#     def right(distance):
#         move(distance, 0, "Horizontal")  

#     def arcLeft(left, radius):
#         right_x, right_y = context['position']['x'] , context['position']['y']
#         left_x, left_y = right_x - left, right_y
#         arc = makeArcTwoPoints(context['sketch'], (right_x, right_y, 0), (left_x, left_y, 0), radius)


#     def diagonalSouthWest(length):
#         x, y = context['position']['x'] , context['position']['y']
#         diagonal(context['sketch'], (x,y,0), 180+45, length)


#     return {
#         'penup': penup,
#         'pendown': pendown,
#         'up': up,
#         'down': down,
#         'left': left,
#         'right': right,
#         'arcLeft': arcLeft,
#         'diagonalSouthWest': diagonalSouthWest
#     }

# _turtle = _polyline_functions()
# penup = _turtle['penup']
# pendown = _turtle['pendown']
# up = _turtle['up']
# down = _turtle['down']
# left = _turtle['left']
# right = _turtle['right']
# arcLeft = _turtle['arcLeft']
# diagonalSouthWest = _turtle['diagonalSouthWest']

from typing import Tuple, Optional
import math
import FreeCAD as App
from FreeCAD import Vector
import Part
from Part import LineSegment
import Sketcher

class TurtleSketch:
    """A turtle graphics-style interface for FreeCAD sketching."""
    
    def __init__(self):
        self._sketch = None
        self._position = Vector(0, 0, 0)
        self._initial_position = None

    @property
    def position(self) -> Vector:
        return self._position

    @position.setter
    def position(self, pos: Vector):
        self._position = pos

    def pendown(self, sketch: 'Sketcher.Sketch', point: Tuple[float, float]) -> None:
        """Start drawing from the specified point."""
        x, y = point
        self._sketch = sketch
        self._position = Vector(x, y, 0)
        self._initial_position = point

    def penup(self, pos: Optional[Tuple[float, float]] = None) -> None:
        """Stop drawing and add constraints to close the shape."""
        if not self._sketch:
            return

        geometry_count = len(self._sketch.Geometry)
        constraints = []

        # Connect consecutive segments
        for i in range(geometry_count - 1):
            constraints.append(
                Sketcher.Constraint("Coincident", i, 2, i + 1, 1)
            )
        
        # Close the shape
        if geometry_count > 0:
            constraints.append(
                Sketcher.Constraint("Coincident", geometry_count - 1, 2, 0, 1)
            )

        # Handle positioning constraints
        if pos:
            x, y = pos
            if pos == (0, 0):
                constraints.append(Sketcher.Constraint("Coincident", 0, 1, -1, 1))
            elif x != 0:
                constraints.append(Sketcher.Constraint("DistanceX", 0, 1, x))
            if y != 0:
                constraints.append(Sketcher.Constraint("DistanceY", 0, 1, y))

        self._sketch.addConstraint(constraints)

    def move(self, dx: float, dy: float, constraint_type: Optional[str] = None) -> None:
        """Move the turtle by the specified delta x and y."""
        if not self._sketch:
            return

        end_pos = Vector(self._position.x + dx, self._position.y + dy, 0)
        
        geo_id = self._sketch.addGeometry(
            LineSegment(self._position, end_pos)
        )
        
        if constraint_type:
            self._sketch.addConstraint(
                Sketcher.Constraint(constraint_type, geo_id)
            )
            
        self._position = end_pos

    def up(self, distance: float) -> None:
        """Move turtle upward."""
        self.move(0, distance, "Vertical")

    def down(self, distance: float) -> None:
        """Move turtle downward."""
        self.move(0, -distance, "Vertical")

    def left(self, distance: float) -> None:
        """Move turtle left."""
        self.move(-distance, 0, "Horizontal")

    def right(self, distance: float) -> None:
        """Move turtle right."""
        self.move(distance, 0, "Horizontal")

    def arc_left(self, left_distance: float, radius: float) -> None:
        """Create an arc to the left with given radius."""
        end_pos = Vector(self._position.x - left_distance, self._position.y, 0)
        
        if hasattr(self, 'make_arc_two_points'):
            self.make_arc_two_points(
                self._sketch,
                (self._position.x, self._position.y, 0),
                (end_pos.x, end_pos.y, 0),
                radius
            )

    def diagonal_southwest(self, length: float) -> None:
        """Move diagonally southwest."""
        if hasattr(self, 'diagonal'):
            self.diagonal(
                self._sketch,
                (self._position.x, self._position.y, 0),
                180 + 45,
                length
            )

# Create singleton instance
turtle = TurtleSketch()

# Export common functions
penup = turtle.penup
pendown = turtle.pendown
up = turtle.up
down = turtle.down
left = turtle.left
right = turtle.right
arc_left = turtle.arc_left
diagonal_southwest = turtle.diagonal_southwest


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


def makeArcTwoPoints(sketch, start_point, end_point, radius):
    """
    Creates an arc in the given sketch defined by two points and a radius.

    :param sketch: The FreeCAD Sketch object to which the arc will be added.
    :param point1: A tuple (x1, y1) defining the first point of the arc.
    :param point2: A tuple (x2, y2) defining the second point of the arc.
    :param radius: The radius of the arc.
    :return: None
    """
    # Convert points to FreeCAD Vectors
    p1 = Vector(start_point)
    p2 = Vector(end_point)

    # Calculate the midpoint and chord length
    midpoint = (p1 + p2) * 0.5
    chord_length = (p2 - p1).Length

    # Check if the radius is valid
    if abs(radius) < chord_length / 2:
        raise ValueError("The radius is too small to form an arc with the given points.")

    # Calculate the perpendicular distance from the midpoint to the arc center
    perpendicular_distance = (radius**2 - (chord_length / 2)**2)**0.5

    # Determine the direction of the perpendicular vector
    direction = (p2 - p1).cross(Vector(0, 0, 1)).normalize()

    # Compute the arc center
    center = midpoint + direction * perpendicular_distance * (1 if radius > 0 else -1)

    # Add the arc to the sketch
    #sketch.addArc(center.x, center.y, p1.x, p1.y, p2.x, p2.y, False)

        # Create a circle in 2D with the calculated center and radius
    circle = Part.Circle(center, Vector(0, 0, 1), abs(radius))

    # Rotate p1 around the center by ±90 degrees to get a distinct third point
    vector_to_rotate = p1 - center
    rotation_angle = -90 if radius > 0 else 90
    rotation = App.Rotation(App.Vector(0, 0, 1), rotation_angle)
    third_point = center + rotation.multVec(vector_to_rotate)


    # Create an arc segment from the circle
    arc = Part.Arc(p1, third_point, p2)

    # Add the arc to the sketch
    sketch.addGeometry(arc, False)
    


#def diagonal(sketch, heading: float, start_point, horizontal_length: float, vertical_length: float):
def diagonal(sketch, start_point,  heading: float, length):
    """
    Draws a diagonal line in the FreeCAD document with a given heading, horizontal and vertical lengths.
    
    Parameters:
        sketch: The sketch object where the geometry will be added.
        start_point (App.Vector): The starting point of the line (x, y, z).
        horizontal_length (float): The horizontal distance to move from the start point.
        vertical_length (float): The vertical distance to move from the start point.
        heading (float): The heading angle (in degrees) where 0° is along the positive Y-axis,
                         90° is along the positive X-axis, 180° is along the negative Y-axis,
                         and 270° is along the negative X-axis.
    """

    x,y,_z = start_point

    # Convert heading to radians
    radians = math.radians(heading)

      # Calculate the horizontal and vertical distances based on the diagonal length and heading
    delta_x = length * math.cos(radians)
    delta_y = length * math.sin(radians)
    
    # Calculate the endpoint of the line by adding the changes to the starting point
    end_point = App.Vector(x + delta_x, y + delta_y, 0)
      
#  # Calculate the direction of movement using the heading
#     delta_x = horizontal_length * math.cos(radians)
#     delta_y = vertical_length * math.sin(radians)
    
#     # Calculate the endpoint by applying the changes to the starting point
#     end_point = App.Vector(start_point.x + delta_x, start_point.y + delta_y, start_point.z)
    
    
    # Create the line segment from start_point to end_point
    line = Part.LineSegment(App.Vector(start_point), App.Vector(end_point))
    
    # Add the line to the sketch
    sketch.addGeometry(line)    # Add the line to the document




    