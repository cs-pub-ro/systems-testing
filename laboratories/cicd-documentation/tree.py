from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Get the root of the tree 
        
        Returns:
            Node: The root node of the tree
        """
        return self.root

    def add(self, data):
        """ Public method to add data to the tree 
        
        Args:
            data (int): Value to add to the tree
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """ Recursive helper method to add data to the tree 
        
        Args:
            data (int): Value to add
            node (Node): Current node in recursion
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
        """ Find a node with the specified data 
        
        Args:
            data (int): Value to search for

        Returns:
            Node: Node containing the value, or None if not found
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        """ Recursive helper method to find a node 
        
        Args:
            data (int): Value to search for
            node (Node): Current node in recursion

        Returns:
            Node: Node with the desired value, or None
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Delete the entire tree by setting root to None """
        self.root = None

    def printTree(self):
        """ Print the tree in inorder traversal """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ Recursive inorder traversal 
        
        Args:
            node (Node): Current node
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Recursive preorder traversal 
        
        Args:
            node (Node): Current node
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """ Recursive postorder traversal 
        
        Args:
            node (Node): Current node
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')
