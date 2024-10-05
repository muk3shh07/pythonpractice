a = int(input("Enter first number::"))
b = int(input("Enter second number::"))

m = min(a,b)

for i in range(1,m+1):
    if(a%i==0 and b%i==0):
        GCD = i
print(f"The GCD of {a} and {b} is {GCD}")    