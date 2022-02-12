Q1 :

string=input("Enter a String : ")
list1=[]
list2=string.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:          
    for i in string:      
        list1.append(i) 
    for j in list1:        
        if j in d:         
            d[j]=d[j]+1    
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t) 
    







