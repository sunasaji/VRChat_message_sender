# Introduction 
This tool shows when your friends became your friend in VRChat, by using VRChat moderation API.

# Getting Started
1. Download zip file at [release](https://github.com/sunasaji/VRChat_Friend_History/releases) and extract it, or prepare Python 3.7.x and clone this repository.
2. Edit credential.json to replace `{USERNAME}` for your VRChat user name, and replace `{PASSWORD}` for your VRChat password.
3. Execute VRChat_Friend_History.exe file, or execute VRChat_Friend_History.py with Python.
4. See generated file named VRChat\_Friend\_History.txt.

# Output file example
```
2018-05-11T17:53:08.648Z username_of_your_1st_friend_in_vrchat
2018-05-11T18:24:14.295Z username_of_your_2nd_friend_in_vrchat
...
```

# Build
In case you want to build the exe by yourself

1. Execute 'pip install requests'
2. Execute 'pip install pyinstaller'
3. Execute 'pyinstaller VRChat\_Friend\_History.py --onefile --noconsole'
4. Find exe file in dist directory

# License
These codes are licensed under MIT License. See [LICENSE](https://github.com/sunasaji/VRChat_Friend_History/blob/master/LICENSE) for details.
