#program to check if a number is an armstrong number or not

num=int(input("enter any number:"))

temp=num
sum=0
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10

if temp==num:
    print("the number",temp,"is an armstrong number")
else:
    print("the number",temp,"is not an armstrong number")