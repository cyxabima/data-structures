def Dec_Bin(number):
    stack = []
    while number != 0:
        stack.append(number % 2)  # reminder will always be zero or 1
        number = number // 2

    ret = ""
    while stack:
        ret += str(stack.pop())

    return ret


print(Dec_Bin(67))
