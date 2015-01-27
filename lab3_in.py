#!/usr/bin/env python2.7
#coding: UTF-8

import argparse
from PIL import Image
    

def data_hide(data, img_Name, res_Img_Name):
    data = [ord(x) for x in data]
    img = Image.open(img_Name)
    raw = [ord(x) for x in img.tostring()]
    i = 0

    size = len(data)
    if size * 8 + 24 > len(raw): #every 24th
		raise Exception('Data too big for this image!')
    #LSB    
    for j in range(24):
        raw[i] = raw[i] & 0xFE | size & 1
        size >>= 1
        i += 1

    for b in data:
        for j in range(8):
            raw[i] = raw[i] & 0xFE | b & 1
            b >>= 1
            i += 1

    raw = [chr(x) for x in raw]
    result_img = Image.fromstring(img.mode, img.size, ''.join(raw))
    result_img.save(res_Img_Name, "BMP")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image')
    parser.add_argument('data', type=argparse.FileType(mode='rb'))
    args = parser.parse_args()

    out_name = "secret.bmp"
    data_hide(args.data.read(), args.image, out_name)
    print "Result saved to", out_name
