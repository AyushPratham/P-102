import os
import shutil

to_dir = "c:/Users/ayush/Downloads"
from_dir = "C:/Users/ayush/Desktop/CodingRelated/Document_Files(P-102)/Download_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.exe','.webp','.jpg','.zip','.ini']:
        path1 = from_dir + '/'+ file_name
        path2 = to_dir + '/' + "Download_Files"
        path3 = to_dir + '/' + "Download_Files" + '/' + file_name
        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1,path3)

            