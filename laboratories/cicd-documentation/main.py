from tree import Tree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()

def test_find_existing_node():
    tree = Tree()
    for val in [5, 3, 8, 1, 4]:
        tree.add(val)
    result = tree._find(3, tree.getRoot())
    assert result is not None and result.data == 3
    print("Test 1 passed")

def test_find_nonexistent_node():
    tree = Tree()
    for val in [5, 3, 8, 1, 4]:
        tree.add(val)
    result = tree._find(10, tree.getRoot())
    assert result is None
    print("Test 2 passed")

if __name__ == "__main__":
    test_find_existing_node()
    test_find_nonexistent_node()
