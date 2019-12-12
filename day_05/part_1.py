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

    input_num = 1
    outputs = []
    index = 0
    while True:
        instr = pad_instr(data[index])
        opcode = instr[3:]
        a_mode = instr[2]
        b_mode = instr[1]
        if opcode in ["01", "02"]:
            a = data[index + 1]
            b = data[index + 2]
            if a_mode == "0":
                a = data[a]
            if b_mode == "0":
                b = data[b]
            if opcode == "01":
                data[data[index + 3]] = a + b
            else:
                data[data[index + 3]] = a * b
            index += 4
        elif opcode == "03":
            data[data[index + 1]] = input_num
            index += 2
        elif opcode == "04":
            outputs.append(data[data[index + 1]])
            index += 2
        elif opcode == "99":
            break

    print(outputs)
