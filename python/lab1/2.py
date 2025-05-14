class Person: 
    def __init__(self, firstName, lastName, qualification = 1):
        self.firstName = firstName
        self.lastName = lastName
        self.qualification = qualification
    def employeeData(self):
        data = f"Имя: {self.firstName} Фамилия: {self.lastName} Квалификация: {self.qualification}"
        return data  
    def __del__(self):
        print(f"До свидания: {self.firstName} {self.lastName}")

worker1 = Person("Алексей", "Иванов", 4)
worker2 = Person("Илья", "Петров", 2)
worker3 = Person("Василий", "Кузнецов", 1)

print(worker1.employeeData())
print(worker2.employeeData())
print(worker3.employeeData())

del worker3

input()