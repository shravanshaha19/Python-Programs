class country:
    def __init__(self,cnm,carea,cpop,scnt):
        self.cnm=cnm
        self.carea=carea
        self.cpop=cpop
        self.scnt=scnt
    def disp1(self):
        print("Country Name:",self.cnm)
        print("Country Area:",self.carea)
        print("Country Population:",self.cpop)
        print("State Count",self.scnt)
class state(country):
    def __init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt):
        country.__init__(self,cnm,carea,cpop,scnt)
        self.snm=snm
        self.sarea=sarea
        self.spop=spop
        self.dcnt=dcnt
    def disp2(self):
        print("State Name:", self.snm)
        print("State Area:", self.sarea)
        print("State Population:", self.spop)
        print("District Count", self.dcnt)
class dist(state):
    def __init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt,dnm,darea,dpop,tcnt):
        country.__init__(self,cnm,carea,cpop,scnt,snm,sarea,spop,dcnt)
        self.dnm=dnm
        self.darea=darea
        self.dpop=dpop
        self.tcnt=tcnt
    def disp3(self):
        print("District Name:", self.dnm)
        print("District Area:", self.darea)
        print("District Population:", self.dpop)
        print("Taluka Count", self.tcnt)
cnm=input("Enter the Country name:")
carea=int(input("Enter the Country Area:"))
cpop=int(input("Enter the Country Population:"))
scnt=int(input("Enter the State Count:"))
snm=input("Enter the State name:")
sarea=int(input("Enter the State Area:"))
spop=int(input("Enter the State Population:"))
dcnt=int(input("Enter the District Count:"))
dnm=input("Enter the District name:")
darea=int(input("Enter the District Area:"))
dpop=int(input("Enter the District Population:"))
tcnt=int(input("Enter the Taluka Count:"))
d1=dist(cnm,carea,cpop,scnt,snm,sarea,spop,dcnt,dnm,darea,dpop,tcnt)
d1.disp1()
d1.disp2()
d1.disp3()