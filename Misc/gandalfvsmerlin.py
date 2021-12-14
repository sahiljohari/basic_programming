def minPower(path):
    initial_power = 1
    current_power = initial_power
        
    for obs in path:
        current_power += obs
        if current_power < 0:
            initial_power -= current_power
            initial_power += 1
            current_power = 1
    return initial_power

paths = [
    [-4, -3, -2],
    [4, -3, 1, 2, -6, 8],
    [-1, 1, -2, 3, -7, 2]
]

for path in paths:
    print(minPower(path))