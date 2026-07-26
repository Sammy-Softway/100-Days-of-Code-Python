#Absolute file path
with open("/Users/samue/OneDrive/Desktop/my-text.txt") as file:
    content = file.read()
    print(content)

#Relative file path
with open("../../../Desktop/my-text.txt") as file:
    content = file.read()
    print(content)