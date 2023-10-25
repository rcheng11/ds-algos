# binary tree search:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val: int):
        '''Creates a binary search tree given a value as the root.'''
        self.root = TreeNode(val)

    def search(self, root, val: int):
        '''Return True if val exists in the BST, False otherwise.'''
        pass

    def insert(self, val: int):
        '''Insert the val as a TreeNode into the BST.'''
        pass

    def remove(self, val: int):
        '''Remove the val as a TreeNode into the BST.'''
        pass

    def run_dfs(self, type: str) -> list[int]:
        '''Runs a depth first search based on the type specified.
        Type can be: inorder, preorder, postorder
        Returns a list of the order in which the nodes were visited.
        '''
        pass

    def run_bfs(self):
        pass