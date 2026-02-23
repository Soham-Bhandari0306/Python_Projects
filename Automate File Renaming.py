import os

def rename_files():
    print("===== Task 4: Automate File Renaming =====\n")

   
    # Take folder path from user
    
    folder_path = input("Enter the folder path: ")

    
    # Check if folder exists
    
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

   
    # Get list of items in folder
    
    files = os.listdir(folder_path)

   
    # Filter only files (ignore folders)
    
    only_files = []
    for file in files:
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            only_files.append(file)

    
    # If no files found
    
    if len(only_files) == 0:
        print("No files found in this folder.")
        return

    print(f"\nTotal files found: {len(only_files)}")
    print("Files will be renamed as file_1, file_2, file_3 ...\n")

    confirm = input("Do you want to continue? (yes/no): ")

    if confirm.lower() != "yes":
        print("Operation cancelled.")
        return

    count = 1

   
    # Renaming process
    
    for file in only_files:
        old_path = os.path.join(folder_path, file)
        extension = os.path.splitext(file)[1]

        new_name = f"file_{count}{extension}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} → {new_name}")
        count += 1

    print("\nAll files renamed successfully!")


# Call the function
rename_files()
