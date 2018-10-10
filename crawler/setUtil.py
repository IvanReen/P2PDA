# *-* coding=utf-8 *-*
# 日志配置
import logging



class LogUtil():
    def __init__(self, filepath):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=filepath,
                            filemode='w')
        self.log = logging

    def info(self, logstr):
        self.log.info(logstr)

    def debug(self, logstr):
        self.log.debug(logstr)

    def warning(self, logstr):
        self.log.warning(logstr)


# 数据库配置
import pymysql
class DatabaseUtil():
    def getConn(self):
        conn = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '7890',
            db = 'p2p',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute('USE p2p')
        return conn, cur


# 处理html格式返回
from bs4 import BeautifulSoup
class HtmlUtil():
    def __init__(self, text):
        self.text = text
        self.soup = BeautifulSoup(text, 'lxml')

    def find(self, tag=None, attributes=None):
        return self.soup.find(tag, attributes)

    def findAll(self, tag=None, attributes=None):
        return self.soup.findAll(tag, attributes)


# 处理json
import json
import sys
# py2
# reload(sys)
# sys.setdefaultencoding('utf8')
class DictUtil():
    def __init__(self, dictObject):
        self.dictObject = dictObject

    def get(self, keyStr):
        getStr = self.dictObject.get(keyStr)
        if getStr is None:
            return
        if (type(getStr) == int or type(getStr) == float or type(getStr) == bool):
            return str(getStr)
        # py2
        # if type(getStr) == unicode:
        #     return getStr.encode('utf-8')
        return getStr

# session工具类
import requests

class SessionUtil():
    def __init__(self, headers=None, cookie=None):
        self.session = requests.Session()
        if headers is None:
            headersStr = {"Accept":"application/json, text/javascript, */*; q=0.01",
                "X-Requested-With":"XMLHttpRequest",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
                "Accept-Encoding":"gzip, deflate, sdch, br",
                "Accept-Language":"zh-CN,zh;q=0.8"
                          }
            self.headers = headersStr
        else:
            self.headers = headers
        self.cookie = cookie

    def getReq(self, url):
        return self.session.get(url, headers=self.headers).text

    def addCookie(self, cookie):
        self.headers['cookie'] = cookie

    def postReq(self, url, param):
        return self.session.post(url, param).text