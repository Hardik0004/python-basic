# class Calculator:
def add(*args):
    if len(args) == 2:
        return args[0] + args[1]
    elif len(args) == 3:
        return args[0] + args[1] + args[2]
# Create an instance of the Calculator class
# calc = Calculator()

# Call the add method with two arguments
result1 = add(2, 3)
print("Result1:", result1)

# # Call the add method with three arguments
# result2 = calc.add(2, 3, 4)
# print("Result2:", result2)
