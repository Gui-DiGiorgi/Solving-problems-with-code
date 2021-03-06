# This script lists the files or counts how many files there are inside of a folder
# The list/count can include its subfolders or not
# It also lists/counts just a certain type of file if specified

import os

def file_lister(c_path,ext = None, result = "name", sub = True):

    # c_path = r'C:/Users/User/Music'

    folders_loc = []

    file_list = []

    # ext = '.mp3'
    
    if sub:

        for i in os.listdir(c_path):
            folders_loc.append(r'{0}/{1}'.format(c_path,i))

        while len(folders_loc) != 0:
            fake_folders_loc = []
            for i in folders_loc:
                if os.path.isdir(i):
                    for f in os.listdir(i):
                        fake_folders_loc.append(r'{0}/{1}'.format(i,f))
                else:
                    if ext == None:
                        file_list.append(i)
                    else:
                        if i[-len(ext)::1]==ext:
                            file_list.append(i)

            folders_loc = []
            folders_loc = fake_folders_loc.copy()
            
    
    else:
    
        for i in os.listdir(c_path):
            full_name = r'{0}/{1}'.format(c_path,i)
            if os.path.isfile(full_name):
                if ext == None:
                    file_list.append(full_name)
                else:
                    if i[-len(ext)::1]==ext:
                        file_list.append(full_name)
                
    if result == "name":
        return file_list
    
    elif result == "n":
        return len(file_list)
