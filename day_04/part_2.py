##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def is_valid_password(num):
    num = str(num)
    if len(num) != 6:
        return False
    last_char = num[0]
    adj = {}
    for char in num[1:]:
        if last_char > char:
            return False
        if char == last_char:
            adj[char] = adj.setdefault(char, 1) + 1
        last_char = char
    return bool([count for count in adj.values() if count == 2])

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    valid = 0
    for num in range(256310, 732736 + 1):
        if is_valid_password(num):
            valid += 1
    print(valid)
