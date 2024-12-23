# Declare weight variable
weight = 8.4

# Ground Shipping
if weight <= 2:
  cost_ground = (1.5*weight) + 20
elif weight <= 6:
  cost_ground = (3*weight) + 20
elif weight <= 10:
  cost_ground = (4*weight) + 20
else:
  cost_ground = (4.75*weight) + 20
print(f"The cost to ship your package with Ground Shipping is: ${cost_ground:.2f}.")

# Premium Ground Shipping
ground_premium = 125.00
print(f"The flat charge for Ground Shipping Premium is: ${ground_premium:.2f}.")

# Drone Shipping
if weight <= 2:
  cost_drone = (4.5*weight)
elif weight <= 6:
  cost_drone = (9*weight) 
elif weight <= 10:
  cost_drone = (12*weight) 
else:
  cost_drone = (14.25*weight) 
print(f"The cost to ship your package with Drone Shipping is: ${cost_drone:.2f}.")
