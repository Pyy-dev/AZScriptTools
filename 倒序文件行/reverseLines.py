#!/usr/bin/env python
# coding=utf-8
# 把文件顺序行变倒序

import os
import time

#读取一个文件每一行,并倒序
def reverseLine(fname):
    linelist = open(fname).readlines()
    linelist.reverse()
    
    [dir,file] = os.path.split(path)
    newFile = dir + '/reverseLines_out.txt'
    
    fileOut = open(newFile, 'w')
    for line in linelist:
        fileOut.write(line)
        print line
    fileOut.close()
    print '【Success】\n已在 ['+dir+'] 目录下创建新文件[reverseLines_out.txt] 请查看！'
    print 'total lines:' , len(linelist)

if __name__ == '__main__' :
    startTime = time.clock()
    path = raw_input('Please input dir with \'YOUR File\':').strip()

    reverseLine(path)
    
    print 'Done! Cost Time: %0.2f second' % (time.clock() - startTime)

