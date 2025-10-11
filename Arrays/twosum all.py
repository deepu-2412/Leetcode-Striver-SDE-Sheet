def twoSum(self, nums: List[int], target: int) -> List[int]:
    visited = {} 
    result = []
    for i, num in enumerate(nums):
        if (target - num) in visited:
            result.append([i , visited[target - num]])
        visited[num] = i
    return result
