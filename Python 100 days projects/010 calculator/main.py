def calc(a, b, operation):
    if operation == "+":
        result = a+b
    elif operation == "-":
        result = a-b
    elif operation == "*":
        result = a*b
    elif operation == "/":
        result = a/b
    else:
        result = f'Invalid result'
    return result

calculator = """
 ______________________
|  __________________  |
| | simple calculator| |
| |__________________| |
|  ___ ___ ___    ___  |
| | 7 | 8 | 9 |  | + | |
| |___|___|___|  |___| |
| | 4 | 5 | 6 |  | - | |
| |___|___|___|  |___| |
| | 1 | 2 | 3 |  | x | |
| |___|___|___|  |___| |
| | . | 0 | = |  | / | |
| |___|___|___|  |___| |
|______________________|
"""
print(calculator)



a = float(input('What is the first number?: '))
print("""
+
-
*
/
""")
operation = input('Pick an operation: ')
b = float(input('What is the second number?: '))

results = calc(a, b, operation)

print(results)

answer = input(f"Type 'y' to continue calculating with {results}, or type 'n' to start a new calculation:").lower()
while answer == 'y':
    a = results
    operation = input('Pick an operation: ')
    b = float(input('What is the second number?: '))
    results = calc(a, b, operation)
    print(results)
    answer = input(f"Type 'y' to continue calculating with {results}, or type 'n' to start a new calculation:").lower()