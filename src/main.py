from sys import argv

from copy_static import copy_static, delete_destination
from generate_pages import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
content_path = "./content"
template_path = "./template.html"

def main():
    base_path = argv[1] if len(argv) > 1 else "/"
    delete_destination(dir_path_public)
    copy_static(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(content_path, template_path, dir_path_public, base_path)
main()