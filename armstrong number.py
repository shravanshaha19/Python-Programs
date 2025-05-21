num=int(input("Enter the number:"))
sum=0
org=num
while num>0:
    rem=num%10
    sum=rem**3
    num//=10
if  org==sum:
    print(org,"Is armstrong.")
else:
    print(num,"Is not armstrong.")