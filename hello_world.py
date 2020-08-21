from hashlib import sha1
import sys
usr = ""
pwd = ""
print("Welcome!")
while True:
	usr = input("Please enter a username:\n")
	print("Username received")
	with open("login_credentials.txt") as login:
		for line in login.readlines():
			if ("usr:" + usr) in line:
				while True:
					pwd = sha1(input("Please input your password:\n").encode()).hexdigest()
					if f"usr:{usr},pwd:{pwd}" not in line:
						print("Sorry! Password was incorrect.")
					else:
						print(f"Welcome, {usr}!")
						input()
						sys.exit()

	print(f"Username {usr} could not be found.")
	while True:
		restart = input("Would you like to create a new account? Y/n\n")
		if restart.lower() == 'y':
			with open("login_credentials.txt", 'a') as login:
				pwd = sha1(input("Add a new password!\n").encode()).hexdigest()
				login.write(f"usr:{usr},pwd:{pwd}\n")
				pwd =""
				print("We'll be sure to remember you for next time!")
			break
		elif restart.lower() == 'n':
			print("Thank you for visiting!")
			input()
			sys.exit()