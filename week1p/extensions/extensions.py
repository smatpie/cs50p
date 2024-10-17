# Take user input
x = input("File name: ").lower().strip()
# condition 1
if "." not in x:
    print("application/octet-stream")
else:
    x = x.rsplit(".", 1)
    # multiple conditions
    match x[1]:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
