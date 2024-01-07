hammer = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                         `'-------'`
                       .-------------.
                   jgs/_______________|
"""


from replit import clear

people = []
person = {}
answer = 'yes'

while answer == 'yes':
    clear()
    print(hammer)
    
    person['name'] = input('What is your name?\n')
    person['bid'] = int(input('What is your bid?\n'))
    people.append(person.copy())
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()


print(people)