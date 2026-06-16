from pydantic import BaseModel,Field,EmailStr,field_validator
from enum import Enum


class Is_study(str,Enum):
    is_yes = "Yes"
    is_no = "No"


class User_Sechamas(BaseModel):
    name : str = Field(min_length=3,max_length=50,examples=["GAME-OVER"])
    age : int = Field(gt=0,examples=[20])
    phone : str = Field(min_length=10,max_length=15,examples=["0300-0101000"])
    email : EmailStr
    address : str
    is_study :Is_study

    @field_validator("email")
    @classmethod
    def check_mail(cls,vl):
        parts = vl.split("@")
        if parts[1] != "gmail.com":
            raise ValueError("Only (gmail.com) is Allowed")
        return vl
