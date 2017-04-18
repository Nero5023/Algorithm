# -*- coding:utf-8 -*-
from math import ceil, log
class MinimalBST:
    def buildMinimalBST(self, vals):
        length = len(vals)
        res = ceil(log(length+1,2))
        return int(res)
