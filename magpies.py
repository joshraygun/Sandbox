num = -1
while num != 0:
	num = int(input("How many magpies (1-10) did you see? (Input 0 to exit)\n"))
	if num == 0:
		break
	elif num > 10:
		print("Sorry, that's too many birds")
	elif num < 0:
		print("Who is taking our birds? Are you taking our birds?")
	else:
		with open("magpies.txt") as rhyme:
			print(rhyme.readlines()[num-1])