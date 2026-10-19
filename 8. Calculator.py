def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

first_number = float(input("Enter the first number: "))
work_over = False
while not work_over:

    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Enter operation: ")
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation try again \n ")
        continue

    second_number = float(input("Enter the second number: "))
    if operation == "+":
        result = add(first_number, second_number)
        print(result)

    elif operation == "-":
        result = sub(first_number, second_number)
        print(result)

    elif operation == "*":
        result = mult(first_number, second_number)
        print(result)

    elif operation == "/":
        result = div(first_number, second_number)
        print(result)

    else:
        print("Invalid operation")

    asking_continue = input(f"Type 'y' to continue calculating with {result}, or 'n' to exit: ")
    if asking_continue == "y":
        first_number = result
        work_over = False

    else:
        work_over = True
        print("Thank you for using this program")


