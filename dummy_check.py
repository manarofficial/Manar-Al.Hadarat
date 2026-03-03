
import requests

try:
    response = requests.get("http://127.0.0.1:8000/requests", headers={"Authorization": "Bearer " + open("token.txt").read().strip() if "token.txt" in locals() else ""})
    # Since we might not have a token easily available without logging in, let's try to query the backend directly via python script if API fails, 
    # but strictly speaking, I want to see what the API returns.
    # Actually, simplest is to just restart the server. It's safer.
    pass
except:
    pass
