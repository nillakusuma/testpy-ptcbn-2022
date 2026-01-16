from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

# =====================
# CONFIG JWT
# =====================
SECRET_KEY = "SECRET123"   # untuk test (nanti boleh taruh di .env)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# =====================
# SCHEMA
# =====================
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


# =====================
# JWT UTILS
# =====================
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

# =====================
# ENDPOINTS
# =====================
@router.post("/login", response_model=Token)
def login(data: LoginRequest):
    # PASSWORD BYPASS SESUAI SOAL
    if data.password != "CBN123!":
        raise HTTPException(status_code=401, detail="Username / Password salah")

    access_token = create_access_token(
        data={"sub": data.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/user")
def current_user(user: dict = Depends(get_current_user)):
    return user
