class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        

def construct(preorder, inorder):
    if len(preorder) != len(inorder):
        raise RuntimeError("preorder and inorder is not the same length")
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return Node(preorder[0], None, None)
    rootValue = preorder[0]
    rootIndexIn = inorder.index(rootValue)
    leftTree = construct(preorder[1:1+rootIndexIn], inorder[:rootIndexIn])
    rightTree = construct(preorder[1+rootIndexIn:], inorder[rootIndexIn+1:])
    return Node(rootValue, leftTree, rightTree)

def preorderIter(node):
    if node is None:
        return
    print(node.value)
    preorderIter(node.left)
    preorderIter(node.right)

def inorderIter(node):
    if node is None:
        return
    inorderIter(node.left)
    print(node.value)
    inorderIter(node.right)


if __name__ == '__main__':
    tree = construct([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
    preorderIter(tree)
    print("--------")
    inorderIter(tree)