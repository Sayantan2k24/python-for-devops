
def update_server_config(file_path, key, value):
    try:
        with open(file_path,"r") as file:
            lines = file.readlines()

            with open(file_path, "w") as file:
                for line in lines:
                    if key in line:
                        file.write(key + "=" + value + "\n")

                    else:
                        file.write(line)
                
                print("All done. Open the file and check!")
    
    except FileNotFoundError:
        print("File not available, Enter a valid path")


def main():
    print("\t\t\t==== Welcome====")
    print("\t\tServer Configuration Management")
    file_path = input("Give the path of the file : ")
    key = input("Give the key that you want to change: ")
    value = input("Give the value now : ")

    update_server_config(file_path, key, value)



if __name__ == '__main__':
    main()