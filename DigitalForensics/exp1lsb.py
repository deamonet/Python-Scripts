from PIL import Image

class LSB:
    def text_normalize(self, text):
        code = ""
        for i in range(0, len(text)):
            code += bin(ord(text[i])).replace('0b', '').zfill(8)
        code += '11111111'
        code += '1' * (3 - len(code) % 3)
        return code

    def text_restore(self, code):
        text = ""
        for i in range(0, len(code)-12, 8):
            count = 0
            for j in range(0, 8):
                count = count*2 + int(code[i+j])
            text += chr(count)

        return text

    def steganize(self, code, image):
        image = image.convert('RGB')
        width = image.size[0]
        height = image.size[1]
        code_len = len(code)
        count = 0
        for i in range(0, width):
            for j in range(0, height):
                if count < code_len:
                    pixel = image.getpixel((i, j))
                    r = pixel[0]
                    g = pixel[1]
                    b = pixel[2]
                    r = r - r % 2 + int(code[count])
                    count += 1
                    g = g - g % 2 + int(code[count])
                    count += 1
                    b = b - b % 2 + int(code[count])
                    count += 1
                    image.putpixel((i, j), (r, g, b))

        return image

    def desteganize(self, image):
        rec_text = ""
        width = image.size[0]
        height = image.size[1]

        count = 0
        for i in range(0, width):
            for j in range(0, height):
                p = image.getpixel((i, j))
                r = p[0]
                g = p[1]
                b = p[2]
                rec_text += str(r % 2)
                rec_text += str(g % 2)
                rec_text += str(b % 2)

                if rec_text[-8:] == '11111111':
                    return self.text_restore(rec_text)
                count += 3

if __name__ == "__main__":
    text = "LOREM IPSUM"
    original_image = "Lenna_(test_image).png"
    output_file = "out_image.png"
    lsb = LSB()
    print("generate text code...")
    code = lsb.text_normalize(text)
    print("open original image...")
    image = Image.open(original_image)
    print("begin steganize")
    image = lsb.steganize(code, image)
    image.save(output_file, format="png")
    print("text in imageture is:")
    image = Image.open(output_file)
    print(lsb.desteganize(image))