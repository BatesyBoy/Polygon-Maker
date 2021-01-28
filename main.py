import turtle
print("============================\n========POLYGON MAKER=======\n============================")#Line 2: Makes Some Simple ASCII Art
t = turtle.Turtle()
while True:
	sides=int(input("> INPUT POLYGON SIDES (3-12) "))#Lines 5-7: Polygon Options
	thick=int(input("> INPUT PEN THICKNESS (1-10) "))
	colour=input("> INPUT COLOUR ").lower()
	if sides>12 or sides<3 or thick>10 or thick<1:#Lines 8-9: Checks For Invalid inputs
		print("> INVALID INPUT- TRY AGAIN")
	else:
		t.color(colour)
		t.pensize(thick)
		for x in range(0,sides): #Lines 13-15: Draws Polygon
			t.forward(500/sides)
			t.right(360/sides)
		rerun=input("> RERUN PROGRAM (Y/N) ").upper()#Lines 16-24: Checks If The Program Should Run Again And If So, If The Canvas Should Be Cleared.
		if not rerun=="Y":
			print("> PROGRAM ENDED")
			break
		else:
			clear=input("> CLEAR CANVAS (Y/N)").upper()
			if clear=="Y":
				t.reset()
			print("> RERUNNING PROGRAM")