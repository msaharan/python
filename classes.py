# Classes and Objects
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

s1 = Student("Alice", 20, "12345")
print(s1.name)
print(s1.age)
print(s1.student_id)