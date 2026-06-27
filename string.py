# function

def greet():
    print("Hello")

# greet()

def greet_name(name):
    print(f"Welcome {name}")

# names = input("Enter your name: ")
# greet_name(names)

def add_print(a,b):
    print(a+b)

# add_print(2,3)

def add_return(a,b):
    return a + b

result = add_return(2,5)
print(result *2)


# Input validation

marks = input('Enter Marks: ')

if marks.isdigit():
    marks = int(marks)
    print(f"Valid marks is {marks}")
else:
    print('Enter Valid Marks')

while True:
    try:
        marks = int(input("Enter Marks"))
        print(f"Valid {marks}")
        break

    except ValueError:
        print("Not a legit Number")








