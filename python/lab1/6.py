class WinDoor:
    def __init__(self, w, h):
        self.square = w * h

class Room:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.wd = []

    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))

    def fullSurface(self):
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        new_square = self.fullSurface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpapers(self, l, w):
        return int(self.workSurface() / (w * l)) + 1

print("Размеры помещения:")
l = float(input("Длина - "))
w = float(input("Ширина - "))
h = float(input("Высота - "))
r1 = Room(l, w, h)

flag = input("Есть неоклеиваемая поверхность? (1 - да, 2 - нет) ")
while flag == '1':
    w = float(input("Ширина окна/двери - "))
    h = float(input("Высота окна/двери - "))
    r1.addWD(w, h)
    flag = input("Добавить еще? (1 - да, 2 - нет) ")

print("Размеры рулона:")
l = float(input("Длина - "))
w = float(input("Ширина - "))

print("Площадь оклейки", r1.workSurface())
print("Количество рулонов", r1.wallpapers(l, w))
