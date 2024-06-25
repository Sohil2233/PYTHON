programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

#retriving item from dictionary
print(programming_dictionary["Bug"])

#Adding new item to dict
programming_dictionary["Loop"]="The action of doing something over again"

#creating empty dict
empty_dict={}

# WIPE up existing dictionary
# programming_dictionary={}

# edit item in dictionary
programming_dictionary["Loop"]="You are in loop"

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


print(programming_dictionary)