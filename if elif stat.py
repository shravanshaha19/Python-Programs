mark=int(input("Enter marks:"))

if(mark>=75 and mark<=100):
    print("F.C.W.D")
elif(mark>=65 and mark<75):
    print("F.C")
elif(mark>=55 and mark<65):
    print("S.C")
elif(mark>=45 and mark<55):
    print("Pass")
elif(mark):
    print("Invalid Marks")
else:
    print("Fail")
