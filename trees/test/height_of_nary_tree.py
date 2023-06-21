import sys

# adding Tree class and helpers to the system path
sys.path.insert(1, "/Users/aidangarton/Desktop/IK/trees/Tree")

from Tree import *


def find_height(root):
    if not root:
        return 0

    if not root.children:
        return 0

    m = 1 + find_height(root.children[0])

    for i in range(1, len(root.children)):
        n = find_height(root.children[i])
        if n + 1 > m:
            m = n + 1

    return m


# find tests for nary trees
