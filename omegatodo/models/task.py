from .meta import Base
from sqlalchemy import Sequence, Boolean, String, Column, Integer, Date, ForeignKey
from .user import User
import datetime

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(100), nullable=False)
    status = Column(Boolean, default=False)
    due = Column(Date)
    owner = Column(ForeignKey('userlist.id'), nullable=False)
    priority = Column(Integer, autoincrement=True)

    def get_status_color(self):
        today = datetime.datetime.now().date()
        if (self.due < today):
            return 'red'
        if (self.due == today):
            return 'yellow'
        else: return 'green'