# Function
# Day1

# Morning routine function
def morning_routine():
    print("Wake up")
    print("Go to the washroom")
    print("Brush your teeth")
    print("Pray")
    print("Wear uniform")
    print("Eat breakfast")
    print("take your bag and go to school!")

# Day 1
print("")
morning_routine()

# Day 2
print("")
morning_routine()
#print("Wake up")
#print("Go to the washroom")
#print("Brush your teeth")
#print("Pray")
#print("Wear uniform")
#print("Eat breakfast")
#print("take your bag and go to school!")

# Day 3
#print("Wake up")
#print("Go to the washroom")
#print("Brush your teeth")
#print("Pray")
#print("Wear uniform")
#print("Eat breakfast")
#print("take your bag and go to school!")

# Day 4
#print("Wake up")
#print("Go to the washroom")
#print("Brush your teeth")
#print("Pray")
#print("Wear uniform")
#print("Eat breakfast")
#print("take your bag and go to school!")


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

# monday 
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
print("")
monday_routine()


# Saturday
print("")
monday_routine()


## We can place all basics inside a function
# such as : variable, data types, conditional, user input and output...

def name():
    name = input("What's your name? ")
    print (name)
    n ="Abdullahi"
    age = 12
    school = "Mvita" 
    print(n, age, school)

print("")
name()

name()

name()

## Function take parameter or argument, like variable takes value

def sum(numX, numY):
    print(numX + numY)

print(" \nFunction with arguement")
numberX = int(input("Write your first number? "))
numberY = int(input("Write your second number? "))
sum(numberX, numberY)
