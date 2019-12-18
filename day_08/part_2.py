##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import auxly

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    width = 25
    height = 6

    data = [int(i) for i in open("input.txt").read().strip()]
    layers = list(auxly.listy.chunk(data, width * height))

    index = 0
    for _ in range(height):
        for _ in range(width):
            for layer in layers:
                if layer[index] == 0:
                    print(" ", end="")
                    break
                elif layer[index] == 1:
                    print("#", end="")
                    break
            index += 1
        print()
