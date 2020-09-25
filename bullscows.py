def digits(number):
    return [int(d) for d in str(number)]

def bulls_and_cows(guess, target):
    guess, target = digits(guess), digits(target)
    bulls = [d1 == d2 for d1, d2 in zip(guess, target)].count(True)
    bovine = 0
    for digit in set(guess):
      bovine += min(guess.count(digit), target.count(digit))
    return bulls, bovine - bulls

print(bulls_and_cows(5518,4618))

