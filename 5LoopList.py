fruit =["Apple", "Banana", "Grape", "Strawberry", "Melon", "Orange"]
for i in fruit:
  print(i+"  pie")
print(fruit)



# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# average heigth
sum=0
for n in range(0, len(student_heights)):
  sum=sum+student_heights[n]

print("total height =",sum)
print("number of students =",len(student_heights))
print("average height =",round(sum/len(student_heights)))



# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# highest score
max=student_scores[0]
for n in range(1, len(student_scores)):
  if student_scores[n]>max:
    max=student_scores[n]
print("The highest score in the class is:",max)



# FizzBuzz game
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif(i%3==0):
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)