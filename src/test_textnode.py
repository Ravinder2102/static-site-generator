import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a link", TextType.LINK, url="example.com")
        node2 = TextNode("This is a link",TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
         node = TextNode("This is some text", TextType.ITALIC)
         node2 = TextNode("This is some text",TextType.BOLD)
         self.assertNotEqual(node, node2)
    
    def test_different_text(self):
        node = TextNode("THIS IS UPPERCASE", TextType.TEXT)
        node2 = TextNode("this is lowercase", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a link", TextType.LINK, url="example.com")
        self.assertEqual("TextNode(This is a link, link, example.com)", repr(node))
if __name__ == "__main__":
    unittest.main()