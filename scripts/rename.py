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

'''
Rename all file in the directory with special random ID
Support for jpg, png and jpeg

'''

import argparse
import uuid
import os
import shutil
from pathlib import Path

args = argparse.ArgumentParser()
args.add_argument('--dir', help="Path to folder", required=True)
cfg = args.parse_args()

def create_dir(path):
    # Create dir if not exists
    if not os.path.exists(path):
        os.makedirs(path)
        return

def get_relative_path(dir):
    relative = Path(dir)
    absolute = relative.absolute()
    return absolute

def rename_image(dir, new_dir):
    count = 1
    # UUID
    id = uuid.uuid4()
    all_files = os.listdir(os.path.abspath(dir))
    for fileName in all_files:
        if fileName[-3:] == 'jpg' or fileName[-3:] == 'png' or fileName[-3:] == 'JPG':
            # picture format
            imgFormat = fileName[-3:]
            
            # Get full path of image from old path
            oldAbsolute = get_relative_path(dir)
            oldPath = newPath = (str(oldAbsolute) + '/' + fileName)
            
            # Get full path of image from new path
            newAbsolute = get_relative_path(new_dir)
            newName = str(id) + '_'+ str(count) + '.' + imgFormat
            newPath = (str(newAbsolute) + '/' + newName)

            # increment count
            count += 1
            
            # Copy images to new dir
            shutil.copy(oldPath, newPath)
        
        elif fileName[-4:] == 'jpeg':
            # picture format
            imgFormat = fileName[-4:]

            # Get full path of image from old path
            oldAbsolute = get_relative_path(dir)
            oldPath = (str(oldAbsolute) + '/' + fileName)
            
            # Get full path of image from new path
            newAbsolute = get_relative_path(new_dir)
            newName = str(id) + '-'+ str(count) + '.' + imgFormat
            newPath = (str(newAbsolute) + '/' + newName)

            # increment count
            count += 1
            
            # Copy images to new dir
            shutil.copy(oldPath, newPath)


def main():
    # check dir exists
    create_dir('renamed')
    # rename image on old directory
    rename_image(cfg.dir, 'renamed')



if __name__=="__main__":
    main()