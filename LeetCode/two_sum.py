def twoSum(nums, target):
    
    hash_map = {}
    
    for i in range(len(nums)):
        i_complement = target - nums[i]
        if i_complement in list(hash_map.values()):
            return [i, list(hash_map.keys())[list(hash_map.values()).index(i_complement)]]
        
        hash_map[i] = nums[i]


num_list = list(map(int, input().split()))
n_target = int(input())

print(twoSum(num_list, n_target))