str1=input()
str1=str1.split()
list1=[]
for i in range(len(str1)):
    list1.append(str1[i])
print(min(list1))
