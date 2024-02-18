# Function is a block of codes which performs a particular task.\
# This method below is called passing an argument or parameters.
name = input('What is your name: ')
age = input('How old are you: ')
def greetings_function(name, age):
    print('Welcome ' +name+  ' You are ' +age+ ' years old this year!')

greetings_function(name, age)

# Functions in python are case sensitive and it wise to know it has an automatic indentation when passing a function but when calling that function, you need to exit the indentation by using the backspace on you keypad or keyboard.

# You start a function with the keyword "def" which simply means, define function.

# Second method of defining or using a function in python.

def functionaries(*names):
    print('Welcome ' +names[2])

functionaries('Samuel', 'Jennifer', 'Alice')

# '*names' defines that we are passing in alot of users name but we dont know who is next on the list, so with the help of the '*' we can then use the '[]' index number of each user to identify.

