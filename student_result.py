import json
import os

File = 'Student.json'

#Load Save data when the program starts

def load_data():
    if os.path.exists(File):
        with open(File, 'r') as f:
            return json.load(f)
    
    return{}

def read_file():
    with open("Student.json", "r") as f:
        content = f.read()
        print(content)

# read_file()

def write_file():
    with open("Student.json", "r") as f:
        for line in f:
            print(line.strip())
# write_file()
def add_content():
    with open("file.txt", "a") as f:
        f.write("Manasi:98\n")

# add_content()

#Save data file

def Save_data(data):
    with open(File, "w") as f:
        json.dump(data, f , indent=4)

Student = load_data()

while True:
    print("\n------STUDENT MANAGER APP------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    #Add Student

    if choice == "1":
        name = input("Enter Studnet Name: ")
        marks = int(input("Enter Marks: "))
        Student[name] = marks
        Save_data(Student)
        print(f"{name} Successfully Added!")
        #Rahul 50

    #View Student
    elif choice =="2":
        if not Student:
            print("No student found!")
        else:
            for name,marks in Student.items():
                print(name, ":", marks)

    #check Result

    elif choice =="3":
        name = input("Enter Student Name: ")

        if name in Student:
            marks = Student[name]

            if marks >= 40:
                print("Pass")
            else:
                print("Fail")

        else:
            print("Student Not Found: ")

    elif choice =="4":
        print("Exiting....")
        break
    else:
        print("In-valid Input")
            


