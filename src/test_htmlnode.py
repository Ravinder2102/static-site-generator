import unittest

from htmlnode import HTMLNode

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