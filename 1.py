class Person():
    def __init__(self, breakfast):
        self.breakfast = breakfast 
class Parent(Person):
    print
    breakfast = "fruit"
class Man(Person):
    print
    breakfast = "donut"
class Woman(Person):
    print
    breakfast = "croissant"
class Worker(Person):
    print
    breakfast = "bacon"
class WorkingMan(Man, Worker):
    print(f"I choose {self.breakfast} for breakfast.")
class WorkingWoman(Worker, Woman):
    print
class Father(Parent, Man):
    print
class Mother(Parent, Woman):
    print
class WorkingFather(WorkingMan, Father):
    print
class WorkingMother(Mother, WorkingWoman):
    print
