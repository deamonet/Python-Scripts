# _*_ coding : utf-8 _*_

#  Python 图像库以及 TAGS 和 GPS 相关的 TAGS
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# 提取 EXIF 数据
def ExtractGPSDictionary(fileName):
    try:
        pilImage = Image.open(fileName)
        # print(pilImage)  # PIL.JpegImagePlugin.JpegImageFile image mode=RGB
        EXIFData = pilImage._getexif()
    except Exception:
        # 如果 PIL 处理发生异常 报告
        return None, None

    # 遍历 EXIFData
    # 搜索 GPS 标签
    imageTimeStamp = "NA"
    cameraModel = "NA"
    cameraMake = "NA"
    if EXIFData:
        for tag, theValue in EXIFData.items():
            # 获取标签
            tagValue = TAGS.get(tag, tag)
            # 收集基本图像数据（如果有)
            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = EXIFData.get(tag)
            if tagValue == 'Make':
                cameraMake = EXIFData.get(tag)
            if tagValue == 'Model':
                cameraModel = EXIFData.get(tag)
            # 检查 GPS 标签
            if tagValue == 'GPSInfo':
                # 找到了 ！
                # 现在创建一个字典来保存 GPS 数据
                gpsDictionary = {}
                # 循环浏览 GPS 信息
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]
        basicEXIFData = [imageTimeStamp, cameraMake, cameraModel]
        return gpsDictionary, basicEXIFData
    else:
        return None, None

# 从 gpsDictionary 中提取纬度和经度值
def ExtractLocation(gps):
    """
    return: 全球定位系统坐标
    """
    # 要执行计算，至少需要 lat lon latRef 和 lonRef
    if "GPSLatitude" in gps and \
            "GPSLongitude" in gps and \
            "GPSLatitudeRef" in gps and \
            "GPSLongitudeRef" in gps:
        latitude = gps["GPSLatitude"]
        latitudeRef = gps["GPSLatitudeRef"]
        longitude = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]

        lat = ConvertToDegrees(latitude)
        lon = ConvertToDegrees(longitude)

        # 检查纬度参考如果赤道以南，则纬度值为负
        if latitudeRef == "S":
            lat = 0 - lat

        if longitude == "W":
            lon = 0 - lon

        # 全球定位系统坐标
        gpsCoor = {
            "Lat": lat,
            "LatRef": latitudeRef,
            "Lon": lon,
            "LonRef": longitudeRef}
        return gpsCoor
    else:
        return None


# 将 GPS 坐标转换为度数
# 以 EXIF 格式输入 gpsCoordinates 值
def ConvertToDegrees(gpsCoordinate):
    try:
        degrees = float(gpsCoordinate[0])
    except BaseException:
        degrees = 0.0
    try:
        minutes = float(gpsCoordinate[1])
    except BaseException:
        minutes = 0.0
    try:
        second = float(gpsCoordinate[2])
    except BaseException:
        second = 0.0
    floatCoordinate = float(degrees + (minutes / 60.0) + (second / 3600.0))
    return floatCoordinate
