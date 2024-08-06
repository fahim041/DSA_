class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def remove(root, val):
    pass

def find_min(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True

def test_bst():
    root = None
    root = insert(root, 10)
    root = insert(root, 5)
    root = insert(root, 15)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 12)
    root = insert(root, 18)
    
    assert search(root, 10) == True
    assert search(root, 5) == True
    assert search(root, 99) == False

    assert find_min(root).val == 3

    print("All tests passed")

test_bst()