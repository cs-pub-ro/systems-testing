from node import Node
import unittest

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        """Recursive helper method to find data in the tree.

        Args:
            data (int): Data to find.
            node (Node): Current node in the search.

        Returns:
            Node: The node containing the data, or None if the data is not found
                  starting from this node.
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """Deletes all nodes in the tree, resetting the root to None."""
        self.root = None

    def printTree(self):
        """Prints the tree data using inorder traversal."""
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Recursive helper method to print tree data using inorder traversal (Left, Root, Right).

        Args:
            node (Node): Current node in the traversal.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Recursive helper method to print tree data using preorder traversal (Root, Left, Right).

        Args:
            node (Node): Current node in the traversal.
        """
        
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Recursive helper method to print tree data using postorder traversal (Left, Right, Root).

        Args:
            node (Node): Current node in the traversal.
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')

class TestTreePrivateFind(unittest.TestCase):

    def setUp(self):
        """Set up a tree for testing."""
        self.tree = Tree()
        #      10
        #     /  \
        #    5    15
        #        /  \
        #       12  20
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)
        self.tree.add(12)
        self.tree.add(20)
        self.root_node = self.tree.getRoot()

    def test_find_existing_item(self):
        """Test _find for items that exist in the tree, starting from the root."""
        self.assertIsNotNone(self.root_node, "Tree root should exist for this test.")

        # Test finding the root item
        found_node = self.tree._find(10, self.root_node)
        self.assertIsNotNone(found_node, "Should find node with data 10.")
        self.assertEqual(found_node.data, 10, "Found node should have data 10.")

        # Test finding a left child item
        found_node = self.tree._find(5, self.root_node)
        self.assertIsNotNone(found_node, "Should find node with data 5.")
        self.assertEqual(found_node.data, 5, "Found node should have data 5.")

        # Test finding a right child item that itself has children
        found_node = self.tree._find(15, self.root_node)
        self.assertIsNotNone(found_node, "Should find node with data 15.")
        self.assertEqual(found_node.data, 15, "Found node should have data 15.")

        # Test finding a nested item (left child of 15)
        found_node = self.tree._find(12, self.root_node)
        self.assertIsNotNone(found_node, "Should find node with data 12.")
        self.assertEqual(found_node.data, 12, "Found node should have data 12.")

        # Test finding another nested item (right child of 15)
        found_node = self.tree._find(20, self.root_node)
        self.assertIsNotNone(found_node, "Should find node with data 20.")
        self.assertEqual(found_node.data, 20, "Found node should have data 20.")

    def test_find_non_existing_item(self):
        """Test _find for items that do not exist in the tree, starting from the root."""
        self.assertIsNotNone(self.root_node, "Tree root should exist for this test.")

        # Item smaller than any in the tree
        not_found_node = self.tree._find(1, self.root_node)
        self.assertIsNone(not_found_node, "Should not find node with data 1.")

        # Item larger than any in the tree
        not_found_node = self.tree._find(100, self.root_node)
        self.assertIsNone(not_found_node, "Should not find node with data 100.")

        # Item that would be a child of a leaf node (e.g., left of 5)
        not_found_node = self.tree._find(3, self.root_node)
        self.assertIsNone(not_found_node, "Should not find node with data 3.")

        # Item that would be in a gap (e.g., between 12 and 15)
        not_found_node = self.tree._find(13, self.root_node)
        self.assertIsNone(not_found_node, "Should not find node with data 13.")

        # Item that would be in another gap (e.g., between 5 and 10, but on the wrong side of 5)
        not_found_node = self.tree._find(7, self.root_node)
        self.assertIsNone(not_found_node, "Should not find node with data 7.")

if __name__ == '__main__':
    unittest.main()
