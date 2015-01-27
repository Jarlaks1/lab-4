#!/usr/bin/env python

import argparse
import sys
import socket

import lab1
import lab2
import lab3_in
import lab3_out

PORT = 55555


def server(key_lab1, key_lab2):
    sock = socket.socket()
    sock.bind(('', PORT))

    sock.listen(100)
    conn, addr = sock.accept()
    conn.settimeout(10)
    picture = ""
    while True:
        data = conn.recv(1000000)
        if not data:
            break
        picture += data
    conn.close()
    
    imgfile = open("tmp2.bmp", 'wb')
    imgfile.write(picture)
    imgfile.close()

    coded_aes = lab3_out.extract_data("tmp2.bmp")
    coded_vig = lab2.AES_main(coded_aes, key_lab2, 'd')
    data = lab1.vig_alg(coded_vig, key_lab1, 'd')
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('key_lab1', type=argparse.FileType(mode='rb'))
    parser.add_argument('key_lab2', type=argparse.FileType(mode='rb'))
    parser.add_argument('output', type=argparse.FileType(mode='wb'))
    args = parser.parse_args()
    
    result = server(args.key_lab1.read(), args.key_lab2.read())
    args.output.write(result)