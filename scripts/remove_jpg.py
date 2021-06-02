import os
import argparse

args = argparse.ArgumentParser()
args.add_argument('--dir', help='Path to folder', required=True)
cfg = args.parse_args()


def rename_files(dir):
    directory_list = os.listdir(dir)
    for f in directory_list:
        src = f
        if '_jpg' in f:
            dst = f.replace('_jpg', '')
            os.rename(os.path.join(dir, src), os.path.join(dir, dst))
        elif '_JPG' in f:
            dst = f.replace('_JPG', '')
            os.rename(os.path.join(dir, src), os.path.join(dir, dst))
        elif '_jpeg' in f:
            dst = f.replace('_jpeg', '')
            os.rename(os.path.join(dir, src), os.path.join(dir, dst))


if __name__ == '__main__':
    rename_files(cfg.dir)