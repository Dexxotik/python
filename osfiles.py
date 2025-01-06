import os  

# Get the current working directory
print("Current Working Directory:", os.getcwd())  

# Change the directory to a new path
os.chdir('C:/Users/Dexxotik/Documents')
print("Current Working Directory after change:", os.getcwd())

# Create a new directory named 'New Folder'
os.mkdir("abc.txt")

# Rename the file 'abc.txt' to 'demofile.txt'
os.rename("abc.txt", "demofile.txt")  
print("The above code renamed current abc.txt to demofile.txt")

# Remove the file 'demofile.txt'
os.remove("demofile.txt")
print("The file has been removed")

# Remove the directory 'New Folder'
os.rmdir("New Folder")
print("The folder has been deleted")
