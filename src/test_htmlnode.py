import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "some text", None,{"fontsize": "12", "color": "Red"})
        node2 = HTMLNode("p", "some text", children=None, props={"fontsize": "12", "color": "Red"})
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "some text", None, {"fontsize": "12", "color": "Red"})
        self.assertEqual("HTMLNode(p, some text, children: None, {'fontsize': '12', 'color': 'Red'})", repr(node))

    def test_children(self):
        child1 = HTMLNode("p", "some text", None, {"fontsize": "12", "color": "Red"})
        child2 = HTMLNode("p", "some text", None, {"fontsize": "14", "color": "Blue"})

        node = HTMLNode("div", None, [child1, child2], {"BackgroundColor": "Yellow", "width": "100px"})
        node2 = HTMLNode("div", value=None, children= [child1, child2], props={"BackgroundColor": "Yellow", "width": "100px"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("div", "lorem ipsum", None, {"class": "lorem ipsum", "fontsize": "12"})
        self.assertEqual(node.props_to_html(),
                         ' class="lorem ipsum" fontsize="12"')

    #leaf node tests   
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "this is a link", {"href": "example.com"})
        self.assertEqual(node.to_html(), '<a href="example.com">this is a link</a>')

    def test_leaf_to_html_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None,"this is raw text")
        self.assertEqual(node.to_html(), "this is raw text")