# -*- coding: utf-8 -*
'''
Created on 2014年3月10日

@author: xinyuan
'''
import logging
from Utils import defines
class Logger():
    _instance = None
    def __init__(self):
        logging.basicConfig(filename = defines.LOGGIN_FILE, level = logging.DEBUG, format ="%(asctime)s - %(name)s - %(levelname)s - %(message)s" )
        self.logger_debug = logging.getLogger("hiprofile_task.debug")
        self.logger_warning = logging.getLogger("hiprofile_task.warning")
    @staticmethod
    def getInstance():
        if not Logger._instance:
            Logger._instance = Logger()
        return Logger._instance
    def debug(self, formatstr, string = None):
        if string:
            self.logger_debug.debug(formatstr % string)
        else:
            self.logger_debug.debug(formatstr)
    def warning(self, formatstr, string = None):
        if string:
            self.logger_warning.warning(formatstr % string)
        else:
            self.logger_warning.warning(formatstr)
