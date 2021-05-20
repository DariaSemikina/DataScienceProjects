import numpy as np


def score_game(game_core, start=1, end=101, size=1000):
    '''
    An interface that calls game core function in a loop 1000 times
    for getting an average number of attempts

    Parameters
    -------
    game_core: int
        the function version name

    Returns
    -------
    score:
        the average number of attempts
    '''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(start, end, size)

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in {score} attempts")

    return (score)


# version 1 of game_core function
def game_core_v1(number):
    '''
    A function that guesses a given number by using a random number
    between its nearest neighbors

    Parameters
    -------
    number: int
        the number which should be guessed

    Returns
    -------
    count:
        the number of guessing attempts
    '''
    count = 1
    predict = np.random.randint(1, 101)
    left_neighbor = 1
    right_neighbor = 101

    while number != predict:
        count += 1
        if number > predict:
            left_neighbor = predict + 1
            predict = np.random.randint(left_neighbor, right_neighbor)
        elif number < predict:
            right_neighbor = predict
            predict = np.random.randint(left_neighbor, right_neighbor)

    return (count)


# version 2 of game_core function
def game_core_v2(number):
    '''
    A function that guesses a given number by using binary search algorithm

    Parameters
    -------
    number: int
        the number which should be guessed

    Returns
    -------
    count:
        the number of guessing attempts
    '''
    count = 1
    predict = np.random.randint(1, 101)
    left_neighbor = 1
    right_neighbor = 101

    while number != predict:
        predict = (left_neighbor + right_neighbor) // 2
        count += 1
        if number > predict:
            left_neighbor = predict + 1
        elif number < predict:
            right_neighbor = predict - 1

    return (count)


# Functions execution
score_game(game_core_v1)
score_game(game_core_v2)