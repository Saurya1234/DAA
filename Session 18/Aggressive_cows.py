class Solution:

    def canPlace(self, stalls, k, dist):
        count = 1
        lastPosition = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - lastPosition >= dist:
                count += 1
                lastPosition = stalls[i]

                if count >= k:
                    return True

        return False

    def aggressiveCows(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if self.canPlace(stalls, k, mid):
                ans = mid
                low = mid + 1   
            else:
                high = mid - 1  

        return ans
