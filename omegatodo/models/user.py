import bcrypt

from .meta import Base
from sqlalchemy import Sequence, String, Column, Integer

class User(Base):
    __tablename__ = 'userlist'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String, unique = True, nullable=False)
    password_hash = Column(String(60))

    def set_password(self, pw):
        password = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = password.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected)
        return False