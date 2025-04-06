energy_to_reroute = 50
taking_energy = 40
remaining_energy = energy_to_reroute - taking_energy

engine_effect = ((taking_energy + 3) * 5) / 4

print(f"Ship engine effect {engine_effect}, leaving {remaining_energy} behind")