# はじめに
VRChat内にテキストメッセージを送るためのツールです。VRChat message APIを使っています。

[English](https://github.com/sunasaji/VRChat_message_sender/blob/master/README.md) | Japanese

# 使い方
1. リリース [release](https://github.com/sunasaji/VRChat_message_sender/releases) からZIP をダウンロードして解凍するか Python3.7.x を入れてソースをダウンロードします。
2. `credential.json` を開き `USERNAME` を自分の VRChat ユーザ名に置き換え, `PASSWORD` を自分の VRChat パスワードに置き換えます。
3. フォルダのアドレスバーを選択して `cmd` を入力してEnterを押します。するとコマンドプロンプトが開きます。
3. メッセージを送りたいフレンドのユーザIDを [VRChat](https://vrchat.net) で確認します。ログインして右側に出てくるフレンドアイコンをクリックしてアドレスバーを見ます。ユーザIDは `usr_` から始まる文字列です。たとえば `usr_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` のような文字列です。
4. `VRChat_message_sender USER_ID_OF_TARGET_USER "MESSAGE"` を実行します。 `USER_ID_OF_TARGET_USER` には確認したユーザIDを入力し、 `MESSAGE` には送りたいメッセージを書きます。例：
```
VRChat_message_sender usr_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx "テストメッセージ"
```

# 自分でビルドする場合

1. Python3.7.x をインストールする
2. `pip install requests` を実行
3. `pip install pyinstaller` を実行
4. `pyinstaller VRChat_message_sender.py --onefile` を実行
5. dist フォルダに exe が生成される

# ライセンス
MIT License です。[LICENSE](https://github.com/sunasaji/VRChat_message_sender/blob/master/LICENSE) ファイルを見てください。
