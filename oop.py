# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

    

# s1= Student("Rahul", 95)
# s2=Student("Manish",85)

# print(s1.name)
# print(s1.marks)
# print(type(s1))


# class dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
    
#     def bark(self):
#         return f"{self.name} Says woof!"

# d = dog("Rex", "Labrador")
# print(d.bark())


# class BankAccount:
#     def __init__(self, Owner, Balance=0):
#         self.Owner = Owner
#         self.Balance= Balance

    
#     def deposit(self, amount):
#         self.Balance +=amount
#         return f"{self.Owner} Deposited {amount}. Total Balance is {self.Balance}"
    
#     def withdrawl(self,amount):
#         if amount > self.Balance:
#                 return f"Insufficient Balance"
#         self.Balance-=amount
#         return f"{self.Owner} Withdraw {amount}.Total Balance is {self.Balance} "
    
# acc1 = BankAccount("Tushar", 150)
# print(acc1.deposit(50))
# acc2 = BankAccount("Manoj",1000)
# print(acc2.withdrawl(400))




######### Inheritance ##########

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class GraduateStudent(Student):
    def __init__(self, name, marks, thesis):
        super().__init__(name, marks)
        self.thesis = thesis


    def print_info(self):
        return f"{self.name} got {self.marks} and he is now eligble for thesis {self.thesis} "


stu1 = GraduateStudent("Mayur",85,"AI")
print(stu1.print_info())
print(stu1.thesis)


        
