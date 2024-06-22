def greet():
    print("hi")
    print("how are you")
    print("k")
greet()

# function allow for inputs

def greet_with_num(number):
    print("you recevied ",number)

greet_with_num(123)

# function with multiple inputs

def greet_me(name,location):
    print("my name is ",name)
    print("i live at ",location)

# greet_me("soul","ves")
# greet_me("ves","soul")
greet_me(location="ves",name="soul")
