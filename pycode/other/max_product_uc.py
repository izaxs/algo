#!/bin/python3
# Two Sigma
# Question Description

# There are N friends, numbered from 1 to N, who buy wholesale products from different companies. There are K pairs of friends (from, to) where each pair of friends is connected by the common company they buy products from. Companies are numbered from 1 to 100. If friends X and Y are connected by company i, while friends Y and Z are also connected by company i, then X, Y and Z are all connected by company i. Find the maximal product of two friends that share the largest group of friends which is connected by a common company. If there are multiple groups tied for the largest group, then find the maximum of group maximal products.
# Example

# From    To    Company
# 1       2     51
# 7       3     51
# 5       6     51
# 10      8     51
# 6       9     51
# 2       3     51

# Everyone uses the same company, but not everyone is connected. A graphical representation is:
# The largest group is [1, 2, 3, 7] and its largest elements are 3 and 7. Their product is 21.
# Function Description
# Complete the function countCompanies in the editor below.
# countCompanies has the following parameter(s):
#     num_friends: an integer, the number of friends
#     friends_from[k]: an integer array where each element denotes the first friend in the pair
#     friends_to[k]: an integer array where each element denotes the second friend in the pair
#     friends_company[k]: an integer array where each element denotes a company used by both friends
# Returns:

#     int: an integer that represents the product of the maximum two friend numbers in the largest group
# Constraints

#     len(friends_to) == len(friends_from) == len(friends_company)
#     2 ≤ num_friends ≤ 100
#     1 ≤ len(friends_to) ≤ min(200, (num_friends × (num_friends - 1)) / 2)
#     1 ≤ friends_company[i] ≤ 100
#     1 ≤ friends_from[i], friends_to[i] ≤ num_friends
#     friends_from[i] ≠ friends_to[i]
#     Each pair of friends can be connected by more than one company.

# Input Format For Custom Testing
# Sample Case 0

# Sample Input

# STDIN     Function
# -----     -----
# 4      →  num_friends = 4
# 5      →  friends_from[] size n = 5
# 1      →  friends_from = [1, 1, 2, 2, 2]
# 1
# 2
# 2
# 2
# 5      →  friends_to[] size n = 5
# 2      →  friends_to = [2, 2, 3, 3, 4]
# 2
# 3
# 3
# 4
# 5      →  friends_company[] size n = 5
# 1      →  friends_company = [1, 2, 1, 3, 3]
# 2
# 1
# 3
# 3
# Sample Output
# 12
# Explanation
# In this case, friends are numbered as 1, 2, 3, and 4 and companies are numbered as 1, 2, and 3.
#     Pair 1 and 2 are a part of the group [1, 2, 3], connected by company 1. Total friends in this group = 3 and pair product = 1 × 2 = 2.
#     Pair 1 and 2 are also a part of the group [1, 2], connected by company 2. Total friends in this group = 2 and pair product = 1 × 2 = 2.
#     Pair 1 and 3 are part of the group [1, 2, 3], connected by company 1. Total friends in this group = 3 and pair product = 1 × 3 = 3.
#     Pair 1 and 4 are not a part of any group.
#     Pair 2 and 3 are a part of the group [2, 3, 4], connected by company 3. Total friends in this group = 3 and pair product = 2 × 3 = 6.
#     Pair 2 and 4 are a part of the group [2, 3, 4], connected by company 3. Total friends in this group = 3 and pair product = 2 × 4 = 8.
#     Pair 3 and 4 are a part of the group [2, 3, 4], connected by company 3. Total friends in this group = 3 and pair product = 3 × 4 = 12.
# The pair which is part of the largest group of friends and with the maximum product of their friend numbers is 3 and 4 with 3 as group size and 12 as their product.
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'countCompanies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num_friends
#  2. INTEGER_ARRAY friends_from
#  3. INTEGER_ARRAY friends_to
#  4. INTEGER_ARRAY friends_company
# find two persons with top 2 max ids that are friends (direct or indirect) and use the same company
#  # rootMap: child->parent: dict[(product_id, person_id)] = product_id,person_id
#  # groupCounter: (product_id, root)-> counter: dict[(product_id, person)] - int
#  root: product_id, person_id
#  N: person  M:pairs K:M M*M
from heapq import nlargest
Node = tuple[int, int]

def getRoot(rootMap: dict[Node, Node], node: Node) -> Node:
    while node in rootMap and rootMap[node] != node:
        node = rootMap[node]
    return node

def buildRootMap(friends_from: list[int], friends_to: list[int], friends_company: list[int]) -> dict[Node, Node]:
    rootMap: dict[Node, Node] = {}
    n = len(friends_from)
    for i in range(n):
        p1 = (friends_company[i], friends_from[i])
        p2 = (friends_company[i], friends_to[i])
        root1, root2 = getRoot(rootMap, p1), getRoot(rootMap, p2)
        rootMap[root1] = root2
    return rootMap

def getMaxGroups(rootMap: dict[Node, Node]) -> list[list[int]]:
    # groupMap: root -> list(person_id)
    groupMap: dict[Node, set[int]] = {}
    for c, p in rootMap.items():
        root = getRoot(rootMap, p)
        group = groupMap.setdefault(root, set())
        group.add(c[1])
        group.add(root[1])
    groups: list[list[int]] = []
    lenMax = 0
    for _, v in groupMap.items():
        if len(v) > lenMax:
            groups.clear()
            groups.append(list(v))
            lenMax = len(v)
        elif len(v) == lenMax:
            groups.append(list(v))
    return groups


def countCompanies(num_friends: int, friends_from: list[int], friends_to: list[int], friends_company: list[int]):
    rootMap = buildRootMap(friends_from, friends_to, friends_company)
    groups = getMaxGroups(rootMap)
    maxProduct = 0
    for g in groups:
        n1, n2 = nlargest(2, g)
        maxProduct = max(maxProduct, n1*n2)
    return maxProduct

if __name__ == '__main__':
    N = 4
    friends_from = [1, 1, 2, 2, 2]
    friends_to = [2, 2, 3, 3, 4]
    friends_company = [1, 2, 1, 3, 3]
    p = countCompanies(N, friends_from, friends_to, friends_company)
    print(p)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     friends_nodes = int(input().strip())

#     friends_from_count = int(input().strip())

#     friends_from = []

#     for _ in range(friends_from_count):
#         friends_from_item = int(input().strip())
#         friends_from.append(friends_from_item)

#     friends_to_count = int(input().strip())

#     friends_to = []

#     for _ in range(friends_to_count):
#         friends_to_item = int(input().strip())
#         friends_to.append(friends_to_item)

#     friends_weight_count = int(input().strip())

#     friends_weight = []

#     for _ in range(friends_weight_count):
#         friends_weight_item = int(input().strip())
#         friends_weight.append(friends_weight_item)

#     result = countCompanies(friends_nodes, friends_from, friends_to, friends_weight)

#     fptr.write(str(result) + '\n')

#     fptr.close()
