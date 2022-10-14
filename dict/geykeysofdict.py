

#get keysofdict
#store dict key inside one list


def getkey(dict):
    list=[]
    for i,j in dict.items():
        list.append(i)
    print(list)     
d={1:'amol',2:'vijayy',3:'rahul',4:'ankita',5:'anushka'}
getkey(d)


#values appenf

def getkey(dict):
    sumofvalue=0
    for i,j in dict.items():
        sumofvalue+=j
    print(sumofvalue)     
d={'amol':80,'vijayy':76,'rahul':58,'ankita':90,'anushka':90}
getkey(d)
