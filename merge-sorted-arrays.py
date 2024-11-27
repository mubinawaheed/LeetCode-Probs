class Solution(object):
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    def merge(self, nums1, m, nums2, n):
        if n == 0 and m > 0 and nums1[-1] != 0:
            return
        if m == 0:
            nums1[:n] = nums2  # Copy nums2 into nums1
        else:
            while True:
                if nums1[-1] == 0:
                    del nums1[-1]
                else:
                    break
            i = 0
            j = 0
            if m > 0 and n > 0:
                while True:

                    while i < len(nums1) and nums1[i] < nums2[j]:
                        i += 1
                    nums1.insert(i, nums2[j])
                    j += 1

                    if j >= len(nums2):
                        break
                if len(nums1) < m + n:
                    for i in range((m + n) - len(nums1)):
                        nums1.append(0)
