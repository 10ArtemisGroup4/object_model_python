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

    #getter and setters
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value not in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            print("Invalid speed! Use SLOW (1), MEDIUM (2), FAST (3)")
            return
        self._speed = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def on(self):
        return self._on