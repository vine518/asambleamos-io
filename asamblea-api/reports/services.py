from sqlalchemy import func
from .votes.models import Vote, db

def get_vote_results():
    results = db.query(Vote.opcion, func.count(Vote.id)).group_by(Vote.opcion).all()
    return dict(results)