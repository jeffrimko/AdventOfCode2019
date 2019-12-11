##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    data = [int(i) for i in open("input.txt").read().strip().split(",")]
    data[1] = 12
    data[2] = 2

    opindex = 0
    while True:
        opcode = data[opindex]
        if opcode in [1,2]:
            a = data[data[opindex + 1]]
            b = data[data[opindex + 2]]
            if opcode == 1:
                data[data[opindex + 3]] = a + b
            else:
                data[data[opindex + 3]] = a * b
            opindex += 4
        if opcode == 99:
            break

    print(data[0])
