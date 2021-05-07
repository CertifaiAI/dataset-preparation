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
        if fileName[-3:] == 'jpg' or fileName[-3:] == 'png':
            # picture format
            imgFormat = fileName[-3:]
            
            # Get full path of image from old path
            oldAbsolute = get_relative_path(dir)
            oldPath = newPath = (str(oldAbsolute) + '/' + fileName)
            
            # Get full path of image from new path
            newAbsolute = get_relative_path(new_dir)
            newName = str(id) + '-'+ str(count) + '.' + imgFormat
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