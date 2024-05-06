import decimal
import random
from decimal import Decimal
import struct


def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

text = "AABCBCACBA"

cumulation = Decimal(1) / Decimal(len(text))
frequency = dict()

for i in text:
    frequency[i] = frequency.get(i, Decimal(0)) + cumulation

frequency_list = list(frequency.items())
frequency_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)

interval = []
symbols = []
interval.append(Decimal(0))
previous = 0

for symbol, freq in frequency_list:
    interval.append(freq + previous)
    previous += freq
    symbols.append(symbol)

print(symbols)
print(interval)

symbols_dict = dict()
for index, symbol in enumerate(symbols):
    symbols_dict[symbol] = index


for row, i in enumerate(text):
    begin = interval[symbols_dict[i]]
    end = interval[symbols_dict[i]+1]

    if row == len(text) - 1:
        print("最终目标区间：{:.8}, {:.8}".format(begin, end))
        code = begin + (end - begin) * Decimal(random.random())
        print("最终编码数字：{:.8}".format(code))
        print("二进制（符号位和整数位）：{}".format(binary(float(code))))
        break

    span = end - begin
    interval[0] = begin
    interval[-1] = end

    for index, symbol in enumerate(symbols):
        interval[index+1] = frequency[symbol] * span + interval[index]
        if index == len(symbols) - 1:
            assert abs(end - interval[index+1]) < 0.0001
    
    print("{}个字符".format(row+1), end=',')
    for index, point in enumerate(interval): 
        print("{:.8}".format(point), end=("\n" if index == len(interval) - 1 else ", "))