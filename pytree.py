#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import sys
import os
from os import walk as walk
from os.path import basename

def tree(path):
    #Initiate indent
    fileindent = ''
    dirindent = '' 
    
    sepno = path.count('/')
    num_dir = 0
    num_file = 0
    count = []
    tracker = []
    isFirst = 0
    for path,dirs, files in sorted(walk(path)):
        #keep track of total directory & files in given path
        num_dir = num_dir + len(dirs)
        num_file = num_file + len(files)
        
        
        depth = path.count('/') - sepno
        total_files = len(dirs) + len(files)
        
        tracker.append([depth, total_files])
        count.append([depth,0])
        dirindent = '│   '*(depth-1)
        fileindent = '    ' * (depth)
        
        #print directory
        if isFirst > 0:
            if count[depth-1][1] == (len(os.listdir(path.replace(basename(path),''))) - 1):
                print(dirindent + '└── ' + basename(path))
                count[depth-1][1] = 0
            else:
                print(dirindent + '├── ' + basename(path))
                count[depth-1][1] +=1
        
        #print non-directory files
        for i, filename in enumerate(files):
            if count[depth][1] == (len(os.listdir(path)) - 1 ):
                print('│   ' * depth + '└── ' + files[i])
                count[depth][1] = 0
            else:
                print('│   ' * depth + '├── ' + files[i])
                count[depth][1] +=1
        isFirst += 1        
    print("%s directories, %s files" % (num_dir, num_file))

if __name__ == '__main__':
   	#if given no path
   	if len(sys.argv) == 1:
   		print('.')
   		path = os.getcwd()
   		tree(path)
   	elif len(sys.argv) == 2:
   		print(sys.argv[1])
   		path = sys.argv[1]
   		tree(path)
   	else:
   		print('Please enter with only one path.')

