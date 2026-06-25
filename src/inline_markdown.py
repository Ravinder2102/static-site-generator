import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        split_string = old_node.text.split(delimiter)
        
        if len(split_string) % 2 == 0:
             raise Exception("Error: Invalid markdown syntax")
        
        for i in range(len(split_string)):
            if split_string[i] == "":
                    continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_string[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_string[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
     img_alt_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     return img_alt_url

def extract_markdown_links(text):
     link_anchor_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     return link_anchor_url