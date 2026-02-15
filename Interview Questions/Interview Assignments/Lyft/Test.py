import sys
import csv

def test_cli_command():
    if len(sys.argv) > 1:
        print("File to be added: ", sys.argv[1])

    return input("Enter y for the commands to execute: ")


def test_txt_file_read():
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        for line in f:
            print(line.strip())

def test_txt_file_write():
    file_path = sys.argv[1]

    # Writing to file
    with open(file_path, "a") as f:
        f.write("\nTesting input from code")

    # Creating New File

    with open("test.txt", "w") as f:
        f.write("\nTesting new file data")

def test_csv_file_read():
    file_path = sys.argv[1]
    with open(file_path, mode="r", newline='') as file:
        reader = csv.reader(file)

        for line in reader:
            print(line)

    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for line in reader:
            print(line)

def test_csv_file_write():
    file_path = sys.argv[1]
    with open(file_path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Country", "Occupation"])

        writer.writerows([{"Name": "Might", "Age": 38, "Country": "Japan", "Occupation": "Hero"}])

if __name__ == "__main__":
    
    # res = test_cli_command()

    # if res == "y" or res == "Y":
    #     test_txt_file_read()
    #     test_txt_file_write()
    test_csv_file_write()
    test_csv_file_read()