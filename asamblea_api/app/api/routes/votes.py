# @app.post("/votes/submit")
# async def submit_vote(vote: VoteSubmit):
#     try:
#         new_vote = Vote(opcion=vote.voto)
#         db.add(new_vote)
#         db.commit()
#         return {"success": True, "message": "Voto registrado correctamente"}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
from fastapi import APIRouter

router = APIRouter()

# @router.post('/votes')
# async def submit_vote(vote: VoteInput,  db: Session = Depends(get_db)):
#     await vote.submit()
