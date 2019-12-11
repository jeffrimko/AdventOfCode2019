##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def trace_wire(path):
    trace = []
    loc_x = 0
    loc_y = 0
    for movement in path:
        direction = movement[0]
        distance = int(movement[1:])
        while distance > 0:
            if direction == "U":
                loc_x += 1
            elif direction == "D":
                loc_x -= 1
            elif direction == "R":
                loc_y += 1
            elif direction == "L":
                loc_y -= 1
            distance -= 1
            trace.append((loc_x, loc_y))
    return trace

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    with open("input.txt") as fi:
        lines = fi.readlines()
        w1 = lines[0]
        w2 = lines[1]
    t1 = trace_wire(w1.split(","))
    t2 = trace_wire(w2.split(","))
    intersects = set(t1) & set(t2)
    print(min(map(lambda c: abs(c[0]) + abs(c[1]), intersects)))
