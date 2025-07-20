# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.db.postgres import Message
from app.models.requests.message import MessageCreate, MessageRead
from app.api.deps import get_db, get_mongo_db

router = APIRouter(prefix="/message", tags=["messages"])

@router.post("/create")
def create_message(message: MessageCreate, db: Session = Depends(get_db),mongo_db=Depends(get_mongo_db)):
    new_message = Message(sender_id=message.sender_id,
                          recipient_id=message.recipient_id)
    db.add(new_message)
    db.commit()

    db_message = db.query(Message).filter((Message.sender_id == new_message.sender_id) & (Message.recipient_id == new_message.recipient_id)).order_by(Message.timestamp.desc()).first()
    mongo_db.messages.insert_one({
        "id": db_message.id,
        "content": message.content,
    })
    return {"success": True, "message": "Message created successfully"}

@router.get("/get/{message_id}", response_model=MessageRead)
def get_message(message_id: int, db: Session = Depends(get_db),mongo_db=Depends(get_mongo_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@router.delete("/delete/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db), mongo_db=Depends(get_mongo_db)):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(message)
    db.commit()
    # Also delete from MongoDB
    mongo_db.messages.delete_one({"id": message_id})
    # Return a success message
    return {"success": True, "message": "Message deleted successfully"}

