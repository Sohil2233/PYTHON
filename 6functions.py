print(f"Hello World!")
num_char=len("Hello World!")#here len()is function. it is buit in function
print(num_char)


# Defining a function
def my_function():
  print("hello")
  print("bye")
# Calling the function
my_function()


#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()



move()
move()
move()
turn_around()
move()
move()
move()
turn_right()



# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
for i in range(0,5):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
    

