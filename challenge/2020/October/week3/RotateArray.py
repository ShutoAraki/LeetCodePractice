"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:
    def gcd(self, a: int, b: int) -> int:
        '''@ShutoAraki
        Greatest Common Divisor using
        Euclidean division
        '''
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''@ShutoAraki
        === Overall approach ===
        Array index is a collection of cyclic groups under mod operation.
        So define a mapping between old and new indices
        and then swap old and new values.
        Keep repeating this process for each subgroup.
        There are gcd(n, k) subgroups in one array.
        '''
        n = len(nums)
        if n <= 1:
            return
        k = k % n
        for i in range(self.gcd(n, k)):
            old_val = nums[i]
            j = i
            while True:
                new_idx = (n - k + j) % n
                if new_idx == i:
                    break
                nums[j] = nums[new_idx]
                j = new_idx
            nums[j] = old_val # Complete the cycle

        # Time: O(N)
        # Space: O(1)
