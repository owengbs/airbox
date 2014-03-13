# -*- coding: utf-8 -*
'''
Created on 2014年3月13日

@author: xinyuan
'''
import http.client
from Utils import logger
class AirHttpClient(object):
    '''
    classdocs
    '''
    def __init__(self, host = "", port = 0):
        '''
        Constructor
        '''
        self.conn = http.client.HTTPConnection(host, port)
    def get(self, url=""):
        self.conn.request("GET", url)
        r1 = self.conn.getresponse()
        if str(r1.status) != "200":
                logger.Logger.getInstance().warning("networking error connecting %s status %s reason %s",(url, r1.status, r1.reason))
                return None
        result = r1.read()
        self.conn.close()
        return result
    def post(self, url, data):
        self.conn.request("POST", url, data)
        r1 = self.conn.getresponse()
        if str(r1.status) != "200":
                logger.Logger.getInstance().warning("networking error connecting %s status %s reason %s",(url, r1.status, r1.reason))