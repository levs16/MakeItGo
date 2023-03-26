import random, os, shutil # Imports

fscan = os.listdir() # Scanning the files and directories
count = 0 # Counter for files and directories

print("\n---------Script--------\nFound files and dirs: ", *fscan, "\n-------------------") # Just a print for files

try: # Using the "try" to execute
    for file in fscan: # scanning the files and dir names in the fscan list

        print(f"Starting...") # Print-out

        if os.path.isfile(file): # Checking, whether the name is file, if yes, then proceed
            print(f"\n---------Script--------\nOverwriting {file}..\n-------------------\n.")
            k = random.randint(9999, 999999) # Getting a random value (can be reblaced with string or a fixed int)
            os.remove(file) # Remove the file
            count += 1 # Add a 1 to the counter after the file deletion thing has been made
            print(f"\n---------Script--------\nOverwritten {file}. Deleted or/and overwritten: {count}\n-------------------\n")
        else: # Or, if name isn't a file, then proceed doing this
            print(f"\n---------Script--------\nDeleting {file} with its contents..\n_______________\n.")
            shutil.rmtree(file) # Using shutil (a library) we're removing the directory
            count += 1
            print(f"\n---------Script--------\nDeleted {file}. Deleted or/and overwritten: {count}\n-------------------\n")

except Exception as ex: # Printing out error (just for script to be beautiful)
    print(f"\n-----Script-Error------\nOops, an error, details: {ex}\n-------------------______\n") # Printing out the error

print(f"Total: {count} file(s) and/or dir(s)")
print("\n=====COMPLETE=====\n") # Notify user that script executed

# Written by Lev Sokolov on Sun. Mar. 4:05 AM.
# USE AT YOUR OWN RISK! CAN REMOVE IMPORTANT FOR YOU FILES!

# MADE ONLY FOR EDUCATIONAL AND TESTING PURPOSES!

