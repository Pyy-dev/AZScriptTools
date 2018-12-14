#!/usr/bin/env python
# coding=utf-8
# 计算传入目录下代码文件数、总共的行数、总共的字符个数

#References: https://www.jianshu.com/p/ea827390b47a

import os
import time
basedir = '/Users/cocozzhang/Documents/Development/iOS/2018/ios_qq_master/Classes/Group/Doraemon'
#'/root/script'
filelists = []
# 指定想要统计的文件类型
whitelist = ['h', 'm', 'mm']
#遍历文件, 递归遍历文件夹中的所有
def getFile(dir):
    global filelists
    for parent,dirnames,filenames in os.walk(dir):
        #for dirname in dirnames:
        #    getFile(os.path.join(parent,dirname)) #递归
        for filename in filenames:
            ext = filename.split('.')[-1] #-1代表数组最后一个
            #只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent,filename))
#统计一个文件的行数
def countLine(fname):
    lineCount = 0 #行数
    charCount = 0 #字符数
    # readlines() >> returns a list containing all the lines in the file
    # xreadlines() >> Returns a generator to loop over every single line in the file

    for file_line in open(fname).xreadlines():
        if file_line.startswith('//'):continue #过滤掉屏蔽代码行
        if file_line != '' and file_line != '\n': #过滤掉空行
            lineCount += 1
            charCount += (len(file_line)-1) #减掉回车
    print fname #+ '----' , lineCount
    return [lineCount, charCount]

if __name__ == '__main__' :
    totalline = 0
    totalText = 0
    startTime = time.clock()
    dir = raw_input('Please input dir with 【YOUR DIR】:').strip()
    getFile(dir)

#    [totalline,totalText] = countLine(dir) #当传入的dir为文件名时，直接计算

    for filelist in filelists:
        [line,text] = countLine(filelist)
        totalline += line
        totalText += text

    print 'total files:',len(filelists)
    print 'total lines:',totalline
    print 'total texts:',totalText
#    print 'Done! Cost Time: %0.2f second' % (time.clock() - startTime)

