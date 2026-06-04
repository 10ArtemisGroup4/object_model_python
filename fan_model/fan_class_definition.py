class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    _SPEED_LABELS = {
        1: 'Slow',
        2: 'Medium',
        3: 'Fast',
    }

    #constructor
    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        self._speed = Fan.SLOW
        self._radius = 5.0
        self._color = "blue"
        self._on = False

        self.speed = speed if speed is not None else Fan.SLOW
        self.radius = radius
        self.color = color
        self.on = on

        