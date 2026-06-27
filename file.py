from collections import Counter

name = 'rahul'
subject ='Maths'
print(name[2:])

name = "Rahul"
name = "K" + name[1:]   # "K" + "ahul" = "Kahul"
print(name)

text = '     Hellow World'

print('hello'.capitalize())


Student ={}
name = input("Enter Student Name: ")
marks = input("Enter Marks: ")
if marks.isdigit():
    marks = int(marks)
    Student[name] = marks
else:
    print("marks must be a number")

s = "Hello"
print(s[::-1])

def reverse_string(s):
    s = list(s)
    left =0
    right = len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return "".join(s)

print(reverse_string('mayur'))



text = "Hello, World! 123"
result =""
for i in text:
    if i.isalnum():
        result+=i
print(result)

count = Counter("Learning")
print(count.keys())
print(count.values())
print(count.items())

