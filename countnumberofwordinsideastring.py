#count nuber of word inside a string
s=input('enter a string:-')
l=s.split()
count=0
for i in range(len(l)):
    count+=1
print('number of word  inside a string:-',count)        