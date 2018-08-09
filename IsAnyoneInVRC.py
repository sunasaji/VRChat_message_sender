import requests
import json
from time import sleep

def end():
    input('enterで終了')
    exit()

sleep_time = 0.1

try:
    credential = json.load(open('credential.json'))
except Exception as e:
    print(e.args)
    end()

apiKey = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'# 18/04/12 時点で公開されているキー
data = {'apiKey':apiKey}

try:
    response = requests.get('https://api.vrchat.cloud/api/1/auth/user/friends', data=data, auth=(credential["username"].encode(), credential["password"]))
except Exception as e:
    print(e.args)
    end()

requests_count = 1

if response.status_code == 401:
    print('ログインに失敗しました') # Failed to login.
    end()

elif response.status_code != 200:
    print('サーバーに接続できませんでした') # Cannot connect to the server.
    end()

else:
    friends = response.json()
    if(len(friends) == 0):
        print('だれもいないよ') # No one is logged in.
        end()

    else:
        for i in range(len(friends)):
            world = friends[i]["location"]
            if world.find("private") != -1:
                world_name = "Private"
            elif world.find("local") != -1:
                world_name = "Local test world"
            else:
                world_id = world[0:world.find(':')]
                try:
                    world_name = requests.get('https://api.vrchat.cloud/api/1/worlds/' + world_id, data=data).json()["name"]
                except Exception as e:
                    print(e.args)
                    end()

                sleep(sleep_time)
                requests_count += 1
                    
            print("{} は {} にいます".format(friends[i]["displayName"], world_name)) # [User name] is in [world name].
        end()