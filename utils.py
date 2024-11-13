import FreeCAD as App
import Part # type: ignore
import Sketcher # type: ignore

class Pen:
    def __init__(self, doc, sketch):
        self.doc = doc
        self.sketch = sketch
        self.position = App.Vector(0, 0, 0)  # Initial position
        self.drawing = False  # Whether the pen is down or up

    def penup(self):
        self.drawing = False  # Stop drawing
        self.position = App.Vector(0, 0, 0)  # Reset to origin

    def pendown(self, start_position):
        self.position = App.Vector(start_position[0], start_position[1], 0)
        self.drawing = True  # Start drawing from the initial position

    def draw_to(self, new_position, is_Horizontal=False, is_Vertical=False):
        if self.drawing:
            line = Part.LineSegment(self.position, new_position)
            line_index = self.sketch.addGeometry(line,False)
            
            
            # if is_Horizontal:
            #    self.sketch.addConstraint(Sketcher.Constraint('Horizontal', line_index))

            # if is_Vertical:
            #    self.sketch.addConstraint(Sketcher.Constraint('Horizontal', line_index))
             
            self.position = new_position  # Update the pen's position



    def up(self, distance):
        new_position = self.position.add(App.Vector(0, distance, 0))
        self.draw_to(new_position, is_Vertical=True)

    def down(self, distance):
        new_position = self.position.add(App.Vector(0, -distance, 0))
        self.draw_to(new_position, is_Vertical=True)

    def left(self, distance):
        new_position = self.position.add(App.Vector(-distance, 0, 0))
        self.draw_to(new_position, is_Horizontal=True)

    def right(self, distance):
        new_position = self.position.add(App.Vector(distance, 0, 0))
        self.draw_to(new_position, is_Horizontal=True)
