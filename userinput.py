#Getting an input from users and we store them in a variable before printing them to the user.
surname = input("your Surname Here: ")
firstName = input("Your firstname Here: ")
otherName = input("Do you have other names: ")
age = input("What's your Age: ")
dob = input("Your Date of Birth: ")
status = input("What is your marital status: ")
address = input("Where do you reside: ")
nationality = input("Your Residence country: ")
birth = input("Your Country of Birth: ")
qualification = input("What is your highest qualification: ")


#Printing to the User.
# print(surname, firstName, otherName, age, dob, status, address, nationality, birth, qualification, 'Check if the data is correct before submitting.')

#We can choose to concatenate.
print('Your name is ' + surname + firstName + ' and you are ' + age + ' years old ' + ' born in ' + dob)

#Converting a string to integer.
value = int(input(" Your Estimate is: "))
print("the Value estimation goes up to ", value)