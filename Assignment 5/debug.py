def bust(total, num1, num2, num3):
    if total > 21 and (num1 == 11 or num2 == 11 or num3 == 11):
        print (total - 10)
    elif total > 21:
        print (0)


def main():
    num1 = int(input("enter a random value twin: "))
    num2 = int(input("enter a random value twin: "))
    num3 = int(input("enter a random value twin: "))

    total = num1 + num2 + num3

    if total <= 21:
        print (total)
    else:
        print (bust(total, num1, num2, num3))


main()

def printHello():
    print("Hello")
    
def printName(x):
    printName(x)
    
def addition(x, y):
    return x + y

def smaller(i, j):
    if i < j: 
        return i
    if j < i: 
        return j
    if j == i:
        return 0

def main():

    printHello()
    print("Hello") 
    
   
    Name = "JayBalla"
    print(Name)
    
    x = 10
    y = 20
   
    print (addition (x,y))
    
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter a second number "))
    #what go here?
    print(smaller(num1, num2))





main()
