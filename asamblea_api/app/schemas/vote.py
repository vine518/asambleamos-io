from pydantic import BaseModel, Field


class VoteInput(BaseModel):
    voter_id: int = Field(..., gt=0)
    question_id: int = Field(..., gt=0)
    vote_option: str = Field(..., min_length=1, max_length=50)
    remarks: str = Field(None, max_length=255)
