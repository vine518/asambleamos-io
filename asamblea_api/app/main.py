from app.core.config import load_environment
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import users, auth
from app.core.middleware.middleware import ExceptionHandlerMiddleware, ExecutionTimeMiddleware, setup_metrics

# from users.models import User, db
# from votes.votes_models import Vote, db
# from reports.reports_services import get_vote_results, db
# from questions.questions_models import QuestionType, Questions


# load_environment()
app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# setup_metrics(app)
# app.add_middleware(ExceptionHandlerMiddleware)
# app.add_middleware(ExecutionTimeMiddleware)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://example.com"],  # Especifica tus dominios permitidos
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )
#


# # Example: New York City coordinates
# MAX_DISTANCE = 100  # Maximum allowed distance in kilometers
#
#
# class LocationValidate(BaseModel):
#     latitude: float
#     longitude: float
#
#
# class VoteSubmit(BaseModel):
#     voto: str
#
#
# class UserCreate(BaseModel):
#     nombre: str
#
#
# class QuestionCreate(BaseModel):
#     contenido: str
#    tipo: QuestionType


#
# @app.post("/votes/validate-location")
# async def validate_location(location: LocationValidate):
#     user_location = (location.latitude, location.longitude)
#     distance = geodesic(ALLOWED_LOCATION, user_location).kilometers
#     return {"valid": distance <= MAX_DISTANCE}
#
# @app.post("/votes/submit")
# async def submit_vote(vote: VoteSubmit):
#     try:
#         new_vote = Vote(opcion=vote.voto)
#         db.add(new_vote)
#         db.commit()
#         return {"success": True, "message": "Voto registrado correctamente"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#
#
# @app.post("/users/register")
# async def register_user(user: UserCreate):
#     try:
#         new_user = User(nombre=user.nombre)
#         db.add(new_user)
#         db.commit()
#         return {"success": True, "message": "Usuario registrado correctamente"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#
# @app.get("/users/quorum")
# async def check_quorum():
#     total_users = db.query(User).count()
#     quorum_threshold = total_users // 2 + 1
#     return {"total_users": total_users, "quorum_threshold": quorum_threshold}
#
# @app.get("/questions")
# async def fetch_all_questions():
#     return db.query(Questions).all()
#
# @app.post("/questions")
# async def create_questions(question: QuestionCreate):
#     try:
#         questionModel = Questions(content=question.contenido, type = question.tipo.name)
#         db.add(questionModel)
#         db.commit()
#         return { "success": True, "message": "Pregunta registrada correctamente"  }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.get("/reports/results")
# async def get_results():
#     return get_vote_results()
