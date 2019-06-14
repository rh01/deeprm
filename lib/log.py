#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Filename: logging
Created Date: 2019/6/14 17:04
Author: Shine

Copyright (c) 2019 41sh.cn
'''

import logging

import os


class Logger(logging.Logger):
    def __init__(self):
        handlers = {
            logging.NOTSET: "logs/notset.log",
            logging.DEBUG: "logs/debug.log",
            logging.INFO: "logs/info.log",
            logging.WARNING: "logs/warning.log",
            logging.ERROR: "logs/error.log",
            logging.CRITICAL: "logs/critical.log",
        }
        self.__loggers = {}
        logLevels = handlers.keys()
        fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
        for level in logLevels:
            # 创建logger
            logger = logging.getLogger(str(level))
            logger.setLevel(level)
            # 创建hander用于写日日志文件
            log_path = os.path.abspath(handlers[level])
            fh = logging.FileHandler(log_path)
            # 定义日志的输出格式
            fh.setFormatter(fmt)
            fh.setLevel(level)
            # 给logger添加hander
            logger.addHandler(fh)
            self.__loggers.update({level: logger})

        # Define a Handler and set a format which output to console
        # if not logger.handlers:
        logger1= logging.getLogger(str(logging.DEBUG))
        self.console = logging.StreamHandler()                  # 定义console handler
        self.console.setLevel(logging.INFO)                     # 定义该handler级别
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  #定义该handler格式
        self.console.setFormatter(formatter)
        # Create an instance
        logging.getLogger().addHandler(self.console)

        #  添加下面一句，在记录日志之后移除句柄
        # logger.removeHandler(self.console)


    def info(self, message):
        self.__loggers[logging.INFO].info(message)
        self.__loggers[logging.INFO].removeHandler(self.console)

    def error(self, message):
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        self.__loggers[logging.CRITICAL].critical(message)
