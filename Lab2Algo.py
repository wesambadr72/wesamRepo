class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, key):
        if self.root == None:
            self.root = TreeNode(key)
        else:
            self.insertRecursive(self.root, key)

    def insertRecursive(self, root, key):
        if key < root.val:
            if root.left == None:
                root.left = TreeNode(key)
            else:
                self.insertRecursive(root.left, key)
        else:
            if root.right == None:
                root.right = TreeNode(key)
            else:
                self.insertRecursive(root.right, key)

    def search(self, key):
      return self.searchRecursive(self.root, key)

    def searchRecursive(self, node, key):
        if node == None:
            return False
        if node.val == key:
            return True

        if key < node.val:
            return self.searchRecursive(node.left, key)
        else:
            return self.searchRecursive(node.right, key)
        
    def delete(self, key):
        self.root = self.deleteRecursive(self.root, key)

    def deleteRecursive(self, node, key):
        if node == None:
            return node

        if key < node.val:
            node.left = self.deleteRecursive(node.left, key)
        elif key > node.val:
            node.right = self.deleteRecursive(node.right, key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left

            temp = self._minValueNode(node.right)
            node.val = temp.val
            node.right = self.deleteRecursive(node.right, temp.val)

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node is not None:
            self._inOrder(node.left)
            print(node.val, end=' ')
            self._inOrder(node.right)

    def preOrder(self):
        self.preOrderRecursive(self.root)
    def preOrderRecursive(self,node):
        if node is not None:
            print(node.val,end=" ")
            self.preOrderRecursive(node.left)
            self.preOrderRecursive(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(80)
    bst.insert(100)
    
    
    
    #numF= 100 
    #print(f"{numF} is 'TRUE' found" if bst.search(numF) else f"{numF} is 'FALSE' not found")
