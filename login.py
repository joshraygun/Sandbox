from hashlib import sha1
import sys
import json
print("Welcome!")
credentials = []
while True:
	try:
		usr = input("Please enter a username:\n")
		with open("login_credentials.json") as login:
			try:
				credentials = json.load(login)
			except json.decoder.JSONDecodeError:
				pass
		for entry in credentials:
			if entry["username"].lower() == usr.lower():
				while True:
					pwd = input("Please, enter your password, or just press enter to quit.\n")
					if entry["password"] == sha1(pwd.encode()).hexdigest():
						print(f"Welcome, " + entry["username"] + "!")
						input()
						sys.exit()
					break
				break
		login.close()		
		print(f"Username {usr} could not be found.")
	except FileNotFoundError:
		print("Building user file.\n")
	while True:
		create = input("Would you like to create a new account? Y/n\n")
		if create.lower() == 'y':
			with open("login_credentials.json", 'w+') as login:
				pwd = sha1(input("Add a new password!\n").encode()).hexdigest() 
				credentials.append({"username":usr,"password":pwd})
				json.dump(credentials, login)
				login.close()
				pwd =""
				print("We'll be sure to remember you for next time!")
			break
		elif create.lower() == 'n':
			print("Thank you for visiting!")
			input()
			sys.exit()