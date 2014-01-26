import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.org import relationship, backref

#check version of sqlalchemy
#print sqlalchemy.__version__

engine = create_engine('sqlite:///:memory:', echo=True)

#print engine.execute("select 1").scalar()

Base = declarative_base()

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

User.__table__ 
Base.metadata.create_all(engine)
ed_user = User('ed', 'Ed Jones', 'edspassword')
#u1 = User(name = 'ed',  fullname = 'Ed Jones', password = 'foobar')

Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

session.add_all([
    User('wendy', 'Wendy Williams', 'foorbar'),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blah')])

our_user = session.query(User).filter_by(name='mary').first()
print our_user

#change password for ed
ed_user.password = 'newpassword'

#session can show us what was changed 
session.dirty

#and it can show us what was added new 
session.new

#and we can commit all changes to the database 
session.commit()

#allows us to iterate through table 
#for instance in session.query(User).order_by(User.id): 
#    print instance.name, instance.fullname

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", backref=backref('addresses', order_by=id))
    
    def __init__(self, email_address):
        self.email_address = email_address
    
    def __repr__(self):
        return "<Address('%s')>" % self.email_address


