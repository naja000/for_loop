#list=[1,2,3,4,5,6,7,8,9,10]
#for i in list:
# print(i)
#num=10
#if num%5==0:
#print("num is divisible")

list=[1,2,3,4,5,6,7,8,9,10]
odd_list=[]
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)