import requests

# =====================
# URL endpoint
# =====================
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/auth/login"
USER_URL = f"{BASE_URL}/api/auth/user"

# =====================
# Data login
# =====================
login_data = {
    "username": "nilla",   # pastikan sesuai user yang dibuat
    "password": "CBN123!"  # password bypass sesuai auth.py
}

# =====================
# 1️⃣ Login untuk dapat token
# =====================
resp = requests.post(LOGIN_URL, json=login_data)

if resp.status_code != 200:
    print(f"Login gagal: {resp.status_code} {resp.text}")
    exit()

token = resp.json().get("access_token")
print("Login sukses! Token:", token)

# =====================
# 2️⃣ Panggil endpoint /user dengan token
# =====================
headers = {"Authorization": f"Bearer {token}"}
resp_user = requests.get(USER_URL, headers=headers)

if resp_user.status_code == 200:
    print("Data user:", resp_user.json())
else:
    print(f"Gagal akses /user: {resp_user.status_code} {resp_user.text}")
