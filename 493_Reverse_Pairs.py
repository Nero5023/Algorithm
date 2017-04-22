class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = self.mergeSort(nums, 0, len(nums)-1)
        return res

    def mergeSort(self, nums, start, end):
        if start >= end:
            return 0
        mid = start + (end-start)/2
        count = self.mergeSort(nums, start, mid) + self.mergeSort(nums, mid+1, end)
        j = mid+1
        for i in range(start, mid+1):
            c = 0
            while j <= end and nums[i] > 2*nums[j]:
                j+=1
                c+=1
                # print c
                # print c == (j-(mid+1))
            count += (j-(mid+1))
        MERGE(nums, start, mid, end)
        return count

def MERGE(A,start,mid,end):
    L = A[start:mid+1]
    R = A[mid+1:end+1]
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  


# class Solution(object):
#     def __init__(self):
#         self.tree = None

#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#         # for i in range(0, len(nums)-1):
#         #     for j in range(i+1, len(nums)):
#         #         if nums[i] > 2*nums[j]:
#         #             res+=1
#         for val in nums:
#             count = sizeOfNodeLarger(self.tree, 2*val)
#             res += count
#             self.tree = insert(self.tree, val)
#         return res



# def sizeOfNode(root):
#     if root is None:
#         return 0
#     return root.size

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.size = 1

# def insert(root, x):
#     if root is None:
#         return TreeNode(x)
#     if x <= root.val:
#         root.left = insert(root.left, x)
#     else:
#         root.right = insert(root.right, x)
#     root.size = 1 + sizeOfNode(root.left) + sizeOfNode(root.right)
#     return root

# # > x
# def sizeOfNodeLarger(root, x):
#     if root is None:
#         return 0
#     if root.val == x:
#         return sizeOfNode(root.right)
#     if x > root.val:
#         return sizeOfNodeLarger(root.right, x)
#     else: # x < root.val
#         leftRes = sizeOfNodeLarger(root.left, x)
#         rightRes = sizeOfNode(root.right)
#         return 1 + leftRes + rightRes



if __name__ == '__main__':
    s = Solution()
    print s.reversePairs([2,4,3,5,1])