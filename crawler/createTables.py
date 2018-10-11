'''
sqlalchemy + alembic数据库迁移
https://blog.csdn.net/qq_15260769/article/details/83003769
'''


from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:7890@127.0.0.1:3306/p2p')
engine = create_engine('sqlite:///mydb.db')

Base = declarative_base()

class PlanList(Base):
    __tablename__ = 'RRDXinPlanList'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(String(20))
    earnInterest = Column(String(20))
    expectedYearRate = Column(String(20))
    fundsUseRate = Column(String(20))
    planId = Column(String(20))
    name = Column(String(20))
    status = Column(String(20))
    subpointCountActual = Column(String(20))
    # isdelete = Column(default=False)


class RRDUplanList(Base):
    __tablename__ = 'RRDUplanList'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(String(20))
    appendMultipleAmount = Column(String(20))
    applyQuitDays = Column(String(20))
    baseInterestRate = Column(String(20))
    beginSellingTime = Column(String(20))
    category = Column(String(20))
    earnInterest = Column(String(20))
    expectedYearRate = Column(String(20))
    extraInterestRate = Column(String(20))
    inalPeriod = Column(String(20))
    uPlanId = Column(String(20))
    lockPeriod = Column(String(20))
    minRegisterAmount = Column(String(20))
    name = Column(String(20))
    oldExpectedRate = Column(String(20))
    processRatio = Column(String(20))
    simpleInterest = Column(String(20))
    status = Column(String(20))
    subPointCount = Column(String(20))
    tag = Column(String(20))

PlanList.metadata.create_all(engine)
RRDUplanList.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)