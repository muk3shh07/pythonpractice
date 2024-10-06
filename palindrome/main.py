str = input("Enter the string::")

rev = str[::-1]

if str == rev:
    print("The word is palindrome.")
else:
    print("The word is not palindrome.")