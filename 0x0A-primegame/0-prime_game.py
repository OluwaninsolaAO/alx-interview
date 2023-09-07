#!/usr/bin/python3
"""0. The Prime Game"""


def isWinner(x: int, nums: list) -> str:
    """determine who the winner of each game is between Ben and Maria"""
    #  print('x:', x, 'nums:', nums)
    ben = 0
    maria = 0

    for round in range(x):
        arr = list(range(1, nums[round] + 1))
        #  print('Round', round + 1, ':', arr)

        index = 0
        while len(arr) > 1:
            index += 1
            #  print('Maria\'s' if index % 2 == 1 else 'Ben\'s', 'move:', arr)
            prime = arr[1]
            for num in arr[:]:
                if num % prime == 0:
                    arr.pop(arr.index(num))
        if index % 2 == 1:
            maria += 1
            #  print('Maria won!', '>>>', 'Ben:', ben, 'Maria:', maria)
        else:
            ben += 1
            #  print('Ben won!', '>>>', 'Ben:', ben, 'Maria:', maria)

    #  print('Ben:', ben, 'Maria:', maria)
    # return results
    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    return None
