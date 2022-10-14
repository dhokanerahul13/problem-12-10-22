#max value of dictinaty



def maxvalues(dict):
    l=[]
    for i,j in dict.items():
        l.append(j)
    print(max(l))  
d={'amol':80,'vijayy':76,'rahul':58,'ankita':90,'anushka':90}
maxvalues(d)