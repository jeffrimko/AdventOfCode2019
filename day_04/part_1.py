##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def is_valid_password(num):
    num = str(num)
    if len(num) != 6:
        return False
    last_char = num[0]
    two_adj = False
    for char in num[1:]:
        if last_char > char:
            return False
        if not two_adj and char == last_char:
            two_adj = True
        last_char = char
    return two_adj

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    valid = 0
    for num in range(256310, 732736 + 1):
        if is_valid_password(num):
            valid += 1
    print(valid)
