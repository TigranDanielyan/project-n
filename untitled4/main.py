class Person:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        print("there person class")

    def Getstarted(self):
        type = input("please give name ")
        if type == self.name:
            type = input("please give password ")
            if type == self.password:
                print("hello", self.name)

        else:
            print ("not in system")


class Teacher (Person):
    def __init__(self,name,password,leverage):
        super().__init__(name,password)
        self.leverage = leverage
        print("ther is teacher subclass")
    def Leveragecheck(self):
        type = input("please give again give your leverage number ")
        if type == self.leverage:
            print ("You are teacher and you can state your date of choice")

class student(Person):
    def __init__(self, name,password,VoteAmountLeverage):
        super().__init__(name,password)
        self.VoteAmountLeverage = VoteAmountLeverage
        print ("theer is student subclass")

    def VoteAmountLeveragecheck(self):
        type = input("please give again give your leverage number")
        if type == self.VoteAmountLeverage:
            print ("You are student and you need 20 more to undo a teacher")


def main ():
    dr1 = Teacher("Anny","113",1)
    dr1.Getstarted()
    dr1.Leveragecheck()
    dr1.oteAmountLeveragecheck()

main()
