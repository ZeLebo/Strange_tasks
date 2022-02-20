from test_task import sorted_arrays_array as test

def test_array_size(result: list):
    test = []
    for i in result:
        if len(i) in test:
            print(result)
            return False
        else:
            test.append(len(i))
    return True


def test_sorted(result: list):
    for i in range(len(result)):
        if i % 2 == 0:
            tmp = result[i][:]
            tmp.sort()
            if tmp != result[i]:
                print(i)
                return False
        else:
            tmp = result[i][:]
            tmp.sort(reverse=True)
            if tmp != result[i]:
                print(i)
                return False
    return True


def main():
    result = test(int(input()))

    if test_array_size(result) and test_sorted(result):
        print("The task is done")
        for i in result:
            print(F"Array: {i}")
        return

    print("You failed this task")


if __name__ == '__main__':
    main()
