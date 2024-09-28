class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
    
        year_binary = bin(int(year))[2:]
        month_binary = bin(int(month))[2:]
        day_binary = bin(int(day))[2:]
        
        result = year_binary + '-' + month_binary + '-' + day_binary
        
        return result
    
s = Solution()
print(s.convertDateToBinary("2012-10-12"))