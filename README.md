# JWT Algorithm Confusion CTF Challenge

This repository contains a small Flask app demonstrating a vulnerable JWT verification (algorithm confusion).

Important: Do NOT commit `private.pem` or `exploit.py` to a public repo. They are ignored by `.gitignore`.

Quick setup (local):

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python logic.py
```

Generate exploit token (locally):

```powershell
python exploit.py > token.txt
python sendtoken.py
```

Deployment notes (Render):
- Ensure `PyJWT==1.7.1` is in `requirements.txt` so the vulnerable behavior is available.
- Start command: `gunicorn logic:app`
- Do NOT upload `private.pem`.

If you want, I can push these changes to your GitHub repo and walk you through connecting Render.
