import unittest
from node import Node
from tree import Tree


class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.root = Node(10)
        self.tree.root.left = Node(5)
        self.tree.root.right = Node(15)

    def test_find_existing_node(self):
        found_node = self.tree._find(5, self.tree.root)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 5)

    def test_find_non_existing_node(self):
        result = self.tree._find(100, self.tree.root)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
