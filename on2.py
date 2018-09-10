str1=input()
flag=0
for i in range(len(str1)):
    if(ord(str1[i])==48 or ord(str1[i])==49):
        flag=flag+1
    else:
        flag=-1
        break
if(flag==-1):
    print("no")
else:
    print("yes")
