# _*_ coding : utf-8 _*_

import csv
import logging

log = logging.getLogger('main._pgps')

# 处理与逗号分隔值操作相关的所有方法
class _CSVWriter:
    def __init__(self, fileName):
        """
        初始化 CSV 文件
        """
        try:
            # 创建一个 writer 对象，然后写入标题行
            self.csvFile = open(fileName, 'w', newline='')
            self.writer = csv.writer(
                self.csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            self.writer.writerow(
                ('Image Path', 'Make', 'Model',
                 'UTC Time', 'Lat Ref', 'Latitude',
                 'Lon Ref', 'Longitude'))
        except Exception as e:
            print(e)
            log.error('CSV File Failure')

    # 将单行写入 csv 文件
    def writeCSVRow(self, fileName, cameraMake, cameraModel, utc,
                    latRef, latValue, lonRef, lonValue):
        self.writer.writerow((fileName, cameraMake, cameraModel, utc,
                              latRef, latValue, lonRef, lonValue))

    # 关闭 CSV 文件
    def __del__(self):
        self.csvFile.close()
