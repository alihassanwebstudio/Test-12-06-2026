from fastapi import APIRouter,Depends,HTTPException
from app.sechamas.valdiation_when_get_data import User_Sechamas as US
from app.models.database1 import User_Model as U
from app.dependicy import get_dependicy
from app.models.post import Post



router = APIRouter(prefix="/user")


@router.post("/post{id}")
def user_post(db = Depends(get_dependicy)):    
    user = Post(
        title = "XXX", 
        description = "XXX",
        )
    # user.post.append(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("")
def get_data(db = Depends(get_dependicy)):
    data = db.query(U).all()
    return data
 

@router.post("")
def save(data : US, db = Depends(get_dependicy)):
    user = U(
        name= data.name,
        age=data.age,
        phone=data.phone,
        email=data.email,
        address=data.address,
        is_study=data.is_study
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"important":"Remberer Your id is your Identity in database","data":user}

@router.get("/id")
def get_data(id : int,db = Depends(get_dependicy)):
    
    data = db.query(U).filter(U.id == id).first()
    if not data:
        raise HTTPException(status_code=404,detail="GAME-OVER You  ID not in the database")
    return data


@router.put("/id")
def update_data(id : int,data_update : US,db = Depends(get_dependicy)):
    data = db.query(U).filter(U.id==id).first()
    if not data:
        raise HTTPException(status_code=404,detail="GAME-OVER You  ID not in the database")
    else:
        data.name = data_update.name
        data.age = data_update.age
        data.phone = data_update.phone
        data.email = data_update.email
        data.address = data_update.address
        data.is_study = data_update.is_study

    db.commit()
    db.refresh(data)

    return "Data Updated"

@router.delete("/id")
def delete(id : int , db = Depends(get_dependicy)):
    data = db.query(U).filter(U.id == id ).first()
    if not data:
        raise HTTPException(status_code=404,detail="GAME-OVER You  ID not in the database")
    else:
        db.delete(data)
        db.commit()
    return "Data Deleted"


