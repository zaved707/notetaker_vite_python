# file_lister.py
import os

def read_file_content(file_path):
    """
    Reads the content of a file and returns it as a raw string with line breaks.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The raw text content of the file, or an error message if the file can't be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied to read the file."
    except Exception as e:
        return f"Error: An unexpected issue occurred - {str(e)}"


def saveFile(content: str, filename: str) -> bool:
   
    try:
        # Ensure the filename ends with .md
        if not filename.lower().endswith('.md'):
            filename += '.md'
            
        # Open file in write mode with UTF-8 encoding
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False



def list_all(folder_path):
    """
    Lists all items (files and directories) in the specified folder.
    
    Args:
        folder_path (str): Path to the folder (e.g., 'path/to/folder' or '.')
    
    Returns:
        list: List of all item names in the folder
    """
    try:
        return os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
        return []

def list_files_only(folder_path):
    """
    Lists only files (excludes directories) in the specified folder.
    
    Args:
        folder_path (str): Path to the folder
    
    Returns:
        list: List of file names in the folder
    """
    try:
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
        return []

def list_files_recursive(folder_path):
    """
    Lists all files recursively in the folder and its subfolders.
    
    Args:
        folder_path (str): Path to the folder
    
    Returns:
        list: List of full file paths
    """
    file_list = []
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    except PermissionError:
        print(f"Error: Permission denied to access part of '{folder_path}'.")
        return []
saveFile('what in the world',r'D:\zaved\pythonprojects\web development\note taking app\notetakingapp_vite\notes\note1.md')