import os
import shutil

def get_downloads_path():
    """Get the Downloads folder path for any user."""
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # macOS/Linux
        return os.path.join(os.environ['HOME'], 'Downloads')

path = get_downloads_path()

def dirCreate():
    # List of folders used for organization
    system_folders = ['Pictures', 'Videos', 'Audio', 'Documents', 'Code',
                     'Compressed', 'Applications', 'Other', 'PowerPoints', 'Folders']
    
    for folder in system_folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def fileSort():
    # List of folders you don't want to move
    exclude_folders = ['Pictures', 'Videos', 'Audio', 'Documents', 'Code',
                      'Compressed', 'Applications', 'Other', 'PowerPoints', 'Folders']
    
    # List of protected system files skipped
    protected_files = ['desktop.ini', 'thumbs.db']
    
    # First, move all files to their respective folders
    for x in os.listdir(path):
        file_path = os.path.join(path, x)

        # Skip directories 
        if os.path.isdir(file_path):
            continue
        
        # Skip protected system files
        if x.lower() in protected_files:
            continue

        try:
            if x.endswith((".txt", ".pdf", ".docx", ".doc")):
                shutil.move(file_path, os.path.join(path, 'Documents', x))
            elif x.endswith((".png", ".jpg", ".gif", ".webp", ".jpeg")):
                shutil.move(file_path, os.path.join(path, 'Pictures', x))
            elif x.endswith((".mp4", ".mov", ".wmv")):
                shutil.move(file_path, os.path.join(path, 'Videos', x))
            elif x.endswith(".mp3"):
                shutil.move(file_path, os.path.join(path, 'Audio', x))
            elif x.endswith((".class", ".py", ".html", ".css", ".js", ".java")):
                shutil.move(file_path, os.path.join(path, 'Code', x))
            elif x.endswith((".zip", ".tar", ".rar", ".7z")):
                shutil.move(file_path, os.path.join(path, 'Compressed', x))
            elif x.endswith((".exe", ".app", ".apk", ".msi")):
                shutil.move(file_path, os.path.join(path, 'Applications', x))
            elif x.endswith((".ppt", ".pptx")):
                shutil.move(file_path, os.path.join(path, 'PowerPoints', x))
            else:
                shutil.move(file_path, os.path.join(path, 'Other', x))
        except (PermissionError, shutil.Error) as e:
            print(f"Could not move file {x}: {e}")
    
    # Then, move all other folders (except our system folders) to the 'Folders' folder
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path) and item not in exclude_folders:
            try:
                shutil.move(item_path, os.path.join(path, 'Folders', item))
            except (PermissionError, shutil.Error) as e:
                print(f"Couldn't move folder {item}: {e}")

dirCreate()
fileSort()