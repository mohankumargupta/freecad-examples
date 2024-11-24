from typing import Tuple, Optional
import math
import FreeCAD as App
from FreeCAD import Vector
#import Part # type: ignore
from Part import LineSegment # type: ignore
import Sketcher # type: ignore
from drawing import diagonal, makeArcTwoPoints

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
        constraints.append(
                Sketcher.Constraint("Coincident", geometry_count - 1, 2, 0, 1)
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
                constraints.append(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, x))
            elif y != 0:
                constraints.append(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, y))
            else:
                pass

        else:
            x_initial,y_initial = self._initial_position
            constraints.append(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, x_initial))
            constraints.append(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, y_initial))
            
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
            makeArcTwoPoints(
                self._sketch,
                (self._position.x, self._position.y, 0),
                (end_pos.x, end_pos.y, 0),
                radius
            )

    def diagonal_southwest(self, length: float) -> None:
        """Move diagonally southwest."""
        if hasattr(self, 'diagonal'):
            diagonal(
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
