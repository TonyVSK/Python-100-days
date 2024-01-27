list = []
answer = 'yes'
counter = 1

while answer == 'yes':
    item = input('Inform a task to the list: ')
    list.append(item)
    answer = input("Do you want to continue? 'yes' or 'no': ")

for task in list:
    print(f'{counter}. {task}')
    counter += 1