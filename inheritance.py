class Parent():
    def __init__(self, name, age, phoneno):
        self.name = name
        self.age = age
        self.phoneno = phoneno

    def displayDetails(self):
        print(self.name)
        print(self.age)
        print(self.phoneno)


class Child(Parent):
    def __init__(self, name, age, phoneno, child_name, child_age, child_number):
        self.child_name = child_name
        self.child_age = child_age
        self.child_number = child_number

        Parent.__init__(self,name, age, phoneno)

    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone_number:", self.phoneno)
        print("Child_name:", self.child_name)
        print("Child_age:", self.child_age)
        print("child Phone number:", self.child_number)

x = Child("Renu","40","9750188078","Leela", "21", "9566629654")
x.printDetails()
x.displayDetails()