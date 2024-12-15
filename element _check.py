import os


def check_files_in_folder(file_list_path, folder_path):
    missing_files = []
    
   
    with open(file_list_path, 'r') as file:
        filenames = file.read().splitlines()  

    
    for file_name in filenames:
        
        file_path = os.path.join(folder_path, file_name)
        
       
        if not os.path.isfile(file_path):
            missing_files.append(file_name)

    return missing_files


file_list_path = "test.txt" 
folder_path = "../fliker_30k/images"  
missing_files = check_files_in_folder(file_list_path, folder_path)

if missing_files:
    print("The following files are missing:")
    for file in missing_files:
        print(file)
else:
    print("All files are present.")
