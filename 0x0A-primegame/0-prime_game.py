#!/usr/bin/python3
"""0. The Prime Game"""


def isWinner(x: int, nums: list) -> str:
    """determine who the winner of each game is between Ben and Maria"""
    ben = 0
    maria = 0
    index = 1

    for round in range(x):
        arr = list(range(2, nums[round] + 1))

        while len(arr) != 0:
            prime = arr[0]
            for num in arr[:]:
                if num % prime == 0:
                    arr.pop(arr.index(num))
            index += 1
        if index % 2 == 1:
            maria += 1
        else:
            ben += 1

    # return results
    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    elif ben == 0 and maria == 0:
        return 'Ben'
    return None
