with open('currency.txt') as f:
    lines = f.readlines()

currentDict={}
for line in lines:
    parsed=line.split('\t')
    currentDict[parsed[0]]=parsed[1]

amount=int(input("Enter the currency amount::"))
print("Enter the name of currency you want to convert this amount to:")
[print(item) for item in currentDict.keys()]
currency = input("Please enter one of the currency you want to convert it to::")

if(currency=='Nepalese Rupee'):
    print(f"{amount} INR is equal to {amount  / float(currentDict[currency])} {currency}")
else:
    print(f"{amount} INR is equal to {amount  * float(currentDict[currency])} {currency}")



    
     
    
