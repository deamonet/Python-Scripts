import zipfile


def zip_cracker(file_path):
    file = zipfile.ZipFile(file_path, 'r')
    for i in range(4995, 5005):
        try:
            file.extractall(pwd = str(i).encode())
            file.close()
            print(f"right password {i}")
            return
        except RuntimeError:
            print(f"wrong password {i}")


if __name__ == '__main__':
    file_path = "exp2.zip"
    zip_cracker(file_path)
