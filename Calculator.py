def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print( "Can't divide by 0")
    return a / b

print("Select operation you want to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

c = input("Enter choice: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if c == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif c == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif c == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif c == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid choice")
