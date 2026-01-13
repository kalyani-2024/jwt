import jwt
from flask import Flask, request, send_file

app = Flask(__name__)

with open("public.pem") as f:
    PUBLIC_KEY = f.read()

@app.route("/admin/flag")
def admin():
    token = request.headers.get("Authorization")
    data = jwt.decode(
        token,
        key=PUBLIC_KEY,
        algorithms=["RS256", "HS256"]  # 🔥 VULN
    )
    if data.get("role") == "admin":
        return "CTF{jwt_alg_confusion}"
    return "Access denied", 403

@app.route("/public.pem")
def pubkey():
    return send_file("public.pem")
