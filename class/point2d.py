# vos import ici
import math


class Point2D(object):
    """Point du plan cartésien

    >>> p1 = Point2D(3, 4)
    >>> p1.x
    3
    >>> p1.y
    4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> p2.x
    0
    >>> p2.y
    0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> p1.x
    4
    >>> p1.y
    5
    >>> print(p1)
    Point2D(4,5)
    >>> p1.distance(p2)
    6.4031242374328485
    """
    # attributs et méthodes ici...
    def __init__(self, x = 0, y = 0):
        """Constructeur

        Args:
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """déplace le point

        Args:
            dx (int, optional): incrément de translation. Defaults to 0.
            dy (int, optional): incrément de translation. Defaults to 0.
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        """description string

        Returns:
            str: description
        """
        return "Point2D(" + str(self.x) + "," + str(self.y)  + ")"

    def distance(self, other):
        """Distance entre 2 points

        Args:
            other (Point2D): point de référence

        Returns:
            float: distance au point de référence
        """
        return math.hypot(other.x - self.x, other.y - self.y)
        
def main():
    # votre code de test ici...
    pass

if __name__ == "__main__":
        main()