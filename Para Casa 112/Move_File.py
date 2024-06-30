import os
import shutil

from_dir = "C:/Users/Gamer/Downloads"
to_dir = "C:/Users/Gamer/Documents/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + '/' +"Arquivos_Documentos"
        path3 = path2 + '/' + file_name

        if os.path.exists(path2):
            print("Movendo Arquivo...")

            shutil.move(path1, path3)
        else:
            print("Criando a Pasta...")
            os.makedirs(path2)    

            print("Movendo Arquivo...")
            shutil.move(path1, path3)

    