from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database import Base
from app.models.post import Post

class User_Model(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    name : Mapped[str]
    age : Mapped[int]
    phone : Mapped[str]
    email : Mapped[str]=mapped_column(
        unique=True
    )
    address : Mapped[str]
    is_study : Mapped[str] # Attribute same in relationhip this is too important
    post:Mapped[list["Post"]] = relationship(
        back_populates="user"
        )
    