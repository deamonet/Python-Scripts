import logging
import time
import _psearch

# 函数入口
if __name__ == '__main__':
    # 版本号
    P_SEARCH_VERSION = '1.1'

    # 启动系统日志文件
    logging.basicConfig(filename="pSearchLog.log",
                        level=logging.DEBUG,
                        format="%(asctime)s==>%(message)s",
                        )

    '''
        filename	指定使用指定的文件名而不是 StreamHandler 创建 FileHandler。
        format	为处理程序使用指定的格式字符串。
        level	将根记录器级别设置为指定的级别。默认生成的 root logger 的 level 是
                logging.WARNING，低于该级别的就不输出了。级别排序：
                CRITICAL > ERROR > WARNING > INFO > DEBUG。
        使用默认格式化程序创建 StreamHandler 并将其添加到根日志记录器中，
        从而完成日志系统的基本配置。如果没有为根日志程序定义处理程序，debug()、
        info()、warning()、error()和 critical() 函数将自动调用 
        basicConfig()。
        如果根日志记录器已经为其配置了处理程序，则此函数不执行任何操作。
    '''
    # 接受命令行命令，检索程序待机
    _psearch.ParseCommandLine()

    # 日志文件开始记录
    log = logging.getLogger('main._psearch')
    log.info("p-search started")
    startTime = time.time()

    # 开始检索敏感词汇
    _psearch.SearchWords()

    # 检索结束后记录时间入日志
    endTime = time.time()
    duration = endTime - startTime
    logging.info('Elapsed Time:' + str(duration) + 'seconds')
    logging.info('')
    logging.info('Program Terminated Normally')
