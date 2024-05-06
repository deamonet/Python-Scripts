# _*_ coding : utf-8 _*_

import os
import _modEXIF
import _csvHandler
import _commandParser
from classLogging import _ForensicLog

# 时间戳、相机、型号
TS = 0
MAKE = 1
MODEL = 2

# 处理命令行参数
userArgs = _commandParser.ParseCommandLine()

# 创建取证日志对象
logPath = userArgs.logPath + 'ForensicLog.txt'
oLog = _ForensicLog(logPath)

oLog.writeLog("INFO", "Scan Started")
csvPath = userArgs.csvPath + "imageResults.csv"
oCsv = _csvHandler._CSVWriter(csvPath)

# print(oCsv) # for test
# 定义要扫描的目录
scanDir = userArgs.scanPath
try:
    picts = os.listdir(scanDir)
except:
    oLog.writeLog("ERROR", "Invalid Directory" + scanDir)
    exit(0)
print("Program Start")
print()
for aFile in picts:
    targetFile = scanDir + aFile
    # print(targetFile) # for test
    if os.path.isfile(targetFile):
        gpsDictionary, EXIFList = _modEXIF.ExtractGPSDictionary(targetFile)
        if gpsDictionary:
            # 从 gpsDictionary 中获取 Lat Lon 值转换为度数返回值是一个字典键值对
            dCoor = _modEXIF.ExtractLocation(gpsDictionary)
            lat = dCoor.get("Lat")
            latRef = dCoor.get("LatRef")
            lon = dCoor.get("Lon")
            lonRef = dCoor.get("LonRef")
            if lat and lon and latRef and lonRef:
                # 百度反查格式：经度在前
                print(str(lon) + ',' + str(lat))
                # 将一行写入输出文件
                oCsv.writeCSVRow(targetFile,  EXIFList[MAKE], EXIFList[MODEL],
                                 EXIFList[TS], latRef, lat, lonRef, lon)
                oLog.writeLog("INFO", "GPS Data Calculated for:" + targetFile)
            else:
                oLog.writeLog("WARNING", "No GPS EXIF Data for:" + targetFile)
        else:
            oLog.writeLog("WARNING", 'No GPS EXIF Data for:' + targetFile)
    else:
        oLog.writeLog("WARNING", targetFile + " not a valid file")

# 清理并关闭日志和CSV文件
del oLog
del oCsv