from sqlalchemy import Table, Column, Integer, ForeignKey

from app.database import Base

chosen = Table('chosen', Base.metadata, 
    Column('user_id', Integer(), ForeignKey("users.id")),
    Column('tank_id', Integer(), ForeignKey("tanks.id"))
)



    


