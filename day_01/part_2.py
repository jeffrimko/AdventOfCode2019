##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import math

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def calc_fuelreq(mass):
    masses = []
    while True:
        mass = math.floor(mass / 3) - 2
        if mass <= 0:
            break
        masses.append(mass)
    return sum(masses)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    masses = open("input.txt").readlines()
    total_fuel = 0
    for mass in masses:
        mass = int(mass.strip())
        total_fuel += calc_fuelreq(mass)
    print(total_fuel)
