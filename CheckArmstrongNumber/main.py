num = int(input("Enter the number::"))
order = len(str(num))
sum = 0
n = num

while(num!=0):
    digit = num % 10
    sum = sum + digit ** order
    num = num // 10

if(sum == n):
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not a armstrong number")