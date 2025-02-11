from sqlalchemy import Column, Integer, String, Float
from database.database import Base

class Movies(Base):
    __tablename__="Moviesmodel"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    show= Column(String, nullable=False, index=True)
    time=Column(Integer,nullable=False, index=True)



