import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):
    def setUp(self):
        """Set up a tree for testing"""
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_node(self):
        """Test finding an existing node in the tree"""
        result = self.tree.find(5)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 5)

    def test_find_non_existing_node(self):
        """Test finding a non-existing node in the tree"""
        result = self.tree.find(20)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()