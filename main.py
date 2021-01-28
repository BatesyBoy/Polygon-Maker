import turtle
print("============================\n========POLYGON MAKER=======\n============================")
t = turtle.Turtle()
while True:
	sides=int(input("> INPUT POLYGON SIDES (3-12) "))
	thick=int(input("> INPUT PEN THICKNESS (1-10) "))
	colour=input("> INPUT COLOUR ").lower()
	if sides>12 or sides<3 or thick>10 or thick<1:
		print("> INVALID INPUT- TRY AGAIN")
	else:
		t.color(colour)
		t.pensize(thick)
		for x in range(0,sides):
			t.forward(500/sides)
			t.right(360/sides)
		rerun=input("> RERUN PROGRAM (Y/N) ").upper()
		if not rerun=="Y":
			print("> PROGRAM ENDED")
			break
		else:
			clear=input("> CLEAR CANVAS (Y/N)").upper()
			if clear=="Y":
				t.reset()
			print("> RERUNNING PROGRAM")