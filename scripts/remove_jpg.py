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