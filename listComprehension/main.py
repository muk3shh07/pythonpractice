#list comprehension
num =[1,2,3,4,5,6,7,8,9,10,11,12]

new_list = [x**2 for x in num if x%2==0]

print(new_list)

# dictionary Comprehension

dict = {
    'Ram': 90,
    'Shyam': 40,
    'Hari': 67,
    'Manoj': 50,
    'Quas': 70,
    'Laila': 90,
    'Majnu': 40,
    'Welsin': 21,
}

new_dict = {name:score for name,score in dict.items() if score >= 50}
print(f"The Students who have passed the exam successfully are::\n {new_dict}")