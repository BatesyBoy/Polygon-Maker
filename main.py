import turtle
print("============================\n========POLYGON MAKER=======\n============================")
t = turtle.Turtle()
while True:
	sides=int(input("> INPUT POLYGON SIDES (3-100) "))
	sideloop=sides
	if sides>100 or sides<3:
		print("> INVALID INPUT- TRY AGAIN")
	else:
		while sideloop>0:
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
