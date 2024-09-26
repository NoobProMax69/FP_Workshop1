#Function to print the title
def title_graphic(title):
    print("--------------------")
    print(f"{title:^20}")
    print("--------------------")

#Function to print the menu
def menu():
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished\n")
    #Return the user's choice as an input
    return int(input("Enter your choice: "))

#Initializing variables
menu_choice = 0
added_items = []
title = input("Enter the title: ")

#Loop to run the program
while menu_choice != 3:
    menu_choice = menu()
    if menu_choice == 1:
        added_items.append(input("Enter an item: "))

    elif menu_choice == 2:
        if not added_items:
            print("The shopping list is empty.\n")
        else:
            print("Currently added items:")
            for item in added_items:
                print(item)
            print("\n")

    elif menu_choice > 3:
        print("Error: Invalid choice, please try again.\n")

if not added_items:
    title_graphic(title)
    print("The shopping list is empty.\n")
else:
    title_graphic(title)
    for item in added_items:
        print(item)