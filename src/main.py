from copy_static import copy_static, delete_destination

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    delete_destination(dir_path_public)
    copy_static(dir_path_static, dir_path_public)

main()