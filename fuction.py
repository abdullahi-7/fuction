## Function
 #Day1

# Morning routine function
def morning_routine():
    print("Wake up")
    print("Go to the washroom")
    print("Brush your teeth")
    print("Pray")
    print("Wear uniform")
    print("Eat breakfast")
    print("take your bag and go to school!")

 #Day 1

print("")
morning_routine()

def monday_routine():
    print("wear uniform")
    print("take your bag")
    print("go to the school")
    print("read the book")
    print("go to the break time")
    print("back to the school")
    print("write")
    print("go to the luch time")
    print("write the question")
    print("go back at home")
    print("pray")

# all the name of the fuction is monday_routine()
#S monday 
print("")
monday_routine()

# Tuesday 
print("")
monday_routine()



# wednesday
print("")
monday_routine()




# thursday 
print("")
monday_routine()
# friday

# print("")
monday_routine()


# Saturday
print("")
monday_routine()


## We can place all basics inside a function
## such as : variable, data types, conditional, user input and output...

def name():
    # name of the variable is question
    name = input("What's your name? ")
    print (name)
    n ="Abdullahi"
    age = 12
    school = "Mvita" 
    print(n, age, school)

print("")
#all the name is the name ofthe fuction
name()

name()

name()

## Function take parameter or argument, like variable takes value

def sum(numX, numY):
    print(numX + numY)

print(" \nFunction with arguement")
numberX = int(input("Write your first number? "))
# the nnumberX is a variable and is a integer
numberY = int(input("Write your second number? "))
# and numberY is a integer
sum(numberX, numberY)

# exercise
# de is a fuction
def num(numbX, numbY):
# the numbX and numbY is name of a fuction
    print(numbX + numbY)


# Variable that take first number from the user
numbeX = int(input("write the first number: "))
# Variable that take second number from the user
numbeY = int(input("write the second number:"))
# calling num() function
num(numbeX, numbeY)

##  return value
print("\nreturning value of function")
def multiply(x):
    return x * 2
# when calling your function place it inside print()
print(multiply(3))

# exercise
#subtruct is a fuction
def subtruct(S):
    return S * 3
# return is used for fuction
print(subtruct("\nnasra\n"))
