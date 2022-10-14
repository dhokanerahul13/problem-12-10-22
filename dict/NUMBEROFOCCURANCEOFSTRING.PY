#WRITE A PROGRAM TO PRINT NUMBER OF OCCURANCE OF EACH CHAR OF STRING

n=input('enter a string:-')
d={}
for i in n:
    d[i]=d.get(i,0)+1
print(d)    

for k,v in d.items():
    print('dictkey is',k,'occurance',v)