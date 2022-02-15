import random


"""
На входе функция получает параметр n - натуральное число.
Необходимо сгенерировать n-массивов, заполнить их случайными числами, каждый массив имеет случайный размер.
Размеры массивов не должны совпадать. Далее необходимо отсортировать массивы.
Массивы с четным порядковым номером отсортировать по возрастанию, с нечетным порядковым номером - по убыванию.
На выходе функция должна вернуть массив с отсортированными массивами.
"""

def q_sort(a: list):
    if a:
        pivot = a[random.choice(range(0, len(a)))]
        less = q_sort([i for i in a if i < pivot])
        greater = q_sort([i for i in a if i > pivot])
        return less + [i for i in a if i == pivot] + greater
    else:
        return a

def sorted_arrays_array(n: int):
    main_array = [] # an array of arrays
    len_array = [] # set of len of arrays
    for i in range(n):
        num = random.randint(1, n) # choose a random number
        while num in len_array: # if the len is already in the array change it
            num = random.randint(1, n * 2) # enlarge the bounds of picking
        len_array.append(num) # I don't think this should be used
    for i in range(n):
        tmp = []
        for j in range(len_array[i]): # fill the arrays with random numbers
            tmp.append(round(random.random() * 1000))
        main_array.append(tmp)

    for i in range(n): # sort the arrays by the rules
        if i % 2 == 0:
            main_array[i] = q_sort(main_array[i])
        else:
            main_array[i] = q_sort(main_array[i])[::-1]
    return main_array

def test_func(result: list) -> bool:
    test = []
    for i in result:
        if len(i) in test:
            return False
        else:
            test.append(len(i))
    return True


def main():
    result = sorted_arrays_array(int(input()))

    if not test_func(result):
        print("You failed this task")
        return

    for i in result:
        print(F"len of array is {len(i)}\n{i}")

if __name__ == '__main__':
    main()
