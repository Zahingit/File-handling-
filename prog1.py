with open("File.1.txt", "w") as file:
    file.write("Hi, this is a sample.\n")
    file.write("It contains multiple lines.\n")
    file.write("Each line has some text.\n")

with open("File.1.txt", "r") as file:
    contents = file.read()
    words = contents.split()
print("words in the file:", words)