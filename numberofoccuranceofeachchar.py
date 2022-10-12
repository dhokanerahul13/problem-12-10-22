#NUMBER OF OCCURACNE OF EACH CHAR INSIDE A STRING

n=input('enter a string:-')
d={}
for i in n:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
for i,j in d.items():
    print('{}={}.times'.format(i,j))   