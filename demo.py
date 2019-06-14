#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Filename: demo
Created Date: 2019/6/14 16:19
Author: Shine

Copyright (c) 2019 41sh.cn
'''

from lib.paramenters import Parameters
from lib.job_distribution import Dist
from lib.log import Logger

def demo1():
    log = Logger()
    pa = Parameters()
    d = Dist(num_res = 4, max_nw_size=10, job_len=10, logger=log)
    nw_len, nw_size = d.bi_model_dist()
    print("{} \t\t {}".format(nw_len, nw_size))



if __name__ == '__main__':
    demo1()


