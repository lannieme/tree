#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import sys
import os
import re
from os import listdir, sep, walk
from os.path import basename, isdir


def printDir(path, padding, isLast):
    if isLast:
        padding = padding + '    '
        tree(path, padding, isLast=False)
    else:
        padding = padding + '|   '
        tree(path, padding, isLast=False)


def tree(dir, padding, isLast=False):
    files = []
# Reference: http://stackoverflow.com/questions/7099290/how-to-ignore-hidden-files-using-os-listdir
    files = [files for files in listdir(dir) if not files.startswith('.')]
# Reference: http://stackoverflow.com/questions/13589560/how-to-sort-list-of-string-without-considering-special-characters-and-with-case
    allfiles = sorted(files, key=lambda x:re.sub('[^A-Za-z]+', '', x).lower())

    for i, filename in enumerate(allfiles):
        path = dir + sep + filename
        if (i == len(files) - 1):
            isLast = True
            print(padding + '`-- ' + filename)
            if isdir(path):
                printDir(path, padding, isLast)
        else:
            isLast = False
            print(padding + '|-- ' + filename)
            if isdir(path):
                printDir(path, padding, isLast)
    padding = padding + '    '


# function to track number of directories and files in given path
def fileTrack(path):
    num_dir = 0
    num_file = 0

    for path, dirs, files in walk(path):
        # Reference: http://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        num_dir = num_dir + len(dirs)
        num_file = num_file + len(files)
    print("%s directories, %s files" % (num_dir, num_file))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        path = os.getcwd()
        tree(path, '', isLast=False)
        print('')
        fileTrack(path)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
        tree(path, '', isLast=False)
        print('')
        fileTrack(path)
    else:
        print('Please enter with only one path.')
