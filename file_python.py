
with open("python.txt", "r") as file:
    content = file.read()

if ("python" in content):
    print("The word 'python' is present in the file.")
else:
    print("The word 'python' is not present in the file.")