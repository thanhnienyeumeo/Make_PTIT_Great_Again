from commons import play

# TEAM A: di truoc

actions = [
    {"craftsman_id": "3c85677b", "action": "build", "action_param": "above"},
    {"craftsman_id": "85f3b3a7", "action": "destroy", "action_param": "right"},
]
start_turn = 2
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzMsIm5hbWUiOiJwdGl0MSIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3NjM3OTk5LCJleHAiOjE2OTc4MTA3OTl9.Jg8X34rTWcXLDUmBupZTmezFWB4lXxrrbrF33jKp13U"
log_label = "team_a"

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
