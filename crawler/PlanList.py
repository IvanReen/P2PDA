# *-* coding=utf-8 *-*

import sys
import traceback
from setUtil import DatabaseUtil, SessionUtil, HtmlUtil, LogUtil, DictUtil
import time
import json
# reload(sys)
# sys.setdefaultencoding('utf8')
def handleData(returnStr):
    jsonData = json.loads(returnStr)
    planList = jsonData.get('data').get('plans')
    return planList
def storeData(jsonOne, conn, cur, logUtil, loanId):
    amount = jsonOne.get('amount')
    earnInterest = jsonOne.get('earnInterest')
    expectedYearRate = jsonOne.get('expectedYearRate')
    fundsuserRate = jsonOne.get('fundsUseRate')
    planId = jsonOne.get('id')
    name = jsonOne.get('name')
    status = jsonOne.get('status')
    subpointCountActual = jsonOne.get('subpointCountActual')
    sql = 'insert into RRDXinPlanList (amount,earnInterest,expectedYearRate,fundsUseRate,planId,name,status,subpointCountActual) values ("'+amount+'","'+earnInterest+'","'+expectedYearRate+'","'+fundsuserRate+'","'+planId+'","'+name+'","'+status+'","'+subpointCountActual+'")'
    print(sql)
    logUtil.warning(loanId)
    cur.execute(sql)
    conn.commit()
session = SessionUtil()
conn, cur = DatabaseUtil().getConn()
logUtil = LogUtil("uplanList.log")
for i in range(1, 73):
    url = 'https://www.renrendai.com/autoinvestplan/listPlan!listPlanJson.action?pageIndex='+str(i)+'&_='+str(int(time.time()))
    try:
        planList = handleData(session.getReq(url))
        for j in range(len(planList)):
            dictObject = DictUtil(planList[j])
            storeData(dictObject, conn, cur, logUtil, str(i))
    except Exception as e:
        logUtil.warning(str(e))
cur.close()
conn.close()
