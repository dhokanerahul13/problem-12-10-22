#remove duolicates from a list

n=input('enter a string:-')
l=[]
for i in n:
    if i not in l:
        l.append(i)
strwithoutduplicates=''.join(l)
print(strwithoutduplicates)