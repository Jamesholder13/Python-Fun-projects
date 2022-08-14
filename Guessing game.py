x = input("x: ")
y = x + 1
# Jame's guessing Game!

score = 0

option1 = 'Voss'
option2 = 'V8'
option3 = 'Coke'
option4 = 'DeerPark'

print("For ordering his favorite drinks ASAP, James had four buttons in his house named 'Voss', 'V8', 'Coke', and DeerPark?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)

answer = 'a'

if answer == 'A' or answer == 'a':
    score += 100
    print("\nYou're Right!")
else:
    print("\nOops,try again!")
