import turtle
print("============================\n========POLYGON MAKER=======\n============================")
t = turtle.Turtle()
while True:
	sides=int(input("> INPUT POLYGON SIDES (3-12) "))
	thick=int(input("> INPUT PEN THICKNESS (1-10) "))
	colour=input("> INPUT COLOUR (RED,BLUE,BLACK,GREEN,YELLOW) ").upper()
	sideloop=sides
	if sides>12 or sides<3 or thick>10 or thick<1:
		print("> INVALID INPUT- TRY AGAIN")
	else:
		if colour=="RED":
			t.color("red")
		elif colour=="BLUE":
			t.color("blue")
		elif colour=="BLACK":
			t.color("black")
		elif colour=="GREEN":
			t.color("green")
		elif colour=="YELLOW":
			t.color("yellow")
		while sideloop>0:
			t.pensize(thick)
			t.forward(500/sides)
			t.right(360/sides)
			sideloop=sideloop-1
		rerun=input("> RERUN PROGRAM (Y/N) ").upper()
		if not rerun=="Y":
			print("> PROGRAM ENDED")
			break
		else:
			t.reset()
			print("> RERUNNING PROGRAM")