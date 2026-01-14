import jwt
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

with open("public.pem") as f:
    PUBLIC_KEY = f.read().strip()

@app.route("/admin/flag")
def admin():
    token = request.headers.get("Authorization")

    if not token:
        return "Token missing", 401

    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]

    try:
        # 🔥 Manually read header (vulnerability)
        header = jwt.get_unverified_header(token)
        alg = header.get("alg")

        if alg == "HS256":
            # 🔥 WRONG: using public key as HMAC secret
            data = jwt.decode(token, PUBLIC_KEY, algorithms=["HS256"])
        elif alg == "RS256":
            data = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        else:
            return "Unsupported alg", 400

    except Exception as e:
        return f"JWT error: {e}", 403

    if data.get("role") == "admin":
        return "CTF{jwt_alg_confusion}"

    return "Access denied", 403

@app.route("/public.pem")
def pubkey():
    return send_file("public.pem")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)