#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Ben
print("Winner: {}".format(isWinner(3, [4, 5, 1])))  # Ben
print("Winner: {}".format(isWinner(2, [1, 2])))  # None
print("Winner: {}".format(isWinner(2, [2, 2])))  # Maria


# Maria wins
print('Maria wins')
print("Winner: {}".format(isWinner(3, [5, 5, 1])))
print("Winner: {}".format(isWinner(1, [2])))
print("Winner: {}".format(isWinner(3, [0, 11, 11])))
print("Winner: {}".format(isWinner(2, [6, 11, 0, 4, 1])))

print('')

# Ben wins
print('ben wins')
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(1, [1])))
print("Winner: {}".format(isWinner(1, [0])))
print("Winner: {}".format(isWinner(3, [0, 0, 0])))
print("Winner: {}".format(isWinner(5, [1, 1, 1, 1, 1])))
print("Winner: {}".format(isWinner(2, [0, 0, 0, 11, 11, 11])))

print('')

# None
print('None')
print("Winner: {}".format(isWinner(4, [2, 3, 5, 10])))
print("Winner: {}".format(isWinner(6, [0, 0, 0, 11, 11, 11])))
print("Winner: {}".format(isWinner(0, [])))
