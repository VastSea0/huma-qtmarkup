def addHtmlTag(Tag,Class,Id,Content,File,Show):
    a = [Tag,Class,Content,Id]
    if Show:
        print(a)
    with open(File, "w") as file:
        file.write(f"<{Tag} class='{Class}' id='{Id}'> {Content} </{Tag}>")


addHtmlTag("h1","","","World helo","index.hml",True)
