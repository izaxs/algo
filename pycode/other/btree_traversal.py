import include
from binarytree import Optional, TreeNode

def preorder(root: TreeNode) -> list[int]:
    stack: list[TreeNode] = []
    result: list[int] = []
    cur: Optional[TreeNode] = root
    while cur or stack:
        if cur:
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return result

def preorder2(root: TreeNode) -> list[int]:
    stack: list[TreeNode] = [root]
    result: list[int] = []
    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return result

def inorder(root: TreeNode) -> list[int]:
    stack: list[TreeNode] = []
    result: list[int] = []
    cur: Optional[TreeNode] = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result

def inorder2(root: TreeNode) -> list[int]:
    stack: list[tuple[TreeNode, bool]] = [(root, False)]
    result: list[int] = []
    while stack:
        cur, visited = stack.pop()
        if not visited:
            stack.append((cur, True))
            if cur.left: stack.append((cur.left, False))
        else:
            result.append(cur.val)
            if cur.right: stack.append((cur.right, False))
    return result

# Morris Traversal
def inorder3(root: TreeNode) -> list[int]:
    result: list[int] = []
    cur: Optional[TreeNode] = root
    while cur:
        if not cur.left:
            result.append(cur.val)
            cur = cur.right
        else:
            linker: TreeNode = cur.left
            while linker.right != cur and linker.right is not None:
                linker = linker.right
            if linker.right == cur:
                result.append(cur.val)
                cur = cur.right
                linker.right = None
            else:
                linker.right = cur
                cur = cur.left
    return result

# def inorder4(root: TreeNode) -> list[int]:


def postorder(root: TreeNode) -> list[int]:
    stack: list[tuple[TreeNode, bool]] = []
    result: list[int] = []
    cur: Optional[TreeNode] = root
    while cur or stack:
        if cur:
            stack.append((cur, False))
            cur = cur.left
        else:
            cur, visited = stack.pop()
            if visited:
                result.append(cur.val)
                cur = None
            else:
                stack.append((cur, True))
                cur = cur.right
    return result

def postorder2(root: TreeNode) -> list[int]:
    stack: list[tuple[TreeNode, int]] = [(root, 0)]
    result: list[int] = []
    while stack:
        cur, state = stack.pop()
        if state == 0:
            stack.append((cur, 1))
            if cur.left: stack.append((cur.left, 0))
        if state == 1:
            stack.append((cur, 2))
            if cur.right: stack.append((cur.right, 0))
        if state == 2:
            result.append(cur.val)
    return result

def _gen_tree() -> TreeNode:
    nodes: list[TreeNode] = []
    for i in range(8):
        nodes.append(TreeNode(i))
    nodes[0].left = nodes[1]
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[3].left = nodes[4]
    nodes[0].right = nodes[5]
    nodes[5].left = nodes[6]
    nodes[5].right = nodes[7]
    return nodes[0]

if __name__ == '__main__':
    root = _gen_tree()
    print(preorder2(root))
    print(inorder3(root))
    print(postorder2(root))
