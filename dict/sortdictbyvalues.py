#sorrt any dict by value 
#sort by keys


def sortitembyvalues(dict):
    print(sorted(dict.items()))
d={'amol':80,'vijayy':76,'rahul':58,'ankita':90,'anushka':90}
sortitembyvalues(d)



#sort by values:-
from collections import OrderedDict
def sortitembyvalues(dict): 
    dict1 = OrderedDict(sorted(dict.items()))
    print(dict1)
    
d={'amol':80,'vijayy':76,'rahul':58,'ankita':90,'anushka':90}
sortitembyvalues(d)










#######################################################pr
print('#######################################################')
#sort dict by values

dict1={'amol':80,'vijayy':76,'rahul':58,'ankita':90,'anushka':90}
sorted_values = sorted(dict1.values()) # Sort the values
print(sorted_values)
sorted_dict = {}
for i in sorted_values:  #58, 76, 80, 90, 90
    for k in dict1.keys():  #all keys
        if dict1[k] == i:  #set values
            sorted_dict[k] = dict1[k]
print(sorted_dict)