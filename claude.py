from typing import Tuple, Optional
import math
import FreeCAD as App
from FreeCAD import Vector
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
        
        # Close the shape
        if geometry_count > 0:
            constraints.append(
                Sketcher.Constraint("Coincident", geometry_count - 1, 2, 0, 1)
            )

        # Handle positioning constraints
        x, y = None, None
        if pos:
            x, y = pos
        else:
            x, y = self._initial_position

        if (x, y) == (0, 0):
            constraints.append(Sketcher.Constraint("Coincident", 0, 1, -1, 1))
        elif x != 0:
            if x > 0:
                constraints.append(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, x))
            else:
                constraints.append(Sketcher.Constraint("DistanceX", 0, 1, -1, 1, -x))
            constraints.append(Sketcher.Constraint('PointOnObject', 0, 1, -1))
        elif y != 0:
            constraints.append(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, y))
            constraints.append(Sketcher.Constraint('PointOnObject', 0, 1, -1))
        else:
            constraints.append(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, x))
            constraints.append(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, y))
            
        self._sketch.addConstraint(constraints)

    def move(self, dx: float, dy: float, constraint_type: Optional[str] = None) -> int:
        """Move the turtle by the specified delta x and y. Returns geometry ID."""
        if not self._sketch:
            return -1

        end_pos = Vector(self._position.x + dx, self._position.y + dy, 0)
        
        geo_id = self._sketch.addGeometry(
            LineSegment(self._position, end_pos)
        )
        
        # Add the primary constraint (Horizontal/Vertical)
        if constraint_type:
            self._sketch.addConstraint(
                Sketcher.Constraint(constraint_type, geo_id)
            )
            
        # Add distance constraints based on the movement type
        if dx != 0:
            if dx > 0:
                self._sketch.addConstraint(
                    Sketcher.Constraint("DistanceX", geo_id, 1, geo_id, 2, dx)
                )
            else:
                self._sketch.addConstraint(
                    Sketcher.Constraint("DistanceX", geo_id, 2, geo_id, 1, -dx)
                )
        if dy != 0:
            if dy > 0:
                self._sketch.addConstraint(
                    Sketcher.Constraint("DistanceY", geo_id, 1, geo_id, 2, dy)
                )
            else:
                self._sketch.addConstraint(
                    Sketcher.Constraint("DistanceY", geo_id, 2, geo_id, 1, -dy)
                )
            
        self._position = end_pos
        return geo_id

    def up(self, distance: float) -> int:
        """Move turtle upward. Returns geometry ID."""
        return self.move(0, distance, "Vertical")

    def down(self, distance: float) -> int:
        """Move turtle downward. Returns geometry ID."""
        return self.move(0, -distance, "Vertical")

    def left(self, distance: float) -> int:
        """Move turtle left. Returns geometry ID."""
        return self.move(-distance, 0, "Horizontal")

    def right(self, distance: float) -> int:
        """Move turtle right. Returns geometry ID."""
        return self.move(distance, 0, "Horizontal")

    def removeConstraint(self, constraint_type: str, geo_id: int) -> None:
        """Remove a specific type of constraint from a geometry element."""
        if not self._sketch:
            return

        # Find the constraint index that matches both the type and geometry ID
        for i, constraint in enumerate(self._sketch.Constraints):
            if (constraint.Type == constraint_type and 
                (constraint.First == geo_id or constraint.Second == geo_id)):
                self._sketch.delConstraint(i)
                break

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
removeConstraint = turtle.removeConstraint