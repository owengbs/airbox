# -*- coding: utf-8 -*
'''
Created on 2014年3月13日

@author: xinyuan
'''
from Utils import logger
from networking import Httpclient
if __name__ == '__main__':
    client = Httpclient.AirHttpClient("db-sns-sms00.db01.baidu.com", 8764)
    data = client.get("service/sendSms.json")
    logger.Logger.getInstance().debug("%s", (data))
    pass