"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 2/3/25
Homework Problem # 3_1
Description of Problem: Calculate the exact amount of wrapping paper needed for a rectangular box by computing its surface area plus a small extra amount, allowing repeated calculations until the user chooses to exit.
"""
def calculate_wrapping_paper():
    print("Welcome to the gift-wrap calculator!") # Welcome message
    
    while True:
        # Prompt user for box dimensions
        dimensions = input("Please enter the box dimensions separated with an x, e.g. 10x20x15: ")
        
        # Exit condition
        if dimensions.lower() == "quit":
            print("Thank you for using the gift-wrap calculator!")
            break
        
        # Convert input string "LxWxH" into three integer values
        try:
            l, w, h = map(int, dimensions.split('x'))  # Split the input by 'x' and convert to integers
        except ValueError:
            print("Invalid input. Please enter dimensions as LxWxH (e.g., 10x20x15).")
            continue  # Ask again if input is incorrect
        
        # Calculate surface area of box
        area1 = l * w
        area2 = w * h
        area3 = h * l
        surface_area = 2 * (area1 + area2 + area3)
        
        # Fudge factor
        smallest_side = min(area1, area2, area3)
        total_paper = surface_area + smallest_side

        print(f"You will need {total_paper}cm of wrapping paper.")
# Run program
calculate_wrapping_paper()
