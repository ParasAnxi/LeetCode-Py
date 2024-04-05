class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        v = [0] * (m + n)
        k = 0

        while i < m and j < n:
          if nums1[i] < nums2[j]:
            v[k] = nums1[i]
            i += 1
          else:
            v[k] = nums2[j]
            j += 1
          k += 1

        while i < m:
          v[k] = nums1[i]
          i += 1
          k += 1

        while j < n:
          v[k] = nums2[j]
          j += 1
          k += 1

        for i in range(m + n):
          nums1[i] = v[i]
