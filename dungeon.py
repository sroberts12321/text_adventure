class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#print color.BOLD + 'Hello World !' + color.END


print("Hello and welcome to the dungeon!")
#char_name = str(input("What would you like to be called? "))

def confirmation():
	char_name = str(input("What would you like to be called? "))
	confirm = input(f"Are you sure you'd like to be called {char_name}? Y/N  ")
	if confirm.lower() == "y":
		print("\n\n\n" + color.RED + "Excelceor!" + color.END + f" Welcome {char_name}, and prepare yourself!")
	else:
		print("Ok...")
		confirmation()

def first_room():
	print("\n\n\nYou find yourself standing at the entrance to a sprawling cave system\nThe air is damp and cool with the scent of mildew and faint decay")
	print("Torch in hand you walk into the cave. \nYou arrive at a fork in the tunnel which way do you go?\n\n")
	first_direction = str(input("\n\n\nLeft or Right? "))
	if first_direction.lower() == "left" or "l":
		second_room()
	elif first_direction.lower() == "right" or "r":
		third_room()

def second_room():
	print("\n\n\nYou follow the path left down a steep decline and end up in a huge chamber filled with pools of dark water.")
	print("The sound of dripping water is heard echoing throughout the chamber and you feel a presence like something is watching you.")
	second_room_reaction = str(input("\n\n\nWhat do you do?\n1. Stay absolutely still for as long as it takes\n2. Investigate the room\n3. Go back\n"))
	if second_room_reaction == "1":
		print("test")
	elif second_room_reaction == "2":
		print("test2")
	elif second_room_reaction == "3":
		first_room()
	else:
		print("Invalid response, here are the options again")
def third_room():
	print("\n\n\nYou died of disentery")


confirmation()
first_room()