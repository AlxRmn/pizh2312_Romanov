class Student():
    def __init__(self, name, group):
        self.__name = name  
        self.__group = group

    def getGroup(self):
        return self.__group

    def setGroup(self, group):
        self.__group = group

st1 = Student("Alex", 1)
st2 = Student("Dima", 2)

st1.setGroup(3)
print(st1.getGroup())