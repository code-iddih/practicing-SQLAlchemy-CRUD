from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import Column, String, DateTime, Integer , create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR , "site.db")

Base = declarative_base()

engine = create_engine(connection_string , echo = True)

session = sessionmaker()

class User(Base):

    # defining the namw of the table
    __tablename__ = 'users'

    id = Column(Integer() , primary_key = True)
    username = Column(String(25) , nullable = False , unique = True)
    email = Column(String(80) , unique = True , nullable = False)
    date_created = Column(DateTime() , default = datetime.utcnow)

    # Returning a Strring representation of the object

    def __repr__(self):
        return f"<User username = {self.username}  & email = {self.email}>"

## Checking if a user can be instantiated

new_user = User(id = 1 , username = "Eric" , email = "ericnyyamwaya99@gmail.com")
print(new_user)