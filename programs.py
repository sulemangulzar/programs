# --1--

'''a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
print("Product: ",a*b)
'''
# ---2---
'''
length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
print("Area: ", length*width )
'''
# ---3---
'''
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
if(a>b):
    print("A is greater")
elif(b>a):
    print("B is greater")
else:
    print("Nums are Equal")
'''
# ---4---
'''
a = int(input("Enter  num: "))
char = input("Enter symbol(-,+,*,/)")
b = int(input("Enter  num: "))

match char:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
'''
# ---5---
'''  
num = int(input("Enter a number greater than one: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
'''
# ---6---
'''
num = int(input("Enter a number: "))
if num>0:
    print("Num is positive.")
elif num<0:
     print("Num is negative.")
else:
     print("Num is zero.")
'''
# ---7---
'''
num = int(input("Enter a number: "))
if (num%3) or (num%5) == 0:
    print("Divisible by both.")
elif num%3 == 0:
     print("Divisible by 3.")
elif num%5 == 0:
     print("Divisible by 5.")
else:
     print("Not divisible.")
'''
# ---8---
'''
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not leap year")
'''
# ---9---
'''
import random


while True:
    print("\nChoose difficulty: Easy / Medium / Hard")
    level = input("Enter level: ").lower()

    if level == "easy":
        max_attempts = 10
    elif level == "medium":
        max_attempts = 7
    elif level == "hard":
        max_attempts = 5
    else:
        print("Invalid level. Try again.")
        continue
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break
        elif guess < number:
            print("Too low 🔽")
        else:
            print("Too high 🔼")
        print(f"Attempts left: {max_attempts - attempts}")

    else:
        print(f"\n❌ You've used all your attempts. The number was {number}.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break
'''
# ----10----

print("Welcome to calculator\n")
while True:
    a = int(input("Enter first  num: "))
    char = input("Enter operator (+, -, *, /): ")
    b = int(input("Enter second num: "))

    match char:
        case "+":
            result = (a+b)
        case "-":
            result = (a-b)
        case "*":
            result = (a*b)
        case "/":
            result = (a/b)
    
   
    print(f"Result of {a} {char} {b}: ", result)
    cal_again = input("Do you want to calculate again? (yes/no): ").lower()
    if cal_again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break
        


