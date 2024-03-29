import os
import shutil
import re

def replace_image_urls(text):
   regex = r"!\[(.*?)\]\((.*?)\)"  # Regex to match image entries

   def replacement(match):
       alt_text, original_url = match.groups()
       filename = original_url.split("/")[-1]  # Extract filename from original URL
       new_url = f"/{filename}"  # Construct the new URL with leading slash
       return f"![{alt_text}]({new_url})"  # Build the modified image tag

   modified_text = re.sub(regex, replacement, text)
   return modified_text

def process_directory(directory):
    img_dir = os.path.join(directory, "img")
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    for root, dirs, files in os.walk(directory):
        if root == img_dir:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".md"):

                with open(file_path, "r") as f:
                    content = f.read()

                content = replace_image_urls(content)
                with open(file_path, "w") as f:
                    f.write(content)
                
                directory_name = os.path.splitext(file)[0]
                new_directory = os.path.join(root, directory_name)
                new_file_path = os.path.join(new_directory, "page.mdx")

                # Create a new directory if it doesn't exist
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)

                # Copy the content of the markdown file to page.md
                shutil.copy(file_path, new_file_path)
                os.remove(file_path)
                
            elif file.endswith((".png", ".jpg", ".mp4")):
                # For .png and .jpg files, copy them to the img directory
                shutil.copy(file_path, os.path.join(img_dir, file))
                os.remove(file_path)
                
if __name__ == "__main__":
    process_directory("./compiled")
    print("Markdown files processed successfully.")
