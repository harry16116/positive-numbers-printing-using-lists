a=[12 , -7 , 5 , 64 , -14]
b=[12 , 14 , -95 , 3]
positive1_num =[]
positive2_num =[]
for x in a:
    if(x>0):
        positive1_num.append(x)
for y in b:
    if(y>0):
        positive2_num.append(y)
print("the list a output is :" ,positive1_num)
print("the list b output is :" ,positive2_num)      
