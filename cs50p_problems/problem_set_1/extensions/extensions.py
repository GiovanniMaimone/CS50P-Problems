extensions = input("File: ").lower().strip()

sulfix = extensions.rsplit(sep=".")[-1]

match sulfix:
    case "gif" | "jpeg" | "png":
        print(f"image/{sulfix}")
    case "jpg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "zip" | "pdf":
        print(f"application/{sulfix}")
    case _:
        print("application/octet-stream")


