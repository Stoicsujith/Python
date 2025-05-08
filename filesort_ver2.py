import os,shutil

def folderpath(folderpath, file_path, foldername):
    for folder in folder_names:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            print(f"Created file: {folder_path}")
            os.makedirs(folder_path)
        else:
            print(f"File not created: {folder_path}")
            
def fileorg(folderpath, file_path):
    for file in file_name:
        src = os.path.join(path, file)
        
        if file.endswith(".xlsx"):
            dest = os.path.join(path, "Excel_file", file)
        elif file.endswith(".docx"):
            dest = os.path.join(path, "Word_file", file)
        elif file.lower().endswith((".jpeg", ".jpg", ".png", ".bmp")):
            dest = os.path.join(path, "Image_file", file)
        elif file.endswith(".pptx"):
            dest = os.path.join(path, "Presentation_file", file)
        elif file.endswith(".txt"):
            dest = os.path.join(path, "Text_file", file)
            
        else:
            continue
        
        if not os.path.exists(dest):
            shutil.move(src, dest) 
            print(f"Moved file {file} -> {dest}")

# folderpath and file path
path = r"C:/Users/sujit/OneDrive/Documents/practicer/" 
file_name = os.listdir(path)

folder_names = ["Excel_file", "Image_file", "Presentation_file", "Text_file", "Word_file"]

folderpath(path, file_name, folder_names)
fileorg(path, file_name)  




        
    
    