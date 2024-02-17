#This excerse is getting input of a user but later wants to change it to something else.

# Outline
# User initial input
# Value to be change
# Result after editing

sentence = input("Enter your Bank statement: ")
print('Your Bank Statement is: ', sentence)

# Correction to be made.
edit = input("Enter the word here: ")

# Value after edited.
result = input("Enter the replacement here: ")

#printing out the final result to the user.
print(sentence.replace(edit, result))