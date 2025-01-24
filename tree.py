"""
This module provides a simple implementation of a binary search tree(BST) with
basic operations such as insertion and traversal, as well as a function to check
if a given binary tree is a BST.

Classes:
    Node: A class to represent a node in a binary search tree.

Functions:
    check_bst(r): Checks if a binary tree is a binary search tree(BST).
"""


class Node:
    """
    A class to represent a node in a binary search tree.

    Attributes
    ----------
    data : any
        The data stored in the node.
    left : Node
        The left child node.
    right : Node
        The right child node.

    Methods
    -------
    __init__(data):
        Initializes the node with data and sets left and right children to None.
    insert(data):
        Inserts a new node with the specified data into the tree.
    pre_order_traversal(visit):
        Traverses the tree in pre-order and applies the visit function to each node.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Inserts a new node with the specified data into the tree.

        Args:
            data (any): The data to insert into the tree.
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def pre_order_traversal(self, visit):
        """
        Traverses the tree in pre-order and applies the visit function to each node.

        Args:
            visit (function): A function to apply to each node during traversal.
        """
        visit(self)
        if self.left:
            self.left.pre_order_traversal(visit)
        if self.right:
            self.right.pre_order_traversal(visit)


def check_bst(r):
    """
    Checks if a binary tree is a binary search tree (BST).

    Args:
        root (Node): The root node of the tree.

    Returns:
        bool: True if the tree is a BST, False otherwise.
    """
    def in_order_traversal(node, last_node_val):
        # Base case: if the node is None, return True
        if not node:
            return True

        # Check the left subtree
        if not in_order_traversal(node.left, last_node_val):
            return False

        # Check current node's value with the last node's value
        if last_node_val[0] is not None and node.data <= last_node_val[0]:
            return False

        # Update the last node's value to the current node's value
        last_node_val[0] = node.data

        # Check the right subtree
        return in_order_traversal(node.right, last_node_val)

    # Start the traversal with the initial last node value as None
    return in_order_traversal(r, [None])

# Example usage:
# Constructing the tree:
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5    7


root = Node(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)

# Check if the tree is a BST
print(check_bst(root))  # Output: True

# Traverse the tree in pre-order
root.pre_order_traversal(lambda node: print(node.data))
