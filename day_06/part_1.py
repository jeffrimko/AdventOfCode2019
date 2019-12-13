##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def count_orbits(target):
    os = orbits.get(target, [])
    count = len(os)  # direct orbits
    for o in os:  # indirect orbits
        count += count_orbits(o)
    return count

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    orbits = {}
    for line in open("input.txt").read().splitlines():
        target, orbited_by  = line.split(")")
        orbits.setdefault(target, [])
        orbits[target].append(orbited_by)

    count = 0
    for target,orbited_by in orbits.items():
        count += count_orbits(target)

    print(count)
