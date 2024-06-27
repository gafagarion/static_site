import os
import shutil
from pathlib import Path

def copy_files_recursive(source,destination):
    source_path = Path(source)
    destination_path = Path(destination)
    if not os.path.exists(destination_path):  
        os.mkdir(destination_path)
    
    for file_or_directory in os.listdir(source_path):
        full_source_path = os.path.join(source_path,file_or_directory)
        full_destination_path = os.path.join(destination_path,file_or_directory)
        print(f" * {full_source_path} -> {full_destination_path}")
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path,full_destination_path)
        else:
            copy_files_recursive(full_source_path,full_destination_path)