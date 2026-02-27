class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        result = 0
        
        for d in num2:
            result = result * 10 + int(d)
        
        final = 0
        for d in num1:
            final = final * 10 + int(d)
        
        return str(result * final)
