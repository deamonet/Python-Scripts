import ntplib
import time


# NTP服务器分别是 国家授时中心 NTP 服务器\中国 NTP 快速授时服务\中国计量科学研究院 NIM 授时服务\国际 NTP 快速授时服务
NIST_LIST = ["ntp.ntsc.ac.cn", "cn.ntp.org.cn", "edu.ntp.org.cn", "ntp1.nim.ac.cn", "time.pool.aliyun.com"]
ntp = ntplib.NTPClient()

for NIST in NIST_LIST:
    print(NIST)
    ntpReponse = ntp.request(NIST)
    if ntpReponse:
        now = time.time()
        print(f"Difference: {now - ntpReponse.tx_time}")
        print(f"seconds")
        print(f"Network Delay:{ntpReponse.delay}")
        utc = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(ntpReponse.tx_time)))
        print(f"UTC: NIST: {utc}")
        gmnow = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(now)))
        print(f"UTC: SYSTEM: {gmnow}")
    else:
        print("no response")

    print("\n")