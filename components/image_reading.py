import easyocr


def image_reading(image_path):

    reader = easyocr.Reader(['en'], gpu = True) #Only if you have a GPU
    results = reader.readtext('./images/test.jpg', detail = 0)
    return results

