
import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def display(self):
        G = nx.DiGraph()
        labels = {}
        self._plot_tree(self.root, G, labels)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, font_size=10, font_color='black', node_color='lightblue', edge_color='black')
        plt.title("Binary Tree Visualization")
        plt.axis('off')
        plt.show()

    def _plot_tree(self, node, G, labels):
        if node:
            G.add_node(node.key)
            labels[node.key] = str(node.key)
            if node.left:
                G.add_edge(node.key, node.left.key)
                self._plot_tree(node.left, G, labels)
            if node.right:
                G.add_edge(node.key, node.right.key)
                self._plot_tree(node.right, G, labels)

# Interactive usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()

    root = int(input("Enter the root value: "))
    binary_tree.insert(root)

    while True:
        key_input = input("Enter a child value (or type 'finished' to end): ")
        if key_input.lower() == 'finished':
            break

        try:
            key = int(key_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        binary_tree.insert(key)

    binary_tree.display()
