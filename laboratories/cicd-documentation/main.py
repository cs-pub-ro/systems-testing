from tree import Tree
from node import Node
import pytest


tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print()
tree._printInorderTree(tree.root)
print()
tree._printPostorderTree(tree.root)
print()
tree._printPreorderTree(tree.root)

    

@pytest.fixture
def create_sample_tree():
    tree = Tree()
    for value in [10, 5, 20, 3, 7, 15, 30]:
        tree.add(value)
    return tree

def test_find_existing_node(create_sample_tree):
    tree = create_sample_tree
    
    node = tree.find(15)
    
    assert node is not None
    assert node.data == 15

def test_find_nonexistent_node(create_sample_tree):
    tree = create_sample_tree
    
    node = tree.find(100)
    
    assert node is None
