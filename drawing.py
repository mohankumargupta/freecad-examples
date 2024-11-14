
def _turtle_functions():
    context = {
        'pen_state': 'up',
        'position': {'x': 0, 'y': 0},
        'geometries': [],
        'constraints': []
    }

    def pendown(x,y):
        context['position']['x'] = x
        context['position']['y'] = y

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