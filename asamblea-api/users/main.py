from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import User, db

app = FastAPI()

class UserCreate(BaseModel):
    nombre: str

@app.post("/users/register")
async def register_user(user: UserCreate):
    try:
        new_user = User(nombre=user.nombre)
        db.add(new_user)
        db.commit()
        return {"success": True, "message": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/quorum")
async def check_quorum():
    total_users = db.query(User).count()
    quorum_threshold = total_users // 2 + 1
    return {"total_users": total_users, "quorum_threshold": quorum_threshold}

