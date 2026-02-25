class Solution:
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        
        ugly = [1] * n
        index = [0] * k
        next_multiple = primes.copy()
        
        for i in range(1, n):
            next_ugly = min(next_multiple)
            ugly[i] = next_ugly
            
            for j in range(k):
                if next_multiple[j] == next_ugly:
                    index[j] += 1
                    next_multiple[j] = ugly[index[j]] * primes[j]
        
        return ugly[n-1]
