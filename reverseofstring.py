#reverse string word
s=input('enter a string:-')
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
reversestring=' '.join(l1)
print(reversestring) 


