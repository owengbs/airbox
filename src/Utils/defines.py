# -*- coding: utf-8 -*
import os
from datetime import date
today = date.today()
SYSTEM_DATE =  today.strftime('%Y-%m-%d %H:%M:%S')
SYSTEM_DATE_FORLOGFILE =  today.strftime('%Y-%m-%d')
SYSTEM_ROOT =  os.path.join(os.getcwd())
LOGGIN_PATH =   SYSTEM_ROOT+"/logs/"
LOGGIN_FILE = LOGGIN_PATH+"log_"+SYSTEM_DATE_FORLOGFILE+".txt"