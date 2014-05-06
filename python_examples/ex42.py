## Animal is-a object
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is an Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person(object):
    def __init__(self, name):
        ## person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a init method
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet cat named satan
mary.pet = satan

## frank is-an employee
frank = Employee("Frank", 120000)

## frank has-a pet dog named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
