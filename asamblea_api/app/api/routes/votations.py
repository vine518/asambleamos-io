from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.vote import Vote
from app.models.voting import Voting
from app.schemas.vote import VotationSchema, VoteSchema

router = APIRouter()


@router.get("/votations", response_model=list[VotationSchema])
def get_votations(db: Session = Depends(get_db)):
    return db.query(Voting).all()


@router.post("/votations/{id}/vote", response_model=VoteSchema)
def vote_in_votation(id: int, vote: VoteSchema, db: Session = Depends(get_db)):
    new_vote = Vote(**vote.dict())
    db.add(new_vote)
    db.commit()
    return new_vote


@router.get("/votations/{id}/results")
def get_votation_results(id: int, db: Session = Depends(get_db)):
    votes = db.query(Voting).filter(Voting.id == id).all()
    if not votes:
        raise HTTPException(status_code=404, detail="No votes found")
    return {"results": votes}


@router.post("/votations/{id}/register/vote", response_model=VoteSchema)
def register_vote(id: int, vote: VoteSchema, db: Session = Depends(get_db)):
    new_vote = Vote(**vote.dict())
    db.add(new_vote)
    db.commit()
    return new_vote


@router.post("/assemblies/{id}/votations", response_model=VotationSchema)
def create_votation(id: int, votation: VotationSchema, db: Session = Depends(get_db)):
    new_votation = Voting(**votation.dict(), assembly_id=id)
    db.add(new_votation)
    db.commit()
    return new_votation


@router.get("/votations/{id}", response_model=VotationSchema)
def get_votation(id: int, db: Session = Depends(get_db)):
    votation = db.query(Voting).filter(Voting.id == id).first()
    if not votation:
        raise HTTPException(status_code=404, detail="Votation not found")
    return votation
