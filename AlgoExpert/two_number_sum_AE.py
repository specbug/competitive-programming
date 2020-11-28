def twoNumberSum(array, targetSum):
    # Write your code here.
    watched = []
    for el in array:
        if el not in watched:
            watched.append(el)
            c_el = targetSum - el
            if c_el in set(array) - set(watched):
                return [el, c_el]
            else:
                watched.append(c_el)

    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    print(twoNumberSum(array, targetSum))
