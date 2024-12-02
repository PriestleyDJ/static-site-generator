import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a text node")

    def test_enum_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertEqual(node.url, "www.test.com")
    
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.test.com")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.test.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, text, www.test.com)")


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This will be a html node", TextType.TEXT, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This will be a html node")

    def test_bold(self):
        node = TextNode("This will be a html node", TextType.BOLD, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This will be a html node")

    def test_italic(self):
        node = TextNode("This will be a html node", TextType.ITALIC, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This will be a html node")

    def test_code(self):
        node = TextNode("This will be a html node", TextType.CODE, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This will be a html node")

    def test_link(self):
        node = TextNode("This will be a html node", TextType.LINK, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This will be a html node")
        self.assertEqual(html_node.props, {"href": "www.test.com"})

    def test_image(self):
        node = TextNode("This will be a html node", TextType.IMAGE, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "www.test.com", "alt": "This will be a html node"})

    def test_wrong_text_type(self):
        node = TextNode("This will be a html node", None, "www.test.com")
        self.assertRaises(Exception, text_node_to_html_node, node)


if __name__ == "__main__":
        unittest.main()
