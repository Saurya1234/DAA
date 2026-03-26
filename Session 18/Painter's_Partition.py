class Solution:

    def canPaint(self, arr, k, maxTime):
        currentTime = 0
        painters = 1

        for i in range(len(arr)):

            if arr[i] > maxTime:
                return False

            if currentTime + arr[i] <= maxTime:
                currentTime += arr[i]
            else:
                painters += 1
                currentTime = arr[i]

                if painters > k:
                    return False

        return True

    def minTime(self, arr, k):
        low = max(arr)
        high = sum(arr)

        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.canPaint(arr, k, mid):
                ans = mid
                high = mid - 1   
            else:
                low = mid + 1    

        return ans
