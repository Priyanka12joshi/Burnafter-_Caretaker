from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime, uuid, pathlib

engine = create_engine("sqlite:///intake.db", echo=False)  # Change later for cloud db
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Intake(Base):
    __tablename__ = "intakes"
    id            = Column(String, primary_key=True)
    ts            = Column(DateTime, default=datetime.datetime.utcnow)
    age           = Column(Integer)
    area          = Column(String(64))
    severity      = Column(String(32))
    comorbidities = Column(Text)
    symptoms      = Column(Text)
    photo_path    = Column(String(256))  
Base.metadata.create_all(engine)
