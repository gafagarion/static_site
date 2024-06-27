from textnode import TextNode
from pathlib import Path
import os
import shutil
from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    generate_pages_recursive("content","template.html","public")


main()
    
       
