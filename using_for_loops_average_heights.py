# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
students = 0
heights = 0
for height in student_heights:
    students += 1
    heights += height

average = round(heights/students)
print(average)