class TwoSum(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False

        buff_dict = {}

        # Create a dictionary, with key of target minus current element in nums, and value of current
        # index. if current element in nums is equal to one of keys in dictionary, return corresponding
        # indeces
        for i in range(len(nums)):

            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
