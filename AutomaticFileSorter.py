import os, shutil

def get_downloads_path():
    """Get the Downloads folder path for any user."""
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # macOS/Linux
        return os.path.join(os.environ['HOME'], 'Downloads')
    
path = get_downloads_path()

def dirCreate():
    folders = ['Pictures', 'Videos', 'Audio', 'Documents', 'Code', 'Compressed', 'Applications', 'Other']
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def fileSort():
    for x in os.listdir(path):
        file_path = os.path.join(path, x)

        if os.path.isdir(file_path):
            continue

        if x.endswith(".txt") or x.endswith(".pdf") or x.endswith(".docx") or x.endswith(".doc"):
            shutil.move(file_path, os.path.join(path, 'Documents', x))
        elif x.endswith(".png") or x.endswith(".jpg") or x.endswith(".gif") or x.endswith("webp") or x.endswith("jpeg"):
            shutil.move(file_path, os.path.join(path, 'Pictures', x))
        elif x.endswith(".mp4") or x.endswith(".mov") or x.endswith(".wmv"):
           shutil.move(file_path, os.path.join(path, 'Videos', x))
        elif x.endswith(".mp3") :
            shutil.move(file_path, os.path.join(path, 'Audio', x))
        elif x.endswith(".class") or x.endswith(".py") or x.endswith(".docx") or x.endswith(".html") or x.endswith(".css"):
             shutil.move(file_path, os.path.join(path, 'Code', x))
        elif x.endswith(".zip") or x.endswith(".tar") :
             shutil.move(file_path, os.path.join(path, 'Compressed', x))
        elif x.endswith(".exe") or x.endswith(".app") or x.endswith(".apk"):
            shutil.move(file_path, os.path.join(path, 'Applications', x))
        else:
            shutil.move(file_path, os.path.join(path, 'Other', x))
        
dirCreate()
fileSort()



