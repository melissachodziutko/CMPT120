

class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        

class Dog(Animal):
    def __init__(self, age, name, breed):
        super().__init__(age, name)
        self.breed = breed
        
    #make a function that checks if the dog is your favorite breed
    #if it is, tell the user that's your favorite breed
    #else, it's still a good dawg

#finish this for me! Cats have an age and a name (already set up)
#some cats have their ear clipped- keep track of if they have their ear clipped or not
#https://bestfriends.org/pet-care-resources/ear-tipping-cats-what-it-and-why-its-done
#in case you were wondering what i was talking about ^ 

class Cat(Animal):
    def __init__(self, age, name):
        #?
        
    #make a function that checks for that clip- if it is, mention to the user that the cat must have been a stray at some point
    #if not, say that the cat was likely always an inside cat!
        
        
def main():
    #Here's a few good examples
    a1 = Animal(10, "buddy")
    print(a1.name)
    d1 = Dog(10, "frank", "lab")
    print(d1.breed)
    #call the function in dog here
    
    #create a cat and call your function

main()
