from itertools import combinations

def answer(num_buns, num_required):
    # One keyring per bunny.
    bunny_keyrings = [[] for num in range(num_buns)]
    # The number of keys each bunny requires is described by this formula, which I noticed by doing some napkin math.
    # If N == 4 and M == 4, bunnies_per_key == 1.
    # If N == 2 and M == 1, bunnies_per_key == 2.
    # If N == 5 and M == 3, bunnies_per_key == 3.
    # This generally fit the formula bunnies_per_key = N - M + 1.
    bunnies_per_key = num_buns - num_required + 1

    for keynum, keyholders in enumerate(combinations(range(num_buns), bunnies_per_key)):
        # print(keynum, keyholders)
        for index in keyholders:
            bunny_keyrings[index].append(keynum)

    return bunny_keyrings