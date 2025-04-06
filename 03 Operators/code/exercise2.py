# Define variables
base_energy = 10
asteroid_density = 5
maneuverability = 3

energy_required = (base_energy + asteroid_density * 2) ** 2 / (maneuverability + 1)
print("The energy required to navigate the asteroid field is:", energy_required)