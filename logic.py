import jwt

print(jwt.__version__)

import json
import base64
import hmac
import hashlib
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
            # Manually verify HS256 using PUBLIC_KEY as HMAC secret (intentionally vulnerable)
            try:
                parts = token.split('.')
                if len(parts) != 3:
                    raise ValueError('Invalid token format')
                header_b, payload_b, sig_b = parts

                def b64url_decode(s):
                    s += '=' * ((4 - len(s) % 4) % 4)
                    return base64.urlsafe_b64decode(s.encode('utf-8'))

                msg = (header_b + '.' + payload_b).encode('utf-8')
                expected_sig = hmac.new(PUBLIC_KEY.encode('utf-8'), msg, hashlib.sha256).digest()
                received_sig = b64url_decode(sig_b)
                if not hmac.compare_digest(expected_sig, received_sig):
                    raise ValueError('Invalid signature')

                payload_json = b64url_decode(payload_b).decode('utf-8')
                data = json.loads(payload_json)
            except Exception as e:
                raise
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