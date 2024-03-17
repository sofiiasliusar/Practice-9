class Person():
    def preference(self):
        print("any breakfast")

class Parent(Person):
    def preference(self):
        print("fruit")
class Man(Person):
    def preference(self):
        print("donut")
    
class Woman(Person):
    def preference(self):
        print("croissant")
    
class Worker(Person):
    def preference(self):
        print("bacon")

class WorkingMan(Man, Worker):
    pass
        
class WorkingWoman(Worker, Woman):
    pass

class Father(Parent, Man):
    pass

class Mother(Parent, Woman):
    pass

class WorkingFather(WorkingMan, Father):
    pass

class WorkingMother(Mother, WorkingWoman):
    pass

jim = WorkingMan()
jim.preference()
joan = WorkingWoman()
joan.preference()
print(jim.preference() or joan.preference())
