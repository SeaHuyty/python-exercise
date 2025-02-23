# Files and Directories: 
from pathlib import Path
# We have: Absolute path and Relative path.
#   Absolute path start from the root of our hard disk
#       Example: c:\Program Files\Microsoft | This is a directory and path on window.
#                /usr/local/bin | This is the path on Mac.
#   Relative path is a path starting from the current directory.
#       Example: The Lib directory in your folder.
path = Path("ecommerce") # We don't have ecommerce directory here, so it will return False.
print(path.exists())
# You can create a new directory if you don't have one.
print(path.mkdir()) # It will return 'None'but you will see the folder you've just created.
print(path.rmdir()) # Here how to delete your directory. 'rm' short for remove. 'mk' short for make.
# We can also view all files in the current directory.
path = Path()
print(path.glob()) # With this we can search for files and directories in the current path.
print(path.glob('*')) # Here we search for all files and all directories.
print(path.glob('*.*')) # Here we only get all the files in the current directory, not directories.
print(path.glob('*.py')) # Here we search for '.py' files
print(path.glob('*.xls')) # Or spreadsheet files. ANYTHINGGG.
# But when we run it will return '<generator object Path.glob at 0xxxxxxxxxxxxxx>'
# So we have to use for loop
from pathlib import Path
path = Path()
for files in path.glob('*'):
    print(files)