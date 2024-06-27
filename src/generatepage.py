from markdown_blocks import (markdown_to_blocks,
                             block_to_block_type,
                             markdown_to_html_node)
import os

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
    template_content.replace("{{Title}}",title)
    template_content.replace("{{Content}}",html)
    
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    
    f = open(dest_path,"x")
    f.write(template_content)
    f.close()
        
    
            
    