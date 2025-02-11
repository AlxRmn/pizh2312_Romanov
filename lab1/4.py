class Add:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Add(self.value + other.value)

num1 = Add(10)
num2 = Add(12)
num3 = num1 + num2

print(num3)