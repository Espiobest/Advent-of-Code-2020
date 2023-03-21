import sys


def solve(a):
    locations = dict()  # Create a dictionary with masks as keys and values being the memory location and its number

    for x in a:  # Assign a new mask else assign memory location new value
        if x[0] == 'mask':
            mask = x[2]
        else:
            new_mask = int_to_mask(len(mask), int(x[2]))
            locations[x[0][4:-1]] = mask_to_int(list(mask), list(new_mask))
    print(sum(locations.values()))


def int_to_mask(length, num):
    return ((length - len(bin(num)[2:])) * '0') + bin(num)[2:]  # Convert the value to its bitmask


def mask_to_int(mask_one, mask_two):  # Put the created mask over the current mask and return it in base 2.
    tmp_mask = [x for x in mask_one]

    for count, x in enumerate(mask_two):
        if tmp_mask[count] == 'X':
            tmp_mask[count] = x
    return int(''.join(tmp_mask), 2)


def main():
    a = [x.split() for x in open("data.txt","r").readlines()]
    solve(a)


main()