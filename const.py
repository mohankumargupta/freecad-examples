from types import SimpleNamespace
from enum import Enum, auto

Constraints = SimpleNamespace()
Constraints.X_AXIS = -1
Constraints.Y_AXIS = -2
Constraints.EDGE = 0
Constraints.LINE_START = 1
Constraints.LINE_END = 2
Constraints.CENTER = 3

class Plane(Enum):
    XY = auto()
    YZ = auto()
    XZ = auto()

