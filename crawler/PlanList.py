'''
爬债权详情
种类不同：优选自动投标服务，U享自动投标服务，薪享自动投标服务，散标，债权转让
'''



import json
import time
import traceback

from setUtil import SessionUtil, DatabaseUtil, LogUtil, DictUtil


def handleData(returnStr):
    jsonData = json.loads(returnStr)
    planList = jsonData.get('data').get('list')
    return planList

def storeData(jsonOne, conn, cur, logUtil, loanId):
    amount = jsonOne.get('amount')
    appendMultipleAmount = jsonOne.get('appendMultipleAmount')
    if appendMultipleAmount == None:
        appendMultipleAmount = '0'
    applyQuitDays = jsonOne.get('applyQuitDays')
    baseInterestRate = jsonOne.get('baseInterestRate')
    beginSellingTime = jsonOne.get('beginSellingTime')
    category = jsonOne.get('category')
    earnInterest = jsonOne.get('earnInterest')
    expectedYearRate = jsonOne.get('expectedYearRate')
    extraInterestRate = jsonOne.get('extraInterestRate')
    inalPeriod = jsonOne.get('inalPeriod')
    if inalPeriod == None:
        inalPeriod = '0'
    uPlanId = jsonOne.get('id')
    lockPeriod = jsonOne.get('lockPeriod')
    minRegisterAmount = jsonOne.get('minRegisterAmount')
    name = jsonOne.get('name')
    oldExpectedRate = jsonOne.get('oldExpectedRate')
    processRatio = jsonOne.get('processRatio')
    simpleInterest = jsonOne.get('simpleInterest')
    status = jsonOne.get('oldExpectedRate')
    subPointCount = jsonOne.get('subPointCount')
    tag = jsonOne.get('tag')
    sql = 'insert into RRDUplanList (amount,appendMultipleAmount,applyQuitDays,baseInterestRate,beginSellingTime,category,earnInterest,expectedYearRate,extraInterestRate,inalPeriod,uPlanId,lockPeriod,minRegisterAmount,name,oldExpectedRate,processRatio,simpleInterest,status,subPointCount,tag) values ("' + amount + '","' + appendMultipleAmount + '","' + applyQuitDays + '","' + baseInterestRate + '","' + beginSellingTime + '","' + category + '","' + earnInterest + '","' + expectedYearRate + '","' + extraInterestRate + '","' + inalPeriod + '","' + uPlanId + '","' + lockPeriod + '","' + minRegisterAmount + '","' + name + '","' + oldExpectedRate + '","' + processRatio + '","' + simpleInterest + '","' + status + '","' + subPointCount + '","' + tag + '")'


    print(sql)
    logUtil.warning(loanId)
    cur.execute(sql)
    conn.commit()

session = SessionUtil()
conn, cur = DatabaseUtil().getConn()
logUtil = LogUtil('uplanList.log')
for i in range(366):
    url='https://www.renrendai.com/pc/p2p/uPlan/getFinancePlanList?startNum='+str(i)+'&limit=10&_='+str(int(time.time()))
    try:
        planList = handleData(session.getReq(url))
        # print(planList)
        for j in range(len(planList)):
            dictObject = DictUtil(planList[j])
            storeData(dictObject, conn, cur, logUtil, str(i))
    except Exception as e:
        logUtil.warning(traceback.print_exc())
        # print(traceback.print_exc())
cur.close()
conn.close()


'''
html版本
'''
# def storeDataHtml(htmlObject, conn, cur, planId, logUtil):
#     logUtil.warning(planId)
#     mytype = str(htmlObject.find('h1', {'class': 'fn-left fn-text-overflow text-big'}).text).split('（')[0]
#     periods = str(
#         htmlObject.find('h1', {'class': 'fn-left fn-text-overflow text-big'}).find('span', {'class': 'text-big'}).text)[
#               3:-3]
#     if htmlObject.find('em', {'class': 'font-24px'}) is None:
#         interest = str(htmlObject.find('span', {'class': 'font-40px num-family'}).text)
#     else:
#         interest = str(htmlObject.find('em', {'class': 'font-24px'}).text)
#     months = str(htmlObject.find('span', {'class': 'font-40px color-dark-text num-family'}).text)
#     amount = str(htmlObject.find('span', {'class': 'font-40px color-dark-text num-family  '}).text).strip()
#     mylimit = str(htmlObject.find('span', {'class': 'fn-left basic-value basic-value-new'}).find('em').text).strip()
#     totalEarnings = htmlObject.find('i', {'class': 'font-36px num-family'}).text
#     lockEndTime = htmlObject.findAll('td')[5].text
#     beginJoinTime = htmlObject.findAll('td')[8].text
#     sql = 'insert into RRDPlanDetail (type,periods,interest,months,amount,mylimit,totalEarnings,lockEndTime,beginJoinTime,planId) values ("' + mytype + '","' + periods + '","' + interest + '","' + months + '","' + amount + '","' + mylimit + '","' + totalEarnings + '","' + lockEndTime + '","' + beginJoinTime + '","' + planId + '")'
#     cur.execute(sql)
#     conn.commit()
#
# session = SessionUtil()
# conn, cur = DatabaseUtil().getConn()
# logUtil = LogUtil('planDetail.log')
# for i in range(77, 13387):
#     url = "https://www.renrendai.com/financeplan/"+str(i)
#     try:
#         from setUtil import HtmlUtil
#         htmlObject = HtmlUtil(session.getReq(url))
#         storeDataHtml(htmlObject, conn, cur, str(i), logUtil)
#     except Exception as e:
#         logUtil.warning(traceback.print_exc())