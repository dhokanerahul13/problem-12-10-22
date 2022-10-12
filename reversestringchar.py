#reverse each charecter of string


s=input('enter a string:-')
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
reversechar=' '.join(l1)   
print(reversechar) 