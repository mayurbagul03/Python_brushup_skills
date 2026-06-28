import json
import os

File = 'Student.json'

class Student:
    def __init__(self,name, marks,age):
        self.name = name
        self.marks = marks
        self.age=age

    def to_dict(self):
        return {"name": self.name, "marks": self.marks, "age": self.age}
    
    

class StudentManager:
    def __init__(self,File):
        self.File = File

    def load_data(self):
        if os.path.exists(self.File):
            try:
                with open(self.File, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return[]
            
    
    def save_data(self, data):
        with open(self.File,"w") as f:
            json.dump(data, f, indent=4)

    
    def add_student(self, name, marks, age):
        data = self.load_data()
        student = Student(name, marks, age)
        data.append(student.to_dict())
        self.save_data(data)
        print(f"{name} added!")

    def view_student(self):
        data = self.load_data()
        for i in data:
            print(i)


manager = StudentManager(File)
name = input("Enter Student Name: ")
marks = int(input('Enter Marks: '))
age = int(input('Enter Student Age: '))
manager.add_student(name,marks,age)
manager.view_student()

        