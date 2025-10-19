from Tree import Tree


class BST(Tree):
    def __init__(self, val, parent=None):
        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BST(val, parent=self)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val, parent=self)
            else:
                self.right.insert(val)

    def delete(self, val):
        # Case 1: single node tree
        if (
            self.parent is None
            and self.left is None
            and self.right is None
            and self.val == val
        ):
            return None

        if self.val == val:
            # Case 2: leaf node
            if self.left is None and self.right is None:
                self.set_for_parent(None)
                return self.find_root()

            # Case 3: only left child
            if self.right is None:
                return self.replace_with_node(self.left)

            # Case 4: only right child
            if self.left is None:
                return self.replace_with_node(self.right)

            # Case 5: two children → use successor
            successor = self.right.find_min()
            self.val = successor.val
            return self.right.delete(successor.val)

        elif val < self.val and self.left:
            return self.left.delete(val)
        elif val > self.val and self.right:
            return self.right.delete(val)

        return self.find_root()  # if the val not found

    def set_for_parent(self, node):
        if self.parent is None:
            return
        if self.parent.left == self:
            self.parent.left = node
        elif self.parent.right == self:
            self.parent.right = node

    def replace_with_node(self, node):
        if self.parent:
            self.set_for_parent(node)
            node.parent = self.parent
            return node.find_root()
        else:
            node.parent = None
            return node

    def find_root(self):
        current = self
        while current.parent is not None:
            current = current.parent
        return current

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
