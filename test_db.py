import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="testtdb",
        user="postgres",
        password="password123"  # ganti sesuai passwordmu
    )
    print("Koneksi berhasil!")
    conn.close()
except Exception as e:
    print("Koneksi gagal:", e)
