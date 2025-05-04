#!/usr/bin/env python3

import os
import hashlib
import json
import requests
import subprocess

# Directories

CONTENT_TYPE_TO_DIR = {
        "Learnings": "Learnings"
    }
EXPORTS_DIR = "exports"
HTML_DIR = os.path.join(EXPORTS_DIR, "html")
OUTPUT_TYPE = ["html"]
HASH_FILE = "hashes.json"
BLOGS_JSON = "blogs.json"
ALWAYS_CREATE = False #for testing

def download_file(url, filename):
    r = requests.get(url)
    r.raise_for_status()
    with open(filename, "wb") as f:
        f.write(r.content)

def compute_sha256(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

# def generate_files(input_md, output_files):
#     for output_type, output_file in output_files.items():
#         cmd = [
#                 "pandoc",
#                 input_md,
#                 "-o",
#                 output_file,
#                 "--resource-path=.:..:../static"
#             ]
        
#         if output_type == "html":
#             # output_html = output_file
#             cmd.extend([ "--embed-resources", "--standalone"])
#         subprocess.run(cmd, check=True)

import os
import subprocess

def generate_files(input_md, output_files):
    input_md = os.path.abspath(input_md)
    md_dir = os.path.dirname(input_md)
    md_file = os.path.basename(input_md)
    
    print(md_dir, md_file)

    for output_type, output_file in output_files.items():
        cmd = [
            "pandoc",
            md_file,  # just the filename
            "-o",
            output_file,
        ]

        if output_type == "html":
            cmd.extend([
                "--embed-resources",
                "--standalone",
                # "--resource-path=."
            ])

        # Run pandoc from the md file's dir so relative images work
        subprocess.run(cmd, check=True, cwd=md_dir)



if __name__=='__main__':
    # os.makedirs(CONTENT_DIR, exist_ok=True)
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    
    for c in OUTPUT_TYPE:
        os.makedirs(os.path.join(EXPORTS_DIR, c), exist_ok=True)

    # Load blogs metadata
    with open(BLOGS_JSON, "r") as f:
        blogs = json.load(f)

    # Load existing hashes
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            hashes = json.load(f)
    else:
        hashes = {}
    
    
    for blog in blogs:
        # if not blog.get("active"):
        #     continue

        slug = blog["slug"]
        title = blog["title"]
        path_url = blog["path"]

        input_md = blog["repo_path"]#os.path.join(content_path, f"{slug}.md")
        output_files = {}
        file_exists = True
        for c in OUTPUT_TYPE:
            current_directory = os.getcwd()
            op_file = os.path.join(current_directory, EXPORTS_DIR, c, f"{slug}.{c}")
            output_files[c] =  op_file
            file_exists = file_exists and os.path.exists(op_file)
        
        stored_hash = hashes.get(slug, None)
        current_hash = compute_sha256(input_md)
        
        if stored_hash and file_exists and not ALWAYS_CREATE:
            # check current file hash
            if stored_hash != current_hash:
                generate_files(input_md, output_files)
                hashes[slug] = current_hash
        else:
            # save all
            generate_files(input_md, output_files)
            hashes[slug] = current_hash

    # Save updated hashes
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=2)

    print("All done.")

        
