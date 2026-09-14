class Solution:
    def climbStairs(self, n: int) -> int:
        tab = [0] * (n + 1)
        tab[n] = 1
        tab[n-1] = 1

        for i in range(n-2, -1, -1):
            print(i)
            tab[i] = tab[i+1]+tab[i+2]
        
        return tab[0]
        