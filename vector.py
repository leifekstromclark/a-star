class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = (x ** 2 + y ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            pass
        else:
            return Vector(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)
    
    def __floordiv__(self, other):
        return Vector(self.x // other, self.y // other)
    
    def normalize(self):
        return self / self.magnitude
    
    def int(self):
        return Vector(int(self.x), int(self.y))