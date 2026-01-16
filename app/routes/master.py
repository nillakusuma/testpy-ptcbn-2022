from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Master
from app.schemas.master import MasterCreate, MasterUpdate, MasterOut
from app.routes.auth import get_current_user

router = APIRouter(
    prefix="/api/master",
    tags=["master"]
)

# =========================
# CREATE
# =========================
@router.post("/", response_model=MasterOut)
def create_master(data: MasterCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    new_master = Master(**data.dict())
    db.add(new_master)
    db.commit()
    db.refresh(new_master)
    return new_master

# =========================
# READ ALL
# =========================
@router.get("/", response_model=list[MasterOut])
def get_all_master(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Master).all()

# =========================
# READ BY ID
# =========================
@router.get("/{master_id}", response_model=MasterOut)
def get_master(master_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    master = db.query(Master).filter(Master.id == master_id).first()
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    return master

# =========================
# UPDATE
# =========================
@router.put("/{master_id}", response_model=MasterOut)
def update_master(master_id: int, data: MasterUpdate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    master = db.query(Master).filter(Master.id == master_id).first()
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(master, key, value)
    db.commit()
    db.refresh(master)
    return master

# =========================
# DELETE
# =========================
@router.delete("/{master_id}")
def delete_master(master_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    master = db.query(Master).filter(Master.id == master_id).first()
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    db.delete(master)
    db.commit()
    return {"detail": "Master deleted successfully"}
