import random

"""
At the input, the function get natural number
You need to generate n arrays of unique size, fill them with random numbers
Then the arrays needed to be sorted:
    Arrays with an even ordinal number should be sorted in ascending order
    Other - in descending order
Function returns the array of arrays
"""


def sorted_arrays_array(n: int):
    if not isinstance(n, int):
        raise TypeError('input number must be an integer')
    if n < 1:
        raise ValueError('Not natural number')

    main_array = []  # an array of arrays
    len_array = set()  # set of len of arrays
    for i in range(n):
        num = random.randint(1, n)  # choose a random number
        while num in len_array:  # if the len is already in the array change it
            num = random.randint(1, n * 2)  # enlarge the bounds of picking
        len_array.add(num)
    for i in range(n):
        len_array = list(len_array)
        # fill the array with random numbers
        tmp = [round(random.random() * 1000) for _ in range(len_array[i])]
        main_array.append(tmp)

    for i in range(n):  # sort the arrays by the rules
        if i % 2 == 0:
            main_array[i].sort()
        else:
            main_array[i].sort(reverse=True)
    return main_array
