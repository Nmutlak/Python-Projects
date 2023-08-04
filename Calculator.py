def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("Welcome to the potential calculator")
print("Select an option below")
print("1. add \n2. subtract \n3. multiply \n4. divide \n5. answer")

choice = int(input("Choice "))
print(choice)
if choice == 1:
    print("Great choice\n Now just input your numbers")
    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))
    answer = add(num1, num2)

elif choice == 2:
    print("Great choice\n Now just input your numbers")
    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))
    answer = subtract(num1, num2)

elif choice == 3:
    print("Great choice\n Now just input your numbers")
    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))
    answer = multiply(num1, num2)

elif choice == 4:
    print("Great choice\n Now just input your numbers")
    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))
    answer = divide(num1, num2)

elif choice == 5:
    print("Too early for that")

else:
    print("invalid option")

while True:
    print("Select an option below")
    print("1. add \n2. subtract \n3. multiply \n4. divide \n5. answer")
    choice = int(input("Choice "))

    if choice == 1:
        print("Great choice\nNow just input your number")
        num = float(input("Number "))
        answer = add(answer, num)

    elif choice == 2:
        print("Great choice\n Now just input your numbers")
        num = float(input("Number "))
        answer = subtract(answer, num)

    elif choice == 3:
        print("Great choice\n Now just input your numbers")
        num = float(input("Number "))
        answer = multiply(answer, num)

    elif choice == 4:
        print("Great choice\n Now just input your numbers")
        num = float(input("Number "))
        answer = divide(answer, num)

    elif choice == 5:
        print("Final answer is: " + str(answer))
        break

    else:
        print("invalid option")