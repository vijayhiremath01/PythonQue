class Solution :
    def majorityElement(self , nums : list[int]) -> int :
        counts = {}
        n = len(nums)
        
        for num in nums :
            counts[num] = counts.get(num , 0 ) + 1 
            
            if counts[num] > n // 2 :
                return num 
            
        return -1 
    
    
#Example Usage
nums = [int(x) for x in input("Enter the elements of the array (comma` separated) : ").split(",")]
solution = Solution()
result = solution.majorityElement(nums) 
print(f"The majority element is: {result}")