from markdown_blocks import (markdown_to_blocks,
                             block_to_block_type,
                             markdown_to_html_node)
import os
from pathlib import Path

def extract_title(markdown):
    title = ""
    found = False
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if (block.startswith("# ") and not block.startswith("## ")):
            if not found:
                found = True
                title = block[2:]
            else:
                raise Exception("Markdown file should have only one h1 header")
    if not found:
        raise Exception("Markdown file should have only one h1 header")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generation page from {from_path} to {dest_path} using {template_path}")
    
    md_content = None
    template_content = None
    
    with open(from_path) as md_file:
        md_content = md_file.read()
    with open(template_path) as template_file:
        template_content = template_file.read()
       
    title = extract_title(md_content)
    html_node = markdown_to_html_node(md_content)
    html = html_node.to_html()
   
    output_content = template_content.replace("{{ Title }}",title)
    output_content = output_content.replace("{{ Content }}",html)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    f = open(dest_path,"w")
    f.write(output_content)
    f.close()
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    source_path = Path(dir_path_content)
    destination_path = Path(dest_dir_path)
    if not os.path.exists(destination_path):  
        os.mkdir(destination_path)
    for file_or_directory in os.listdir(source_path):
        full_source_path = os.path.join(source_path,file_or_directory)
        full_destination_path = os.path.join(destination_path,file_or_directory)
        if os.path.isfile(full_source_path):
            (root,ext) = os.path.splitext(full_source_path)
            if ext == ".md":
                (head,tail) =  os.path.splitext(full_destination_path)
                full_destination_path = head + ".html"
                generate_page(full_source_path, template_path, full_destination_path)
        else:
            generate_pages_recursive(full_source_path, template_path, full_destination_path)
