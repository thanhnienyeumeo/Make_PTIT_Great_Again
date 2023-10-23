import requests
game_id = 308
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMsIm5hbWUiOiJwdGl0MSIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3NzMyMTA1LCJleHAiOjE2OTc5MDQ5MDV9.QhQ77VUzIYeQP-ubLiHwKFc4q7eu2I7h-am9CbAwzS8'
url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions"

status = requests.get(
url,
headers={"Authorization": token},
    )
print(status.json())