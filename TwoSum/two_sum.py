import enum


class TwoSum:
    def twoSum(self, nums, target):
        #iterate through every combination
        #brute force method
        indexes = []
        
        for i in range(len(nums) - 1 ):
            for j in nums[i + 1:]:
                print("Combo: " + str(nums[i]) + " and " + str(j))
                if(nums[i] + j == target):
                    indexes = [i, nums.index(j)]
                    return indexes
                                

    def twoSumHash(self, nums, target):
        hashmap = {}
        for i, value in enumerate(nums):
            compliment = target - value
            print(hashmap)
            if compliment in hashmap:
                return [hashmap[compliment], i]
            else:
                hashmap[value] = i