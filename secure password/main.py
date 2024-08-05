secure = (('s','$'),('a','@'),('o','0'),('h','#'),('i','1'))

def securePassword(password):
    for a,b in secure:
        password= password.replace(a,b)
    return password

if __name__=="__main__":
    password = input("Enter your password::")
    password = securePassword(password)
    print(f"Your password is {password}")