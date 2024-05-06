import argparse
import os
import logging
import sys

log = logging.getLogger('main._psearch')

MIN_WORD = 5
MAX_WORD = 15
PREDECESSOR_SIZE = 32
WINDOW_SIZE = 128


# Name: ParseCommand() Function
#
# Desc : Process and Validate the command line arguments
#
# Input ：none
def ParseCommandLine():
    parser = argparse.ArgumentParser('Python Search')
    '''
        add_argument 方法：
        ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
            定义单个的命令行参数应当如何解析：
            name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
            action - 当参数在命令行中出现时使用的动作基本类型。
            nargs - 命令行参数应当消耗的数目。
            const - 被一些 action 和 nargs 选择所需求的常数。
            default - 当参数未在命令行中出现时使用的值。
            type - 命令行参数应当被转换成的类型。
            choices - 可用的参数的容器。
            required - 此命令行选项是否可省略 （仅选项可用）。
            help - 一个此选项作用的简单描述。
            metavar - 在使用方法消息中使用的参数值示例。
            dest - 被添加到 parse_args() 所返回对象上的属性名。
    '''
    # 对任何DisplayMessage的调用 将显示到标准输出设备  'store_true' and 'store_false' - 分别用于存储True和False值的特殊用例
    parser.add_argument('-v', '--verbose', help="enables printing of additional program messages",
                        action='store_true')
    # 选择指定的 关键词 文件路径
    parser.add_argument('-k', '--keyWords', type=ValidateFileRead, required=True,
                        help="specify the file containing search words")
    # 选择指定的 搜索文件 的文件路径
    parser.add_argument('-t', '--srchTarget', type=ValidateFileRead, required=True,
                        help="specify the target file to search")
    # parser.add_argument('-m', ' --theMatrix ', type=ValidateFileRead, required=True,
    #                     help="specify the weighted matrix file ")

    # 全局变量存储接收到的命令行参数
    global gl_args
    gl_args = parser.parse_args()
    DisplayMessage("Command line processed: Successfully")
    return


# Name: ValidateFi1eRead Function
#
# Desc: Function that wi11 validate that a fi1e exists and is readab1e
#
# Input: A file name with fu11 path
def ValidateFileRead(theFile):
    # 检查文件路径是否存在
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')
    # 检查是否是可读的文件
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')


# Name: DisplayMessage() Function
#
# Desc: Displays the message if the verbose command line option is present
#
# Input : message type string
def DisplayMessage(msg):
    # 在控制台打印消息
    if gl_args.verbose:
        print(msg)
    return


# Name SearchWords()
#
# Uses command line arguments
#
# Searches the target file for、 keywords
#
def SearchWords():
    # 创建一个集合来存储敏感词汇
    search_words = set()

    # 获取敏感词，存储在search_words集合中
    try:
        # 打开毒品相关词语的文件
        file_words = open(gl_args.keyWords)
        # 逐行读取与毒品相关的词语，去空格后加入集合
        for line in file_words:
            search_words.add(line.strip())
    except:
        # 如果打开失败，进入异常语句，并在log文件中记录此错误
        log.error('Keyword File Failure:' + gl_args.keyWords)
        sys.exit()
    finally:
        file_words.close()

    # 记录获取敏感词成功
    log.info('Search Words ')
    log.info('Input File: ' + gl_args.keyWords)
    log.info(search_words)

    # 打开被搜索文件，存储在ba_target中
    try:
        target_file = open(gl_args.srchTarget, 'rb')
        ba_target = bytearray(target_file.read())
    except:
        log.error('Target File Failure :' + gl_args.srchTarget)
        sys.exit()
    finally:
        target_file.close()
    # 记录了目标文件的大小
    size_of_target = len(ba_target)

    # 记录获取被搜索文档成功
    log.info('Target of Search: ' + gl_args.srchTarget)
    log.info('File Size: ' + str(size_of_target))

    # 通过用 0替代所有非字母字符的方式对 baTarget进行修改 。
    # 为了确保可以显示目标文件的原始内容，还进行了备份
    ba_target_copy = ba_target

    for i in range(0, size_of_target):
        character = chr(ba_target[i])
        if not character.isalpha():
            ba_target[i] = 0

    index_of_words = []

    cnt = 0
    for i in range(0, size_of_target):
        character = chr(ba_target[i])
        if character.isalpha():
            cnt += 1
        else:
            if MIN_WORD <= cnt <= MAX_WORD:
                new_word = ""
                for z in range(i - cnt, i):
                    new_word = new_word + chr(ba_target[z])
                new_word = new_word.lower()
                if new_word in search_words:
                    PrintBuffer(new_word, i - cnt, ba_target_copy,
                                i - PREDECESSOR_SIZE, WINDOW_SIZE)
                    index_of_words.append([new_word, i - cnt])
                    cnt = 0
                    print()
                # else:
                #     if word_check.isWordProbable(new_word):
                #         index_of_words.append([new_word, i - cnt])
                #     cnt = 0
            else:
                cnt = 0
    PrintAllWordsFound(index_of_words)
    return


#
# Print Hexidecimal / ASCIl Page Heading
#
def PrintHeading():
    print("Offset   00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F ASCII")
    print("--------------------------------------------------------------")
    return


#
# Print Buffer
#
# Prints Buffer contents for words that are discovered parameters
# 1) Word found
# 2) Direct Offset to beginning of the word
# 3 buff The bytearray holding the target
# 4) offset starting position in the buffer for printing
# 5) hexSize , size of hex display windows to print
#
def PrintBuffer(word, direct_offset, buff, offset, hex_size):
    print("Found : " + word + " At Address; ")
    print("%08x " % direct_offset)
    PrintHeading()
    for i in range(offset, offset + hex_size, 16):
        for j in range(0, 17):
            if j == 0:
                print("%08x " % i, end='')
            else:
                byte_value = buff[i + j]
                print("%02x " % byte_value, end='')
        # print()
        for j in range(0, 16):
            byte_value = buff[i + j]
            if 0x20 <= byte_value <= 0x7f:
                print("%c" % byte_value, end='')
            else:
                print('.', end='')
        print()
    return


#
# PrintAllWordsFound
#
def PrintAllWordsFound(wordList):
    print("Index of All Words")
    print("一一一一一一一一一一一一一一一一一一")
    wordList.sort()
    for entry in wordList:
        print(entry)
    print("一一一一一一一一一一一一一一一一一一")
    print()
    return

#
# Class matrix
#
# init method , loads the matrix into the set
# weightedMatrix
#
# isWordProbable method
# 1) Calculates the weight of the provided word
# 2) Verifies the minimum length
# 3) Calculates the weight for the word
# 4) Tests the word for existence in the matrix
# 5) Returns true or false
# class ClassMatrix:
#     weightedMatrix = set()
#
#     def __init__(self):
#         try:
#             file_the_matrix = open(gl_args.theMatrix, 'rb')
#             for line in file_the_matrix:
#                 value = line.strip()
#                 self.weightedMatrix.add(int(value, 16))
#         except:
#             log.error('Matrix File Error:' + gl_args.theMatrix)
#             sys.exit()
#         finally:
#             file_the_matrix.close()
#         return
#
#     def isWordProbable(self, the_word):
#         if len(the_word) < MIN_WORD:
#             return False
#         else:
#             BASE = 96
#             word_weight = 0
#             for i in range(4, 0, -1):
#                 char_value = (ord(the_word[i]) - BASE)
#                 shift_value = (i - 1) * 8
#                 char_weight = char_value << shift_value
#                 word_weight = (word_weight | char_weight)
#             if word_weight in self.weightedMatrix:
#                 return True
#             else:
#                 return False
