# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = listToArr(head)
        return constructBST(arr, 0, len(arr)-1)
        

def listToArr(head):
    res = []
    node = head
    while node is not None:
        res.append(node.val)
        node = node.next
    return res

def constructBST(arr, start, end):
    if start > end:
        return None
    mid = start + (end - start)//2
    node = TreeNode(arr[mid])
    node.left  = constructBST(arr, start, mid-1)
    node.right = constructBST(arr, mid+1, end)
    return node
