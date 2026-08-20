word="donkey"
with open("don.txt")as f:
    content=f.read()
if (word in content):
    word="####"

with open("don.txt","w")as f:
    f.write(content)