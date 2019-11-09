class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.recursiveTree(pRoot.left, pRoot.right)

    def recursiveTree(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.recursiveTree(left.left, right.right) and self.recursiveTree(left.right, right.left)
        return False
