"""This module is designed to calculate the surface area 
of the treated surface and 
the number of necessary rolls of wallpaper.
"""
class WinDoor:
     
    def __init__(self, w, h):
        self.square = w * h

class Room:
    """
    Room with given dimensions.

    Attributes:
        length, width, height: Room dimensions.
        wd (list): List of WinDoor objects (windows/doors).

    Methods:
        __init__(l, w, h): Initializes room.
        addWD(w, h): Adds a window/door.
        fullSerface(): Total wall area.
        workSurface(): Wall area excluding windows/doors.
        wallpapers(l, w): Calculates wallpaper rolls needed.
    """

    def __init__(self, l, w, h):
        """
        Initializes room with length, width, and height.
        """
        self.length = l
        self.width = w
        self.height = h
        self.wd = []

    def addWD(self, w, h):
        """Adds window/door to the room."""
        self.wd.append(WinDoor(w, h))

    def fullSerface(self):
        """Returns total wall area."""
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        """Returns net wall area (excluding windows/doors)."""
        new_square = self.fullSerface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpapers(self, l, w):
        """Returns number of wallpaper rolls needed."""
        return int(self.workSurface() / (w * l)) + 1