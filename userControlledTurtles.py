import turtle
dist = int(input("How far? "))
angle = int(input("What angle? "))
reps = int(input("How many times? "))
turtle.clear()
i = 0
while i <= reps:
	turtle.forward(dist)
	turtle.right(angle)
	i += 1