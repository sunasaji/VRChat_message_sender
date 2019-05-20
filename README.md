# Introduction 
Send text message to VRChat user in the game, by using VRChat message API.

English | [Japanese](https://github.com/sunasaji/VRChat_message_sender/blob/master/README-ja.md)

**Notice: This tool does not work on 2019/5/21, since the "message" API endpoint used by this tool is currently unavailable in VRChat system**

# Getting Started
1. Download zip file at [release](https://github.com/sunasaji/VRChat_message_sender/releases) and extract it, or prepare Python 3.7.x and clone this repository.
2. Edit credential.json to replace `USERNAME` for your VRChat user name, and replace `PASSWORD` for your VRChat password.
3. Select address bar of the folder and type `cmd` and press enter key. Then command prompt will be opened.
4. Check your friend's user id at [VRChat](https://vrchat.net). Open your friend page by clicking user icon at the right side, and see address bar. User id is the string starts with `usr_`, for example `usr_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
5. Execute `VRChat_message_sender USER_ID_OF_TARGET_USER "MESSAGE"`. Use checked user id for `USER_ID_OF_TARGET_USER` and fill message as you like in `MESSAGE`. Example:
```
VRChat_message_sender usr_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx "This is a test message"
```

# Build
In case you want to build the exe by yourself

1. Install Python3.7.x
2. Execute `pip install requests`
3. Execute `pip install pyinstaller`
4. Execute `pyinstaller VRChat_message_sender --onefile`
5. Find exe file in dist directory

# License
These codes are licensed under MIT License. See [LICENSE](https://github.com/sunasaji/VRChat_message_sender/blob/master/LICENSE) for details.
