from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine(
    url="sqlite:///sqlite1.db",
    connect_args={"check_same_thread":False}

)

LocalSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()
