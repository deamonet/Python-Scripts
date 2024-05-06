#pip install msoffcrypto-tool
import msoffcrypto


def iterate_keys(crypted_file_path):
    for i in range(4995, 5005):
        try:
            word = msoffcrypto.OfficeFile(open(crypted_file_path, 'rb'))
            word.load_key(password=str(i), verify_password=True)
            print(f"right password {i}")
            return
        except msoffcrypto.exceptions.InvalidKeyError:
            print(f"wrong password:\t{i}")


if __name__ == '__main__':
    crypted_file_path = "./exp2.docx"
    print("password: 5000")
    print("iterate from 4800 to 5200")
    iterate_keys(crypted_file_path)
