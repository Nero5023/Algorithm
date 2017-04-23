# -*- coding:utf-8 -*-
class Exchange:
    def exchangeOddEven(self, x):
        # write code here
        return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)

if __name__ == '__main__':
    print Exchange().exchangeOddEven(10)