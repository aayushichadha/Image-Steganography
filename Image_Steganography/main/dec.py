from PIL import Image
def decode_image(img):
    
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0:
                length = r
                print length
            elif index <= length:
                msg += chr(r)
            index += 1
    print index        
    return msg
encoded_image_file = "enc_beach.png"
img2 = Image.open(encoded_image_file)
print(img2, img2.mode)  # test
hidden_text = decode_image(img2)
print(hidden_text)
