# _*_ coding : utf-8 _*_

import argparse  # Python 标准库 - 命令行选项、参数的解析器
import os  # 标准库操作系统函数


def ParseCommandLine():
    """
    解析命令行参数
    使用 Python 标准库模块 argparse 处理和验证命令行参数
    :return theArgs: 命令行参数
    """
    parser = argparse.ArgumentParser('Python gpsExtractor')
    # 可以打印附加的程序消息
    parser.add_argument(
        '-v',
        '--verbose',
        help='enables printing of additional program messages',
        action='store_true')
    # 指定取证日志输出文件的目录
    parser.add_argument(
        '-l',
        '--logPath',
        type=ValidateDirectory,
        required=True,
        help='specify the directory for forensic log output file')
    # 指定 csv 文件的目录
    parser.add_argument(
        '-c',
        '--csvPath',
        type=ValidateDirectory,
        required=True,
        help='specify the directory for the csv file')
    # 指定要扫描的目录
    parser.add_argument(
        '-d',
        '--scanPath',
        type=ValidateDirectory,
        required=True,
        help='specify the directory to scan')
    theArgs = parser.parse_args()
    return theArgs


def ValidateDirectory(theDir):
    """
    验证文件夹可写
    :param theDir: 路径
    :return theDir:  路径
    """
    # 验证路径是目录
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')
    # 验证路径是否可写
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')
