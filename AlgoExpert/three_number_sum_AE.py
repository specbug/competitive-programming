def recursiveSearch(arr, target_sum, ret):
    final = []
    for i in range(len(arr)):
        rem = target_sum - arr[i]
        if not ret:
            if i < len(arr)-1:
                final += [[arr[i]] + l for l in recursiveSearch(arr[i+1:], rem, True)]
        else:
            if rem in arr[i+1:]:
                final.append([arr[i], rem])
    return final


def threeNumberSum(array, targetSum):
    array = sorted(array)
    return recursiveSearch(array, targetSum, False)

if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0

    print(threeNumberSum(array, targetSum))
