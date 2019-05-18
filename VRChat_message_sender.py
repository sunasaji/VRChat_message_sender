import requests
import json
from sys import exit,argv,stdout

def end():
    exit()

args = argv
if len(argv) != 3:
    print('Usage: VRChat_message_sender USER_ID_OF_TARGET_USER "MESSAGE"')
    end()

target_usr_id = args[1]
message = args[2]

try:
    credential = json.load(open('credential.json'))
except Exception as e:
    print(e.args[1])
    end()

apiKey = 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26'# 18/04/12 時点で公開されているキー

try:
    response = requests.post(
        'https://api.vrchat.cloud/api/1/user/' + target_usr_id + '/message',
        data={'apiKey':apiKey, 'type':'message', 'message':message},
        auth=(credential["username"], credential["password"])
    )

except Exception as e:
    print(e.args[1])
    end()

if response.status_code == 401:
    print('ログインに失敗しました') # Failed to login.
    end()

elif response.status_code != 200:
    print('サーバーに接続できませんでした') # Cannot connect to the server.
    json.dump(response.json(),stdout,indent=4)
    print('')
    end()

else:
    print('送信しました')
    end()
