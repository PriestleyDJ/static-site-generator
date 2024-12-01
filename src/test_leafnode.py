import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a leaf node")
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")

    def test_to_html2(self):
        props = {"href": "www.test.com"}
        node = LeafNode("a", "This is a leaf node", props)
        self.assertEqual(node.to_html(), "<a href=www.test.com>This is a leaf node</a>")

    def test_to_html3(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html4(self):
        node = LeafNode(None, "This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")
