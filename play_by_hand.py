import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMsIm5hbWUiOiJwdGl0MSIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3NjM3OTk5LCJleHAiOjE2OTc4MTA3OTl9.Jg8X34rTWcXLDUmBupZTmezFWB4lXxrrbrF33jKp13U"
team = "team_a"
game_id = 308
field_id = 155
url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions"
get_status_url = f"https://procon2023.duckdns.org/api/player/games/{game_id}"
max_turn = 30
time_per_turn = 15
turn = 9

actions = [
    {"craftsman_id": "66991045", "action": "move", "action_param": "right"},
]


if url is None:
    raise Exception("No url")

status = requests.get(
get_status_url,
headers={"Authorization": token},
    )
if status.status_code != 200:
    print(status.content)
    exit()
print(status.json())
# if True:
#         res = requests.post(
#             url,
#             json={"turn": turn, "actions": actions},
#             headers={"Authorization": token},
#         )
#         print(f"{turn}/{max_turn}", team, res.status_code)
#         if res.status_code != 200:
#             print(res.content)