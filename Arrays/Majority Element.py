def majorityElement(self, nums: List[int]) -> int:
    d=list(set(nums))
    for i in range(len(d)):
        if nums.count(d[i]) > len(nums)/2:
            return d[i]
