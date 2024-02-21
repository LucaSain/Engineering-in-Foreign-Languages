import os
import shutil

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
                # For Markdown files, create a new directory and copy the file to it
                directory_name = os.path.splitext(file)[0]
                new_directory = os.path.join(directory, directory_name)
                new_file_path = os.path.join(new_directory, "page.md")

                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)
                
                # Read the content of the markdown file
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Update image links in the markdown content
                updated_content = re.sub(r'\((.*?)(?:/img/)?(.*?)\.(?:png|jpg|mp4)\)', r'(/img/\2.\1)', content)

                # Write the updated content back to the page.md file
                with open(new_file_path, 'w') as f:
                    f.write(updated_content)
                
            elif file.endswith((".png", ".jpg", ".mp4")):
                # For .png and .jpg files, copy them to the img directory
                shutil.copy(file_path, os.path.join(img_dir, file))
                os.remove(file_path)
                
if __name__ == "__main__":
    process_directory("./compiled")
    print("Markdown files processed successfully.")
