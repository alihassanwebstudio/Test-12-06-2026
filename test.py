@router.get("/post")
def all_user_post(db = Depends(get_db)):
    users = db.query(User).options(selectinload(User.posts)).first()

    return users
@router.get("/post/{user_id}")
def view_user_post(user_id: int, db = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

@router.post("/post/{user_id}")
def save_user_post(user_id: int,data: UserSchema, db = Depends(get_db)):
    user = db.get(User, user_id)
    post = Post(
        title="hello",
        description = "test",
    )
    user.posts.append(post)
    
    # db.add(post)
    db.commit()
    db.refresh(post)
    return post




    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )



    from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database import Base
# from app.models.user import User

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(String(50))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    description: Mapped[str]

    user: Mapped["User"] = relationship(
        back_populates="posts"
    )

    category: Mapped["Category"] = relationship(
        back_populates="posts"
    )