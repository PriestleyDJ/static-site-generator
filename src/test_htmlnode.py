import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        props = {"href": "www.test.com"}
        node_child = HtmlNode("<p>", "this is the child html node")
        node = HtmlNode("<h1>", "this is a html node", node_child, props)
        self.assertEqual(repr(node), "HtmlNode(tag=<h1>, value=this is a html node, children=HtmlNode(tag=<p>, value=this is the child html node, children=None, props=None), props={'href': 'www.test.com'})")

    def test_tag_eq(self):
        node = HtmlNode("<h1>")
        self.assertEqual(node.tag, "<h1>")

    def test_value_eq(self):
        node = HtmlNode("<h1>", "This is a htmlnode")
        self.assertEqual(node.value, "This is a htmlnode")

    def test_to_html(self):
        node = HtmlNode("<h1>", "This is a htmlnode")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HtmlNode("<h1>", "This is a htmlnode", props={"href": "www.test.com"})
        self.assertEqual(node.props_to_html(), " href=www.test.com") 

    def test_props_to_html2(self):
        node = HtmlNode("<h1>", "This is a htmlnode", props={"href": "www.test.com", "alt": "alt text"})
        self.assertEqual(node.props_to_html(), " href=www.test.com alt=alt text") 

    # LeafNode tests
    def test_values(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a leaf node")
        self.assertEqual(node.props, None)

    def test_to_html2(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")

    def test_to_html3(self):
        props = {"href": "www.test.com"}
        node = LeafNode("a", "This is a leaf node", props)
        self.assertEqual(node.to_html(), "<a href=www.test.com>This is a leaf node</a>")

    def test_to_html4(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html5(self):
        node = LeafNode(None, "This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")

    # ParentNode tests
    def test_values(self):
        node = ParentNode("h1", [LeafNode("b", "This is a child node"), LeafNode("b", "This is another child node")])
        children = [HtmlNode(tag="b", value="This is a child node", children=None, props=None), HtmlNode(tag="b", value="This is another child node", children=None, props=None)]
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, None)

    def test_to_html_nested_parents(self):
        node = ParentNode("h1", [ParentNode("p", [LeafNode("h3", "This is a leaf node")]), LeafNode("h2", "This is another leaf node")])
        self.assertEqual(node.to_html(), "<h1><p><h3>This is a leaf node</h3></p><h2>This is another leaf node</h2></h1>")

    def test_to_html_no_parents(self):
        node = ParentNode("h1", [LeafNode("p", "This is a leaf node")])
        self.assertEqual(node.to_html(), "<h1><p>This is a leaf node</p></h1>")

    def test_no_children(self):
        node = ParentNode("h1", [])
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = ParentNode("", [])
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()

