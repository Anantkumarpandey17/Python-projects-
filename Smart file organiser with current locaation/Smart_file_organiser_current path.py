import os

# os.chdir("Downloads")
print(os.getcwd())

lst = os.listdir()

folders = ["Images","Documents","Audio", "Vedios", "Python","Other"]

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
    
for items in lst:
    name, extension = os.path.splitext(items)

    if extension == ".jpg" or extension == ".png":
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Images",items)
        os.rename(old_path,new_path)
   
    elif extension == ".pdf" or extension == ".txt":
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Documents",items)
        os.rename(old_path,new_path)
    
    elif extension == ".mp3":
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Audio",items)
        os.rename(old_path,new_path)

    elif extension == ".mp4":
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Vedios",items)
        os.rename(old_path,new_path)

    elif extension == ".py":
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Python",items)
        os.rename(old_path,new_path)

    else:
        old_path = os.path.join(os.getcwd(),items)
        new_path = os.path.join(os.getcwd(),"Other",items)
        os.rename(old_path,new_path)




