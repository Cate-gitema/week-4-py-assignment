def main():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully.")

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Create a new filename to write the modified content
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename}.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Could not read the file.")

# Run the main function
main()

        