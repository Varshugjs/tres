str1=input()
str1=str1.split()
num1=int(str1[0])
num2=int(str1[1])
res=num1+num2
if res%2==0:
    print("even")
else:
    print("odd")
