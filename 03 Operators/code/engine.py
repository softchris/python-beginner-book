working_bay_energy = 50
engine_min_value = 10
engine_max_value = 100
energy_rerouted = 30

print("The working bay initially had", working_bay_energy, "units of energy. Tabitha decided to reroute", energy_rerouted, "units of energy to the engines.")
print("After rerouting, the working bay is left with", working_bay_energy - energy_rerouted, "units of energy.")
print("Using the rerouting equation, the engine effect is calculated as:")
engine_effect = ((energy_rerouted + 3) * 5) / 4
print("Engine effect =", engine_effect)

if engine_min_value <= engine_effect <= engine_max_value:
    print("The engine effect is within the safe limits.")
else:
    print("Warning: The engine effect is outside the safe limits!")