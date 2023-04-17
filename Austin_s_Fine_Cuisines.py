# Dolan, Austin
# ICS 110P Assignment 11
# November 17 2022
# Program that displays my restaurant menu using a dictionary and allows user to add items, remove items, and keeps track of cost of all items.


def print_menu(menu):
	# Print out menu for guest to view names of items and prices
	print("                   _   _       _       ______ _               _____      _     _                 ")
	print(r"    /\            | | (_)     ( )     |  ____(_)             / ____|    (_)   (_)                ")
	print(r"   /  \  _   _ ___| |_ _ _ __ |/ ___  | |__   _ _ __   ___  | |    _   _ _ ___ _ _ __   ___  ___ ")
	print(r"  / /\ \| | | / __| __| | '_ \  / __| |  __| | | '_ \ / _ \ | |   | | | | / __| | '_ \ / _ \/ __|")
	print(r" / ____ \ |_| \__ \ |_| | | | | \__ \ | |    | | | | |  __/ | |___| |_| | \__ \ | | | |  __/\__ \ ")
	print(r"/_/    \_\__,_|___/\__|_|_| |_| |___/ |_|    |_|_| |_|\___|  \_____\__,_|_|___/_|_| |_|\___||___/")
	print()
	print()
	print("                                  _ __ ___   ___ _ __  _   _ ")
	print(r"                                 | '_ ` _ \ / _ \ '_ \| | | |")
	print(r"                                 | | | | | |  __/ | | | |_| |")
	print(r"                                 |_| |_| |_|\___|_| |_|\__,_|")
	print("                         _______________________________________________                             ")
	# Loop through every item in menu and display name of item and price
	for m in menu:
		print(f"\t\t\t<| {m.upper()}\n\t\t\t\t\t\t\t\t${menu[m]:,.2f} |>          ")
	print("                         _______________________________________________                             ")

def main():
	# Create dictionary with keys(names of items) and values(prices of items)
	menu = {'garlic bread' : 6.95, 'cheese bread' : 9.50, 'caprese salad' : 14.95, 'caesar salad' : 12.95, 'greek salad' : 11.95, 'house salad' : 11.95, 'calamari pasta' : 14.95, 'ribeye pupu' : 21.99, 'chicken parm' : 23.99, 'shrimp alfredo' : 34.99, 'jambalaya pasta' : 25.99, 'chicken alfredo' : 18.99, 'ny cheesecake' : 9.50}
	# Variables
	total = 0.0
	change_item = ""
	prompt_be_seated = "\nWould you like to be seated so that you can begin ordering? (yes or no) "
	prompt_instructions = "\nYou can 1. add an item, 2. remove an item, or 3. check-out. What would you like to do? (1, 2, or 3) "
	prompt_add_item = "\nWhat item would you like to add to your order?(type name of item) "
	prompt_remove_item = "\nWhat item would you like to remove from your order? "
	# Take user name
	user_name = input("Hello, and welcome to Austin's Fine Cuisines, what's your name?\n").capitalize()
	print(f"\n{user_name}, here at AFC you can order or remove items until you feel you are ready to check out.\n I will keep a running tab for you so you know exactly how much you are going to spend.\n")
	# Run print_menu and pass dictionary(menu) to function
	print_menu(menu)
	# Take input in form of yes or no from user used to start loop
	run_afc = input(prompt_be_seated).lower()
	while run_afc != 'no':
		if run_afc == 'yes':
			# Ask the user what they would like to do: 
			try:
				command = int(input(prompt_instructions))
				# 1. Add item accesses price of item and adds cost to total
				if command == 1:
					change_item = input(prompt_add_item).lower()
					if change_item in menu:
						total += menu[change_item]
						print(f"Cost of {change_item.upper()} is ${menu[change_item]}.")
						print(f"{change_item.upper()} has been added to your order.", end = " ")
						print(f"Current total: ${total:,.2f}")
					else:
						print(f"{change_item} is not currently on the menu.\n")
				# 2. Delete item removes cost of item from total		
				elif command == 2:
					change_item = input(prompt_remove_item).lower()
					if change_item in menu:
						total -= menu[change_item]
						print(f"Cost of {change_item.upper()} is ${menu[change_item]}.")
						print(f"{change_item.upper()} has been removed from your order.", end = " ")
						print(f"Current total: ${total:,.2f}")
					else:
						print(f"{change_item} is not currently on the menu.\n")
				# 3. Checkout will print out total cost of items user wants to purchase and ends program		
				elif command == 3:
					print(f"\nThe total cost of your order is ${total:,.2f}")
					print("Thank's for dining at Austin's Fine Cuisines!\n  Goodbye!")
					break
				else:
					print("\nThat is not a command I recognize.")
			except ValueError as e:
				print("\nThat is not a valid response. Please try again.")
				print("Error:", end = " ")
				print(e)
		else:
			print(f"\n{run_afc} is not a valid response.")
			run_afc = input(prompt_be_seated).lower()
		
main()

