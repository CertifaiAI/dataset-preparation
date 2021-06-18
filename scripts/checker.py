#
# Copyright (c) 2021 CertifAI Sdn. Bhd.
#
# This program is part of OSRFramework. You can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import imghdr
from PIL import Image
import shutil

supported_image_ext = ('png', 'bmp', 'jpeg')

if __name__ == '__main__':
    root_dir = "."
    files_in_dir = os.listdir(root_dir)
    log_file = open("unsupported_images.txt", "w+")

    targeted_path = os.getcwd()    # user also can modify the path they want save their unsupported images, exp : change the os.getcwd() to "C:\\Users\\ken\\Documents"
    directory = "UnsupportedImg"
    path = os.path.join(targeted_path, directory)

    if not os.path.exists("UnsupportedImg"):
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

    
    
