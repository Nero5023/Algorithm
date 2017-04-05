class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumAll = sum(nums)
        if sumAll & 1:
            return False
        target = sumAll >> 1
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for t in range(target, num-1, -1):
                dp[t] = dp[t] or dp[t - num]
        return dp[target]



# bool canPartition(vector<int>& nums) {
#     int sum = accumulate(nums.begin(), nums.end(), 0), target = sum >> 1;
#     if (sum & 1) return false;
#     vector<int> dp(target + 1, 0);
#     dp[0] = 1;
#     for(auto num : nums) 
#         for(int i = target; i >= num; i--)
#             dp[i] = dp[i] || dp[i - num];
#     return dp[target];
# }

if __name__ == '__main__':
    s = Solution()
    print s.canPartition([1,5,11,5])