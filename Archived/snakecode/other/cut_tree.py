# Two Sigma HackerRank
class TreeNode:
    def __init__(self, id: int, val: int) -> None:
        self.id = id
        self.val = val
        self.children: list[TreeNode] = []

def min_diff(parents: list[int], volumes: list[int]) -> int:
    tree: dict[int, TreeNode] = {}
    rootId = -1
    for cur, parent in enumerate(parents):
        curNode = tree.setdefault(cur, TreeNode(cur, volumes[cur]))
        if parent >= 0:
            parentNode = tree.setdefault(parent, TreeNode(parent, volumes[parent]))
            parentNode.children.append(curNode)
        else:
            rootId = cur
    counter: dict[int, int] = {}
    sumTree(tree[rootId], counter)
    totalVolume = sum(volumes)
    closest = totalVolume
    for v in counter.values():
        diff = abs(v*2-totalVolume)
        closest = min(diff, closest)
    return closest

def sumTree(root: TreeNode, counter: dict[int, int]) -> int:
    counter[root.id] = root.val
    if root.children:
        volSum = sum([sumTree(n, counter) for n in root.children])
        counter[root.id] += volSum
    return counter[root.id]

parents = [1,5,3,1,3,-1,7,5,7]
volumes = [5,1,1,3,8,4,0,6,0]
print(min_diff(parents, volumes))
