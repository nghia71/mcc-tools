from math import ceil, sqrt
from random import choice, shuffle
import sys
from mcc_api import Pegasus


#
# Determine if a number is a prime by looking at the remainder
# when divided the number by all integers
# between 2 and the number's square root
#
def is_prime(number):
    for i in range(2, ceil(sqrt(number)+1)):
        if number % i == 0:
            return False
    return True


#
# Verify if any odd number equal to or larger than the given number is a prime
#
def my_next_prime(number):
    number = int(number)
    next_prime = number if number % 2 == 1 else number + 1
    found_prime = False
    while not found_prime:
        found_prime = is_prime(next_prime)
        if found_prime:
            return next_prime
        next_prime += 2
    return next_prime

#
# Find the position of the fake coin in two weighings
#
def my_fake_coin(coins):
    my_coins = [int(c) for c in coins]  # Convert to integers
    group_a, group_b, group_c = my_coins[0:3], my_coins[3:6], my_coins[6:]
    weight_a, weight_b = sum(group_a), sum(group_b)

    if weight_a < weight_b:  # First weighing, fake coin is in group A
        if group_a[0] < group_a[1]:
            return 0
        elif group_a[0] > group_a[1]:
            return 1
        else:  # group_a[0] == group_a[1]
            return 2
    elif weight_a > weight_b:  # fake coin is in group B
        if group_b[0] < group_b[1]:
            return 3
        elif group_b[0] > group_b[1]:
            return 4
        else:  # group_a[0] == group_a[1]
            return 5
    else:  # weight_a == weight_b, fake coin is in group C
        if group_c[0] < group_c[1]:
            return 6
        else:  # group_c[0] < group_c[1]
            return 7


#
# Demonstrate the move sequence of a knight
#
def my_move_sequence(position):
    valid_moves = {
        1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9],
        6: [1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
    }

    current_position = int(position)
    move_sequence = [current_position]  # starts from the given position

    while len(move_sequence) < 8:  # until all 8 moves are made
        next_postion_1, next_postion_2 = valid_moves[current_position]
        if next_postion_1 not in move_sequence:
            current_position = next_postion_1
            move_sequence.append(next_postion_1)
        elif next_postion_2 not in move_sequence:
            current_position = next_postion_2
            move_sequence.append(next_postion_2)
        else:
            break
    return ''.join(['%s' % i for i in move_sequence])


if __name__ == '__main__':
    # Setup your credentials
    conf_file = sys.argv[1] if len(sys.argv) > 0 else 'mcc.conf'
    p = Pegasus(conf_file, test=True)

    ########################################
    # Task for the next_prime problem: uncomment and make them work
    #
    result = p.submit('next_prime', my_next_prime, 3)
    print('next_prime:', result)

    ########################################
    # Task for the fake_coin problem: uncomment and make them work
    #
    result = p.submit('fake_coin', my_fake_coin, 3)
    print('fake_coin', result)

    ########################################
    # Task for the move_sequence problem: uncomment and make them work
    #
    result = p.submit('move_sequence', my_move_sequence, 3)
    print('move_sequence', result)
