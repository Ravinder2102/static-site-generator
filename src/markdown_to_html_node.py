from inline_markdown import markdown_to_blocks, text_to_textnodes
from blocktype import block_to_block_type, BlockType
from htmlnode import ParentNode, HTMLNode
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextType, TextNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_block = None
        if block_type == BlockType.PARAGRAPH:
            html_block = paragraph_to_html_node(block)
        elif block_type == BlockType.HEADING:
            html_block = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            html_block = code_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            html_block = quote_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            html_block = ul_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            html_block = ol_to_html_node(block)
        html_nodes.append(html_block)
    root_node = ParentNode("div", html_nodes)
    return root_node

# Extract title from md
def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 Header found") 

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def paragraph_to_html_node(para: str) -> ParentNode:
    text = para.replace("\n", " ")
    children = text_to_children(text)
    html_block = ParentNode("p", children)
    return html_block

def heading_to_html_node(heading: str) -> ParentNode:
    heading_size = 0
    for char in heading:
        if char == "#":
            heading_size += 1
        elif char == " ":
            break
    clean_heading =heading[heading_size + 1:]
    children = text_to_children(clean_heading)
    html_block = ParentNode(f"h{heading_size}",children)
    return html_block

def code_to_html_node(code: str) -> ParentNode:
    clean_code = code[4:len(code) - 3]
    code_text_node = TextNode(clean_code, TextType.CODE)
    code_html_block = text_node_to_html_node(code_text_node)
    code_pre_block = ParentNode("pre", [code_html_block])
    return code_pre_block

def quote_to_html_node(quote: str) -> ParentNode:
    quote_lines = quote.splitlines()
    clean_lines = []
    for line in quote_lines:
        clean_lines.append(line.lstrip(">").strip())
    clean_quote = " ".join(clean_lines)
    children = text_to_children(clean_quote)
    html_block = ParentNode("blockquote", children)
    return html_block

def ul_to_html_node(ul: str) -> ParentNode:
    ul_lines = ul.splitlines()
    line_html_nodes = []
    for line in ul_lines:
        clean_line = line.lstrip("-").strip()
        line_children = text_to_children(clean_line)
        parent_line = ParentNode("li", line_children)
        line_html_nodes.append(parent_line)
    html_block = ParentNode("ul", line_html_nodes)
    return html_block

def ol_to_html_node(ol: str) -> ParentNode:
    ol_lines = ol.splitlines()
    line_html_nodes = []
    for line in ol_lines:
        clean_line = line.split(". ", 1)[1]
        line_children = text_to_children(clean_line)
        parent_line = ParentNode("li", line_children)
        line_html_nodes.append(parent_line)
    html_block = ParentNode("ol", line_html_nodes)
    return html_block
