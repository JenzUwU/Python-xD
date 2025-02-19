from art import logo
def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
# print(operations["/"](10,2))
def calculator():
    print(logo)
    should_accumulate=True
    while should_accumulate:
        num1=float(input("What is the First number?"))
        for symbols in operations:
            print(symbols)
        operation_symbol=input("Enter the operation")
        num2=float(input("Whats the next number?"))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input("do u want to continue type 'y' or type 'n' ").lower()
        if choice=="y":
            num1=answer
        if choice=="n":
            should_accumulate=False
            print("\n"*20)
            calculator()
calculator()