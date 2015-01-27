#!/usr/bin/env python

import argparse
import sys
import socket

import lab1
import lab2
import lab3_in
import lab3_out

PORT = 55555

def client(data, key_lab1, key_lab2, picture, host):
    data_vig = lab1.vig_alg(data, key_lab1, 'c')
    data_aes = lab2.AES_main(data_vig, key_lab2, 'c')
    picture_name = "tmp.bmp"
    lab3_in.data_hide(data_aes, picture , picture_name)
    pic = open(picture_name, 'rb')
    picture_data = pic.read()

    sock = socket.socket()
    sock.connect((host, PORT))
    sock.send(picture_data)
    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType(mode='rb'))
    parser.add_argument('key_lab1', type=argparse.FileType(mode='rb'))
    parser.add_argument('key_lab2', type=argparse.FileType(mode='rb'))
    parser.add_argument('picture')
    parser.add_argument('server_address')
    args = parser.parse_args()

    client(args.input.read(), args.key_lab1.read(), args.key_lab2.read(), args.picture, args.server_address)