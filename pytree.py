#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import sys
import os
from os import listdir, sep, walk
from os.path import basename, isdir


def printDir(path, padding, isLast):
    if isLast:
        padding = padding + '   '
        tree(path, padding, isLast=False)
    else:
        padding = padding + '│   '
        tree(path, padding, isLast=False)


def tree(dir, padding, isLast=False):
    files = []
    files = listdir(dir)
    files = sorted(files)

    for i, file in enumerate(files):
        path = dir + sep + file
        if (i == len(files) - 1):
            isLast = True
            print(padding + '└── ' + file)
            if isdir(path):
                printDir(path, padding, isLast)
        else:
            isLast = False
            print(padding + '├── ' + file)
            if isdir(path):
                printDir(path, padding, isLast)
    padding = padding + '   '


# function to track number of directories and files in given path
def fileTrack(path):
    num_dir = 0
    num_file = 0

    for path, dirs, files in walk(path):
        # keep track of total directory & files in given path
        num_dir = num_dir + len(dirs)
        num_file = num_file + len(files)
    print("%s directories, %s files" % (num_dir, num_file))

if __name__ == '__main__':
# if given no path
    if len(sys.argv) == 1:
        print('.')
        path = os.getcwd()
        tree(path, '', isLast=False)
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        tree(path, '', isLast=False)
        fileTrack(path)
    else:
        print('Please enter with only one path.')
