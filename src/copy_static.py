import os
import shutil

def delete_destination(destination: str) -> None:
    print(f"Deleting {destination} directory")
    if os.path.exists(destination):
        shutil.rmtree(destination)
        
def copy_static(source: str, destination: str) -> None:
    # raise error if src doesn't exist
    if not os.path.exists(source):
        raise Exception("source is not valid path")
    # Make destination dir if it does not exist
    if not os.path.exists(destination):
        os.mkdir(destination)

    src_content = os.listdir(source)
    
    # loop over each filename
    # copy if a file
    # recurse if it is a dir
    for content in src_content:
        content_path = os.path.join(source, content)
        if os.path.isfile(content_path):
            print(f"Copying: Content path = {content_path}, Destination Path = {destination}")
            shutil.copy(content_path, destination)
        else:
            copy_static(content_path, os.path.join(destination, content))
    