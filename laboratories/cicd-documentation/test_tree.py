import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for value in [10, 5, 15, 3, 7, 12, 18]:
            self.tree.add(value)

    def test_find_existing_node(self):
        node = self.tree._find(3, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)

    def test_find_nonexistent_node(self):
        node = self.tree._find(71, self.tree.root)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
