from app.app import db
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
