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

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images_found = extract_markdown_images(old_node.text)
        if not images_found:
            new_nodes.append(old_node)
            continue
        else:
            remaining_text = old_node.text
            for image in images_found:
                alt = image[0]
                url = image[1]
                sections = remaining_text.split(f"![{alt}]({url})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                remaining_text = sections[1]

            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
                  


def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links_found = extract_markdown_links(old_node.text)
        if not links_found:
            new_nodes.append(old_node)
            continue
        else:
            remaining_text = old_node.text
            for link in links_found:
                link_text = link[0]
                url = link[1]
                sections = remaining_text.split(f"[{link_text}]({url})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                remaining_text = sections[1]

            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes