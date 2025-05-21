class clg:
    def __init__(self,clgnm,clgloc,dcnt,scnt):
        self.clgnm=clgnm
        self.clgloc=clgloc
        self.dcnt=dcnt
        self.scnt=scnt
    def dis1(self):
        print("College name:",self.clgnm)
        print("College location:",self.clgloc)
        print("Department count:",self.dcnt)
        print("Student count:",self.scnt)
class stud(clg):
    def __init__(self,clgnm,clgloc,dcnt,scnt,nm,rn,mark):
        clg.__init__(self,clgnm,clgloc,dcnt,scnt)
        self.nm=nm
        self.rn=rn
        self.mark=mark
    def dis2(self):
        print("Student name:",self.nm)
        print("Roll no:",self.rn)
        print("Marks:",self.mark)
clgnm=input("Enter colleg name:")
clgloc=input("Enter college location:")
dcnt=int(input("Enter department count:"))
scnt=int(input("Enter student count:"))
nm=input("Enter student name:")
rn=int(input("Enter roll no:"))
mark=float(input("Enter mark:"))
s1=stud(clgnm,clgloc,dcnt,scnt,nm,rn,mark)
s1.dis1()
s1.dis2()

