#!/usr/bin/python3

from sys import *


def open_file(filename):
    source_code = open(filename, 'r').read()
    #print(source_code)
    return source_code


def run():
    data = open_file(argv[1])

run()
