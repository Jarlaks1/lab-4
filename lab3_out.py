#!/usr/bin/env python2.7
#coding: UTF-8

import argparse
from PIL import Image

def extract_data(img_Name):
    img = Image.open(img_Name)
    raw = [ord(x) for x in img.tostring()]
    i = 0

    size = 0
    while i < 24:
        size |= (raw[i] & 1) << i
        i += 1

    result = [0] * size
    for j in range(size):
        result[j] = 0
        for k in range(8):
            result[j] |= (raw[i] & 1) << k
            i += 1

    return ''.join([chr(i) for i in result])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image')
    parser.add_argument('output', type=argparse.FileType(mode='wb'))
    args = parser.parse_args()

    extract_res = extract_data(args.image)
    args.output.write(extract_res)
