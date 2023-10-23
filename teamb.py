from commons import play

# TEAM B: di sau
actions = [
    {"craftsman_id": "66991045", "action": "build", "action_param": "left"},
]
start_turn = 29
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzQsIm5hbWUiOiJwdGl0MiIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3NjM4NDE4LCJleHAiOjE2OTc4MTEyMTh9.c5VdLu-XsctV6MlecrdaV7lhu_AFNav5iZH0oHGD6aA"
log_label = "team_b"

# COMMON SETTINGS
game_id = 307
url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions"
max_turn = 30
time_per_turn = 15

play(
    actions,
    token,
    log_label,
    turn=start_turn,
    url=url,
    max_turn=max_turn,
    time_per_turn=time_per_turn,
)
