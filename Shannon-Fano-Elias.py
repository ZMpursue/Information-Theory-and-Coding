import math
import io
import sys
import numpy as np
import os
import copy


keys = dict()


def dec2bin(x):
    x -= int(x)
    bins = []
    while x:
        x *= 2
        bins.append(1 if x >= 1. else 0)
        x -= int(x)
    return bins

def bin2dec(b):
  d = 0
  for i, x in enumerate(b):
    d += 2**(-i-1)*x
  return d

def coding(l):
    ll=[l[0]/2,]
    for i in range(1,l.size):
        ll.append(l[0:i].sum() + 0.5 * l[i])

    length = []
    for i in range(l.size):
        length.append(math.ceil(- math.log2(l[i]) + 1))

    for i in range(0,len(ll)):
        bin = dec2bin(ll[i])
        s = ''
        for j in range(length[i]):
            s = s + str(bin[j])
        keys[str(l[i])] = s


    return ll,length

if __name__ == "__main__":

    s = input('[*] 请输入字符概率分布:')
    #n = int(input('[*] 请输入编码进制：'))

    arr = s.split(" ")
    l = np.array(arr).astype(np.float)
    # if l.sum() != 1:
    #     print('[*] 求和不为1')
    #     os._exit()
    l = l[np.argsort(-l)]
    print('[*] 排序后的概率分布：',l)
    ll,length = coding(l)
    print('[*] 累加概率分布:', ll)
    print('[*] 码长计算结果:', length)
    print('[*] Shannon-Fano-Elias编码结果:',keys)


