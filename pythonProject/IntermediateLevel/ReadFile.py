# Read Mode
# file = open('test.txt')
# print(file.read()) # Read entire file
# print(file.read(4))  # Read only 4 characters
# print(file.readline())  # Read only first line
# print(file.readlines())  # Reads all the lines and return them as each line a string element in a list.
# Write Mode
# file.write('abc')
# L = ["Anupama", "Selenium", "Python"]
# file.writelines(L)
file = open('geek.txt', 'w')
file.write("This is the write command \n")
file.write("It allows us to write in a particular file \n")
file.close()
# Append Mode
# file1 = open('test.txt')
# print(file1.read())
# # print(file1.write("Tomorrow \n"))
# file1.close()
# print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line=file.readline()

# values = [mobiles, washingmachines, refrigerators]
# for line in file.readline():
#     print(line)


#file.close()


# Open the text file in reading mode
with open('text.txt', 'r') as f:
  # Read all the lines of the text file into a list
  lines = f.readlines()
  # Iterate over the lines, and skip every other line
  for i in range(0, len(lines), 2):
    # Print the current line
    print(lines[i])

import csv

with open('in.csv', 'w') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['first_name'], row['last_name'])