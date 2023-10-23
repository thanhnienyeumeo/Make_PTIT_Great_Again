import requests
import random
import time
import json
import datetime
# game_id = 310

# get_status_url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/status"
# get_actions_url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions"

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMsIm5hbWUiOiJwdGl0MSIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3OTgwMjU4LCJleHAiOjE2OTgxNTMwNTh9.DBFoajKKkmDtc-Xh4ki-chuRpwKptdi-DaHvNyg8COs"

# status = requests.get(
# get_status_url,
# headers={"Authorization": token},
#     )

# if status.status_code != 200:
#     print(status.content)

# print(status.json())