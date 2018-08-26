from __future__ import (absolute_import, division, print_function)
from PIL import Image
import six
import os
import fire
import imagehash


def compute_phash(img_name, hashfunc=imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
               f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(
            ".gif") or '.jpg' in f
    if not is_image(img_name):
        # print("is not img name", img_name)
        return
    hash = hashfunc(Image.open(img_name))
    return str(hash), os.path.basename(img_name)


if __name__ == '__main__':
  fire.Fire(compute_phash)

