class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_count = Counter(digits)
        result = []

       
        for num in range(100, 1000, 2):
            num_count = Counter(int(d) for d in str(num))
            
            
            if all(num_count[d] <= digit_count[d] for d in num_count):
                result.append(num)

        return result        
