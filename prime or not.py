count=0
no=int(input("Enter a number:"))
for i in range(1,11):
    if(no%i==0):
        count=count+1
if(count==2):
    print(no,"Is prime.")
else:
    print(no,"Is not prime.")