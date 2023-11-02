import requests
import time
import json


#start part
start = ["below","right"]
list = ["build", "build", "move"]
direction = ["above", "left", "upper_left"]

change = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], 
          "right": [1, 0], "lower_left": [-1, 1], "lower_right": [1, 1], 
          "upper_left": [-1, -1], "upper_right": [1, -1]}


#get information part
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzQsIm5hbWUiOiJwdGl0MiIsImlzX2FkbWluIjpmYWxzZSwiaWF0IjoxNjk3OTk0MzMwLCJleHAiOjE2OTgxNjcxMzB9.GHWbkvz-NGKcQ8wOUFut7wN5oELEv9LLNMXu0-c3Roo"
log_label = "team_b" #team_a or team_b
game_id = 309 #

url = f"https://procon2023.duckdns.org/api/player/games/{game_id}/actions" #url to post action
get_status_url = f"https://procon2023.duckdns.org/api/player/games/{game_id}"

a = time.time()

status = requests.get(
get_status_url,
headers={"Authorization": token},
    )


# print('time delay is: ', time.time() - a)
if status.status_code != 200:
    print(status.content)


body = status.json()


field_id = body['field_id']

max_turn = body['num_of_turns']
time_per_turn = body['time_per_turn']
start_turn = 3 #2 or 3

field_infor = body['field']

actions = []
craft_coor = {} #danh sach cac craftmen
craftsmen = json.loads(field_infor['craftsmen'])

for i in craftsmen:
    if(i['side'] == 'B'):
        actions.append({'craftsman_id': i['id'], 'action': 'move', 'action_param': 'right'})
        craft_coor[i['id']] = [i['x'], i['y']]




def play(acts, token, team, turn=2, url=None, max_turn=100, time_per_turn=10):
    cnt = 0
    if url is None:
        raise Exception("No url")
    while turn < max_turn:
        if(turn // 2 <= 2):
            for e in actions:
             e["action"] = "build"
             e["action_param"] = start[turn // 2 - 1]
        else:
            for e in actions:
                e["action"] = list[cnt % 3]
                if(e["action"] == 'build'):
                    e["action_param"] = direction[cnt % 3]
                elif(e["action"] == 'move'):
                    e["action_param"] = direction[2]
                    craft_coor[e["craftsman_id"]][0] += change[e["action_param"]][0]
                    craft_coor[e["craftsman_id"]][1] += change[e["action_param"]][1]
            cnt+=1
        
        res = requests.post(
            url,
            json={"turn": turn, "actions": actions},
            headers={"Authorization": token},
        )
        print(actions)

        print(f"{turn}/{max_turn}", team, res.status_code)
        print(craft_coor)


        if res.status_code != 200:
            print(res.content)
            time.sleep(time_per_turn)
           
            continue
        
        json.dump(res.json(), open('res.json', 'w'))

        turn += 2
        time.sleep(time_per_turn * 2)

play(
    actions,
    token,
    log_label,
    turn=start_turn,
    url=url,
    max_turn=max_turn,
    time_per_turn=time_per_turn,
)
