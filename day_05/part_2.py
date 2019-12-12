##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def pad_instr(instr_num):
    return f"{instr_num:05}"

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    data = [int(i) for i in open("input.txt").read().strip().split(",")]

    input_num = 5
    outputs = []
    index = 0
    while True:
        instr = pad_instr(data[index])
        opcode = instr[3:]
        a_mode = instr[2]
        b_mode = instr[1]
        c_mode = instr[0]
        if opcode in ["01", "02", "05", "06", "07", "08"]:
            a = data[index + 1]
            b = data[index + 2]
            if a_mode == "0":
                a = data[a]
            if b_mode == "0":
                b = data[b]
            if opcode == "01":
                data[data[index + 3]] = a + b
                index += 4
            elif opcode == "02":
                data[data[index + 3]] = a * b
                index += 4
            elif opcode == "05":
                if a != 0:
                    index = b
                else:
                    index += 3
            elif opcode == "06":
                if a == 0:
                    index = b
                else:
                    index += 3
            elif opcode in ["07", "08"]:
                c = data[index + 3]
                if opcode == "07":
                    if a < b:
                        data[c] = 1
                    else:
                        data[c] = 0
                if opcode == "08":
                    if a == b:
                        data[c] = 1
                    else:
                        data[c] = 0
                index += 4
        elif opcode == "03":
            a = data[index + 1]
            data[a] = input_num
            index += 2
        elif opcode == "04":
            a = data[index + 1]
            outputs.append(data[a])
            index += 2
        elif opcode == "99":
            break

    print(outputs)
