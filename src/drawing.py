import FreeCAD as App
from FreeCAD import Base # type: ignore
import Part # type: ignore
import Sketcher # type: ignore

LineSegment = Part.LineSegment
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

    # Fix the bottom left corner of the rectangle
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 2, 2, corner[0]))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 2, 2, corner[1]))

    # add dimensions
    if lengths[0] == lengths[1]:
        sketch.addConstraint(Sketcher.Constraint("Equal", i + 2, i + 3))
        sketch.addConstraint(Sketcher.Constraint("Distance", i + 0, hmax - hmin))
    else:
        sketch.addConstraint(Sketcher.Constraint("Distance", i + 1, vmax - vmin))
        sketch.addConstraint(Sketcher.Constraint("Distance", i + 0, hmax - hmin))

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
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 0, 1, center[0]))
    sketch.addConstraint(Sketcher.Constraint("DistanceX", i + 2, 1, center[0]))
    
    # Constrain vertical center
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 1, 1, center[1]))
    sketch.addConstraint(Sketcher.Constraint("DistanceY", i + 3, 1, center[1]))