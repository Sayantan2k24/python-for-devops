# validate the file path

def validate_file_path(file_path):
    try:
        with open(file_path, "r"):
            pass
    except FileNotFoundError:
        print("Error: File not found. Enter a valid path.")
        return False
    except Exception as e:
        print(f"An error occurred while validating the file: {e}")
        return False

    return True

# update server config file 

def update_server_config(file_path, key, value):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            for line in lines:
                if key in line:
                    file.write(key + "=" + value + "\n")
                else:
                    file.write(line)

        print("Configuration updated successfully. Check the file for changes!")

    except FileNotFoundError:
        print("Error: File not found. Enter a valid path.")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("\t\t\t==== Welcome ====")
    print("\t\tServer Configuration Management")

    file_path = input("Enter the path of the configuration file: ")

    # Validate file path
    if not validate_file_path(file_path):
        return

    key = input("Enter the key you want to change: ")
    value = input("Enter the new value: ")

    update_server_config(file_path, key, value)

if __name__ == '__main__':
    main()
