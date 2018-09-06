class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        count = []
        j = 0
        k = 0
        if (m+n)%2 == 0:
            index = (m+n)/2
            if m == 0:
                return (nums2[n/2] + nums2[n/2 - 1])/2.0
            if n == 0:
                return (nums1[m/2] + nums1[m/2 - 1])/2.0
            for i in range((m+n)):
                if j >= m and k < n:
                    count.insert(i,nums2[k])
                    k += 1
                if j < m and k >= n:
                    count.insert(i,nums1[j])
                    j += 1
                if j < m and k < n:
                    if nums1[j] <= nums2[k]:
                        count.insert(i,nums1[j])
                        j += 1
                    else:
                        count.insert(i,nums2[k])
                        k += 1
                if i == index:
                    return (count[index] + count[index -1])/2.0
        else:
            index = (m+n)/2
            if m == 0:
                return (nums2[n/2])
            if n == 0:
                return (nums1[m/2])
            for i in range((m+n)):
                if j >= m and k < n:
                    count.insert(i,nums2[k])
                    k += 1
                if j < m and k >= n:
                    count.insert(i,nums1[j])
                    j += 1
                if j < m and k < n:
                    if nums1[j] <= nums2[k]:
                        count.insert(i,nums1[j])
                        j += 1
                    else:
                        count.insert(i,nums2[k])
                        k += 1
                if i == index:
                    return (count[index])