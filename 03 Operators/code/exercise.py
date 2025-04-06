import math

from_coord = (1, 2, 3)
to_coord = (4, 5, 6)

# calc distance
distance = math.sqrt((to_coord[0] - from_coord[0]) ** 2 + (to_coord[1] - from_coord[1]) ** 2 + (to_coord[2] - from_coord[2]) ** 2)

print("The distance between the coordinates", from_coord, "and", to_coord, "is", distance)
