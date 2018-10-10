from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:7890@127.0.0.1:3306/p2p')

Base = declarative_base()

class PlanList(Base):
    __tablename__ = 'RRDXinPlanList'

    # id = Column(String(20), primary_key=True, autoincrement=True)
    amount = Column(String(20))
    earnInterest = Column(String(20))
    expectedYearRate = Column(String(20))
    fundsUseRate = Column(String(20))
    planId = Column(String(20), primary_key=True)
    name = Column(String(20))
    status = Column(String(20))
    subpointCountActual = Column(String(20))
    # isdelete = Column(default=False)

PlanList.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)