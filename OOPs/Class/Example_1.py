class Student:
    def __init__(self, currentCity):
        self.name = "Sonu Kumar"
        self.grades = (90, 90, 80, 93, 95)
        self.city = currentCity

    def average(self):
        return sum(self.grades) / len(self.grades)


studentObj = Student("Bangalore")
print(studentObj.name)  # Sonu Kumar
print(studentObj.city)  # Bangalore
print(Student.average(studentObj))  # 89.6
print(studentObj.average())  # 89.6
