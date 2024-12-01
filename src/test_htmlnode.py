import unittest
from htmlnode import HtmlNode

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


if __name__ == "__main__":
    unittest.main()

