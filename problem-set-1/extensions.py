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

file_name = input("File name: ")

if ".gif" in file_name:
    print(extensions_dict[".gif"])
elif ".jpg" in file_name:
    print(extensions_dict[".jpg"])
elif ".jpeg" in file_name:
    print(extensions_dict[".jpeg"])
elif ".png" in file_name:
    print(extensions_dict[".png"])
elif ".pdf" in file_name:
    print(extensions_dict[".pdf"])
elif ".txt" in file_name:
    print(extensions_dict[".tx"])
elif ".zip" in file_name:
    print(extensions_dict[".zip"])
else:
    print(extensions_dict["no-suffix"])