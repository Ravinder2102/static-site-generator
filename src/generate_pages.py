import os

from markdown_to_html_node import markdown_to_html_node, extract_title

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path,"r") as file:
        md_content = file.read()
    
    with open(template_path, "r") as file:
        template = file.read()
    
    root_node = markdown_to_html_node(md_content)
    html_str = root_node.to_html()
    
    title = extract_title(md_content)
    
    template = template.replace("{{ Title }}", title, 1)
    template = template.replace("{{ Content }}", html_str, 1)

    if os.path.dirname(dest_path):
        os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)

    