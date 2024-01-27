import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


newValue=pandas.DataFrame(student_dict)
for (index, row) in newValue.iterrows():
    if row.student == "Angela":
        print(row.student)