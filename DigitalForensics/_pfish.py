# -*- coding: utf-8 -*-
"""
Created on Mon May 9 22:41:03 2022

@author: Celine
"""

import os
import stat
import time
import hashlib
import argparse
import csv
import logging
 
log = logging.getLogger('main._pfish')
 
#
# Name: ParseCommand() Function
#
# Desc: Process and Validate the command line arguments
#                  use Python Standard Library module argparse
#
# Input: none
#
# Actions:
#                Uses the standard library argparse to process the command line
#                establisthes a global variable gl_args where any of the functions can
#                obtain argument information
#
def ParseCommandLine():
    # 首先创建一个新的解析器，并对它做一个简单的描述。然后增加一个新的参数
    # 与参教相关的帮助消息被帮助系统使用
    parser = argparse.ArgumentParser('Python file system hashing ..p-fish')
    parser.add_argument('-v', '--verbose', help='allows progress message to be displayed', action='store_true')
    
    # 设置一个组，其中的哈希类型选择是互斥的和必需的
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--md5', help='specififes MD5 algorithm', action='store_true')
    group.add_argument('--sha256', help='specififes SHA256 algorithm', action='store_true')
    group.add_argument('--sha512', help='specififes SHA512 algorithm', action='store_true')
    # 允许用户指定遍历的开始或根路径
    parser.add_argument('-d', '--rootPath', type=ValidateDirectory, required=True, help="specify the root path for  hashing")
    # 指定遍历的起始点，以及在哪里创建报告
    parser.add_argument('-r', '--reportPath', type=ValidateDirectoryWritable, required=True, help="specify the path for reports and logs will be written")
    
    # 创建一个全局变量对象来保存已验证的参数
    global gl_args
    global gl_hashType
 
    gl_args = parser.parse_args()
    # 确定用户选择的哈希算法
    # 如果用户选择md5/sha256/sha512，那么gl_args.md5/gl_args.sha256/gl_args.sha512就会被设置为True
    if gl_args.md5:
        gl_hashType = 'MD5'
    elif gl_args.sha256:
        gl_hashType = 'SHA256'
    elif gl_args.sha512:
        gl_hashType = 'SHA512'
    # 如果用户选择的不是上述三种，则给出提示信息并记录在日志中
    else:
        gl_hashType = "Unknown"
        logging.error('Unknown Hash Type Specified')
    DisplayMessage("Command line processed: Successfully")
    return
 
# End ParseCommandLine ====================================================
#
# Name: WalkPath() Function
#,
# Desc: Walk the path specified on the command line use Python Standard Library module os and sys
#
# Input: none, uses command line arguments
#
# Actions:
#                  Uses the standard Library modules os and sys to traverse the directory structure starting a root
#                  path specified by the user. For each file discovered. WalkPath will call the Function HashFile()
#                  to perform the file hashing
# 
 
def WalkPath():
    # 首先对变量processCount进行初始化，以便对成功处理的文件数量进行计数
    processCount = 0
    errorCount = 0
    # 初始化CVS
    oCVS = _CSVWriter(gl_args.reportPath + 'fileSystemReport.csv', gl_hashType)
    
    # 创建一个循环，处理从根路径开始的所有文件。所有子目录也将被处理
    # 然后向日志文件发送一条消息，以记录根路径的值
    log.info('Root Path: ' + gl_args.rootPath)
    for root, dirs, files in os.walk(gl_args.rootPath):
        #对于每个文件，获取文件名并调用HashFile函数
        for file in files:
            # 生成加入路径的文件名
            fname = os.path.join(root, file)
            # 调用HashFile函数对CSV写入器访问，将哈希运算结果写入CSV文件中
            result = HashFile(fname, file, oCVS)
            # 哈希运算结果为True时，processCount的值+1
            if result is True:
                processCount += 1
            # 否则，errorCount的值+1
            else:
                errorCount += 1
    # 所有目录和文件处理完成后,关闭CVSWriter，并且函数会向主程序返回成功处理的文件数目
    oCVS.writerClose()
    return(processCount)
 
#End WalkPath ===============================================================
#
# Name: HashFile Function
#
# Desc: Processes a single file which includes performing a hash of the file and the extraction of metadata
#                  garding the file processed use Python Standard Library modules hashlib, is, and sys
#
# Input: theFile = the full path of the file
#           simpleName = just the filename itselt
#
# Actions:
#                 Attempts to hash the file and extract metadata Call GenerateReport for successful hashed files
#
def HashFile(theFile, simpleName, o_result):
    # 在试图对文件进行哈希计算之前，对于每一个文件都有几个事项需要验证
    # 路径是否存在？
    if os.path.exists(theFile):
        # 路径是一个链接而不是一个真实的文件吗？
        if not os.path.islink(theFile):
            # 文件是真实的吗？
            if os.path.isfile(theFile):
                # 试图打开和读取文件时，运用了 try方法
                try:
                    # 使用‘rb’只读方式打开读取文件
                    f = open(theFile, 'rb')
                except IOError:
                    # 如果打开失败，则报告错误
                    log.warning('Open Failed: ' + theFile)
                    return
                else:
                    try:
                        # 尝试读取文件
                        rd = f.read()
                    except IOError:
                         # 如果读取失败，则关闭文件并报告错误
                        f.close()
                        log.warning('Read Failed: ' + theFile)
                        return
                    else:
                        # 成功文件已打开，我们可以从中读取
                        # 查询文件统计信息
                        theFileStats = os.stat(theFile)
                        (mode, info, dev, nlink, uid, gid, size, atime, mtime, ctime)  = os.stat(theFile)
                    
                        # 输出文件名
                        DisplayMessage("Processing File: " + theFile)
                    
                        # 以字节为单位输出文件
                        fileSize = str(size)
                    
                        # 输出MAC时间
                        modifiedTime = time.ctime(mtime)
                        accessTime = time.ctime(atime)
                        createdTime = time.ctime(ctime)
                        ownerID = str(uid)
                        groupID = str(gid)
                        fileMode = bin(mode)
                    
                    # 处理哈希文件，进行文件的哈希计算，要以用户指定的方法来
                    if gl_args.md5:
                        # 计算并输出MD5
                        hash = hashlib.md5()
                        hash.update(rd)
                        hexMD5 = hash.hexdigest()
                        hashValue = hexMD5.upper()
                    elif gl_args.sha256:
                        # 计算并输出SHA256
                        hash = hashlib.sha256()
                        hash.update(rd)
                        hexSHA256 = hash.hexdigest()
                        hashValue = hexSHA256.upper()
                    elif gl_args.sha512:
                        # 计算并输出SHA512
                        hash = hashlib.sha512()
                        hash.update(rd)
                        hexSHA512 = hash.hexdigest()
                        hashValue = hexSHA512.upper()
                    else:
                        log.error('Hash not Selected')
                        # 文件处理完成，关闭活动文件
                        print("==========================================")
                        f.close()
                        
                    # 文件处理完成，使用CSV类将记录写入报告文件，然后成功返回调用函数WalkPath
                    o_result.writeCSVRow(simpleName, theFile, fileSize, modifiedTime, accessTime, createdTime, hashValue, ownerID, groupID, mode)
                    return True
            # 上述每一项验证都有相应的错误记录
            # 在错误发生时发送到日志文件中
            # 如果一个文件被忽视，程序将返回值，然后处理下一个文件
            else:
                log.warning('[' + repr(simpleName) + ', Skipped NOT a File' + ']')
                return False
        else:
            log.warning('[' + repr(simpleName) + ', Skipped Link NOT a File' + ']' )
            return False
    else:
        log.warning('[' + repr(simpleName) + ', Path does NOT exist' + ']')
        return False
# End HashFile Funtion====================================================
#
# Name: ValidateDirectory Function
#
#
# Desc: Function that will validate a directory path as existing and readable. Used for argument 
#           validation only
#
# Input: a directory path string
#
# Actions:
#                if valid will return the Directory String
#                if invalid it will raise an ArgumentTypeError within argparse
#                which will in turn be reported by argparse to the user
#
def ValidateDirectory(theDir):
    # 验证路径是否为目录
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')
    # 验证路径是否可读
    if os.access(theDir, os.R_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not readable')
#End ValidateDirectory ==============================================
#
# Name: ValidateDirectoryWritable Function
#
# Desc: Function that will validate a directory path as existing and writable. Used for 
#             argument validation only
#
# Input: a directory path String
#
# Actions:
#                       if valid will return the Directory String
#
#                       if invalid it will raise an ArgumentTypeError within argparse which will
#                       in turn be reported by argparse to the user
#
def ValidateDirectoryWritable(theDir):
    # 验证路径是否为目录
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')
    
    # 验证路径是否可写
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')
## End ValidateDirectoryWritable====================================================
#
# Name: DisplayMessage() Function
#
#
# Desc: Displays the message if the verbose if the verbose command line option is present 
#
# Input: message type string
#
# Actions:
#                  Uses the standard library print function to display the message
#                
def DisplayMessage(msg):
    if gl_args.verbose:
        print(msg)
    return
## End DisplayMessage====================================================
#
# Class: _CSVWriter
#
#
# Desc: Handles all methods related to comma separated value operations
#
 
#
# Methods constructor :              Initializes the CSV File
#                  writeCVSRow: Wirtes a single row to the csv file
#                  writerClose:     Close the CSV File
#
class _CSVWriter:
    def __init__(self, fileName, hashType):
        try:
            # 创建输出文件csvFile
            # 用写模式打开csv文件
            self.csvFile = open(fileName, 'w')
            # 初始化writer对象，然后写入首行
            self.writer = csv.writer(self.csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            # 写出所有列名组成标题行
            self.writer.writerow(('File', 'Path', 'Size', 'modified Time', 'Access Time', 'Created Time', hashType, 'Owner', 'Group', 'Mode'))
        except:
            # 如果在初始化过程中发生了任何差错，将会抛出一个异常，并且产生一个日志项
            log.error('CSV File Failure')
    #成功完成文件的哈希计算后将记录写入报告文件
    def writeCSVRow(self, fileName, filePath, fileSize, mTime, aTime, cTime, hashVal, own, grp, mod):
        self.writer.writerow((fileName, filePath, fileSize, mTime, aTime, cTime, hashVal, own, grp, mod))
    # 关闭csvFile文件
    def writerClose(self):
        self.csvFile.close()
