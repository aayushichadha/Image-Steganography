from PIL import Image
def encode_image(img, msg):
    
    length = len(msg)
    print length
    if length > 1500:
        print("text too long! (don't exeed 255 characters)")
        return False
   
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                    print asc
                elif index <= length:
                    c = msg[index - 1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g, b))
                index += 1
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                    print asc
                elif index <= length:
                    c = msg[index - 1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g, b, a))
                index += 1
    return encoded

def decode_image(img):
    """
    check the red portion of an image (r, g, b) tuple for
    hidden message characters (ASCII values)
    """
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b= img.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = img.getpixel((col, row))		
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
                print length
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg



    
    
