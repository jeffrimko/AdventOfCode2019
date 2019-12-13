##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def get_orbits(target):
    direct_orbits = orbits.get(target, [])
    count = len(direct_orbits)  # direct orbits
    indirect_orbits = []
    for o in direct_orbits:  # indirect orbits
        indirect_orbits += get_orbits(o)
    return direct_orbits + indirect_orbits

def jump(orbits, src, dst):
    count = 1
    if dst in get_orbits(src):
        orbited_by = orbits[src]
        for o in orbited_by:
            if dst in get_orbits(o):
                count += jump(orbits, o, dst)
                break
    else:
        for target,orbited_by in orbits.items():
            if src in orbited_by:
                count += jump(orbits, target, dst)
                break
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

    src = "YOU"
    dst = "SAN"
    count = jump(orbits, src, dst)

    # NOTE: The first two jumps are subtracted since they are the src and the
    # original orbited object. These are not considered actual jumps just setup.
    print(count - 2)
