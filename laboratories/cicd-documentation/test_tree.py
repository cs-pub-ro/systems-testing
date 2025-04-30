import pytest
from tree import Tree
from node import Node

@pytest.fixture
def example_tree():
    t = Tree()
    for value in [10, 5, 15, 3, 7]:
        t.add(value)
    return t

def test_find_existing_node(example_tree):
    node = example_tree._find(7, example_tree.getRoot())
    assert node is not None
    assert node.data == 7

def test_find_non_existing_node(example_tree):
    node = example_tree._find(42, example_tree.getRoot())
    assert node is None
