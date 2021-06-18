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

from PIL import Image
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string('image', None, 'path to input image')

def main(argv):
    im = Image.open(FLAGS.image)
    rgb_im = im.convert('RGB')
    rgb_im.save('test.jpeg')

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass