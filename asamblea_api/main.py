from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from users.models import User, db
from votes.votes_models import Vote, db
from geopy.distance import geodesic

app = FastAPI()

ALLOWED_LOCATION = (40.7128, -74.0060)  # Example: New York City coordinates
MAX_DISTANCE = 1  # Maximum allowed distance in kilometers

class LocationValidate(BaseModel):
    latitude: float
    longitude: float

class VoteSubmit(BaseModel):
    voto: str

class UserCreate(BaseModel):
    nombre: str

@app.post("/votes/validate-location")
async def validate_location(location: LocationValidate):
    user_location = (location.latitude, location.longitude)
    distance = geodesic(ALLOWED_LOCATION, user_location).kilometers
    return {"valid": distance <= MAX_DISTANCE}

@app.post("/votes/submit")
async def submit_vote(vote: VoteSubmit):
    try:
        new_vote = Vote(opcion=vote.voto)
        db.add(new_vote)
        db.commit()
        return {"success": True, "message": "Voto registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


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

@app.get("/reports/results")
async def get_results():
    return get_vote_results()
