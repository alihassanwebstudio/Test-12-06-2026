from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,ForeignKey
from app.database import Base
# from app.models.database1 import User_Model


class Post(Base):
    __tablename__ = "Posts"
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    user_id:Mapped[int] = mapped_column(
        ForeignKey("Users.id")
        
    )
     
    user:Mapped["User_Model"] = relationship(
        back_populates="post" 
    )

    
