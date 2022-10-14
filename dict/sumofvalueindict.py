#program to print sum of values od dictinry



def sumofvalues(dict):
    list=[]
    for i,j in dict.items():
        list.append(j)
    print(list)     
d={1:'amol',2:'vijayy',3:'rahul',4:'ankita',5:'anushka'}
sumofvalues(d)
