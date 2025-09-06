#2 Different ways (homework from lesson 2)
#Make a function that prints from 0 to a number 

m=0
while m<=20:
    print(m)
    m=m+5

for p in range(50):
    print(p)

#Making the function

def something(n):
    m=0
    while m <= n:
        print(m)
        m=m + 1

something(9)

print()
#next function
def homework2(numTimes):
    for i in range(numTimes+ 1):
        print(i)

homework2(10)

def return1():
    return 1

var=1
var2=return1()

def checkGreater10(x):
    if x>10:
        return True
    else:
        return False
        
a=checkGreater10(9)
print(a)

print(checkGreater10(9))

#arrays

bob=[1, 2, 3]
print(bob)

bob.append(10)
print(bob)

bob.remove(3)
print(bob)

print(bob[1])

bob[1]=25
print(bob)

bob[2]=42
print(bob)

print(bob[0] + bob[1] + bob[2])

#Get user input
x = input("What is your name?: ")
print(x)