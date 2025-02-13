"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 2/3/25
Homework Problem # 3_3
Description of Problem: Create an interactive cafe menu where the user can order an item by entering either its name or number, ensuring case-insensitivity and prompting until a valid selection is made.
"""
# Define menu items as a constant list
MENU = ["ham", "eggs", "bacon", "fish", "toast", "spam", "fruit"]

def breakfast_cafe():
    print("Welcome to the Breakfast Café!") # Welcome message
    
    while True: # Continue prompting until a valid selection is made
        print("Please select a menu item:")
        # Print numbered list of menu items
        for i, item in enumerate(MENU, start=1):
            print(f"\t{i}. {item}")
        
        # Prompt user for their selection
        order = input("Your order? ").strip().lower()
        
        # Check if input is a number
        if order.isdigit():
            index = int(order) - 1 # Convert to zero-based index
            if 0 <= index < len(MENU): # Ensure the number is within range
                print(f"A delicious order of {MENU[index]} has been put in for you!")
                break # Exit loop
        # Check if input is a menu item name
        elif order in (item.lower() for item in MENU):
            print(f"A delicious order of {order} has been put in for you!")
            break
        else:
            # Prompt again if input is invalid
            print("Sorry, I don't think we carry that.")
# Run program
breakfast_cafe()
