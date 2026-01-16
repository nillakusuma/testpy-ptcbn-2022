from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.master import Master
from app.schemas.master import MasterCreate, MasterResponse
from app.routes.auth import get_current_user

router = APIRouter(
    prefix="/api/master",
    tags=["master"]
)

@router.post("", response_model=MasterResponse)
def create_master(
    data: MasterCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    item = Master(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("", response_model=list[MasterResponse])
def get_master(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    offset = (page - 1) * limit
    return db.query(Master).offset(offset).limit(limit).all()
    return data

@router.get("/{id}", response_model=MasterResponse)
def get_master_by_id(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    item = db.query(Master).filter(Master.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Data not found")
    return item

@router.put("/{id}", response_model=MasterResponse)
def update_master(
    id: int,
    data: MasterCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    item = db.query(Master).filter(Master.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Data not found")

    item.name = data.name
    item.description = data.description
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id}")
def delete_master(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    item = db.query(Master).filter(Master.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Data not found")

    db.delete(item)
    db.commit()
    return {"message": "Deleted"}

