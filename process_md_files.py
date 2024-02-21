import os
import shutil

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                directory_name = os.path.splitext(file)[0]
                new_directory = os.path.join(root, directory_name)
                new_file_path = os.path.join(new_directory, "page.md")

                # Create a new directory if it doesn't exist
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)

                # Copy the content of the markdown file to page.md
                shutil.copy(file_path, new_file_path)

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    process_directory(directory)
    print("Markdown files processed successfully.")
