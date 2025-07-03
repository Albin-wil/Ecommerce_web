def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error: Divison by zero"
    return x/y
print("Simple calculator")
print("1. Add")
print("2. sub")
print("3. mul")
print("3. div")

while True:
    choice =input("Enter your choice(1/2/3/4):")
    if choice in['1','2','3','4']:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if choice=="1":
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif choice=="2":
            print(f"{num1}-{num2}={sub(num1,num2)}")
        elif choice=="3":
            print(f"{num1}*{num2}={mult(num1,num2)}")
        else:
            print(f"{num1}/{num2}={div(num1,num2)}")
    else:
        print("Invalid choice.please try again")