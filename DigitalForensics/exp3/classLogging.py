# _*_ coding : utf-8 _*_
import logging

# 处理取证记录操作
class _ForensicLog:
    def __init__(self, logName):
        try:
            logging.basicConfig(
                # encoding='utf-8',
                filename=logName,
                level=logging.DEBUG,
                format='%(asctime)s -%(levelname)s- %(message)s')
        except BaseException:   # 取证日志初始化失败...正在中止
            print('Forensic Log Initialization Failure ... Aborting')
            exit(0)

    def writeLog(self, logType, logMessage):
        """
        将记录写入日志
        """
        if logType == 'INFO':
            logging.info(logMessage)
        elif logType == 'ERROR':
            logging.error(logMessage)
        elif logType == 'WARNING':
            logging.warning(logMessage)
        else:
            logging.error(logMessage)
        return

    # 写入信息消息并关闭记录器
    def __del__(self):
        logging.info('Logging Shutdown')
        logging.shutdown()
