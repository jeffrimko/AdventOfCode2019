##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import itertools

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class Computer:
    def __init__(self, name, phase, data):
        self.name = name
        self.data = data
        self.index = 0
        self.status = "running"
        self.inputs = [phase]

    def process(self, inputs):
        self.inputs += inputs
        outputs = []
        while True:
            instr = pad_instr(self.data[self.index])
            opcode = instr[3:]
            a_mode = instr[2]
            b_mode = instr[1]
            if opcode in ["01", "02", "05", "06", "07", "08"]:
                a = self.data[self.index + 1]
                b = self.data[self.index + 2]
                if a_mode == "0":
                    a = self.data[a]
                if b_mode == "0":
                    b = self.data[b]
                if opcode == "01":
                    self.data[self.data[self.index + 3]] = a + b
                    self.index += 4
                elif opcode == "02":
                    self.data[self.data[self.index + 3]] = a * b
                    self.index += 4
                elif opcode == "05":
                    if a != 0:
                        self.index = b
                    else:
                        self.index += 3
                elif opcode == "06":
                    if a == 0:
                        self.index = b
                    else:
                        self.index += 3
                elif opcode in ["07", "08"]:
                    c = self.data[self.index + 3]
                    if opcode == "07":
                        if a < b:
                            self.data[c] = 1
                        else:
                            self.data[c] = 0
                    if opcode == "08":
                        if a == b:
                            self.data[c] = 1
                        else:
                            self.data[c] = 0
                    self.index += 4
            elif opcode == "03":
                a = self.data[self.index + 1]
                self.data[a] = self.inputs.pop(0)
                self.index += 2
            elif opcode == "04":
                a = self.data[self.index + 1]
                outputs.append(self.data[a])
                self.index += 2
                return outputs
            elif opcode == "99":
                self.status = "halted"
                return outputs

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
    max_inputs = None
    max_output = 0
    for phases in itertools.permutations([5,6,7,8,9]):
        output = [0]
        e_output = 0
        computers = []
        names = "ABCDE"
        for name,phase in zip(names,phases):
            computers.append(Computer(name, phase, data))

        while computers[-1].status != "halted":
            for c in computers:
                output = c.process(output)
                if c.name == "E" and output:
                    e_output = output[0]
        if e_output > max_output:
            max_output = e_output
            max_inputs = phases
    print(max_inputs, max_output)
