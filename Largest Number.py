class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
    
        def compare(a, b):
            if a + b > b + a:
                return -1 
            else:
                return 1  
        
        nums_str.sort(key=cmp_to_key(compare))
        
        result = ''.join(nums_str)
        
        return '0' if result[0] == '0' else result

  
s = Solution()
print(s.largestNumber([10, 2])
