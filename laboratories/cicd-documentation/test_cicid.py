import pytest
from tree import Tree

# def test_preorder():
#     tree = Tree()
#     for i in [2, 3, 4, 10, 12]:
#         tree.add(i)
#     assert tree._getPreorderTree(tree.root) == [2, 3, 10, 4, 12]

# def test_postorder():
#     tree = Tree()
#     for i in [10, 5, 15, 3, 7]:
#         tree.add(i)
#     assert tree._getPostorderTree(tree.root) == [3, 7, 5, 15, 10]

def test_find():
    tree = Tree()
    for i in [10, 5, 15, 3, 7]:
        tree.add(i)
    node = tree._find(5, tree.root)
    assert node is not None
    assert node.data == 5

def test_not_find():
    tree = Tree()
    for i in [2,3,4,10,12]:
        tree.add(i)
    node = tree._find(3,tree.root)
    assert node is not None