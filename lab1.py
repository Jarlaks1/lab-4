#!/usr/bin/env python

import argparse
from operator import add, sub
from itertools import cycle

def vig_alg(in_, key_, mod_):
    f = (add if mod_ == 'c' else sub)
    in_ = [ord(i) for i in in_]
    key_ = [ord(i) for i in key_]
    res_ = str()
    for d, k in zip(in_, cycle(key_)):
        c = (f(d, k) + 256) % 256
        res_ += chr(c)
    return res_

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('in_', type=argparse.FileType(mode='rb'))
    parser.add_argument('out_', type=argparse.FileType(mode='wb'))
    parser.add_argument('key_', type=argparse.FileType(mode='rb'))
    parser.add_argument('mod_', choices=['c', 'd'])
    args = parser.parse_args()

    
    res_ = vig_alg(args.in_.read(), args.key_.read(), args.mod_)
    args.out_.write(res_)
