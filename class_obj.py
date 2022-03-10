class employee:
    def __init__(self,name,idno,phnno,hospital):
        self.name=input("enter the name")
        self.idno=input("enter your idno")
        self.phnno=input("enter your phnno")
        self.hospital=input("enter your hospital")


    def printData(self):
        print(self.name)
        print(self.idno)
        print(self.phnno)
        print(self.hospital)


a=employee("name","idno","phnno","hospital")
a.printData()