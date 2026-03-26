class Solution:
    def minEatingSpeed(self, piles, h):
        st = 1
        end = max(piles)

        while st <= end:
            mid = st + (end - st) // 2
            totalhr = 0

            for pile in piles:
                totalhr += (pile + mid - 1) // mid   

            if totalhr <= h:
                end = mid - 1   
            else:
                st = mid + 1   

        return st
