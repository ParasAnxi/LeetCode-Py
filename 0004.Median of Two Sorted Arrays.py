class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2,nums1)
        left , right = 0, n
        while left <= right:
            part1 = (left + right) // 2
            part2 = (m + n + 1) // 2 - part1
            l1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            r1 = float('inf') if part1 == n else nums1[part1]
            l2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            r2 = float('inf') if part2 == m else nums2[part2]
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                else: 
                    return max(l1,l2)    
            elif l1 > r2:
                right = part1 - 1
            else:
                left = part1 + 1
        return 0.0
