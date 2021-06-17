import os
import imghdr
from PIL import Image
import shutil

supported_image_ext = ('png', 'bmp', 'jpeg')

if __name__ == '__main__':
    root_dir = "."
    files_in_dir = os.listdir(root_dir)
    log_file = open("unsupported_images.txt", "w+")

    original_path = os.getcwd()    # user also can modify the path they want save their unsupported images, exp : "C:\\Users\\ken\\Documents"
    directory = "UnsupportedImg"
    path = os.path.join(original_path, directory)
    os.mkdir(path)
    
    for file in files_in_dir:
        if os.path.isfile(file):
            image_type = imghdr.what(file)
            if image_type is not None and image_type not in supported_image_ext:
                log_str = "Filename: {} - Image type: {}".format(file, image_type)
                print(log_str)
                log_file.write(log_str + "\n")
                im = Image.open(file).convert("RGB")
                name = os.path.splitext(file)[0]
                im.save("{}.jpg".format(name), "jpeg")
                shutil.move(file, path)
    log_file.close()

    
    
