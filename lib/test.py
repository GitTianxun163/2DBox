def eplinse(text,path):
    content = ""
    for s in text[::-1]:
        if s == '-':
            content += "-"
            continue
        elif s == '\n':
            content += "\n"
            continue
        content += chr(ord(s)-32)
    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

def readpass(path):
    with open(path,"r",encoding="utf-8") as f:
        text = f.read()
    content = ""
    for s in text[::-1]:
        if s == '-':
            content += "-"
            continue
        elif s == '\n':
            content += "\n"
            continue
        content += chr(ord(s)+32)
    print(content)
    # with open("temp","w",encoding="utf-8") as f:
    #     f.write(content)
    return content

# readpass("data\\world\\世界.world")

