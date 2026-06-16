from app.database import LocalSession

def get_dependicy():
    db = LocalSession()
    yield db
    db.close()