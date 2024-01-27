student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato=pandas.DataFrame(data)
# dictionary_name = {}


newdict = {row.letter:row.code for (index,row) in nato.iterrows()}
print(newdict)

# for (index, row) in nato.iterrows():

#     dictionary_name[row.letter] = row.code
#     #print(row.code)
# print(dictionary_name)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Insert a name: ').upper()
return_word = [newdict[letter] for letter in word]
print(return_word)

if 2+2 ==4:
    print('hello')
elif 2+2 == 5:
    print('pinto')
elif 2+2 ==7:
    print('ovo')
else:
    print()