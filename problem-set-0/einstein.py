# Einstein thought problem
# author : jguerreiro

"""
  E = m.c²
  E -> energy
  M -> mass
  C -> speed of light (constant)
"""

SPEED_OF_LIGHT = 300000000 # 300mi of km/h

print("Welcome to the E = m.c² calculator!\n")

mass = int(input("What is the mass? "))

energy = mass * (SPEED_OF_LIGHT ** 2)

print(f'The energy is: {energy}')

# Simple tests

# energy50 = 4500000000000000000
# energy14 = 1260000000000000000
# energy1 = 90000000000000000

# test50 = True if mass == 50 and energy14 else False
# print(f'Passed! -> Mass = 50 -> result: {test50}')

# test14 = True if mass == 14 and energy14 else False
# print(f'Passed! -> Mass = 14 -> result: {test14}')

# test1 = True if mass == 1 and energy1 else False
# print(f'Passed! -> Mass = 1 -> result: {test1}')