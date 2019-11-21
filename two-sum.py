def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,j in enumerate(nums):
            num = target - j
            if num in dic:
                return [dic[num],i]
            dic[j] = i 
        return []
