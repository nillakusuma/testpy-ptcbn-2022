# create_user.py
from app.database import SessionLocal
from app.models import User
from app.utils import hash_password

# Ganti data user sesuai kebutuhan
username = "nilla"
email = "nilla@example.com"
password = "CBN123!"  # password asli

db = SessionLocal()

# cek apakah user sudah ada
existing_user = db.query(User).filter(User.username == username).first()
if existing_user:
    print(f"User '{username}' sudah ada!")
else:
    hashed = hash_password(password)
    user = User(username=username, email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    print(f"User '{username}' berhasil dibuat!")

db.close()
