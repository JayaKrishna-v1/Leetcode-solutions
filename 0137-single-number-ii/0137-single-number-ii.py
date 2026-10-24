class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(32):              
            count = 0
            for n in nums:
                if (n >> i) & 1:           
                    count += 1
            if count % 3:                  
                result |= (1 << i)          

        if result >= 2**31:                 
            result -= 2**32
        return result