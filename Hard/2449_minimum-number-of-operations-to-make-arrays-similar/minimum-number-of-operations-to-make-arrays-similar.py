class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
# Reference 1: https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/discuss/2734189/C%2B%2BPython-Sort-odds-and-evens
# Reference 2: https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/discuss/2734078/C%2B%2B-Java-Python-Sort-odd-and-even-explained
# Reference 3: https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/discuss/2734085/PythonRustC%2B%2B-simply-consider-evens-and-odds-(with-detailed-comments)
#======== <Solution 1> ========#
        # The number of odd and even numbers in both arrays is the same since the parity of a number stays the same by adding multiples of 2 to it
        # Seperate both arrays into odd and even arrays respectively, and count the number of steps separately to avoid mismatch
        # Sort the arrays to achieve the minimum steps
        nums_odd = sorted(filter(lambda x: x % 2, nums))
        nums_even = sorted(filter(lambda x: not x % 2, nums))
        target_odd = sorted(filter(lambda x: x % 2, target))
        target_even = sorted(filter(lambda x: not x % 2, target))
        # Each step increases or decreases the value by 2
        steps_odd = sum(abs(n - t) // 2 for n, t in zip(nums_odd, target_odd))
        steps_even = sum(abs(n - t) // 2 for n, t in zip(nums_even, target_even))
        # Each operation contains 2 steps
        return (steps_odd + steps_even) // 2

#======== <Solution 2> ========#
        nums.sort(key=lambda x: [x % 2, x])
        target.sort(key=lambda x: [x % 2, x])
        return sum(abs(n - t) for n, t in zip(nums, target)) // 4
