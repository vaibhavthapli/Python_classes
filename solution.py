# Q1

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# total = num1 + num2
# print(f"Sum of two numbers is {total}")
# print(f"Total of {num1} and {num2} is {total}")

# Q2

# a = "123"
# print(type(a))
# b = int(a)
# print(type(b))
#
# c= 123
# print(type(c))
# d= str(c)
# print(type(d))

#Q3

# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = length * width
# print(f"Area of rectangle is {area}")

#Q4

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter teh second number: "))
# num3 = int(input("Enter the third number: "))
# average = (num1 + num2 + num3)/3
# print(f"Average is {average}")

#Q5 Convert a fl oat to an integer and vice versa.

#Q6

# f = float(input("Enter temperature in Fahrenheit : "))
# c = (f-32)*5/9
# print(f"Answer = {c}")
# print(f"{f} Fahrenheit = {c} Celsius")

#Q7
# print("Enter marks of 5 subjects")
# s1 = float(input("Enter marks of first subject: "))
# s2 = float(input("Enter marks of second subject: "))
# s3 = float(input("Enter marks of third subject: "))
# s4 = float(input("Enter marks of forth subject: "))
# s5 = float(input("Enter marks of fifth subject: "))
# total = s1 + s2+ s3+ s4 + s5
# average = total/5
# percentage = (total/500.0)*100
# print(f"Total marks = {total}")
# print(f"Average marks = {average}")
# print(f"Percentage = {percentage}")

#Q8

games_palyed = int(input("Enter the number of games played: "))
game_won = int(input("Enter hte number of games won: "))
game_loss = int(input("Enter the number of games loss: "))

game_ties = games_palyed - game_won - game_loss
print(f"Games ties = {game_ties}")

total_points = (game_won*4) + (game_ties*2)
print(total_points)
