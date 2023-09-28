
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt5.QtCore import Qt

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

class BinaryTreeWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Binary Tree Visualization')

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.tree = BinaryTree()
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(1)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(9)

        self.draw_tree(self.tree.root, 400, 50, 400)

    def draw_tree(self, node, x, y, spacing):
        if node:
            item = QGraphicsEllipseItem(x - 20, y - 20, 40, 40)
            item.setFlag(QGraphicsEllipseItem.ItemIsMovable)
            text_item = QGraphicsTextItem(str(node.key))
            text_item.setPos(x - 10, y - 10)
            self.scene.addItem(item)
            self.scene.addItem(text_item)

            if node.left:
                left_x = x - spacing
                left_y = y + 100
                self.scene.addLine(x, y, left_x, left_y)
                self.draw_tree(node.left, left_x, left_y, spacing / 2)

            if node.right:
                right_x = x + spacing
                right_y = y + 100
                self.scene.addLine(x, y, right_x, right_y)
                self.draw_tree(node.right, right_x, right_y, spacing / 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BinaryTreeWidget()
    ex.show()
    sys.exit(app.exec_())