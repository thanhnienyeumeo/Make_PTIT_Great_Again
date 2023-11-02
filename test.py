game_id = 310
url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions" #url to post action
get_status_url = f"https://procon2023.duckdns.org/api/player/games/{game_id}"
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMsIm5hbWUiOiJwdGl0MSIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk4NjgwMDI2LCJleHAiOjE2OTg4NTI4MjZ9.1kw4iaIL1KU62bZ3bcdf8yp2QuPD1NWNbAE93_uBJ_Q'
import requests
status = requests.get(
get_status_url,
headers={"Authorization": token},
    )
print(status.json())