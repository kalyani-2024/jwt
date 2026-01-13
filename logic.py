@app.route("/admin/flag")
def admin():
    token = request.headers.get("Authorization")

    if not token:
        return "Token missing", 401

    # OPTIONAL: handle Bearer tokens
    if token.startswith("Bearer "):
        token = token.split(" ", 1)[1]

    try:
        data = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256", "HS256"]  # 🔥 still vulnerable
        )
    except Exception as e:
        return f"JWT error: {str(e)}", 403

    if data.get("role") == "admin":
        return "CTF{jwt_alg_confusion}"

    return "Access denied", 403
