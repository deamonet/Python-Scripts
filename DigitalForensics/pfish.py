# -*- coding: utf-8 -*-
"""
Created on Mon May 9 22:32:03 2022

@author: Celine
"""
#Version 1.0

import logging
import time
import sys
import _pfish
 
 
 
if __name__ == '__main__':       
    # 软件版本号
    PFISH_VERSION = '1.0'
    
    # 初始化日志，打开日志记录
    # 将日志存储在pFishLog.log文件中，将日志记录设置为最低级别DEBUG，确保所有送往日志记录器的消息都是可见的
    logging.basicConfig(filename='pFishLog.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    
    # 调用_pfish模块中的ParseCommandLine函数
    # 如果解析成功，函数将返回此处，否则将向用户发送一条消息并退出程序
    _pfish.ParseCommandLine()
    
    # 记录启动时间，对时间进行跟踪
    startTime = time.time()
    
    # 记录欢迎信息
    logging.info('')
    logging.info('Welcome to p-fish version' + PFISH_VERSION + '...New Scan Started')
    logging.info('')
    # 这里可以添加关于组织、调查员姓名、案件编号以及其它案件与相关信息
    # 调用_pfish模块中的DisplayMessage函数，打印消息
    _pfish.DisplayMessage('Welcome to p-fish ...version' + PFISH_VERSION)
    
    # 记录一些有关系统的信息
    logging.info('System: ' + sys.platform)
    logging.info('Version: ' + sys.version)
    
    # 调用_pfish模块中的WalkPath函数，从根路径开始遍历目录结构，进行哈希处理，并返回成功处理的文件数量
    filesProcessed = _pfish.WalkPath()
    
    # 记录结束时间并计算持续时间，得到执行文件系统哈希操作花费的秒数
    endTime = time.time()
    duration = endTime - startTime
    # 事件已处理的文件提示消息
    logging.info('Files Processed: ' + str(filesProcessed))
    # 事件运行时间提示消息
    logging.info('Elapsed Time: ' + str(duration) + 'seconds')
    logging.info('')
    # 程序正常终止提示消息
    logging.info('Program Terminated Normally')
    logging.info('')
    
    # 调用_pfish模块中的DisplayMessage函数，打印消息
    # _pfish.DisplayMessage('程序运行:  ' + str(duration) + ' 秒')
    _pfish.DisplayMessage("Program End")
