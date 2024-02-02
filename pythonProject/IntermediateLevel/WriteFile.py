# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readline()   # Amazon is the best online shopping, Flipkart is the Online shopping
    reversed(content)        # Flipkart is the Online shopping, Amazon is the best online shopping
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
