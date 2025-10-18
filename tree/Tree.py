class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self):
        """
        Processing is this search is printing
        or it is actually traversing all node
        """

        print(self.val)

        if self.left:
            self.left.dfs()  # yes it is a recursive algo

        if self.right:
            self.right.dfs()

    def bfs(self):
        queue = [self]

        while queue:
            to_process = queue.pop(0)  # dequeue basically

            print(to_process.val)

            if to_process.left:
                queue.append(to_process.left)  # enqueue basically

            if to_process.right:
                queue.append(to_process.right)

    def dfs_in_order(self):

        if self.left:
            self.left.dfs_in_order()  # yes it is a recursive algo

        print(self.val)

        if self.right:
            self.right.dfs_in_order()

    def dfs_apply(self, fn):
        fn(self)

        if self.left:
            self.left.dfs_apply(fn)

        if self.right:
            self.right.dfs_apply(fn)


if __name__ == "__main__":
    t1 = TreeNode(1)

    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)
    t1.right.left = TreeNode(6)
    t1.right.right = TreeNode(7)
    t1.right.right.right = TreeNode(18)

    print("Result of BFS")
    t1.bfs()

    print("Result of in_order DFS")
    t1.dfs_in_order()

    t1.dfs_apply(
        lambda tree_node: print(
            f"""
==============================
val:{tree_node.val}
left:{tree_node.left and tree_node.left.val}
right:{tree_node.right and tree_node.right.val}
==============================
            """
        )
    )
