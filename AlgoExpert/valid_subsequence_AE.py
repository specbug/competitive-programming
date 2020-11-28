def isValidSubsequence(array, sequence):
    for i in sequence:
        if i in array:
            arr_ind = array.index(i)
            if arr_ind + 1 > len(array) - 1:
                array = []
            else:
                array = array[arr_ind + 1:]
        else:
            return False

    return True


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

    print(isValidSubsequence(array, sequence))
