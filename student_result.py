Student ={}

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
            


