with open('currency.txt') as f:
    lines = f.readlines()

currentDict={}
for line in lines:
    parsed=line.split('\t')
    currentDict[parsed[0]]=parsed[1]
    
     
    
