from tree import Tree
from node import Node
import unittest

tree = Tree()

class TestTreeFunctions(unittest.TestCase):
    
    def setUp(self):
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)

    def test_find_existing_node(self):
        node = tree._find(3, tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)

    def test_find_nonexistent_node(self):
        node = tree._find(10, tree.root)
        self.assertIsNone(node)
