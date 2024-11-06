# This program shows why it is important to close the file after its use
# def write_to_file():
#     f = open("exam_soultion.txt", "w")
#     f.write("This is a test.")

#     read_from_file()    

# def read_from_file():
#     file = open("exam_soultion.txt", "r")
#     content = file.read()
#     print("File content:", content)

# write_to_file()


# for note the python automatically close the file when we exit the function
# check it if its true by running the below code

def write_to_file():
    f = open("exam_soultion.txt", "w")
    f.write("This is a test.")

def read_from_file():
    file = open("exam_soultion.txt", "r")
    content = file.read()
    print("File content:", content)

write_to_file()
read_from_file()