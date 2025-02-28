def add_to_str(fmt_str, current_range):
    if len(current_range) == 1:
        fmt_str.append(f'{current_range[0]}')
    elif len(current_range) == 2:
        fmt_str.append(f'{current_range[0]}')
        fmt_str.append(f'{current_range[1]}')
    else:
        fmt_str.append(f'{current_range[0]}-{current_range[-1]}')

    return fmt_str

def solution(args):
    current_range = []
    current_range.append(args[0])
    fmt_str = []
    for (x,y) in zip(args[:-1], args[1:]):
        if x+1 == y:
            current_range.append(y)
        else:
            fmt_str = add_to_str(fmt_str, current_range)
            current_range = [y]
        # print(fmt_str)

    fmt_str = add_to_str(fmt_str, current_range)

    return ','.join(fmt_str)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))   # '-6,-3-1,3-5,7-11,14,15,17-20')