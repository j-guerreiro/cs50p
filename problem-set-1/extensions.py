# Extensions problem
# author: jguerreiro

extensions_dict = {
".gif": "image/gif",
".jpg": "image/jpg",
".jpeg": "image/jpeg",
".png": "image/png",
".pdf": "application/pdf",
".txt": "text/plain",
".zip": "application/zip",
"no-suffix": "application/octet-stream"
}

fileName = input("File name: ")

if ".gif" in fileName:
    print(extensions_dict[".gif"])
elif ".jpg" in fileName:
    print(extensions_dict[".jpg"])
elif ".jpeg" in fileName:
    print(extensions_dict[".jpeg"])
elif ".png" in fileName:
    print(extensions_dict[".png"])
elif ".pdf" in fileName:
    print(extensions_dict[".pdf"])
elif ".txt" in fileName:
    print(extensions_dict[".tx"])
elif ".zip" in fileName:
    print(extensions_dict[".zip"])
else:
    print(extensions_dict["no-suffix"])