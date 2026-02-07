# JWT Algorithm Confusion CTF Challenge

This repository contains a small Flask app demonstrating a vulnerable JWT verification (algorithm confusion).

Question: Signed but Not Safe


A company rolled out a new authentication system using JWT access tokens.
 	They claim the tokens are securely signed and cannot be tampered with.
During a routine pentest, you intercept the following access token from a low‑privileged user: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoidXNlciIsImlzcyI6ImF1dGgtc2VydmljZSIsImV4cCI6MTk5OTk5OTk5OX0.XYZ_SIGNATURE
The backend validates the token and uses it to authorize access to    https://jwt-dun.vercel.app/ 
However, the system was built in a rush. Something about the token verification logic doesn’t feel right. Gain access and retrieve the flag.

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
