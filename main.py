#WEEEK 7(LOOPS)
#loops
#for loops

for i in range(5):
    print("welcome to kenya\n")

mylist =[45.7,89.0,34.6,23.5]
for j in mylist:
    print(j, end= ",")

for i in "Jane" :
    print(i.capitalize())
    print(i.lower())

mylist3 = range (7,18,3)
for i,no in enumerate(mylist3):
    print("Index ",i," has value",no,".\n")
    print("Index"+str(i)+" has value" "+str(")

#while loop
y=3
while y< 10:
    print(y)
    y+=1


#Range
l1=range(7)
l2=range(7,20)
l3=range(7,20,3)
print(l1)
print(l2)
print(l3)

for i in l1:
    print(i,end="")
for i in l2:
    print(i,end="")
for i in l3:
    print(i,end="")


for i in range(1,6):
    print(i, end="")
    for j in range(1,6):
        if i<j:
            print(j, end=" ")
            print()

numbs =[5,6,8,9,5,7,5,2,4,5,8,9,5]
for i in numbs:
    if i==5:
        continue
    elif i==7:
        break

        print(i, end="")

#WEEK 8(PYTHON FUNCTIONS)
def funcl1():
    print("i love programming")
    funcl()

#parametralised function
#quadratic equations
def quad(a, b, c):
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print("The discriminant is negative")
        print("The roots are complex")
    elif discriminant == 0:
        print("The roots are equal")
        x1 = -b / (2*a)
        print("x1 = x2 =", x1)
    else:
        print("The roots are distinct")
        x1 = (-b + (discriminant ** 0.5)) / (2*a)
        x2 = (-b - (discriminant ** 0.5)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
n=int(input('Enter a number'))
if n > 70:
    print("The BusFare is Overpriced")
elif n ==70:
    print("The Busfare is Okay")
else:
    print("Invalid Input, Please try again")






