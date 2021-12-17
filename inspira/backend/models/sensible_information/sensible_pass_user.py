from inspira.backend.core.database import Base
from sqlalchemy import Column, String, Integer


class UserPwd(Base):
    __tablename__ = 'userpwd'

    id_userpwd = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String)
    password = Column(String)
    host_id = Column(String)
