import requests
import random
import time


def random_action(actions):
    for crfm in actions:
        crfm["action"] = random.choice(["build", "move"])
        if crfm["action"] == "build":
            crfm["action_param"] = random.choice(["above", "below", "left", "right"])
        elif crfm["action"] == "move":
            crfm["action_param"] = random.choice(
                [
                    "up",
                    "down",
                    "left",
                    "right",
                    "upper_left",
                    "upper_right",
                    "lower_left",
                    "lower_right",
                ]
            )
    return actions


def play(acts, token, team, turn=2, url=None, max_turn=100, time_per_turn=10):
    if url is None:
        raise Exception("No url")
    while turn < max_turn:
        actions = random_action(acts)
        res = requests.post(
            url,
            json={"turn": turn, "actions": actions},
            headers={"Authorization": token},
        )

        print(f"{turn}/{max_turn}", team, res.status_code)
        if res.status_code != 200:
            print(res.content)
        turn += 2
        time.sleep(time_per_turn * 2)
