from FreeCAD import Base # type: ignore
import Part # type: ignore

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