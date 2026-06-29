import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="school"
)
cursor=conn.cursor()

# File = 'Student.json'

class Student:
    def __init__(self,name, marks,age):
        self.name = name
        self.marks = marks
        self.age=age

    def to_dict(self):
        return {"name": self.name, "marks": self.marks, "age": self.age}
    
    

class StudentManager:
    # def __init__(self,File):
    #     self.File = File

    # def load_data(self):
    #     if os.path.exists(self.File):
    #         try:
    #             with open(self.File, "r") as f:
    #                 return json.load(f)
    #         except json.JSONDecodeError:
    #             return []   
    #     return[]
            
    
    # def save_data(self, data):
    #     with open(self.File,"w") as f:
    #         json.dump(data, f, indent=4)

    
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


# manager = StudentManager(File)
# name = input("Enter Student Name: ")
# marks = int(input('Enter Marks: '))
# age = int(input('Enter Student Age: '))
# manager.add_student(name,marks,age) 
# manager.view_student()
def database_creat():
    name = input("Enter Student Name: ")
    marks = int(input("Enter Students Marks: "))
    age = int(input("Enter Age"))

    sql = "INSERT INTO students (name,marks,age) VALUES (%s,%s,%s)"
    Values = (name, marks,age)
    cursor.execute(sql, Values)

    conn.commit()

    print(f"{name} added to database")

    conn.close()

def database_view():
    cursor.execute("SELECT id, name FROM students")
    Students =cursor.fetchall()

    for student in Students:
        print(student)
        
database_view()