from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.vote import NotificationSchema

router = APIRouter()


@router.post("/notificaciones")
def send_notifications(notification: NotificationSchema, db: Session = Depends(get_db)):
    # Notification logic
    return {"message": "Notifications sent successfully"}
