# Check object is a subclass of a particular class

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print("Dog is a subclass of Animal? –>",issubclass(Dog,Animal))
print("Animal is a subclass of Dog? –>",issubclass(Animal,Dog))
print("Cat is a subclass of Animal? –>",issubclass(Cat,Animal))
print("Puppy is a subclass of Animal–>",issubclass(Puppy,Animal))
