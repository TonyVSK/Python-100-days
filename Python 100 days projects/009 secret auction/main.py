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


# add people from auction
while answer == 'yes':
    clear()
    print(hammer)
    
    person['name'] = input('What is your name?\n')
    person['bid'] = int(input('What is your bid?\n$'))
    people.append(person.copy())
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

#see who won
bigger = people[0]
for each_person in people:
    if each_person['bid']>bigger['bid']:
        bigger=each_person

clear()
print(f"The winner is {bigger['name']} with a bid of {bigger['bid']}")
