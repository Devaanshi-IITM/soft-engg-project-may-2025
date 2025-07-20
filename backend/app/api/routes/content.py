# app/routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.db.postgres import Content
from app.models.requests.content import ContentCreate, ContentRead
from app.api.deps import get_db

router = APIRouter(prefix="/content", tags=["content"])

@router.post("/create")
def create_content(content: ContentCreate, db: Session = Depends(get_db)):
    new_content = Content(title=content.title,
                          type=content.type,
                          file_url=content.file_url)
    db.add(new_content)
    db.commit()
    return {"success": True, "message": "Content created successfully"}

@router.get("/get/{content_id}", response_model=ContentRead)
def get_content(content_id: int, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.delete("/delete/{content_id}")
def delete_content(content_id: int, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    db.delete(content)
    db.commit()
    return {"success": True, "message": "Content deleted successfully"}

