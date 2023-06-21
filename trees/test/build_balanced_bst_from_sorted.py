"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


def build_balanced_bst(a):
    return helper(a, 0, len(a) - 1)


def helper(arr, lo, hi):
    if lo > hi:
        return

    mid = (hi - lo) // 2 + lo
    node = BinaryTreeNode(arr[mid])

    node.left = helper(arr, lo, mid - 1)
    node.right = helper(arr, mid + 1, hi)

    return node


arr = []

root = build_balanced_bst(arr)
