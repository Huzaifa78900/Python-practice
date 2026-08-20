word="donkey"
with open("don.txt")as f:
    content=f.read()

contentNew=content.replace(word,"####")

with open("don.txt","w")as f:
    f.write(contentNew)