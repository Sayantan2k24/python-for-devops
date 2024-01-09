import os


folder_paths = input("Enter a list of folder paths separated by spaces: ").split()

for folder in folder_paths:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please give a valid folder name, looks like this folder " + folder + " does not exist")
        continue

    except PermissionError:
        print("No access to this folder - " + folder)
        continue

    print("===listing files for the folder - " + folder )

    for file in files:
        print(file)



'''

Run in Linux OS

[krish@data2 ~]$ python test.py
Enter a list of folder paths separated by spaces: /xyz /root /opt
Please give a valid folder name, looks like this folder /xyz does not exist
No access to this folder - /root
===listing files for the folder - /opt
VBoxGuestAdditions-6.1.26
containerd

'''