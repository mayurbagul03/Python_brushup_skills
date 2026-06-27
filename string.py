from collections import Counter


text ='Hello'
for ch in text:
    print(ch, end='')


for index, ch in enumerate(text):
    print(index , ch)

for i in range(len(text)):
    print(i,text[i])
i=0
while i < len(text):
    print(text[i])
    i+=1
text = "h e l l o"
for ch in text:
    if ch == " ":
        continue       # skip spaces
    print(ch, end='')
# h e l l o   (spaces skipped, not printed)


while True:                      # runs forever...
    choice = input("Enter choice (q to quit): ")
    if choice == "q":
        break                    # ...until break ends it
    print("You entered:", choice)