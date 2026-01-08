# vos imports ici
import math

from point2d import *

class Vector2D(object):
    """
    Vecteur dans un plan
    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O,A)
    >>> v2 = Vector2D(O,B)
    >>> v3 = Vector2D(O,C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1+v2)
    Vector2D(2,1)
    >>> print(v1+v3)
    Vector2D(1,1)
    >>> print(v1-v3)
    Vector2D(1,-1)
    >>> print(v1+v3 == v2)
    True
    """
    # attributs et méthodes ici...
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __abs__(self):
        return math.sqrt(self.y.x ** 2 + self.y.y ** 2)
    
    def __str__(self):
        return "Vector2D(" + str(self.y.x) + "," + str(self.y.y) + ")"
        
    def __eq__(self, other):
        return other.x.x == self.x.x and other.x.y == self.x.y and other.y.x == self.y.x and other.y.y == self.y.y
        
    def __neg__(self):
        return Vector2D(
            Point2D(-self.x.x, - self.x.y),
            Point2D(-self.y.x, - self.y.y)
        )
        
    def __add__(self, other):
        return Vector2D(
            Point2D(self.x.x + other.x.x, self.x.y + other.x.y),
            Point2D(self.y.x + other.y.x, self.y.y + other.y.y)
        )
        
    def __sub__(self, other):
        return Vector2D(
            Point2D(self.x.x - other.x.x, self.x.y - other.x.y),
            Point2D(self.y.x - other.y.x, self.y.y - other.y.y)
        )

def main():
    pass
    O = Point2D()
    A = Point2D(1, 0)
    B = Point2D(1, 1)
    v1 = Vector2D(O,A)
    v2 = Vector2D(O,B)
    print(v1)
    print(v2)
    print(abs(v1))
    print(abs(v2))
    print(-v1)
    print(v1+v2)

if __name__ == "__main__":
    main()