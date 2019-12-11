##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    for noun in range(100):
        for verb in range(100):
            with open("input.txt") as fi:
                data = [int(i) for i in fi.read().strip().split(",")]
            data[1] = noun
            data[2] = verb

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
            if data[0] == 19690720:
                print(100 * noun + verb)
                exit()
