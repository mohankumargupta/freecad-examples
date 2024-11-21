# yourmodule.pyi
from typing import Callable
import Sketcher

def _polyline_functions() -> dict[str, Callable]:
    """
    Returns a dictionary of functions for polyline operations.

    The dictionary contains functions like `penup`, `pendown`, `up`, `down`, 
    `left`, `right`, and `arcLeft`, each responsible for a specific operation
    in the polyline drawing process.

    Returns:
        dict: A dictionary mapping function names to function implementations.
    """
    ...

penup: Callable[[], None]
"""
Puts the pen up.
"""

pendown: Callable[[Sketcher.SketchObject, tuple[float, float]], None]
"""
Puts the pen down on the given sketch at the specified coordinates.

Args:
    sketch (Sketcher.SketchObject): The sketch to which geometry is added.
    point (tuple[float, float]): The (x, y) coordinates where the pen is placed.
"""

up: Callable[[float], None]
"""
Moves the pen up by a specified distance.

Args:
    distance (float): The distance to move the pen in the upward direction.
"""

down: Callable[[float], None]
"""
Moves the pen down by a specified distance.

Args:
    distance (float): The distance to move the pen in the downward direction.
"""

left: Callable[[float], None]
"""
Moves the pen left by a specified distance.

Args:
    distance (float): The distance to move the pen in the left direction.
"""

right: Callable[[float], None]
"""
Moves the pen right by a specified distance.

Args:
    distance (float): The distance to move the pen in the right direction.
"""

arcLeft: Callable[[float, float], None]
"""
Draws an arc to the left with a given radius.

Args:
    left (float): The leftward distance to draw the arc.
    radius (float): The radius of the arc.
"""
