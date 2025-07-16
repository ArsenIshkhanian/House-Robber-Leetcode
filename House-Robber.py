class Solution:
    def rob(self, nums) -> int:
        amount = []
        count = []
        def rec(nums, amount, count):
            if nums == []:
                amount.append(sum(count))
            for i in range(min(2, len(nums))):
                count.append(nums[i])
                rec(nums[i + 2:], amount, count)
                count.pop()
            return amount
        return max(rec(nums, amount, count))