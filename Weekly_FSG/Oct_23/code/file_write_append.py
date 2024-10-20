# This program shows the difference between write mode and append mode
with open('example.txt', 'w') as file:
    file.write('This is write mode.\n')

# with open('example.txt', 'a') as file:
#      file.write('This is append mode.\n')

with open('example.txt', 'r') as file:
    print(file.read())

# To observe the difference between 'write' (w) and 'append' (a) modes:
# Step 1: First, comment out the code that opens the file in append mode 
# and run the program with 'write' mode.
#
# Step 2: Now, comment out the 'write' mode code, uncomment the 'append'
# mode code, and run the program again.
