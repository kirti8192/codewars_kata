import itertools

def get_adjacent():
    # ┌───┬───┬───┐
    # │ 1 │ 2 │ 3 │
    # ├───┼───┼───┤
    # │ 4 │ 5 │ 6 │
    # ├───┼───┼───┤
    # │ 7 │ 8 │ 9 │
    # └───┼───┼───┘
    #     │ 0 │
    #     └───┘

    adjacent_key = {
        '1': ['1', '2', '4'], 
        '2': ['1', '2', '3', '5'], 
        '3': ['2', '3', '6'], 
        '4': ['1', '4', '5', '7'], 
        '5': ['2', '4', '5', '6', '8'], 
        '6': ['3', '5', '6', '9'], 
        '7': ['4', '7', '8'], 
        '8': ['5', '7', '8', '9', '0'], 
        '9': ['6', '8', '9'], 
        '0': ['0', '8']
    }

    return adjacent_key

def get_pins(observed):

    num_digits = len(observed)
    candidate_pins = []
    adjacent_key = get_adjacent()

    if not observed:
        return []
    
    candidate_pins = adjacent_key[observed[0]]
    for ii in range(1, num_digits):
        next_adjacent_list = adjacent_key[observed[ii]]     # get adjacent list for character ii
        candidate_pins = [item[0]+item[1] for item in itertools.product(candidate_pins, next_adjacent_list)]
        # print(candidate_pins)

    return candidate_pins

print(get_pins('369'))

    # [
    #         "339","366","399","658","636","258","268","669","668","266","369","398",
    #         "256","296","259","368","638","396","238","356","659","639","666","359",
    #         "336","299","338","696","269","358","656","698","699","298","236","239"
    #     ]