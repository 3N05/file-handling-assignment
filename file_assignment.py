def file_read_write():
    """Reads from a file and writes a modified version to a new file."""
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File successfully modified and saved as output.txt")

    except FileNotFoundError:
        print("❌ input.txt not found. Please make sure the file exists.")


def error_handling_lab():
    """Asks the user for a filename and handles errors."""
    filename = input("Enter a filename: ")

    try:
        with open(filename, "r") as f:
            print("📄 File content:")
            print(f.read())
    except FileNotFoundError:
        print("❌ Error: File does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("--- File Read & Write Challenge ---")
    file_read_write()

    print("\n--- Error Handling Lab ---")
    error_handling_lab()
