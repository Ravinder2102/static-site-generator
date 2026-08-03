from copy_static import copy_static, delete_destination
from generate_pages import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
content_path = "./content/index.md"
template_path = "./template.html"
index_path = "./public/index.html"

def main():
    delete_destination(dir_path_public)
    copy_static(dir_path_static, dir_path_public)
    generate_page(content_path, template_path, index_path)
main()