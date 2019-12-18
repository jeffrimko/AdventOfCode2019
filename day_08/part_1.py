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

    num_zeros = []
    layers = list(auxly.listy.chunk(data, width * height))
    for layer in layers:
        num_zeros.append(layer.count(0))
    min_zeros = min(num_zeros)
    min_index = num_zeros.index(min_zeros)
    min_zero_layer = layers[min_index]
    print(min_zero_layer.count(1) * min_zero_layer.count(2))
