from datetime import date

def FindAge(birthyear): 
    current_date = date.today()
    year = current_date.year
    currentAge = year - birthyear 
    return currentAge

CA = FindAge(2004)
print(f"Your are {CA} years old now.")
