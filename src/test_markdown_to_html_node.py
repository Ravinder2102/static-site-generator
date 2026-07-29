import unittest
from markdown_to_html_node import markdown_to_html_node, extract_title
class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = """
- Apple
- _Banana_
- Pear

1. Bear
2. Dog
3. Cat

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Apple</li><li><i>Banana</i></li><li>Pear</li></ul><ol><li>Bear</li><li>Dog</li><li>Cat</li></ol></div>"
        )

    def test_headings(self):
        md = """
# Heading 1

some text

### Heading 3

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p>some text</p><h3>Heading 3</h3></div>"
        )

    def test_blockquote(self):
        md = """
> This is some quote and
> this is the next part of that quote

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is some quote and this is the next part of that quote</blockquote></div>"
        )
# Title extraction tests
    def test_extract_title(self):
        md = """
# Title

"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Title"
        )

    def test_no_title(self):
        md = """
## Hello

"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()