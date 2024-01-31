# Exercice: Pass any number using *args in a function to sum these numbers


def add(*args):
    counter = 0
    for number in args:
        counter += number
    return counter


result = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(result)