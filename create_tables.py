from app.database import Base, engine
from app.models import Master, User

# Buat semua tabel
Base.metadata.create_all(bind=engine)

print("Tabel berhasil dibuat!")
