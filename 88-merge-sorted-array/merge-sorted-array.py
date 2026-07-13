class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i, j = 0, 0
        
        # Everything below is now properly indented inside the function
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
                
        if i < m:
            while i < m:
                result.append(nums1[i])
                i += 1
                
        if j < n:
            while j < n:
                result.append(nums2[j])
                j += 1
                
        for k in range(m + n):
            nums1[k] = result[k]